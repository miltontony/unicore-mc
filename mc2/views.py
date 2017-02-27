import requests
import logging

from django.conf import settings
from django.views.generic import ListView, UpdateView, View
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.db.models import F, Sum, FloatField
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

from mama_cas.views import LoginView
from mama_cas.utils import redirect
from mama_cas.utils import to_bool
from mama_cas.models import ServiceTicket

from mc2.controllers.base import exceptions
from mc2.controllers.base.models import Controller
from mc2.controllers.base.views import ControllerViewMixin
from mc2.models import UserSettings
from mc2.organizations.models import Organization
from mc2.forms import UserSettingsForm
from mc2.organizations.utils import active_organization

from mc2 import forms

logger = logging.getLogger(__name__)


class HomepageView(ControllerViewMixin, ListView):
    template_name = 'mc2/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomepageView, self).get_context_data(*args, **kwargs)
        active_org = active_organization(self.request)
        if active_org:
            context.update(
                {'is_admin': active_org.has_admin(self.request.user)})
        return context

    def get_queryset(self):
        return self.get_controllers_queryset(self.request).order_by('name')


class CreateAccountView(FormView):
    """
    Allow a new user to create an account.

    """

    form_class = forms.CreateAccountForm
    template_name = "account/create_account.html"

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password1 = form.cleaned_data["password1"]
        password2 = form.cleaned_data["password2"]
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        user = User.objects.create_user(username=username, password=password1)

        user.password2 = password2
        user.first_name = first_name
        user.last_name = last_name
        if form.cleaned_data["email"]:
            user.email = form.cleaned_data["email"]
            user.save()
        user.save()

        authed_user = authenticate(username=username, password=password1)
        login(self.request, authed_user)
        return HttpResponseRedirect(form.cleaned_data.get("next", "/"))


class DashboardView(HomepageView):
    template_name = 'mc2/dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardView, self).get_context_data(*args, **kwargs)
        results = self.get_queryset().annotate(
            total_mem=F('marathon_mem') * F('marathon_instances'),
            total_cpus=F('marathon_cpus') * F('marathon_instances'),
        ).aggregate(
            Sum(F('total_mem'), output_field=FloatField()),
            Sum(F('total_cpus'), output_field=FloatField())
        )

        context.update({
            'total_memory': (results.get('total_mem__sum') or 0) / 1024.0,
            'total_containers': self.get_queryset().count(),
            'total_suspended_containers':
                self.get_queryset().filter(marathon_instances=0).count(),
            'total_cpus': results.get('total_cpus__sum') or 0,
            'orgs': Organization.objects.for_user(self.request.user).annotate(
                total_mem=Sum(
                    (F('controller__marathon_mem') *
                     F('controller__marathon_instances')) / 1024.0,
                    output_field=FloatField()),
                total_cpus=Sum(
                    F('controller__marathon_cpus') *
                    F('controller__marathon_instances'),
                    output_field=FloatField()),
            )
        })
        return context


class UserSettingsView(UpdateView):
    model = UserSettings
    form_class = UserSettingsForm

    def get_object(self, *args, **kwargs):
        return UserSettings.objects.get(user=self.request.user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserSettingsView, self).form_valid(form)

    def get_success_url(self):
        return self.request.GET.get('next', '/')


class MC2LoginView(LoginView):
    def get(self, request, *args, **kwargs):
        self.request.session['service'] = self.request.GET.get('service')

        service = request.GET.get('service')
        renew = to_bool(request.GET.get('renew'))
        gateway = to_bool(request.GET.get('gateway'))

        if renew:
            logger.debug("Renew request received by credential requestor")
        elif gateway and service:
            logger.debug("Gateway request received by credential requestor")
            if request.user.is_authenticated():

                st = ServiceTicket.objects.create_ticket(service=service,
                                                         user=request.user)
                if self.warn_user():
                    return redirect('cas_warn', params={'service': service,
                                                        'ticket': st.ticket})
                return redirect(service, params={'ticket': st.ticket})

            else:
                return redirect(service)
        elif request.user.is_authenticated():
            if service:
                logger.debug("Service ticket request received by "
                             "credential requestor")
                st = ServiceTicket.objects.create_ticket(service=service,
                                                         user=request.user)
                if self.warn_user():
                    return redirect('cas_warn', params={'service': service,
                                                        'ticket': st.ticket})
                return redirect(service, params={'ticket': st.ticket})
            else:
                msg = _("You are logged in as %s") % request.user
                messages.success(request, msg)
                return redirect('home')
        return super(LoginView, self).get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(LoginView, self).get_context_data(*args, **kwargs)
        context.update({'service': self.request.session['service']})
        return context

    def form_valid(self, form):
        login(self.request, form.user)
        logger.info("Single sign-on session started for %s" % form.user)

        if form.cleaned_data.get('warn'):
            self.request.session['warn'] = True

        service = self.request.GET.get('service')
        if service:
            st = ServiceTicket.objects.create_ticket(service=service,
                                                     user=self.request.user,
                                                     primary=True)
            return redirect(service, params={'ticket': st.ticket})
        return redirect('home')


class AppsHealth(View):
    def get(self, request):
        """
        Get the health details of all the apps
        :param request:
        :return: a json with the health details of the all the apps
        """

        # Get list of all app_ids from the database
        controllers = Controller.objects.values_list('slug', flat=True)
        data = []
        try:
            # Get details of all the apps running on Marathon
            resp_all_apps = requests.get(
                '%(host)s/v2/apps/' % {
                    'host': settings.MESOS_MARATHON_HOST,
                },
                json={})
            # Get details about all deployments on Marathon
            resp_deployments = requests.get(
                '%(host)s/v2/deployments' % {
                    'host': settings.MESOS_MARATHON_HOST,
                },
                json={}
            )

            # Get health statuses of all apps on MC2
            for app in resp_all_apps.json().get('apps'):
                # For each app on Marathon, check if it exists on MC2
                if app['id'][1:] in controllers:

                    # Check if the app is being deployed
                    deploying = False
                    for dep in resp_deployments.json():
                        for dep_app in dep['affectedApps']:
                            if dep_app == app['id']:
                                deploying = True
                                break

                    # Check if the Marathon health check path is defined
                    health_defined = False
                    if len(app.get('healthChecks')) > 0:
                        health_defined = True

                    status = {
                        'app_id': app['id'][1:],
                        'instances': app.get('instances'),
                        'staged': app.get('tasksStaged'),
                        'running': app.get('tasksRunning'),
                        'health_defined': health_defined,
                        'healthy': app.get('tasksHealthy'),
                        'unhealthy': app.get('tasksUnhealthy'),
                        'deploying': deploying,
                        'error': False,
                    }
                    data.append(status)

            json_data = {
                'error': False,
                'message': 'No Error',
                'apps_health': data,
            }
            return JsonResponse(json_data)

        except Exception as e:
            # Return an error message if an exception occurs
            return JsonResponse({
                'error': True,
                'message': e.message,
                'apps_health': [],
            })
