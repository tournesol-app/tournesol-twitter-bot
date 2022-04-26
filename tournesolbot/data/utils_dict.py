from collections import OrderedDict

ACCEPTED_LANGUAGE = {"en": "english", "fr": "french"}

# File path for the different languages

already_shared_filepath = {
    "en": "data/alreadysharedvideos.txt",
    "fr": "data/alreadysharedvideos_fr.txt",
}

already_answered_filepath = {
    "en": "data/alreadyansweredtweet.txt",
    "fr": "data/alreadyansweredtweet_fr.txt",
}


# Text in different languages for the possible tweets

daily_tweet_text = {
    "en": [
        "Today, I recommend '",
        "' by ",
        ", rated on #Tournesol\U0001F33B ",
        " times by ",
        " contributors, favorite criteria:\n- ",
        "\n- ",
        "\nyoutu.be/",
    ],
    "fr": [
        "Aujourd'hui, je recommande '",
        "' de ",
        ", noté sur #Tournesol\U0001F33B ",
        " fois par ",
        " contributeurs, critères favoris:\n- ",
        "\n- ",
        "\nyoutu.be/",
    ],
}

video_details_tweet_text = {
    "en": [
        "Hello @",
        ", this video has been rated on #Tournesol\U0001F33B ",
        " times by ",
        " contributors, favorite criteria:\n- ",
        "\n- ",
        "\n- ",
    ],
    "fr": [
        "Bonjour @",
        ", cette vidéo a été notée sur #Tournesol\U0001F33B ",
        " fois par ",
        " contributeurs, critères favoris:\n- ",
        "\n- ",
        "\n- ",
    ],
}

not_found_video_tweet_text = {
    "en": [
        "Sorry @",
        ", this video has not been rated on #Tournesol\U0001F33B. "
        "Please consider to add it and rate it on https://tournesol.app",
    ],
    "fr": [
        "Désolé @",
        ", cette vidéo n'a jamais été notée sur #Tournesol\U0001F33B. "
        "Vous pouver l'ajouter et la noter sur https://tournesol.app",
    ],
}


# Dict of criteria with their different traduction + _quantile name
CRITERIA_DICT = OrderedDict(
    [
        (
            "largely_recommended",
            [
                "Should be largely recommended",
                "Devrait être largement recommendé",
                "largely_recommended_quantile",
            ],
        ),
        (
            "reliability",
            ["Reliable and not misleading", "Fiable & non trompeur", "reliability_quantile"],
        ),
        (
            "importance",
            ["Important and actionable", "Important & actionnable", "importance_quantile"],
        ),
        (
            "engaging",
            [
                "Engaging and thought-provoking",
                "Stimulant & suscite la réflexion",
                "engaging_quantile",
            ],
        ),
        ("pedagogy", ["Clear and pedagogical", "Clair & pédagogique", "pedagogy_quantile"]),
        (
            "layman_friendly",
            ["Layman-friendly", "Accessible aux non-spécialistes", "layman_friendly_quantile"],
        ),
        (
            "diversity_inclusion",
            ["Diversity and Inclusion", "Diversité & inclusion", "diversity_inclusion_quantile"],
        ),
        (
            "backfire_risk",
            [
                "Resilience to backfiring risks",
                "Résistant aux retours négatifs",
                "backfire_risk_quantile",
            ],
        ),
        (
            "better_habits",
            [
                "Encourages better habits",
                "Encourage de meilleures habitudes",
                "better_habits_quantile",
            ],
        ),
        (
            "entertaining_relaxing",
            [
                "Entertaining and relaxing",
                "Divertissant & relaxant",
                "entertaining_relaxing_quantile",
            ],
        ),
    ]
)


