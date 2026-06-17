"""District data and templates for 35 Maharashtra local SEO landing pages.
"""

DISTRICTS = [
    ("ahilyanagar", "Ahilyanagar", "19.0948", "74.7480", "industrial_manufacturing"),
    ("akola", "Akola", "20.7002", "77.0082", "agriculture_forest_mineral"),
    ("amaravati", "Amaravati", "20.9320", "77.7523", "agriculture_forest_mineral"),
    ("beed", "Beed", "18.9902", "75.7601", "agriculture_forest_mineral"),
    ("bhandara", "Bhandara", "21.1714", "79.6547", "agriculture_forest_mineral"),
    ("buldhana", "Buldhana", "20.5317", "76.1842", "agriculture_forest_mineral"),
    ("chandrapur", "Chandrapur", "19.9615", "79.2961", "agriculture_forest_mineral"),
    ("dharashiv", "Dharashiv", "18.1861", "76.0419", "agriculture_forest_mineral"),
    ("dhule", "Dhule", "20.9042", "74.7749", "agriculture_forest_mineral"),
    ("gadchiroli", "Gadchiroli", "20.1005", "80.0001", "agriculture_forest_mineral"),
    ("gondia", "Gondia", "21.4598", "80.1950", "agriculture_forest_mineral"),
    ("hingoli", "Hingoli", "19.7214", "77.1420", "agriculture_forest_mineral"),
    ("jalgaon", "Jalgaon", "21.0077", "75.5626", "textiles_agro_processing"),
    ("jalna", "Jalna", "19.8410", "75.8864", "textiles_agro_processing"),
    ("kolhapur", "Kolhapur", "16.7050", "74.2433", "industrial_manufacturing"),
    ("latur", "Latur", "18.4088", "76.5604", "agriculture_forest_mineral"),
    ("mumbai-city", "Mumbai City", "18.9690", "72.8210", "finance_corp"),
    ("mumbai-suburban", "Mumbai Suburban", "19.1300", "72.8750", "it_tech"),
    ("nagpur", "Nagpur", "21.1458", "79.0882", "industrial_manufacturing"),
    ("nanded", "Nanded", "19.1628", "77.3176", "agriculture_forest_mineral"),
    ("nandurbar", "Nandurbar", "21.7456", "74.1245", "agriculture_forest_mineral"),
    ("nashik", "Nashik", "19.9975", "73.7898", "industrial_manufacturing"),
    ("palghar", "Palghar", "19.6974", "72.7659", "industrial_manufacturing"),
    ("parbhani", "Parbhani", "19.2608", "76.7748", "agriculture_forest_mineral"),
    ("pune", "Pune", "18.5204", "73.8567", "it_tech"),
    ("raigad", "Raigad", "18.5158", "72.9333", "ports_coastal"),
    ("ratnagiri", "Ratnagiri", "16.9902", "73.3120", "ports_coastal"),
    ("sangli", "Sangli", "16.8524", "74.5815", "textiles_agro_processing"),
    ("satara", "Satara", "17.6805", "73.9918", "agriculture_forest_mineral"),
    ("sindhudurg", "Sindhudurg", "16.1264", "73.5684", "ports_coastal"),
    ("solapur", "Solapur", "17.6599", "75.9064", "textiles_agro_processing"),
    ("thane", "Thane", "19.2183", "72.9781", "it_tech"),
    ("wardha", "Wardha", "20.7453", "78.6022", "agriculture_forest_mineral"),
    ("washim", "Washim", "20.1010", "77.1328", "agriculture_forest_mineral"),
    ("yavatmal", "Yavatmal", "20.3888", "78.1311", "agriculture_forest_mineral")
]

