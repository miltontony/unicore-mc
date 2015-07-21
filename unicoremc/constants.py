NEW_REPO_NAME_FORMAT = (
    'unicore-cms-content-'
    '%(app_type)s-%(country)s%(suffix)s')

# NOTE: It's probably better to move all unicore-cms apps to their own
# virtual env.
MARATHON_CMD = (
    "/usr/local/bin/uwsgi "
    "--pypy-home /usr/local/bin/ "
    "--pypy-ini-paste %(config_path)s "
    "--http :5656 "
    "--processes 1 "
    "--threads 1 "
    "--static-map /static=/var/app/static"
)

LANGUAGES = {
    "aar": "Afar",
    "abk": "Abkhazian",
    "ace": "Achinese",
    "ach": "Acoli",
    "ada": "Adangme",
    "afa": "Afro-Asiatic",
    "afh": "Afrihili",
    "afr": "Afrikaans",
    "aka": "Akan",
    "akk": "Akkadian",
    "ale": "Aleut",
    "alg": "Algonquian languages",
    "amh": "Amharic",
    "ang": "English, Old",
    "apa": "Apache languages",
    "ara": "Arabic",
    "arc": "Aramaic",
    "arn": "Araucanian",
    "arp": "Arapaho",
    "art": "Artificial",
    "arw": "Arawak",
    "asm": "Assamese",
    "ath": "Athapascan languages",
    "aus": "Australian languages",
    "ava": "Avaric",
    "ave": "Avestan",
    "awa": "Awadhi",
    "aym": "Aymara",
    "aze": "Azerbaijani",
    "bad": "Banda",
    "bai": "Bamileke languages",
    "bak": "Bashkir",
    "bal": "Baluchi",
    "bam": "Bambara",
    "ban": "Balinese",
    "bas": "Basa",
    "bat": "Baltic",
    "bej": "Beja",
    "bel": "Belarussian (Byelorussian)",
    "bem": "Bemba",
    "ben": "Bengali (Bengali, Bangla)",
    "ber": "Berber",
    "bho": "Bhojpuri",
    "bih": "Bihari",
    "bik": "Bikol",
    "bin": "Bini",
    "bis": "Bislama",
    "bla": "Siksika",
    "bnt": "Bantu",
    "tib": "Tibetan",
    "bos": "Bosnian",
    "bra": "Braj",
    "bre": "Breton",
    "btk": "Batak (Indonesia)",
    "bua": "Buriat",
    "bug": "Buginese",
    "bul": "Bulgarian",
    "cad": "Caddo",
    "cai": "Central American Indian",
    "car": "Carib",
    "cat": "Catalan",
    "cau": "Caucasian",
    "ceb": "Cebuano",
    "cel": "Celtic",
    "cze": "Czech",
    "cha": "Chamorro",
    "chb": "Chibcha",
    "che": "Chechen",
    "chg": "Chagatai",
    "chk": "Chuukese",
    "chm": "Mari",
    "chn": "Chinook jargon",
    "cho": "Choctaw",
    "chp": "Chipewyan",
    "chr": "Cherokee",
    "chu": "Church Slavic",
    "chv": "Chuvash",
    "chy": "Cheyenne",
    "cmc": "Chamic languages",
    "cop": "Coptic",
    "cor": "Cornish",
    "cos": "Corsican",
    "cpe": "Creoles and pidgins, English-based",
    "cpf": "Creoles and pidgins, French-based",
    "cpp": "Creoles and pidgins, Portuguese-based",
    "cre": "Cree",
    "crp": "Creoles and pidgins",
    "cus": "Cushitic",
    "wel": "Welsh",
    "dak": "Dakota",
    "dan": "Danish",
    "day": "Dayak",
    "del": "Delaware",
    "den": "Slave (Athapascan)",
    "ger": "German",
    "dgr": "Dogrib",
    "din": "Dinka",
    "div": "Divehi",
    "doi": "Dogri",
    "dra": "Dravidian",
    "dua": "Duala",
    "dum": "Dutch, Middle",
    "dyu": "Dyula",
    "dzo": "Dzongkha (Bhutani)",
    "efi": "Efik",
    "egy": "Egyptian (Ancient)",
    "eka": "Ekajuk",
    "gre": "Greek, Modern",
    "elx": "Elamite",
    "eng": "English",
    "enm": "English, Middle",
    "epo": "Esperanto",
    "est": "Estonian",
    "baq": "Basque",
    "ewe": "Ewe",
    "ewo": "Ewondo",
    "fan": "Fang",
    "fao": "Faroese",
    "per": "Persian",
    "fat": "Fanti",
    "fil": "Filipino",
    "fij": "Fijian (Fiji)",
    "fin": "Finnish",
    "fiu": "Finno-Ugrian",
    "fon": "Fon",
    "fre": "French",
    "frm": "French, Middle",
    "fro": "French, Old",
    "fry": "Frisian",
    "ful": "Fulah",
    "fur": "Friulian",
    "gaa": "Ga",
    "gay": "Gayo",
    "gba": "Gbaya",
    "gem": "Germanic",
    "gez": "Geez",
    "gil": "Gilbertese",
    "gla": "Gaelic (Scots) (Scots Gaelic)",
    "gle": "Irish",
    "glg": "Gallegan (Galician)",
    "glv": "Manx (Manx Gaelic)",
    "gmh": "German, Middle High",
    "goh": "German, Old High",
    "gon": "Gondi",
    "gor": "Gorontalo",
    "got": "Gothic",
    "grb": "Grebo",
    "grc": "Greek, Ancient",
    "grn": "Guarani",
    "guj": "Gujarati",
    "gwi": "Gwich'in",
    "hai": "Haida",
    "hau": "Hausa",
    "haw": "Hawaiian",
    "heb": "Hebrew",
    "her": "Herero",
    "hil": "Hiligaynon",
    "him": "Himachali",
    "hin": "Hindi",
    "hit": "Hittite",
    "hmn": "Hmong",
    "hmo": "Hiri Motu",
    "hrv": "Croatian",
    "hun": "Hungarian",
    "hup": "Hupa",
    "arm": "Armenian",
    "iba": "Iban",
    "ibo": "Igbo",
    "ijo": "Ijo",
    "iku": "Inuktitut",
    "ile": "Interlingue",
    "ilo": "Iloko",
    "ina": "Interlingua",
    "inc": "Indic",
    "ind": "Indonesian (Bahasa)",
    "ine": "Indo-European",
    "ipk": "Inupiaq (Inupiak)",
    "ira": "Iranian",
    "iro": "Iroquoian languages",
    "ice": "Icelandic",
    "ita": "Italian",
    "jav": "Javanese",
    "jpn": "Japanese",
    "jpr": "Judeo-Persian",
    "jrb": "Judeo-Arabic",
    "kaa": "Kara-Kalpak",
    "kab": "Kabyle",
    "kac": "Kachin",
    "kal": "Kalaallisut (Greenlandic)",
    "kam": "Kamba",
    "kan": "Kannada",
    "kar": "Karen",
    "kas": "Kashmiri",
    "geo": "Georgian",
    "kau": "Kanuri",
    "kaw": "Kawi",
    "kaz": "Kazakh",
    "kha": "Khasi",
    "khi": "Khoisan",
    "khm": "Khmer (Cambodian)",
    "kho": "Khotanese",
    "kik": "Kikuyu",
    "kin": "Kinyarwanda",
    "kir": "Kirghiz",
    "kmb": "Kimbundu",
    "kok": "Konkani",
    "kom": "Komi",
    "kon": "Kongo",
    "kor": "Korean",
    "kos": "Kosraean",
    "kpe": "Kpelle",
    "kro": "Kru",
    "kru": "Kurukh",
    "kua": "Kuanyama",
    "kum": "Kumyk",
    "kur": "Kurdish",
    "kut": "Kutenai",
    "lad": "Ladino",
    "lah": "Lahnda",
    "lam": "Lamba",
    "lao": "Lao (Laothian)",
    "lat": "Latin",
    "lav": "Latvian (Latvian, Lettish)",
    "lez": "Lezghian",
    "lin": "Lingala",
    "lit": "Lithuanian",
    "lol": "Mongo",
    "loz": "Lozi",
    "ltz": "Letzeburgesch (Luxembourgish)",
    "lua": "Luba-Lulua",
    "lub": "Luba-Katanga",
    "lug": "Ganda",
    "lui": "Luiseno",
    "lun": "Lunda",
    "luo": "Luo (Kenya and Tanzania)",
    "lus": "Lushai",
    "mad": "Madurese",
    "mag": "Magahi",
    "mah": "Marshall",
    "mai": "Maithili",
    "mak": "Makasar",
    "mal": "Malayalam",
    "man": "Mandingo",
    "map": "Austronesian",
    "mar": "Marathi",
    "mas": "Masai",
    "mdr": "Mandar",
    "men": "Mende",
    "mga": "Irish, Middle",
    "mic": "Micmac",
    "min": "Minangkabau",
    "mis": "Miscellaneous languages",
    "mac": "Macedonian",
    "mkh": "Mon-Khmer",
    "mlg": "Malagasy",
    "mlt": "Maltese",
    "mnc": "Manchu",
    "mni": "Manipuri",
    "mno": "Manobo languages",
    "moh": "Mohawk",
    "mol": "Moldavian",
    "mon": "Mongolian",
    "mos": "Mossi",
    "mao": "Maori",
    "may": "Malay",
    "mul": "Multiple languages",
    "mun": "Munda languages",
    "mus": "Creek",
    "mwr": "Marwari",
    "bur": "Burmese",
    "myn": "Mayan languages",
    "nah": "Nahuatl",
    "nai": "North American Indian",
    "nau": "Nauru",
    "nav": "Navajo",
    "nbl": "Ndebele, South",
    "nde": "Ndebele, North",
    "ndo": "Ndonga",
    "nep": "Nepali",
    "new": "Newari",
    "nia": "Nias",
    "nic": "Niger-Kordofanian",
    "niu": "Niuean",
    "dut": "Dutch",
    "nno": "Norwegian Nynorsk",
    "nob": "Norwegian Bokmal",
    "non": "Norse, Old",
    "nor": "Norwegian",
    "nso": "Sotho, Northern",
    "nub": "Nubian languages",
    "nya": "Chichewa; Nyanja",
    "nym": "Nyamwezi",
    "nyn": "Nyankole",
    "nyo": "Nyoro",
    "nzi": "Nzima",
    "oci": "Occitan",
    "oji": "Ojibwa",
    "ori": "Oriya",
    "orm": "Oromo",
    "osa": "Osage",
    "oss": "Ossetian; Ossetic",
    "ota": "Turkish, Ottoman",
    "oto": "Otomian languages",
    "paa": "Papuan",
    "pag": "Pangasinan",
    "pal": "Pahlavi",
    "pam": "Pampanga",
    "pan": "Panjabi (Punjabi)",
    "pap": "Papiamento",
    "pau": "Palauan",
    "peo": "Persian, Old",
    "phi": "Philippine",
    "phn": "Phoenician",
    "pli": "Pali",
    "pol": "Polish",
    "pon": "Pohnpeian",
    "por": "Portuguese",
    "pra": "Prakrit languages",
    "pro": "ProvenAal, Old",
    "pus": "Pushto (Pashto, Pushto)",
    "que": "Quechua",
    "raj": "Rajasthani",
    "rap": "Rapanui",
    "rar": "Rarotongan",
    "roa": "Romance",
    "roh": "Raeto-Romance, (Rhaeto-Romance)",
    "rom": "Romany",
    "rum": "Romanian",
    "run": "Rundi",
    "rus": "Russian",
    "sad": "Sandawe",
    "sag": "Sango (Sangho)",
    "sah": "Yakut",
    "sai": "South American Indian",
    "sal": "Salishan languages",
    "sam": "Samaritan Aramaic",
    "san": "Sanskrit",
    "sas": "Sasak",
    "sat": "Santali",
    "sco": "Scots",
    "sel": "Selkup",
    "sem": "Semitic",
    "sga": "Irish, Old",
    "sgn": "Sign languages",
    "shn": "Shan",
    "sid": "Sidamo",
    "sin": "Sinhalese (Singhalese)",
    "sio": "Siouan languages",
    "sit": "Sino-Tibetan",
    "sla": "Slavic",
    "slo": "Slovak",
    "slv": "Slovenian",
    "sme": "Northern Sami",
    "smi": "Sami languages Other",
    "smo": "Samoan",
    "sna": "Shona",
    "snd": "Sindhi",
    "snk": "Soninke",
    "sog": "Sogdian",
    "som": "Somali",
    "son": "Songhai",
    "sot": "Sotho, Southern (Sesotho)",
    "spa": "Spanish",
    "alb": "Albanian",
    "srd": "Sardinian",
    "srp": "Serbian",
    "srr": "Serer",
    "ssa": "Nilo-Saharan",
    "ssw": "Swati",
    "suk": "Sukuma",
    "sun": "Sundanese",
    "sus": "Susu",
    "sux": "Sumerian",
    "swa": "Swahili",
    "swe": "Swedish",
    "syr": "Syriac",
    "tah": "Tahitian",
    "tai": "Tai",
    "tam": "Tamil",
    "tat": "Tatar",
    "tel": "Telugu",
    "tem": "Timne",
    "ter": "Tereno",
    "tet": "Tetum",
    "tgk": "Tajik",
    "tgl": "Tagalog",
    "tha": "Thai",
    "tig": "Tigre",
    "tir": "Tigrinya",
    "tiv": "Tiv",
    "tkl": "Tokelau",
    "tli": "Tlingit",
    "tmh": "Tamashek",
    "tog": "Tonga (Nyasa)",
    "ton": "Tonga (Tonga Islands)",
    "tpi": "Tok Pisin",
    "tsi": "Tsimshian",
    "tsn": "Tswana",
    "tso": "Tsonga",
    "tuk": "Turkmen",
    "tum": "Tumbuka",
    "tur": "Turkish",
    "tut": "Altaic",
    "tvl": "Tuvalu",
    "twi": "Twi",
    "tyv": "Tuvinian",
    "uga": "Ugaritic",
    "uig": "Uighur",
    "ukr": "Ukrainian",
    "umb": "Umbundu",
    "und": "Undetermined",
    "urd": "Urdu",
    "uzb": "Uzbek",
    "vai": "Vai",
    "ven": "Venda",
    "vie": "Vietnamese",
    "vol": "Volapuk",
    "vot": "Votic",
    "wak": "Wakashan languages",
    "wal": "Walamo",
    "war": "Waray",
    "was": "Washo",
    "wen": "Sorbian languages",
    "wol": "Wolof",
    "xho": "Xhosa",
    "yao": "Yao",
    "yap": "Yapese",
    "yid": "Yiddish",
    "yor": "Yoruba",
    "ypk": "Yupik languages",
    "zap": "Zapotec",
    "zen": "Zenaga",
    "zha": "Zhuang",
    "chi": "Chinese",
    "znd": "Zande",
    "zul": "Zulu",
    "zun": "Zuni"
}

