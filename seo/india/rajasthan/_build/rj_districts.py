"""District data and templates for 46 Rajasthan local SEO landing pages.
"""

DISTRICTS = [
    ("ajmer", "Ajmer", "26.4499", "74.6399", "tourism_historic"),
    ("alwar", "Alwar", "27.5530", "76.6346", "industrial_mineral"),
    ("anupgarh", "Anupgarh", "29.1911", "73.2086", "crafts_border"),
    ("balotra", "Balotra", "25.8314", "72.2415", "industrial_mineral"),
    ("banswara", "Banswara", "23.5461", "74.4350", "crafts_border"),
    ("baran", "Baran", "25.1011", "76.5164", "agriculture_mandi"),
    ("barmer", "Barmer", "25.7531", "71.4181", "crafts_border"),
    ("beawar", "Beawar", "26.1012", "74.3230", "industrial_mineral"),
    ("bharatpur", "Bharatpur", "27.2152", "77.5030", "crafts_border"),
    ("bhilwara", "Bhilwara", "25.3484", "74.6433", "industrial_mineral"),
    ("bikaner", "Bikaner", "28.0167", "73.3117", "agriculture_mandi"),
    ("bundi", "Bundi", "25.4418", "75.6366", "tourism_historic"),
    ("chittorgarh", "Chittorgarh", "24.8887", "74.6269", "tourism_historic"),
    ("churu", "Churu", "28.2900", "74.9600", "crafts_border"),
    ("dausa", "Dausa", "26.8900", "76.3300", "crafts_border"),
    ("deeg", "Deeg", "27.4700", "77.3300", "crafts_border"),
    ("didwana-kuchaman", "Didwana Kuchaman", "27.4000", "74.5700", "crafts_border"),
    ("dholpur", "Dholpur", "26.6972", "77.8897", "crafts_border"),
    ("dungarpur", "Dungarpur", "23.8400", "73.7200", "crafts_border"),
    ("hanumangarh", "Hanumangarh", "29.5800", "74.3200", "agriculture_mandi"),
    ("jaipur", "Jaipur", "26.9124", "75.7873", "it_services"),
    ("jaipur-rural", "Jaipur Rural", "26.9200", "75.8000", "it_services"),
    ("jaisalmer", "Jaisalmer", "26.9157", "70.9083", "tourism_historic"),
    ("jalore", "Jalore", "25.3500", "72.6200", "crafts_border"),
    ("jhalawar", "Jhalawar", "24.6000", "76.1500", "agriculture_mandi"),
    ("jhunjhunu", "Jhunjhunu", "28.1300", "75.4000", "crafts_border"),
    ("jodhpur", "Jodhpur", "26.2389", "73.0243", "tourism_historic"),
    ("jodhpur-rural", "Jodhpur Rural", "26.2400", "73.0300", "crafts_border"),
    ("karauli", "Karauli", "26.5000", "77.0200", "crafts_border"),
    ("kekri", "Kekri", "25.9700", "75.1500", "crafts_border"),
    ("khairthal-tijara", "Khairthal Tijara", "27.8000", "76.6300", "crafts_border"),
    ("kota", "Kota", "25.1805", "75.8308", "education_coaching"),
    ("kotputli-behror", "Kotputli Behror", "27.7000", "76.2000", "crafts_border"),
    ("nagaur", "Nagaur", "27.2000", "73.7300", "crafts_border"),
    ("pali", "Pali", "25.7725", "73.3233", "industrial_mineral"),
    ("phalodi", "Phalodi", "27.1300", "72.3700", "crafts_border"),
    ("pratapgarh", "Pratapgarh", "24.0300", "74.7800", "crafts_border"),
    ("rajsamand", "Rajsamand", "25.0700", "73.8800", "industrial_mineral"),
    ("salumber", "Salumber", "24.1300", "74.0500", "crafts_border"),
    ("sawai-madhopur", "Sawai Madhopur", "25.9928", "76.3842", "tourism_historic"),
    ("shahpura", "Shahpura", "25.6300", "74.9300", "crafts_border"),
    ("sikar", "Sikar", "27.6119", "75.1398", "education_coaching"),
    ("sirohi", "Sirohi", "24.8826", "72.8631", "crafts_border"),
    ("sri-ganganagar", "Sri Ganganagar", "29.9038", "73.8772", "agriculture_mandi"),
    ("tonk", "Tonk", "26.1600", "75.7900", "agriculture_mandi"),
    ("udaipur", "Udaipur", "24.5854", "73.7125", "tourism_historic")
]

