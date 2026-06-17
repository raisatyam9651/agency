"""District data and templates for 38 Bihar local SEO landing pages.
"""

DISTRICTS = [
    ("araria", "Araria", "26.1487", "87.5219", "mandi_trade_logistics"),
    ("arwal", "Arwal", "25.2400", "84.6900", "local_services_infrastructure"),
    ("aurangabad", "Aurangabad", "24.7500", "84.3700", "local_services_infrastructure"),
    ("banka", "Banka", "24.8800", "86.9200", "handicrafts_textiles"),
    ("begusarai", "Begusarai", "25.4200", "86.1300", "agro_processing_mills"),
    ("bhagalpur", "Bhagalpur", "25.2425", "86.9842", "handicrafts_textiles"),
    ("bhojpur", "Bhojpur", "25.5600", "84.5200", "heritage_pilgrimage_tourism"),
    ("buxar", "Buxar", "25.5764", "83.9777", "local_services_infrastructure"),
    ("darbhanga", "Darbhanga", "26.1542", "85.8918", "handicrafts_textiles"),
    ("east-champaran", "East Champaran", "26.6400", "84.8500", "agro_processing_mills"),
    ("gaya", "Gaya", "24.7955", "84.9994", "heritage_pilgrimage_tourism"),
    ("gopalganj", "Gopalganj", "26.4700", "84.4400", "local_services_infrastructure"),
    ("jamui", "Jamui", "24.9200", "86.2200", "local_services_infrastructure"),
    ("jehanabad", "Jehanabad", "25.2100", "84.9900", "local_services_infrastructure"),
    ("kaimur", "Kaimur", "25.0400", "83.6100", "local_services_infrastructure"),
    ("katihar", "Katihar", "25.5390", "87.5719", "mandi_trade_logistics"),
    ("khagaria", "Khagaria", "25.5023", "86.4735", "mandi_trade_logistics"),
    ("kishanganj", "Kishanganj", "26.0900", "87.9400", "mandi_trade_logistics"),
    ("lakhisarai", "Lakhisarai", "25.1600", "86.0900", "local_services_infrastructure"),
    ("madhepura", "Madhepura", "25.9200", "86.7900", "mandi_trade_logistics"),
    ("madhubani", "Madhubani", "26.3500", "86.0700", "handicrafts_textiles"),
    ("munger", "Munger", "25.3708", "86.4735", "local_services_infrastructure"),
    ("muzaffarpur", "Muzaffarpur", "26.1209", "85.3647", "agro_processing_mills"),
    ("nalanda", "Nalanda", "25.1300", "85.4400", "heritage_pilgrimage_tourism"),
    ("nawada", "Nawada", "24.8800", "85.5300", "local_services_infrastructure"),
    ("patna", "Patna", "25.6093", "85.1376", "admin_tech_finance"),
    ("purnia", "Purnia", "25.7771", "87.4753", "mandi_trade_logistics"),
    ("rohtas", "Rohtas", "24.9600", "84.0200", "agro_processing_mills"),
    ("saharsa", "Saharsa", "25.8800", "86.6000", "mandi_trade_logistics"),
    ("samastipur", "Samastipur", "25.8581", "85.7787", "agro_processing_mills"),
    ("saran", "Saran", "25.8400", "84.7500", "local_services_infrastructure"),
    ("sheikhpura", "Sheikhpura", "25.1400", "85.8500", "local_services_infrastructure"),
    ("sheohar", "Sheohar", "26.5100", "85.2900", "local_services_infrastructure"),
    ("sitamarhi", "Sitamarhi", "26.5900", "85.4900", "local_services_infrastructure"),
    ("siwan", "Siwan", "26.2200", "84.3600", "local_services_infrastructure"),
    ("supaul", "Supaul", "26.1200", "86.6000", "local_services_infrastructure"),
    ("vaishali", "Vaishali", "25.6800", "85.2100", "agro_processing_mills"),
    ("west-champaran", "West Champaran", "26.7200", "84.5000", "agro_processing_mills"),
]