COUNTRIES = {
    "AF": "Afghanistan",
    "AX": "Aland Islands",
    "AL": "Albania",
    "DZ": "Algeria",
    "AS": "American Samoa",
    "AD": "AndorrA",
    "AO": "Angola",
    "AI": "Anguilla",
    "AQ": "Antarctica",
    "AG": "Antigua and Barbuda",
    "AR": "Argentina",
    "AM": "Armenia",
    "AW": "Aruba",
    "AU": "Australia",
    "AT": "Austria",
    "AZ": "Azerbaijan",
    "BS": "Bahamas",
    "BH": "Bahrain",
    "BD": "Bangladesh",
    "BB": "Barbados",
    "BY": "Belarus",
    "BE": "Belgium",
    "BZ": "Belize",
    "BJ": "Benin",
    "BM": "Bermuda",
    "BT": "Bhutan",
    "BO": "Bolivia",
    "BA": "Bosnia and Herzegovina",
    "BW": "Botswana",
    "BV": "Bouvet Island",
    "BR": "Brazil",
    "IO": "British Indian Ocean Territory",
    "BN": "Brunei Darussalam",
    "BG": "Bulgaria",
    "BF": "Burkina Faso",
    "BI": "Burundi",
    "KH": "Cambodia",
    "CM": "Cameroon",
    "CA": "Canada",
    "CV": "Cape Verde",
    "KY": "Cayman Islands",
    "CF": "Central African Republic",
    "TD": "Chad",
    "CL": "Chile",
    "CN": "China",
    "CX": "Christmas Island",
    "CC": "Cocos (Keeling) Islands",
    "CO": "Colombia",
    "KM": "Comoros",
    "CG": "Congo",
    "CD": "Congo, The Democratic Republic of the",
    "CK": "Cook Islands",
    "CR": "Costa Rica",
    "CI": "Cote D'Ivoire",
    "HR": "Croatia",
    "CU": "Cuba",
    "CY": "Cyprus",
    "CZ": "Czech Republic",
    "DK": "Denmark",
    "DJ": "Djibouti",
    "DM": "Dominica",
    "DO": "Dominican Republic",
    "EC": "Ecuador",
    "EG": "Egypt",
    "SV": "El Salvador",
    "GQ": "Equatorial Guinea",
    "ER": "Eritrea",
    "EE": "Estonia",
    "ET": "Ethiopia",
    "FK": "Falkland Islands (Malvinas)",
    "FO": "Faroe Islands",
    "FJ": "Fiji",
    "FI": "Finland",
    "FR": "France",
    "GF": "French Guiana",
    "PF": "French Polynesia",
    "TF": "French Southern Territories",
    "GA": "Gabon",
    "GM": "Gambia",
    "GE": "Georgia",
    "DE": "Germany",
    "GH": "Ghana",
    "GI": "Gibraltar",
    "GR": "Greece",
    "GL": "Greenland",
    "GD": "Grenada",
    "GP": "Guadeloupe",
    "GU": "Guam",
    "GT": "Guatemala",
    "GG": "Guernsey",
    "GN": "Guinea",
    "GW": "Guinea-Bissau",
    "GY": "Guyana",
    "HT": "Haiti",
    "HM": "Heard Island and Mcdonald Islands",
    "VA": "Holy See (Vatican City State)",
    "HN": "Honduras",
    "HK": "Hong Kong",
    "HU": "Hungary",
    "IS": "Iceland",
    "IN": "India",
    "ID": "Indonesia",
    "IR": "Iran, Islamic Republic Of",
    "IQ": "Iraq",
    "IE": "Ireland",
    "IM": "Isle of Man",
    "IL": "Israel",
    "IT": "Italy",
    "JM": "Jamaica",
    "JP": "Japan",
    "JE": "Jersey",
    "JO": "Jordan",
    "KZ": "Kazakhstan",
    "KE": "Kenya",
    "KI": "Kiribati",
    "KP": "Korea, Democratic People\'s Republic of",
    "KR": "Korea, Republic of",
    "KW": "Kuwait",
    "KG": "Kyrgyzstan",
    "LA": "Lao People\'s Democratic Republic",
    "LV": "Latvia",
    "LB": "Lebanon",
    "LS": "Lesotho",
    "LR": "Liberia",
    "LY": "Libyan Arab Jamahiriya",
    "LI": "Liechtenstein",
    "LT": "Lithuania",
    "LU": "Luxembourg",
    "MO": "Macao",
    "MK": "Macedonia, The Former Yugoslav Republic of",
    "MG": "Madagascar",
    "MW": "Malawi",
    "MY": "Malaysia",
    "MV": "Maldives",
    "ML": "Mali",
    "MT": "Malta",
    "MH": "Marshall Islands",
    "MQ": "Martinique",
    "MR": "Mauritania",
    "MU": "Mauritius",
    "YT": "Mayotte",
    "MX": "Mexico",
    "FM": "Micronesia, Federated States of",
    "MD": "Moldova, Republic of",
    "MC": "Monaco",
    "MN": "Mongolia",
    "MS": "Montserrat",
    "MA": "Morocco",
    "MZ": "Mozambique",
    "MM": "Myanmar",
    "NA": "Namibia",
    "NR": "Nauru",
    "NP": "Nepal",
    "NL": "Netherlands",
    "AN": "Netherlands Antilles",
    "NC": "New Caledonia",
    "NZ": "New Zealand",
    "NI": "Nicaragua",
    "NE": "Niger",
    "NG": "Nigeria",
    "NU": "Niue",
    "NF": "Norfolk Island",
    "MP": "Northern Mariana Islands",
    "NO": "Norway",
    "OM": "Oman",
    "PK": "Pakistan",
    "PW": "Palau",
    "PS": "Palestinian Territory, Occupied",
    "PA": "Panama",
    "PG": "Papua New Guinea",
    "PY": "Paraguay",
    "PE": "Peru",
    "PH": "Philippines",
    "PN": "Pitcairn",
    "PL": "Poland",
    "PT": "Portugal",
    "PR": "Puerto Rico",
    "QA": "Qatar",
    "RE": "Reunion",
    "RO": "Romania",
    "RU": "Russian Federation",
    "RW": "Rwanda",
    "SH": "Saint Helena",
    "KN": "Saint Kitts and Nevis",
    "LC": "Saint Lucia",
    "PM": "Saint Pierre and Miquelon",
    "VC": "Saint Vincent and the Grenadines",
    "WS": "Samoa",
    "SM": "San Marino",
    "ST": "Sao Tome and Principe",
    "SA": "Saudi Arabia",
    "SN": "Senegal",
    "CS": "Serbia and Montenegro",
    "SC": "Seychelles",
    "SL": "Sierra Leone",
    "SG": "Singapore",
    "SK": "Slovakia",
    "SI": "Slovenia",
    "SB": "Solomon Islands",
    "SO": "Somalia",
    "ZA": "South Africa",
    "GS": "South Georgia and the South Sandwich Islands",
    "ES": "Spain",
    "LK": "Sri Lanka",
    "SD": "Sudan",
    "SR": "Suriname",
    "SJ": "Svalbard and Jan Mayen",
    "SZ": "Swaziland",
    "SE": "Sweden",
    "CH": "Switzerland",
    "SY": "Syrian Arab Republic",
    "TW": "Taiwan, Province of China",
    "TJ": "Tajikistan",
    "TZ": "Tanzania, United Republic of",
    "TH": "Thailand",
    "TL": "Timor-Leste",
    "TG": "Togo",
    "TK": "Tokelau",
    "TO": "Tonga",
    "TT": "Trinidad and Tobago",
    "TN": "Tunisia",
    "TR": "Turkey",
    "TM": "Turkmenistan",
    "TC": "Turks and Caicos Islands",
    "TV": "Tuvalu",
    "UG": "Uganda",
    "UA": "Ukraine",
    "AE": "United Arab Emirates",
    "GB": "United Kingdom",
    "US": "United States",
    "UM": "United States Minor Outlying Islands",
    "UY": "Uruguay",
    "UZ": "Uzbekistan",
    "VU": "Vanuatu",
    "VE": "Venezuela",
    "VN": "Viet Nam",
    "VG": "Virgin Islands, British",
    "VI": "Virgin Islands, U.S.",
    "WF": "Wallis and Futuna",
    "EH": "Western Sahara",
    "YE": "Yemen",
    "ZM": "Zambia",
    "ZW": "Zimbabwe"}
COUNTRY_CHOICES = [
    (code, name) for code, name in sorted(COUNTRIES.items(), key=lambda x:x[1])
]
