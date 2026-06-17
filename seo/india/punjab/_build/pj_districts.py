"""District data and templates for 23 Punjab local SEO landing pages.
"""

DISTRICTS = [
    ("amritsar", "Amritsar", "31.6340", "74.8723", "heritage_border_tourism"),
    ("barnala", "Barnala", "30.3810", "75.5460", "agro_dairy_processing"),
    ("bathinda", "Bathinda", "30.2110", "74.9455", "agro_dairy_processing"),
    ("faridkot", "Faridkot", "30.6740", "74.7580", "agro_dairy_processing"),
    ("fatehgarh-sahib", "Fatehgarh Sahib", "30.6420", "76.3920", "local_services_infrastructure"),
    ("fazilka", "Fazilka", "30.4030", "74.0280", "agro_dairy_processing"),
    ("ferozepur", "Ferozepur", "30.9334", "74.6136", "heritage_border_tourism"),
    ("gurdaspur", "Gurdaspur", "32.0403", "75.4025", "heritage_border_tourism"),
    ("hoshiarpur", "Hoshiarpur", "31.5320", "75.9110", "light_manufacturing_trade"),
    ("jalandhar", "Jalandhar", "31.3260", "75.5762", "industrial_manufacturing"),
    ("kapurthala", "Kapurthala", "31.3800", "75.3800", "light_manufacturing_trade"),
    ("ludhiana", "Ludhiana", "30.9010", "75.8573", "industrial_manufacturing"),
    ("malerkotla", "Malerkotla", "30.5320", "75.8830", "local_services_infrastructure"),
    ("mansa", "Mansa", "29.9940", "75.3950", "agro_dairy_processing"),
    ("moga", "Moga", "30.8160", "75.1720", "agro_dairy_processing"),
    ("mohali", "Mohali", "30.7046", "76.7179", "it_pharma_admin"),
    ("muktsar", "Muktsar", "30.4730", "74.5120", "agro_dairy_processing"),
    ("pathankot", "Pathankot", "32.2747", "75.6421", "heritage_border_tourism"),
    ("patiala", "Patiala", "30.3398", "76.3869", "it_pharma_admin"),
    ("rupnagar", "Rupnagar", "31.0400", "76.5300", "local_services_infrastructure"),
    ("sangrur", "Sangrur", "30.2450", "75.8440", "agro_dairy_processing"),
    ("shaheed-bhagat-singh-nagar", "Shaheed Bhagat Singh Nagar", "31.0990", "76.0990", "local_services_infrastructure"),
    ("tarn-taran", "Tarn Taran", "31.4510", "74.9280", "heritage_border_tourism"),
]