CATEGORIES_COPIES = {
    "it_tech": {
        "tagline": "IT parks · enterprise software · SaaS tech stars · technology consulting",
        "hero_stat_target": "25",
        "why_features": [
            ("Hinjewadi & Magarpatta tech SEO", "We optimize tech startup and IT services portals to rank for competitive global and regional transactional queries, aligning metadata with major tech park centers."),
            ("Enterprise link acquisitions", "Securing high-authority contextual links from leading technology platforms, SaaS directories, and global startup columns."),
            ("Mobile-first JS optimization", "Pune and Thane mobile search behavior is heavy. We configure server-side rendering pathways and optimize Core Web Vitals for immediate loading."),
            ("E-E-A-T institutional trust", "Aligning local schema with corporate office codes and setting clear author bylines to establish industry authority.")
        ],
        "testimonials": {
            "quote": "Our B2B SaaS startup in Pune's Hinjewadi tech zone saw organic growth of 5x within 6 months of onboarding NEXUS. Their Core Web Vitals optimization and JS rendering tactics solved our indexation gaps.",
            "author": "Sarang Deshmukh",
            "role": "Founder, SaaSFlow India · Pune",
            "avatar": "SD"
        },
        "pricing_desc_local": "For early-stage technology startups and local software consulting firms.",
        "pricing_desc_growth": "For expanding SaaS platforms and digital agencies capturing regional Maharashtra networks.",
        "pricing_desc_authority": "For enterprise technology groups, multi-location software brands, and high-growth startups.",
        "faqs": [
            ("How long does SEO take for Pune tech startups?", "Due to high competition in IT hubs like Hinjewadi, local map pack rankings take 45-60 days, while global B2B organic keywords require 4-6 months to build competitive topical authority."),
            ("Do you rank SaaS products in Thane?", "Yes, we optimize product directories, implement review schema, and target transactional B2B keywords to drive demo signups.")
        ]
    },
    "finance_corp": {
        "tagline": "Financial consultancies · wealth managers · corporate offices · stock advisors",
        "hero_stat_target": "32",
        "why_features": [
            ("BKC & Nariman Point schema", "We configure advanced organization and financial service schema aligned with Mumbai's primary financial business districts."),
            ("High-trust author profiles", "Google ranks financial sites under YMYL (Your Money or Your Life). We build detailed, credentialed author profiles to satisfy E-E-A-T benchmarks."),
            ("Digital PR & high-authority links", "Acquiring authority mentions and editorial links from premium financial journals, business newspapers, and corporate portals."),
            ("Bilingual search integration", "Trading and wealth clients search in English and Hinglish. We optimize metadata for both search behaviors to capture all transactional traffic.")
        ],
        "testimonials": {
            "quote": "NEXUS optimized our wealth management portal in Nariman Point. In 4 months, organic leads grew by 3.5x and we achieved rank #1 for major investment consulting search terms.",
            "author": "Meera Shah",
            "role": "Managing Partner, Shah Wealth Advisors · Mumbai",
            "avatar": "MS"
        },
        "pricing_desc_local": "For independent wealth managers and single-location financial advisors.",
        "pricing_desc_growth": "For regional advisory firms and brokerage groups targeting NCR and Western India markets.",
        "pricing_desc_authority": "For national wealth consultancies, banking networks, and enterprise investment portals.",
        "faqs": [
            ("How do you rank wealth management firms in Mumbai?", "We focus heavily on E-E-A-T and YMYL optimization, refining credentials, author profiles, and acquiring high-authority financial backlinks to build topical credibility."),
            ("Do you manage Google Business Profiles for Nariman Point offices?", "Yes. GBP verification, category optimization, geotagged office photos, and regular post scheduling are fully covered.")
        ]
    },
    "industrial_manufacturing": {
        "tagline": "Automotive clusters · engineering plants · manufacturing units · industrial trade",
        "hero_stat_target": "20",
        "why_features": [
            ("B2B industrial catalog SEO", "We optimize heavy machinery and automotive parts product catalogs to rank for technical product codes and wholesale specifications."),
            ("MIDC industrial zone targeting", "Resolving duplicate map listings and optimizing coordinates in MIDC corridors (Chinchwad, Ambad, Waluj) to secure local map packs."),
            ("International wholesale links", "Securing contextually relevant links from global trade boards, industrial directories, and export portals."),
            ("Technical crawl efficiency", "Heavy catalogs have crawl budget issues. We clean index directives, manage faceted search filters, and ensure fast index paths.")
        ],
        "testimonials": {
            "quote": "Our engineering components manufacturing plant in Nashik was completely invisible online. NEXUS overhauled our product catalogs and optimized our map listing, leading to a 3x increase in bulk B2B inquiries.",
            "author": "Prasad Kulkarni",
            "role": "Director, Kulkarni Precision Engineering · Nashik",
            "avatar": "PK"
        },
        "pricing_desc_local": "For small-scale manufacturing units and local engineering workshops.",
        "pricing_desc_growth": "For MIDC-based manufacturers and regional component exporters.",
        "pricing_desc_authority": "For national industrial groups, large auto component factories, and heavy exporters.",
        "faqs": [
            ("Can you rank my MIDC Nashik factory for global export queries?", "Yes, we build multilingual landing pages, target international B2B buyer terms, and optimize catalog structures for global crawl pathways."),
            ("What is the typical timeline for industrial local maps rankings?", "We see map pack movement in MIDC zones within 30-45 days by resolving NAP errors and building local citations.")
        ]
    },
    "ports_coastal": {
        "tagline": "Maritime logistics · fisheries trade · coastal tourism · horticulture exports",
        "hero_stat_target": "18",
        "why_features": [
            ("Coastal tourism & hospitality pack", "We optimize local listings for beach resorts and travel agencies, capturing mobile travelers searching for accommodations in real-time."),
            ("Logistics & shipping route SEO", "Ranking maritime logistics providers and cargo agents for high-intent port transportation routes."),
            ("Local directory citation networks", "Enriching local NAP data mapped to coastal pin codes (415xxx, 416xxx) for local authority."),
            ("Voice search for agri-export", "Alphonso mango and cashew exporters search via voice in Marathi and Hindi. We structure FAQs to capture these voice intents.")
        ],
        "testimonials": {
            "quote": "We run a coastal resort and horticulture export house in Ratnagiri. NEXUS ranked us #1 for Alphonso mango trade queries and luxury coastal resort terms, doubling our bookings.",
            "author": "Aniket Sawant",
            "role": "Owner, Sawant Coastal Resorts · Ratnagiri",
            "avatar": "AS"
        },
        "pricing_desc_local": "For boutique beach resorts, local homestays, and local cold storage setups.",
        "pricing_desc_growth": "For regional logistics providers and large horticulture exporters.",
        "pricing_desc_authority": "For shipping lines, large port operators, and national travel networks.",
        "faqs": [
            ("How does SEO help Ratnagiri mango exporters?", "It positions your website in front of national and international buyers searching for authentic, bulk agricultural exports, cutting out the middlemen."),
            ("Do you optimize listings for Konkan beach hotels?", "Yes, we configure hotel schemas, integrate booking pathways, and manage reviews to push you to the top of Google's travel packs.")
        ]
    },
    "textiles_agro_processing": {
        "tagline": "Textile powerlooms · sugar processing · grape trade · agro-industrial networks",
        "hero_stat_target": "22",
        "why_features": [
            ("Bulk textile search maps", "We optimize direct-to-buyer search queries for uniform manufacturers, powerlooms, and garment trade buyers."),
            ("Sugar & agro processing schemas", "Implementing custom product and manufacturing schemas to display certifications and technical specifications."),
            ("Local trade citation cleanups", "Building clean directory listings across agro-industrial corridors to boost map placement."),
            ("Hinglish trade queries", "Traders search using mixed keywords like 'Solapur chadar wholesale price'. We optimize metadata to match these exact query terms.")
        ],
        "testimonials": {
            "quote": "Our Solapur textile manufacturing unit was dependent on third-party trade agents. NEXUS ranked our catalog on page-1 for wholesale uniforms and home textiles, driving direct bulk orders.",
            "author": "Siddhesh Shah",
            "role": "Managing Director, Shah Powerloom Fabrics · Solapur",
            "avatar": "SS"
        },
        "pricing_desc_local": "For local weavers, powerloom owners, and agro-retailers.",
        "pricing_desc_growth": "For regional textile brands and cooperative sugar factories.",
        "pricing_desc_authority": "For national textile exporters, sugar consortiums, and large grape trading networks.",
        "faqs": [
            ("How does local SEO help textile manufacturers in Solapur?", "By ranking your catalog for wholesale queries, allowing retail buyers to contact your factory directly for bulk contracts."),
            ("Can you rank agro-processing mills for wholesale sugarcane trade?", "Yes, we build local crop-trading landing pages, optimize for regional mandis, and build authoritative regional links.")
        ]
    },
    "agriculture_forest_mineral": {
        "tagline": "Pulse mandis · grain trade · forest products · regional mineral logistics",
        "hero_stat_target": "16",
        "why_features": [
            ("Mandi trade optimization", "We target commercial agricultural and mining supply terms to connect local traders with national buyers."),
            ("Geo-tagged warehousing GBP", "Optimizing Google Business Profiles with verified storage facilities and geotagged imagery for high local map pack rankings."),
            ("Regional citation maps", "Structuring citations across Maharashtra's tier-2 and tier-3 postcodes to secure geographic authority."),
            ("Bilingual search tags", "Agri-traders search heavily in Marathi and Hindi. We optimize voice search FAQ schemas to capture regional buyer behavior.")
        ],
        "testimonials": {
            "quote": "Our pulse processing and cold storage unit in Latur needed bulk trade contracts. NEXUS optimized our maps and ranked us for wholesale dal storage terms, bringing us inquiries from three new states.",
            "author": "Ganesh Jadhav",
            "role": "Partner, Jadhav Agro Storage · Latur",
            "avatar": "GJ"
        },
        "pricing_desc_local": "For local traders, mandi agents, and single-location cold storages.",
        "pricing_desc_growth": "For regional grain distributors, pulse mills, and logistics agencies.",
        "pricing_desc_authority": "For state-wide agricultural cooperatives, national crop traders, and mining firms.",
        "faqs": [
            ("How does local SEO help Latur pulse traders?", "It makes your storage and wholesale trading business discoverable to food processing companies and commodity buyers nationwide."),
            ("Do you optimize listings for forest and mineral mining areas?", "Yes, we configure map coordinates, establish NAP consistency, and target B2B logistical route queries.")
        ]
    }
}