CATEGORIES_COPIES = {
    "tourism_historic": {
        "tagline": "Palace tourism · heritage hospitality · cultural tours · desert safaris",
        "hero_stat_target": "28",
        "why_features": [
            ("Hospitality schema & mapping", "We implement rich hotel schema showing room configurations, dining options, and local tourist attraction coordinates to secure high local maps placements."),
            ("Global search optimization", "Rajasthan tourism keywords attract heavy international queries. We rank your brand for global travel and holiday search terms."),
            ("Mobile voice-intent search", "Tourists on the move search using voice ('best sunset point Udaipur', 'places to eat in Jaisalmer'). We optimize FAQ content for fast voice answers."),
            ("High-authority travel backlinks", "Acquiring organic links from global travel publications, premium lifestyle blogs, and regional tourism guides.")
        ],
        "testimonials": {
            "quote": "We run a premium heritage hotel in Udaipur. NEXUS optimized our local schema and maps listing. Our organic guest bookings grew by 2.5x in 4 months, cutting down third-party OTA commissions significantly.",
            "author": "Digvijay Singh",
            "role": "Managing Director, Mewar Palace Heritage Hotel · Udaipur",
            "avatar": "DS"
        },
        "pricing_desc_local": "For boutique heritage hotels, local tour guide agencies, and local craft dealers.",
        "pricing_desc_growth": "For premium resort groups, travel portals, and multi-city tour operators.",
        "pricing_desc_authority": "For national hotel chains, luxury palaces, and national tourism portals.",
        "faqs": [
            ("How does local SEO help heritage hotels in Rajasthan?", "It captures tourists searching in real-time for rooms, boutique experiences, and dining, allowing them to book directly with you rather than via commission-heavy travel portals."),
            ("Can you rank my travel agency for desert safaris in Jaisalmer?", "Yes, we design focused activity landing pages, optimize travel itineraries, and manage local map rankings for activity search queries.")
        ]
    },
    "industrial_mineral": {
        "tagline": "Textile processing · marble & granite mining · cement manufacture · mineral logistics",
        "hero_stat_target": "22",
        "why_features": [
            ("B2B wholesale catalogs", "We optimize direct-to-buyer search queries for marble grit, stone blocks, and cement grades with structured product databases."),
            ("Mining cluster maps visibility", "Correcting map listings, coordinates, and local citations in stone mining areas to capture industrial logistics buyers."),
            ("Trade link networks", "Acquiring authority links from global logistics networks, construction journals, and mineral trading platforms."),
            ("Bilingual search tags", "Contractors search using both English and Hinglish terms. We structure keyword maps to capture both buyer groups.")
        ],
        "testimonials": {
            "quote": "Our marble mining and export house in Rajsamand was relying entirely on trade brokers. NEXUS ranked our catalog on page-1 for wholesale granite and marble quarries, bringing us direct buyers from NCR and overseas.",
            "author": "Rajendra Vyas",
            "role": "Partner, Vyas Marble & Mining · Rajsamand",
            "avatar": "RV"
        },
        "pricing_desc_local": "For quarry owners, marble processors, and regional transport agents.",
        "pricing_desc_growth": "For regional mining corporations and stone exporters targeting national building projects.",
        "pricing_desc_authority": "For national cement manufacturers, large mining conglomerates, and international stone exporters.",
        "faqs": [
            ("How do you rank industrial quarry companies in Rajasthan?", "We optimize catalog databases for technical search keywords, clean crawl directives, and build authority links from building material and construction domains."),
            ("Do you rank marble manufacturers for global export?", "Yes, we write multilingual content, target export keywords, and build global trade citations.")
        ]
    },
    "it_services": {
        "tagline": "Modern corporate hubs · tech start-ups · professional consultancies · BPO centers",
        "hero_stat_target": "24",
        "why_features": [
            ("Enterprise B2B search terms", "We rank IT consultancies and BPO agencies for high-value organic queries, capturing key business deciders."),
            ("Thorough technical audits", "Configuring clean site structures, handling JavaScript rendering issues, and optimizing mobile speeds."),
            ("Startup link building", "Acquiring high-power backlinks from top tech directories, SaaS columns, and startup news networks."),
            ("E-E-A-T credentials optimization", "Aligning local citations with tech parks and corporate districts to establish high credibility.")
        ],
        "testimonials": {
            "quote": "Our software consultancy in Jaipur was struggling to capture enterprise client queries. NEXUS rewrote our service pages and optimized our Core Web Vitals, growing our inbound corporate leads by 4x.",
            "author": "Alok Sharma",
            "role": "Founder, DevGrow Technologies · Jaipur",
            "avatar": "AS"
        },
        "pricing_desc_local": "For local software consulting setups and early-stage tech teams.",
        "pricing_desc_growth": "For expanding SaaS startups and regional corporate consultancies.",
        "pricing_desc_authority": "For enterprise technology brands, BPO centers, and VC-funded startups.",
        "faqs": [
            ("How long does SEO take for Jaipur IT firms?", "Expect maps visibility within 60 days. Harder global B2B keywords require 4-6 months of consistent content and link building."),
            ("Do you handle e-commerce SEO for Rajasthani D2C brands?", "Yes, we optimize product directories, category schemas, and checkouts for Shopify and WooCommerce.")
        ]
    },
    "education_coaching": {
        "tagline": "National coaching centres · student housing · university systems · colleges",
        "hero_stat_target": "20",
        "why_features": [
            ("Admission season targeting", "Coaching search volume spikes during admission months (March-June). We optimize content drop cadences to capture parent search behavior."),
            ("Locality search intent maps", "Students and parents search by neighborhood (e.g. 'hostels near landmark kota'). We target localized neighborhood terms."),
            ("High-trust school schema", "Injecting detailed educational institution and FAQ schemas to capture direct search answers."),
            ("Review acquisition loops", "In education, reviews are the highest conversion factor. We build student and parent review collection cycles.")
        ],
        "testimonials": {
            "quote": "We run a premium student housing network and coaching prep center in Kota. NEXUS ranked us #1 for coaching hostel queries, doubling our student inquiries in 90 days before the admission season.",
            "author": "Sunil Birla",
            "role": "Managing Director, Birla Student Housing · Kota",
            "avatar": "SB"
        },
        "pricing_desc_local": "For single-location student hostels, tuition centres, and local schools.",
        "pricing_desc_growth": "For regional coaching institutes, colleges, and student housing networks.",
        "pricing_desc_authority": "For national test prep brands, multi-city educational groups, and universities.",
        "faqs": [
            ("How does SEO help coaching centers in Kota?", "It positions your academy directly in front of parents searching for specialized test prep, increasing admissions without expensive print advertising."),
            ("Do you optimize listings for coaching center hostels?", "Yes, we optimize local listings for student hostels, PG rooms, and coordinate maps to rank you in maps packs.")
        ]
    },
    "agriculture_mandi": {
        "tagline": "Grain mandis · cotton ginning · oilseed warehouses · agricultural logistics",
        "hero_stat_target": "16",
        "why_features": [
            ("Agricultural commodity rankings", "We target wholesale crop, seed, and cotton supply keywords to connect local mandis with food processing buyers."),
            ("Warehousing maps optimization", "Configuring map pins and verifying GBP profiles for remote mandi and warehouse areas."),
            ("Local crop price schemas", "Implementing crop catalog structures and local pricing schemas to establish direct trading credibility."),
            ("Voice search in Hindi & Punjabi", "Farmers and traders search via voice. We structure keyword intents for regional spoken dialects.")
        ],
        "testimonials": {
            "quote": "NEXUS optimized our cold storage and grain trading portal in Sri Ganganagar. Bulk inquiries from out-of-state crop buyers grew by 3x in 3 months by ranking for wholesale agricultural supply queries.",
            "author": "Harpreet Singh",
            "role": "Owner, Singh Grain Traders · Sri Ganganagar",
            "avatar": "HS"
        },
        "pricing_desc_local": "For local crop dealers, cold storage managers, and mandi agents.",
        "pricing_desc_growth": "For regional crop distributors and agricultural logistics companies.",
        "pricing_desc_authority": "For national crop trading organizations, state cooperatives, and bulk storage chains.",
        "faqs": [
            ("How does local SEO help agri-traders in Sri Ganganagar?", "It connects your mandi shop or storage facility with bulk buyers and food manufacturing firms looking for direct supply lines in Rajasthan's grain belt."),
            ("Do you verify listings in rural warehouse zones?", "Yes, we resolve NAP data inconsistencies and manage coordinates in mandi areas to ensure map indexation.")
        ]
    },
    "crafts_border": {
        "tagline": "Artisanal handicrafts · handloom weaving · block prints · local trade checkposts",
        "hero_stat_target": "14",
        "why_features": [
            ("Craft & handloom keyword map", "We target authentic artisanal search terms (block print, handloom, blue pottery) to capture premium design buyers."),
            ("Local citation listings", "Verifying NAP coordinates and building local listings in regional handicraft clusters."),
            ("Export and B2B directories", "Registering your business in high-value trade directories and acquiring links from craft organizations."),
            ("Bilingual product search", "We structure product descriptions in English and Hindi, helping search engines serve both regional and national buyers.")
        ],
        "testimonials": {
            "quote": "Our handloom textile brand in Barmer was relying on local agents. NEXUS ranked us for wholesale block print and handloom fabric terms. We secured wholesale deals with two major design brands in Mumbai and Bangalore.",
            "author": "Khimraj Jain",
            "role": "Founder, Jain Barmer Handlooms · Barmer",
            "avatar": "KJ"
        },
        "pricing_desc_local": "For boutique handicraft shops, local weavers, and retail showrooms.",
        "pricing_desc_growth": "For regional export houses and craft co-ops looking to access national retail chains.",
        "pricing_desc_authority": "For large export corporations, national craft portals, and artisanal guilds.",
        "faqs": [
            ("Can local SEO help Barmer craft shops get wholesale clients?", "Yes, we optimize your site for bulk buyers and export queries, enabling retail houses across major cities to buy directly from your workshop."),
            ("How long does it take to rank for specialized handicrafts?", "Due to lower competition for highly specific crafts, niche pages can rank on page-1 within 45-75 days.")
        ]
    }
}
