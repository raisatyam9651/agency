"""District data and templates for 75 Uttar Pradesh local SEO landing pages.
"""

DISTRICTS = [
    ("agra", "Agra", "27.1767", "78.0081", "tourism_historic"),
    ("aligarh", "Aligarh", "27.8974", "78.0880", "administrative_edu"),
    ("ambedkar-nagar", "Ambedkar Nagar", "26.4180", "82.5204", "agriculture_trade"),
    ("amethi", "Amethi", "26.1557", "81.8015", "agriculture_trade"),
    ("amroha", "Amroha", "28.9056", "78.4682", "handicraft_export"),
    ("auraiya", "Auraiya", "26.4674", "79.5167", "agriculture_trade"),
    ("ayodhya", "Ayodhya", "26.7922", "82.1998", "tourism_historic"),
    ("azamgarh", "Azamgarh", "26.0667", "83.1833", "agriculture_trade"),
    ("baghpat", "Baghpat", "28.9500", "77.2167", "agriculture_trade"),
    ("bahraich", "Bahraich", "27.5750", "81.5944", "agriculture_trade"),
    ("ballia", "Ballia", "25.7667", "84.1500", "agriculture_trade"),
    ("balrampur", "Balrampur", "27.4333", "82.1833", "agriculture_trade"),
    ("banda", "Banda", "25.4833", "80.3333", "agriculture_trade"),
    ("barabanki", "Barabanki", "26.9292", "81.1896", "agriculture_trade"),
    ("bareilly", "Bareilly", "28.3670", "79.4300", "handicraft_export"),
    ("basti", "Basti", "26.8167", "82.7167", "agriculture_trade"),
    ("bhadohi", "Bhadohi", "25.2630", "82.4631", "handicraft_export"),
    ("bijnor", "Bijnor", "29.3724", "78.1359", "agriculture_trade"),
    ("badaun", "Badaun", "28.0500", "79.1167", "agriculture_trade"),
    ("bulandshahr", "Bulandshahr", "28.4100", "77.8500", "agriculture_trade"),
    ("chandauli", "Chandauli", "25.2667", "83.2667", "agriculture_trade"),
    ("chitrakoot", "Chitrakoot", "25.1767", "80.8643", "tourism_historic"),
    ("deoria", "Deoria", "26.5000", "83.7833", "agriculture_trade"),
    ("etah", "Etah", "27.6333", "78.6667", "agriculture_trade"),
    ("etawah", "Etawah", "26.7667", "79.0167", "agriculture_trade"),
    ("farrukhabad", "Farrukhabad", "27.3833", "79.5833", "agriculture_trade"),
    ("fatehpur", "Fatehpur", "25.9333", "80.8000", "agriculture_trade"),
    ("firozabad", "Firozabad", "27.1500", "78.4000", "handicraft_export"),
    ("gautam-buddha-nagar", "Gautam Buddha Nagar", "28.5355", "77.3910", "it_tech"),
    ("ghaziabad", "Ghaziabad", "28.6692", "77.4538", "it_tech"),
    ("ghazipur", "Ghazipur", "25.5833", "83.5833", "agriculture_trade"),
    ("gonda", "Gonda", "27.1300", "81.9600", "agriculture_trade"),
    ("gorakhpur", "Gorakhpur", "26.7606", "83.3731", "administrative_edu"),
    ("hamirpur", "Hamirpur", "25.9500", "80.1500", "agriculture_trade"),
    ("hapur", "Hapur", "28.7251", "77.7760", "agriculture_trade"),
    ("hardoi", "Hardoi", "27.4167", "80.1167", "agriculture_trade"),
    ("hathras", "Hathras", "27.6000", "78.0500", "agriculture_trade"),
    ("jalaun", "Jalaun", "26.0167", "79.4333", "agriculture_trade"),
    ("jaunpur", "Jaunpur", "25.7500", "82.6833", "agriculture_trade"),
    ("jhansi", "Jhansi", "25.4333", "78.5833", "administrative_edu"),
    ("kannauj", "Kannauj", "27.0500", "79.9167", "handicraft_export"),
    ("kanpur-dehat", "Kanpur Dehat", "26.4674", "79.8500", "industrial"),
    ("kanpur-nagar", "Kanpur Nagar", "26.4499", "80.3319", "industrial"),
    ("kasganj", "Kasganj", "27.8100", "78.6500", "agriculture_trade"),
    ("kaushambi", "Kaushambi", "25.3333", "81.3833", "agriculture_trade"),
    ("kushinagar", "Kushinagar", "26.7408", "83.8883", "tourism_historic"),
    ("lakhimpur-kheri", "Lakhimpur Kheri", "27.9500", "80.7833", "agriculture_trade"),
    ("lalitpur", "Lalitpur", "24.6833", "78.4167", "agriculture_trade"),
    ("lucknow", "Lucknow", "26.8467", "80.9462", "administrative_edu"),
    ("maharajganj", "Maharajganj", "27.1500", "83.5667", "agriculture_trade"),
    ("mahoba", "Mahoba", "25.2833", "79.8667", "agriculture_trade"),
    ("mainpuri", "Mainpuri", "27.2333", "79.0333", "agriculture_trade"),
    ("mathura", "Mathura", "27.4924", "77.6737", "tourism_historic"),
    ("mau", "Mau", "25.9500", "83.5667", "agriculture_trade"),
    ("meerut", "Meerut", "28.9845", "77.7064", "administrative_edu"),
    ("mirzapur", "Mirzapur", "25.1500", "82.5833", "handicraft_export"),
    ("moradabad", "Moradabad", "28.8386", "78.7733", "handicraft_export"),
    ("muzaffarnagar", "Muzaffarnagar", "29.4708", "77.7033", "agriculture_trade"),
    ("pilibhit", "Pilibhit", "28.6333", "79.8000", "agriculture_trade"),
    ("pratapgarh", "Pratapgarh", "25.9000", "81.9833", "agriculture_trade"),
    ("prayagraj", "Prayagraj", "25.4358", "81.8463", "administrative_edu"),
    ("raebareli", "Raebareli", "26.2236", "81.2400", "industrial"),
    ("rampur", "Rampur", "28.8124", "79.0267", "agriculture_trade"),
    ("saharanpur", "Saharanpur", "29.9640", "77.5460", "handicraft_export"),
    ("sambhal", "Sambhal", "28.5800", "78.5500", "handicraft_export"),
    ("sant-kabir-nagar", "Sant Kabir Nagar", "26.7800", "83.0200", "agriculture_trade"),
    ("shahjahanpur", "Shahjahanpur", "27.8833", "79.9167", "agriculture_trade"),
    ("shamli", "Shamli", "29.4500", "77.3167", "agriculture_trade"),
    ("shrawasti", "Shrawasti", "27.5200", "82.0500", "agriculture_trade"),
    ("siddharthnagar", "Siddharthnagar", "27.2800", "83.1000", "agriculture_trade"),
    ("sitapur", "Sitapur", "27.5667", "80.6833", "agriculture_trade"),
    ("sonbhadra", "Sonbhadra", "24.6850", "83.0650", "agriculture_trade"),
    ("sultanpur", "Sultanpur", "26.2631", "82.0725", "agriculture_trade"),
    ("unnao", "Unnao", "26.5473", "80.4938", "industrial"),
    ("varanasi", "Varanasi", "25.3176", "82.9739", "tourism_historic")
]