CATEGORIES_COPIES = {
    "admin_tech_finance": {
        "tagline": "State capital IT services · coaching clusters · legal & financial advisory · digital startups",
        "hero_stat_target": "28",
        "why_features": [
            ("Patna corporate GBP dominance", "We optimize Google Business Profiles for coaching centers, legal firms, diagnostics, and IT consultancies packed in dense capital city corridors — ensuring you rank in local pack searches."),
            ("Competitive coaching SEO", "Patna is India's coaching capital after Kota. We build topical authority and local citations that outrank franchise aggregators for coaching-related queries."),
            ("Multi-sector schema deployment", "From hospital schema to legal service markup — we configure JSON-LD structured data tailored to Patna's diverse professional sectors."),
            ("Hindi + Hinglish voice intent", "Patna buyers search in Hindi and Hinglish. We optimize FAQ schemas, voice queries, and bilingual landing pages for both variants.")
        ],
        "testimonials": {
            "quote": "Our legal advisory firm in Boring Road was invisible online. NEXUS restructured our Google Business Profile, built out service pages, and ranked us top-3 for civil lawyer queries in Patna within 60 days.",
            "author": "Ankit Srivastava",
            "role": "Partner, Srivastava & Associates · Patna",
            "avatar": "AS"
        },
        "pricing_desc_local": "For independent consultants, local coaching centers, and small clinics in Patna.",
        "pricing_desc_growth": "For expanding coaching chains, mid-size hospitals, and regional IT consultancies.",
        "pricing_desc_authority": "For large hospital networks, enterprise-level coaching brands, and statewide legal firms.",
        "faqs": [
            ("How does SEO help coaching institutes in Patna?", "It positions your coaching brand directly in front of students and parents searching for competitive exam preparation in Patna, reducing your dependence on offline banners and pamphlets."),
            ("Can you rank Patna hospitals for city-wide medical queries?", "Yes, we optimize multi-location GBP listings, build medical schema, and target condition-specific long-tail keywords for hospitals and diagnostics.")
        ]
    },
    "agro_processing_mills": {
        "tagline": "Sugar & rice mills · litchi & mango processing · dairy cooperatives · agricultural cold storage",
        "hero_stat_target": "22",
        "why_features": [
            ("Agro commodity keyword mapping", "We target wholesale rice, sugar, litchi, and dairy supply keywords to connect Bihar's mandis and processing units with national buyers."),
            ("Cold storage & mill GBP setup", "Optimizing map listings for cold storages, rice mills, and sugar factories scattered in semi-urban zones with inaccurate coordinates."),
            ("Seasonal product campaign SEO", "Bihar's litchi and mango trade is seasonal. We plan content and campaign calendars around harvest cycles to capture peak-demand search volumes."),
            ("Farmer & dealer review loops", "In agri-commerce, reviews are the highest trust signal. We build structured review acquisition workflows from local dealers and cooperative members.")
        ],
        "testimonials": {
            "quote": "We run a rice and wheat cold storage network in Begusarai. NEXUS optimized our storage listings, ran seasonal keyword campaigns, and brought in 3 national food processing contracts within 4 months.",
            "author": "Rajesh Yadav",
            "role": "Director, Yadav Agri Cold Chain · Begusarai",
            "avatar": "RY"
        },
        "pricing_desc_local": "For single-location mills, local cold storages, and small dairy cooperatives.",
        "pricing_desc_growth": "For regional food processing brands and mid-size agricultural distributors.",
        "pricing_desc_authority": "For large sugar mills, national rice exporters, and statewide dairy corporations.",
        "faqs": [
            ("How does local SEO help rice mills in Bihar?", "It connects your processing unit directly with wholesale traders, food brands, and government procurement agencies searching for verified suppliers online."),
            ("Can you rank seasonal litchi businesses in Muzaffarpur?", "Yes, we build seasonal SEO content, optimize GBP with seasonal products, and launch timed backlink campaigns during harvest-to-market cycles.")
        ]
    },
    "heritage_pilgrimage_tourism": {
        "tagline": "Bodh Gaya pilgrimage · Nalanda & Rajgir heritage · temple tourism · boutique hospitality",
        "hero_stat_target": "18",
        "why_features": [
            ("Pilgrimage & heritage schema", "We implement rich hotel, tour package, and attraction schema showing room configurations, travel itineraries, and coordinates to secure maps placements."),
            ("Global Buddhist tourism SEO", "Bodh Gaya attracts international Buddhist pilgrims. We rank your hospitality brand for English, Japanese, Thai, and Korean travel queries."),
            ("Mobile voice-intent search", "Tourists on the move search using voice. We optimize FAQ content and local listings for quick voice answers about nearby hotels, guides, and transport."),
            ("High-authority travel backlinks", "Acquiring organic links from travel publications, pilgrimage portals, and international heritage directories to build domain authority.")
        ],
        "testimonials": {
            "quote": "Our boutique guesthouse near Bodh Gaya temple was dependent on walk-ins. NEXUS ranked us for international Buddhist pilgrimage hotel queries, tripling our direct bookings in one season.",
            "author": "Prabhas Kumar",
            "role": "Owner, Bodhi Tree Heritage Stay · Gaya",
            "avatar": "PK"
        },
        "pricing_desc_local": "For local guesthouses, tour guides, and small travel agents near heritage sites.",
        "pricing_desc_growth": "For regional hotel chains, pilgrimage transport services, and activity booking portals.",
        "pricing_desc_authority": "For luxury heritage resorts, international travel brands, and large hospitality groups.",
        "faqs": [
            ("How does SEO help hotels near Bodh Gaya?", "It captures pilgrims and tourists searching in real-time for rooms, heritage experiences, and guides — allowing them to book directly with you instead of aggregators."),
            ("Can you rank my travel agency for Nalanda & Rajgir packages?", "Yes, we design focused itinerary landing pages, optimize travel content, and manage local map rankings for heritage circuit keywords.")
        ]
    },
    "handicrafts_textiles": {
        "tagline": "Bhagalpuri Tussar silk · Madhubani art · handloom cooperatives · artisan trade clusters",
        "hero_stat_target": "16",
        "why_features": [
            ("Artisan product catalog SEO", "We optimize handloom and Madhubani art catalogs with detailed product schema — fabric type, weave technique, and certification — to rank in niche craft buyer searches."),
            ("E-commerce & marketplace visibility", "Many artisan sellers rely on marketplaces. We optimize your standalone store to compete with aggregators using structured data and direct-to-consumer landing pages."),
            ("GI-tagged product authority", "Bhagalpuri silk and Madhubani paintings carry GI tags. We build topical authority around these heritage products to establish trust and rank for premium buyer keywords."),
            ("Bilingual buyer optimization", "Craft buyers search in English and Hindi. We optimize page elements for both query behaviors to capture domestic and international art collector leads.")
        ],
        "testimonials": {
            "quote": "Our Bhagalpuri Tussar silk cooperative was losing direct orders to marketplace middlemen. NEXUS built our product pages, optimized our GBP, and we now receive 40% of orders directly through organic search.",
            "author": "Suman Devi",
            "role": "Chairperson, Bhagalpur Silk Weavers Cooperative",
            "avatar": "SD"
        },
        "pricing_desc_local": "For individual artisans, small handloom workshops, and local craft showrooms.",
        "pricing_desc_growth": "For regional craft cooperatives, mid-size silk exporters, and online artisan stores.",
        "pricing_desc_authority": "For national handloom brands, large textile export houses, and GI-tagged product corporations.",
        "faqs": [
            ("How does SEO help Madhubani artists sell online?", "It makes your art directly discoverable to collectors, interior designers, and corporate gifting buyers searching for authentic Madhubani paintings — bypassing marketplace fees."),
            ("Can you rank Bhagalpuri silk for international buyers?", "Yes, we write multilingual content, target international craft buyer keywords, and build backlinks from global textile and fashion directories.")
        ]
    },
    "mandi_trade_logistics": {
        "tagline": "Agricultural mandis · maize & jute trade · grain warehousing · border logistics corridors",
        "hero_stat_target": "20",
        "why_features": [
            ("Mandi & wholesale keyword maps", "We target wholesale crop, grain, and jute supply keywords to connect large mandi operators with food processors, exporters, and government buyers."),
            ("Geotagged warehouse GBP", "Optimizing Google Business Profiles with verified facilities, geotagged imagery, and accurate coordinates for scattered warehousing complexes."),
            ("Cross-border trade visibility", "Districts like Kishanganj and Araria border Nepal and Bangladesh. We optimize for cross-border trade logistics and customs clearing queries."),
            ("Multilingual voice optimization", "Traders search using voice in Hindi and Maithili. We structure FAQ schemas and bilingual content to capture regional trading queries.")
        ],
        "testimonials": {
            "quote": "Our grain warehousing and forwarding business in Purnia was entirely referral-based. NEXUS ranked us for wholesale maize storage and Bihar logistics queries, bringing in corporate contracts from two new states.",
            "author": "Mohammad Irfan",
            "role": "Managing Partner, Purnia Agri Logistics · Purnia",
            "avatar": "MI"
        },
        "pricing_desc_local": "For local mandi commission agents, small warehouses, and border customs brokers.",
        "pricing_desc_growth": "For regional grain trading networks and mid-size logistics providers.",
        "pricing_desc_authority": "For large commodity trading houses, national warehousing chains, and cross-border logistics firms.",
        "faqs": [
            ("How does local SEO help mandi traders in Purnia?", "It positions your warehousing and wholesale trading business in front of food processing companies, commodity buyers, and government procurement portals searching nationwide."),
            ("Do you optimize for cross-border trade queries in Kishanganj?", "Yes, we target customs clearing, border logistics, and Nepal-India trade keywords to capture high-value commercial intent queries.")
        ]
    },
    "local_services_infrastructure": {
        "tagline": "Private clinics & diagnostics · local manufacturing · education centers · stone quarries & construction",
        "hero_stat_target": "14",
        "why_features": [
            ("Hyperlocal GBP dominance", "In smaller districts, being the #1 Google Maps result is everything. We verify, optimize, and defend your local listing against competitors."),
            ("Service area SEO expansion", "We extend your visibility beyond your district into surrounding talukas and blocks, capturing search demand from adjacent areas with no local competition."),
            ("Review acquisition & trust building", "Local buyers trust reviews more than advertising. We implement structured review workflows that build social proof and improve local pack rankings."),
            ("Mobile-first speed optimization", "Smaller district users are heavily mobile-dependent. We optimize core web vitals, page speed, and mobile UX to ensure fast, frictionless discovery.")
        ],
        "testimonials": {
            "quote": "Our diagnostic center in Munger had zero online presence. NEXUS set up our GBP, built service pages, and within 3 months we were the top result for pathology lab and blood test queries in the district.",
            "author": "Dr. Priya Kumari",
            "role": "Director, Kumari Diagnostics · Munger",
            "avatar": "PK"
        },
        "pricing_desc_local": "For single-location clinics, tuition centers, small shops, and local service providers.",
        "pricing_desc_growth": "For expanding diagnostic chains, regional coaching centers, and multi-location dealerships.",
        "pricing_desc_authority": "For district-level hospital networks, large educational institutions, and construction firms.",
        "faqs": [
            ("Is SEO worth it for small-town businesses in Bihar?", "Absolutely. In smaller districts, competition is low — meaning faster rankings, lower cost, and disproportionately high returns from being the #1 local result."),
            ("How quickly can my clinic rank in a small Bihar district?", "In low-competition districts, GBP optimization alone can produce top-3 maps rankings within 30 days. Full organic results follow in 60-90 days.")
        ]
    }
}