CATEGORIES_COPIES = {
    "industrial_manufacturing": {
        "tagline": "Hosiery & knitwear clusters · cycle & auto parts · sports goods · hand tools & rubber industry",
        "hero_stat_target": "30",
        "why_features": [
            ("Industrial hub GBP dominance", "We optimize Google Business Profiles for Ludhiana's hosiery powerhouses and Jalandhar's sports goods factories — ensuring you rank in B2B industrial searches."),
            ("B2B product catalog SEO", "We target wholesale hosiery, cycle parts, hand tools, and sports equipment keywords to connect Punjab's manufacturers with national and international buyers."),
            ("Export keyword targeting", "Punjab's industrial hubs export globally. We optimize for international B2B buyer terms, trade directories, and export compliance keywords."),
            ("Multilingual Punjabi-Hindi SEO", "Industrial buyers search in Punjabi, Hindi, and English. We build parallel content and schema for all three search variants.")
        ],
        "testimonials": {
            "quote": "Our hosiery manufacturing unit in Ludhiana was losing orders to online aggregators. NEXUS rebuilt our product catalog pages, optimized our GBP, and drove a 4x increase in direct wholesale inquiries within 5 months.",
            "author": "Harpreet Singh Gill",
            "role": "Director, Gill Hosiery Mills · Ludhiana",
            "avatar": "HG"
        },
        "pricing_desc_local": "For single-unit hosiery workshops, local parts dealers, and small sports goods manufacturers.",
        "pricing_desc_growth": "For expanding manufacturing brands, mid-size exporters, and regional industrial distributors.",
        "pricing_desc_authority": "For large industrial conglomerates, national hosiery brands, and international sports goods exporters.",
        "faqs": [
            ("How does SEO help Ludhiana hosiery manufacturers?", "It positions your factory directly in front of retail chains, corporate uniform buyers, and international importers searching for direct manufacturers — cutting out broker margins."),
            ("Can you rank Jalandhar sports goods for global buyers?", "Yes, we build multilingual product pages, target international trade keywords, and secure backlinks from global sports equipment directories and trade portals.")
        ]
    },
    "it_pharma_admin": {
        "tagline": "IT City Mohali tech corridor · pharma clusters · educational hubs · state administration",
        "hero_stat_target": "24",
        "why_features": [
            ("Mohali IT park visibility", "We configure advanced organization and SaaS schema aligned with Mohali's IT City business district to capture high-value B2B tech queries."),
            ("Pharma & healthcare schema", "Medical and pharma sites fall under Google's YMYL guidelines. We build detailed E-E-A-T profiles, medical schema, and credentialed author pages."),
            ("Startup link building", "Acquiring high-power backlinks from top tech directories, SaaS columns, startup news networks, and educational publications."),
            ("University & coaching SEO", "Patiala and Mohali have major universities and coaching centers. We rank educational brands for competitive admission and course queries.")
        ],
        "testimonials": {
            "quote": "Our SaaS consulting firm in Mohali IT City needed enterprise leads. NEXUS restructured our service pages, built technical content, and ranked us top-3 for IT consulting queries in the Chandigarh tricity.",
            "author": "Ramandeep Kaur",
            "role": "CEO, Kaur Tech Solutions · Mohali",
            "avatar": "RK"
        },
        "pricing_desc_local": "For IT City consultants, independent pharma retailers, and local coaching centers.",
        "pricing_desc_growth": "For expanding SaaS brands, regional pharma distributors, and mid-size educational institutions.",
        "pricing_desc_authority": "For enterprise technology groups, large pharma manufacturers, and university-level institutions.",
        "faqs": [
            ("How long does SEO take for Mohali IT firms?", "Expect local maps visibility within 60 days. Harder national B2B and SaaS keywords require 4-6 months of consistent content and link building."),
            ("Can you rank pharma companies in Patiala?", "Yes, we build YMYL-compliant content, implement medical schema, and establish E-E-A-T credentials for pharma brands.")
        ]
    },
    "agro_dairy_processing": {
        "tagline": "Wheat & rice mills · cotton ginning · dairy cooperatives · sugar refineries · agricultural mandis",
        "hero_stat_target": "20",
        "why_features": [
            ("Agro commodity keyword mapping", "We target wholesale wheat, rice, cotton, and dairy supply keywords to connect Punjab's mandis and mills with national food processors and buyers."),
            ("Cold storage & mill GBP setup", "Optimizing map listings for cold storages, rice mills, cotton gins, and sugar factories scattered across rural Punjab with inaccurate map coordinates."),
            ("Seasonal crop campaign SEO", "Punjab's farming is seasonal. We plan content calendars around rabi and kharif harvest cycles to capture peak-demand agricultural search volumes."),
            ("Cooperative & mandi review systems", "In agri-trade, trust is everything. We build structured review acquisition workflows from local farmers, dealers, and cooperative members.")
        ],
        "testimonials": {
            "quote": "We run a wheat and rice processing mill in Bathinda. NEXUS optimized our storage listings, targeted wholesale grain keywords, and connected us with 4 major food processing contracts in 6 months.",
            "author": "Gurpreet Singh Sidhu",
            "role": "Director, Sidhu Agro Mills · Bathinda",
            "avatar": "GS"
        },
        "pricing_desc_local": "For single-location mills, small dairy cooperatives, and local mandi commission agents.",
        "pricing_desc_growth": "For regional food processing brands and mid-size agricultural distributors.",
        "pricing_desc_authority": "For large sugar refineries, national grain exporters, and statewide dairy corporations.",
        "faqs": [
            ("How does local SEO help rice mills in Punjab?", "It connects your processing unit directly with wholesale traders, food brands, and government procurement agencies searching for verified suppliers online."),
            ("Can you rank dairy cooperatives in Bathinda?", "Yes, we optimize cooperative listings, build supply chain content, and target wholesale dairy product keywords for B2B buyer visibility.")
        ]
    },
    "heritage_border_tourism": {
        "tagline": "Golden Temple pilgrimage · Wagah border tourism · Pathankot adventure · border trade corridors",
        "hero_stat_target": "22",
        "why_features": [
            ("Pilgrimage & heritage schema", "We implement rich hotel, tour package, and attraction schema for Golden Temple area hotels and guesthouses — securing prominent maps placements."),
            ("Global Sikh tourism SEO", "Amritsar attracts international Sikh pilgrims. We rank hospitality brands for Punjabi, English, and international travel queries from UK, Canada, and Australia."),
            ("Adventure & border tourism", "Pathankot adventure tourism and Wagah border ceremonies drive massive footfall. We optimize for real-time travel queries and mobile voice searches."),
            ("Border trade logistics SEO", "Ferozepur and Amritsar are border trade corridors. We target cross-border logistics, customs clearing, and Indo-Pak trade keywords.")
        ],
        "testimonials": {
            "quote": "Our heritage hotel near Golden Temple was losing bookings to OTAs. NEXUS ranked us for direct pilgrimage hotel queries, reducing our OTA commission costs by 60% and tripling direct bookings.",
            "author": "Manpreet Kaur Bedi",
            "role": "Owner, Bedi Heritage Stays · Amritsar",
            "avatar": "MB"
        },
        "pricing_desc_local": "For local guesthouses, tour guides, dhaba restaurants, and small travel agents.",
        "pricing_desc_growth": "For regional hotel chains, pilgrimage transport services, and adventure booking portals.",
        "pricing_desc_authority": "For luxury heritage resorts, international travel brands, and large hospitality groups.",
        "faqs": [
            ("How does SEO help hotels near Golden Temple?", "It captures pilgrims and tourists searching in real-time for rooms, heritage experiences, and langar visit guides — allowing them to book directly instead of through OTAs."),
            ("Can you rank Pathankot adventure tourism businesses?", "Yes, we design activity landing pages, optimize for adventure sport keywords like paragliding and trekking, and manage local map rankings.")
        ]
    },
    "light_manufacturing_trade": {
        "tagline": "Railway coach factories · furniture & woodwork · light engineering · agricultural implements",
        "hero_stat_target": "16",
        "why_features": [
            ("Niche manufacturing GBP", "We verify, optimize, and defend Google Business Profiles for furniture workshops, agricultural implement dealers, and railway component suppliers."),
            ("Product catalog structured data", "We implement detailed product schema for furniture catalogs, woodwork specifications, and agricultural tool listings to rank in niche buyer searches."),
            ("Service area SEO expansion", "We extend your visibility beyond your district into surrounding areas, capturing search demand from adjacent markets with low competition."),
            ("Trade directory link building", "Building authority through backlinks from manufacturing directories, engineering publications, and furniture trade associations.")
        ],
        "testimonials": {
            "quote": "Our furniture workshop in Hoshiarpur depended entirely on showroom walk-ins. NEXUS built our product catalog online, optimized our GBP, and we now receive 35% of orders through organic search.",
            "author": "Rajinder Kumar",
            "role": "Proprietor, Kumar Furniture Works · Hoshiarpur",
            "avatar": "RK"
        },
        "pricing_desc_local": "For individual workshops, small furniture showrooms, and local implement dealers.",
        "pricing_desc_growth": "For expanding furniture brands, regional agricultural dealers, and mid-size engineering firms.",
        "pricing_desc_authority": "For large manufacturing units, national furniture retailers, and industrial component exporters.",
        "faqs": [
            ("How does SEO help furniture businesses in Hoshiarpur?", "It makes your workshop discoverable to interior designers, corporate buyers, and consumers searching for custom furniture — expanding beyond showroom-only sales."),
            ("Can you rank agricultural implement dealers?", "Yes, we optimize product listings, target farming equipment keywords, and build backlinks from agricultural trade directories.")
        ]
    },
    "local_services_infrastructure": {
        "tagline": "Private clinics & diagnostics · education centers · local retail · small manufacturing units",
        "hero_stat_target": "14",
        "why_features": [
            ("Hyperlocal GBP dominance", "In smaller districts, being the #1 Google Maps result is everything. We verify, optimize, and defend your local listing against competitors."),
            ("Service area SEO expansion", "We extend your visibility beyond your district into surrounding talukas and blocks, capturing search demand from adjacent areas with no local competition."),
            ("Review acquisition & trust building", "Local buyers trust reviews more than advertising. We implement structured review workflows that build social proof and improve local pack rankings."),
            ("Mobile-first speed optimization", "Smaller district users are heavily mobile-dependent. We optimize core web vitals, page speed, and mobile UX to ensure fast, frictionless discovery.")
        ],
        "testimonials": {
            "quote": "Our diagnostic center in Fatehgarh Sahib had zero online visibility. NEXUS set up our GBP, built service pages, and within 2 months we were the top result for blood test and pathology lab queries.",
            "author": "Dr. Navjot Singh",
            "role": "Director, Singh Diagnostics · Fatehgarh Sahib",
            "avatar": "NS"
        },
        "pricing_desc_local": "For single-location clinics, tuition centers, small shops, and local service providers.",
        "pricing_desc_growth": "For expanding diagnostic chains, regional coaching centers, and multi-location dealerships.",
        "pricing_desc_authority": "For district-level hospital networks, large educational institutions, and construction firms.",
        "faqs": [
            ("Is SEO worth it for small-town businesses in Punjab?", "Absolutely. In smaller districts, competition is low — meaning faster rankings, lower cost, and disproportionately high returns from being the #1 local result."),
            ("How quickly can my clinic rank in a small Punjab district?", "In low-competition districts, GBP optimization alone can produce top-3 maps rankings within 30 days. Full organic results follow in 60-90 days.")
        ]
    }
}