# Business categories and copy templates mapping
CATEGORIES_COPIES = {
    "it_tech": {
        "tagline": "IT parks · software startups · tech centers · corporate advisories",
        "hero_stat_target": "24",
        "why_features": [
            ("NCR IT infrastructure", "We rank your tech startup or B2B consultancy for high-value organic search terms. Optimizing for tech parks, software clusters, and corporate headquarters."),
            ("Enterprise link building", "Acquiring premium links from global technology publications, startup portals, and high-authority business directories."),
            ("Mobile-first & JS rendering", "Noida & Ghaziabad tech search is mobile-heavy. We configure secure server response paths, fast Core Web Vitals, and JS framework indexes."),
            ("E-E-A-T trust signals", "Aligning directory schema with corporate postal prefixes (201301, 201001, etc.) and building clear author profiles for high-trust rankings.")
        ],
        "testimonials": {
            "quote": "NEXUS took over our B2B SaaS startup's organic campaign from our Noida sector-62 office. In 5 months, they drove our organic traffic up by 4.5× and ranked us #1 for major CRM software queries.",
            "author": "Vikash Singhal",
            "role": "CEO, CloudSphere Solutions · Noida",
            "avatar": "VS"
        },
        "pricing_desc_local": "For early-stage tech startups and local IT consulting setups.",
        "pricing_desc_growth": "For expanding SaaS brands and regional consultancies capturing NCR markets.",
        "pricing_desc_authority": "For enterprise technology groups, major IT hubs, and VC-funded startups.",
        "faqs": [
            ("How long does SEO take for Noida tech companies?", "Given the high concentration of IT firms in Noida, expect map pack rankings in 60 days, while global B2B keywords require 4-6 months to build competitive topical maps."),
            ("Do you handle SEO for e-commerce brands in Ghaziabad?", "Yes, we specialize in Shopify and WooCommerce setups, category indexation, and product structured data to drive sales.")
        ]
    },
    "industrial": {
        "tagline": "Heavy engineering · manufacturing plants · industrial trade · logistics",
        "hero_stat_target": "20",
        "why_features": [
            ("B2B wholesale queries", "We rank your industrial manufacturing or logistics plant for high-intent wholesale keywords to connect you with bulk buyers across India."),
            ("NAP map packet audits", "Resolving duplicate local pins in congested industrial sectors (Okhla, Dada Nagar, Unnao) to build consistent search signals."),
            ("Route & logistics targeting", "We compile programmatic cargo route pages to drive freight and warehousing contract requests directly to you."),
            ("Bilingual trade terms", "Trading communities search in Hindi and Hinglish. We optimize bilingual metadata to capture maximum local trade volume.")
        ],
        "testimonials": {
            "quote": "Our leather export manufacturing unit in Kanpur was invisible on Google. NEXUS rebuilt our product directories and optimized our maps listing. Bulk inquiries from out-of-state grew by 3× in 90 days.",
            "author": "Mohammad Asif",
            "role": "Managing Director, Asif Leather Exports · Kanpur",
            "avatar": "MA"
        },
        "pricing_desc_local": "For single-location local manufacturing units and transport agents.",
        "pricing_desc_growth": "For regional industrial firms and logistics groups capturing NCR & state trade channels.",
        "pricing_desc_authority": "For national industrial groups, manufacturing plants, and export corporations.",
        "faqs": [
            ("Can you help my factory rank for wholesale bulk contracts?", "Yes, we specialize in B2B catalog structures, raw materials schemas, and wholesale keyword ranking campaigns across North India."),
            ("Do you optimize Google Business Profiles for industrial zones?", "Yes, we verify listings, manage map coordinates, and upload geotagged warehouse photos to guarantee map indexation.")
        ]
    },
    "tourism_historic": {
        "tagline": "Spiritual tourism · cultural heritage · hospitality services · local trade",
        "hero_stat_target": "22",
        "why_features": [
            ("Spiritual & heritage searches", "We optimize your hotel, travel agency, or retail shop to rank for the massive tourist and devotee search traffic visiting UP's historic centers."),
            ("Local maps pack visibility", "Positioning your hospitality business at the top of the local 3-pack for highly competitive tourist-intent queries."),
            ("Voice & mobile tourist queries", "Tourists search on-the-go. We implement specialized Schema structures and fast page speeds to capture immediate mobile searches."),
            ("High-value travel links", "Securing editorial link mentions from global travel portals, lifestyle channels, and regional news networks.")
        ],
        "testimonials": {
            "quote": "Operating a premium hotel near the Ayodhya temple, ranking on Google was critical. NEXUS optimized our hotel schemas, updated our maps listing, and doubled our direct bookings in 4 months.",
            "author": "Aditya Shrivastav",
            "role": "General Manager, Heritage Inn · Ayodhya",
            "avatar": "AS"
        },
        "pricing_desc_local": "For boutique hotels, local tour guides, and local handicraft shops.",
        "pricing_desc_growth": "For premium hospitality groups, luxury hotels, and regional travel agencies.",
        "pricing_desc_authority": "For national travel networks, large hotel chains, and premium heritage projects.",
        "faqs": [
            ("How does tourism SEO help local businesses?", "It captures tourists searching for accommodations, dining, shopping, and tours in real-time, sending high-intent leads straight to you."),
            ("Can you rank my hotel globally for overseas travelers?", "Yes. We implement multi-region optimizations, clean travel schema, and target international search keywords.")
        ]
    },
    "handicraft_export": {
        "tagline": "Artisanal exporters · brassware industries · carpet exporters · wood carvers",
        "hero_stat_target": "18",
        "why_features": [
            ("Export trade visibility", "We rank your export business globally, connecting your brassware, carpets, or wood carvings directly with international importers."),
            ("Artisanal keyword optimization", "We target specialized high-value keywords to capture queries for authentic, handmade regional crafts."),
            ("High-domain PR backlinks", "Acquiring editorial links from international design portals, home decor magazines, and national B2B export directories."),
            ("Bilingual trade maps", "Mapping bulk purchase intent queries to connect you with retail chains and wholesale buyers nationwide.")
        ],
        "testimonials": {
            "quote": "Our brassware export house in Moradabad was relying entirely on offline fairs. NEXUS optimized our product directories and ranked us globally. We secured three major importers from Europe in 6 months.",
            "author": "Amit Agarwal",
            "role": "Founder, Moradabad Artisans Export · Moradabad",
            "avatar": "AA"
        },
        "pricing_desc_local": "For local craft workshops and retail showrooms.",
        "pricing_desc_growth": "For regional export houses and trade dealers looking to enter international markets.",
        "pricing_desc_authority": "For large export corporations, artisanal groups, and national craft portals.",
        "faqs": [
            ("Do you work with craft exporters seeking B2B buyers?", "Yes, we design catalog landing pages and target import-intent search terms to capture wholesale inquiries from B2B buyers globally."),
            ("How long does it take to rank for craft exports?", "Given the specialized nature of export terms, pages can achieve top ranks for niche keywords in 45-75 days.")
        ]
    },
    "administrative_edu": {
        "tagline": "Regional commercial hubs · university networks · professional service providers",
        "hero_stat_target": "20",
        "why_features": [
            ("Institutional enrollment SEO", "We rank universities, schools, and coaching networks for high-volume academic search queries to drive registrations."),
            ("Professional service visibility", "We optimize clinics, lawyers, and consultancies to rank #1 for local resident searches in UP's major hubs."),
            ("Sector-targeted GBP campaigns", "Correcting location errors, category pins, and verifying map profiles to ensure direct resident contact."),
            ("Mobile residential searches", "Over 80% of regional searches are mobile. We optimize for fast page loads, local maps, and local directories.")
        ],
        "testimonials": {
            "quote": "NEXUS took over local SEO for our multi-specialty hospital in Lucknow. Their local page optimization and review acquisition program grew our monthly organic patient bookings by 2.2×.",
            "author": "Dr. Sandeep Verma",
            "role": "Director, Awadh Healthcare · Lucknow",
            "avatar": "SV"
        },
        "pricing_desc_local": "For local tuition academies, private practices, and single-location service shops.",
        "pricing_desc_growth": "For regional colleges, hospitals, and growing professional service groups.",
        "pricing_desc_authority": "For multi-city educational chains, hospital groups, and corporate advisory firms.",
        "faqs": [
            ("How do you target educational admissions queries?", "We build parent-focused content, implement school listings schemas, and manage localized maps optimization to capture course enrollment queries."),
            ("What is the cost of administrative center local SEO?", "Our retainers start at ₹30,000/month for Local, ₹65,000/month for Growth, and custom for enterprise setups.")
        ]
    },
    "agriculture_trade": {
        "tagline": "Sugarcane mandis · grain distribution · cold storage · agro-trade networks",
        "hero_stat_target": "16",
        "why_features": [
            ("Agro-input & trader queries", "We rank your cold storage facility, mandi trading firm, or fertilizer distribution network for bulk commercial searches."),
            ("Mandi trade search optimization", "Capturing regional crop queries and buyer intents across major agricultural districts of Uttar Pradesh."),
            ("Local directory citation setups", "Enriching local directory signals to align maps listings with local postal codes for strong local pack search power."),
            ("Voice search compatibility", "Sugarcane and grain traders search heavily via voice in Hindi. We structure search tags and FAQ schemas for spoken Hindi.")
        ],
        "testimonials": {
            "quote": "We run a cold storage and potato trading business near Farrukhabad. NEXUS built our local listing and ranked us for wholesale cold storage queries. Bulk farmer and trader inquiries doubled.",
            "author": "Yogesh Yadav",
            "role": "Owner, Yadav Cold Storage · Farrukhabad",
            "avatar": "YY"
        },
        "pricing_desc_local": "For single-location cold storages, local dealers, and mandi shops.",
        "pricing_desc_growth": "For agro-trade distributors and regional trading companies looking to expand NCR/UP reach.",
        "pricing_desc_authority": "For national crop trading organizations, large seed corporations, and logistics groups.",
        "faqs": [
            ("How does SEO help agricultural traders?", "It makes you discoverable to crop buyers, food processors, and national bulk purchasers searching for reliable storage or trade partners in UP's mandis."),
            ("Do you optimize listings for rural postcodes?", "Yes. We audit NAP listings, clean up verification details, and configure map pins for precise rural trade area indexation.")
        ]
    }
}