# Dictionnary of YouTube channel name pair with the Twitter account of the creator
YT_2_TWITTER = {
    # English channels
    "3Blue1Brown": "@3blue1brown",
    "Kurzgesagt – In a Nutshell": "@Kurz_Gesagt",
    "Vox": "@voxdotcom",
    "CrashCourse": "@TheCrashCourse",
    "Vsauce": "@tweetsauce",
    "CGP Grey": "@cgpgrey",
    "Veritasium": "@veritasium",
    "SmarterEveryDay": "@smartereveryday",
    "It's Okay To Be Smart": "@okaytobesmart",
    "Mark Rober": "@MarkRober",
    "Kyle Hill": "@Sci_Phile",
    "Stand-up Maths": "@standupmaths",
    "Science4All (english)": "@le_science4all",
    "AsapSCIENCE": "@AsapSCIENCE",
    "Medlife Crisis": "@MedCrisis",
    "Airbus": "@Airbus",
    "Extra Credits": "@ExtraCreditz",
    "Yuval Noah Harari": "@harari_yuval",
    "Today I Found Out": "@TodayIFoundOut1",
    "Philosophy Tube": "@PhilosophyTube",
    "Reuters": "@Reuters",
    "Julia Galef": "@juliagalef",
    "Tournesol": "@TournesolApp",
    "TEDx Talks": "@TEDx",
    "Scott Manley": "@DJSnM",
    "Sixty Symbols": "@periodicvideos",
    "CosmicSkeptic": "@CosmicSkeptic",
    "Anthony Magnabosco": "@magnabosco",
    "MinuteEarth": "@MinuteEarth",
    "minutephysics": "@minutephysics",
    "Above The Noise": "@ATN_PBS",
    "Two Minute Papers": "@twominutepapers",
    "Primer": "@primerlearning",
    "Partnership on AI": "@PartnershipAI",
    "Sabine Hossenfelder": "@skdh",
    "stanfordonline": "@StanfordOnline",
    "Lex Fridman": "@lexfridman",
    "Lex Clips": "@lexfridman",
    "Zach Star": "@ImZachStar",
    "nature video": "@NaturePodcast",
    "LastWeekTonight": "@LastWeekTonight",
    "Tom Scott": "@tomscott",
    "Numberphile": "@numberphile",
    "Tibees": "@TobyHendy",
    "Wintergatan": "@wintergatan",
    "Neil Halloran": "@neilhalloran",
    "Adam Ragusea": "@aragusea",
    "PBS Space Time": "@PBSSpaceTime",
    "Earthling Ed": "'Earthling Ed'",
    "60 Minutes": "@60Minutes",
    "Vsauce2": "@VsauceTwo",
    "vlogbrothers": "@hankgreen",
    "SciShow": "@SciShow",
    "Joe Scott": "@answerswithjoe",
    "Be Smart": "@okaytobesmart",
    "Guardian News":"@guardiannews",
    "Up and Atom":"@upndatom",
    # French channels
    "Science4All": "@le_science4all",
    "Monsieur Phi": "@MonsieurPhi",
    "Heu?reka": "@Heu7reka",
    "ScienceEtonnante": "@dlouapre",
    "Dans Ton Corps": "@jmnl",
    "Allo Docteurs": "@Allodocteurs",
    "Hygiène Mentale": "@HygieneMentale",
    "Stupid Economics": "@Stupid_Eco",
    "Dr Nozman": "@DrNozman",
    "Fouloscopie": "@Mehdi_Moussaid",
    "L'Histoire nous le dira": "@LHistoireDira",
    "LE ROI DES RATS": "@leroidesrats",
    "Les Revues du Monde": "@revuesdumonde",
    "Chat Sceptique": "@ChatSceptique",
    "Étincelles, EPFL": "@le_science4all",
    "Cyrus North": "@CyrusNorth",
    "ARTE": "@ARTEfr",
    "Officiel DEFAKATOR": "@DEFAKATOR_Off",
    "Defakator Vite Fait": "@DEFAKATOR_Off",
    "horizon-gull": "@hackingsocialfr",
    "Mr. Sam - Point d'interrogation": "@MrSam144",
    "e-penser": "@epenser",
    "DirtyBiology": "@dirtybiology",
    "Philoxime": "@philoxime",
    "Scilabus": "@Scilabus",
    "Sci+": "@Scilabus",
    "Homo Fabulus": "@HomoFabulus",
    "AstronoGeek": "@AstronoGeek",
    "Aude WTFake": "@WTFake_",
    "La Tronche en Biais": "@TroncheBiais",
    "Spline LND": "@Spline_LND",
    "Running Addict": "@RunningAddictFr",
    "BLAST - Le souffle de l'info": "@blast_france",
    "Vlanx": "@vlanx0",
    "Le Monde": "@lemondefr",
    "String Theory FR": "@StringTheoryFR",
    "Max Bird": "@MaxBirdOfficiel",
    "la chaîne humaine": "@adrien_fabre",
    "DIMENSION DÉBAT": "@DIMENSION_YT",
    "Tzitzimitl - Esprit Critique": "@Tzitzimitl",
    "La Psy Qui Parle": "@LaPsyQuiParle",
    "Un Créatif": "@un_creatif",
    "Jamy - Epicurieux": "@gourmaud_jamy",
    "Balade Mentale": "@BaladeMentale",
    "Licarion Rock": "@LicarionRock",
    "Pour Info": "'Pour Info'",
    "Scienticfiz": "None",
    "Info ou Mytho ? ": "'Info ou Mytho ?'",
    "28 minutes - ARTE": "@ARTEfr",
    "CNRS": "@CNRS",
    "ApresLaBiere": "@ApresLaBiere",
    "aurelien barrau": "'Aurelien Barrau'",
    "Radio-Canada Info": "@RadioCanadaInfo",
    "52 minutes": "@RadioTeleSuisse",
    "Le Point Genius": "@lePointGenius",
    "Le Vortex - ARTE": "@ARTEfr",
    "Le Vortex - ARTE ": "@ARTEfr",
    "Defend Intelligence": "@defintelligence",
    "Asclépios": "@Asclepios_YT",
    "Libre Influence": "'Libre Influence'",
    "Vox Pop - ARTE": "@ARTEfr",
    "Micode": "@Micode",
    "Micode • Enquêtes": "@Micode",
    "Ben Névert": "'Ben Névert'",
    "BLAST, Le souffle de l'info": "@blast_france",
    "Narada - MP2I": "'Narada - MP2I'",
    "Konbini": "@konbini",
    "G Milgram": "@GGmilgram",
    "Et si c'était faux": "@EtSiCetaitFaux",
    "Nota Bene": "@NotaBeneMovies",
    "Le Réveilleur": "@Le_Reveilleur",
    "HugoDécrypte - Actus du jour": "@HugoDecrypte",
    "C'est une autre histoire": "@ManonBrilCUAH",
    "Mediapart": "@Mediapart",
    "Diable Positif": "@DiablePositif",
    "Temps Présent": "@RadioTeleSuisse",
    "Géopolitis": "@RadioTeleSuisse",
    "PsykoCouac": "@pedrosanchau",
    "Osons Causer": "@OsonsCauser",
    "Le Fossoyeur de Films": "@FrancoisTheurel",
    "écologie rationnelle": "@ERationnelle",
    "Altis play": "@AlTi5",
    "Science de comptoir": "@Sciencecomptoir",
    "Jean-Marc Jancovici": "@JMJancovici",
    "Guillaume Fleurance":"None",
    "maximemusqua":"@MaximeMusqua",
    "Pour 1nfo - la Cyber expliquée":"@Romain_PourInfo",
    "Ami des lobbies":"@AmidesLobbies",
    "L214 éthique et animaux":"@L214",
    "Avides de recherche":"@AvidesR",
    "Le Dessous des Cartes - ARTE":"@ARTEfr",
    "La mal biaisée":"@MizPoline",
    "Le Média":"@LeMediaTV",
    "Real Myop":"@RealMyop",
}
