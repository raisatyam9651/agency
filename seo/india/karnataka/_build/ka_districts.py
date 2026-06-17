"""District data and templates for 31 Karnataka local SEO landing pages.
"""

DISTRICTS = [
    ("bagalkot", "Bagalkot", "16.1813", "75.6958", "mining_mineral"),
    ("ballari", "Ballari", "15.1394", "76.9214", "mining_mineral"),
    ("belagavi", "Belagavi", "15.8497", "74.4977", "industrial_manufacturing"),
    ("bengaluru-rural", "Bengaluru Rural", "13.2038", "77.3006", "it_biotech"),
    ("bengaluru-urban", "Bengaluru Urban", "12.9716", "77.5946", "it_biotech"),
    ("bidar", "Bidar", "17.9104", "77.5199", "heritage_trade"),
    ("chamarajanagar", "Chamarajanagar", "11.9261", "76.9437", "agro_spice"),
    ("chikkaballapur", "Chikkaballapur", "13.4354", "77.7275", "heritage_trade"),
    ("chikkamagaluru", "Chikkamagaluru", "13.3161", "75.7720", "agro_spice"),
    ("chitradurga", "Chitradurga", "14.2251", "76.4005", "heritage_trade"),
    ("dakshina-kannada", "Dakshina Kannada", "12.8708", "74.8801", "ports_coastal"),
    ("davanagere", "Davanagere", "14.4644", "75.9218", "agro_spice"),
    ("dharwad", "Dharwad", "15.4589", "75.0078", "industrial_manufacturing"),
    ("gadag", "Gadag", "15.4283", "75.6264", "heritage_trade"),
    ("hassan", "Hassan", "13.0072", "76.1026", "agro_spice"),
    ("haveri", "Haveri", "14.7937", "75.4050", "agro_spice"),
    ("kalaburagi", "Kalaburagi", "17.3291", "76.8343", "heritage_trade"),
    ("kodagu", "Kodagu", "12.2602", "75.7380", "heritage_trade"),
    ("kola", "Kola", "13.1363", "78.1293", "heritage_trade"),
    ("koppal", "Koppal", "15.3524", "76.1557", "mining_mineral"),
    ("mandya", "Mandya", "12.5218", "76.8951", "agro_spice"),
    ("mysuru", "Mysuru", "12.2958", "76.6394", "heritage_trade"),
    ("raichur", "Raichur", "16.2076", "77.3556", "mining_mineral"),
    ("ramanagara", "Ramanagara", "12.7209", "77.2781", "industrial_manufacturing"),
    ("shivamogga", "Shivamogga", "13.9299", "75.5681", "agro_spice"),
    ("tumakuru", "Tumakuru", "13.3392", "77.1140", "industrial_manufacturing"),
    ("udupi", "Udupi", "13.3409", "74.7421", "ports_coastal"),
    ("uttara-kannada", "Uttara Kannada", "14.8080", "74.5680", "ports_coastal"),
    ("vijayapura", "Vijayapura", "16.8302", "75.7100", "mining_mineral"),
    ("vijayanagara", "Vijayanagara", "15.2689", "76.3909", "heritage_trade"),
    ("yadgir", "Yadgir", "16.7600", "77.1400", "heritage_trade")
]

CATEGORIES_COPIES = {
    "it_biotech": {
        "tagline": "IT corridors · software startups · tech parks & corporate campuses",
        "hero_stat_target": "28",
        "why_features": [
            ("Tech park & GBP mapping", "We optimize Google Business Profiles for high-trust software and tech search corridors like Electronic City & Whitefield."),
            ("Technical site indexing", "Configuring fast rendering for JS frameworks (React, Next.js), proper crawl structures, and canonical schemas."),
            ("Startup PR & link building", "Acquiring high-authority organic links from tech journals, startup networks, and premium software columns."),
            ("E-E-A-T trust structures", "Structuring authority pages showing certifications, technical awards, and high-trust B2B corporate testimonials.")
        ],
        "testimonials": {
            "quote": "Our tech consultancy in Bengaluru Urban was competing in a highly crowded market. NEXUS optimized our technical content silos and ranked us for high-intent corporate IT services, generating 4x inbound business requests.",
            "author": "Rohan Murthy",
            "role": "Founder, Murthy Tech Solutions · Bengaluru",
            "avatar": "RM"
        },
        "pricing_desc_local": "For boutique dev setups, local IT consultancies, and digital agencies.",
        "pricing_desc_growth": "For expanding SaaS startups and regional corporate consultancies.",
        "pricing_desc_authority": "For enterprise technology groups, multinational software firms, and VC-funded startups.",
        "faqs": [
            ("How long does SEO take for Bengaluru IT firms?", "Local search visibility improves within 60 days. Harder global software product keywords require 4-6 months of consistent link building and topical mapping."),
            ("Do you do SaaS e-commerce SEO?", "Yes, we specialize in Shopify, WooCommerce, and custom web product storefront optimizations.")
        ]
    },
    "industrial_manufacturing": {
        "tagline": "Aerospace clusters · machine tools · automotive manufacturing · engineering workshops",
        "hero_stat_target": "22",
        "why_features": [
            ("B2B catalog database setup", "Optimizing wholesale queries, machinery models, and components with technical schema formats."),
            ("Industrial estate GBP pack", "Correcting coordinate maps and listings in industrial areas to secure map placement for local buyers."),
            ("Trade directories validation", "Structuring listings across industrial databases, export councils, and engineering directories."),
            ("Hinglish bulk search terms", "Capturing queries that mix English terms with Hindi/Kannada phrases to ensure all local leads are captured.")
        ],
        "testimonials": {
            "quote": "Our aerospace machine tools company in Belagavi relied entirely on offline brokers. NEXUS ranked us #1 for wholesale engineering exports in Karnataka, bringing us direct corporate contracts.",
            "author": "Anand Kulkarni",
            "role": "Director, Belgaum Engineering Works · Belagavi",
            "avatar": "AK"
        },
        "pricing_desc_local": "For local machine shops, component dealers, and tool workshops.",
        "pricing_desc_growth": "For regional industrial suppliers and parts manufacturers.",
        "pricing_desc_authority": "For national industrial manufacturers, aerospace suppliers, and export engineering houses.",
        "faqs": [
            ("Can you rank my factory for heavy equipment export?", "Yes, we write global-targeted content, optimize specifications, and build international trade backlinks."),
            ("Do you clean up GIDC or KIADB mapping errors?", "Yes, verifying addresses and map coordinates in heavy industrial zones is part of our audit.")
        ]
    },
    "ports_coastal": {
        "tagline": "Mangalore port logistics · seafood exports · coastal shipping · plantation trade",
        "hero_stat_target": "18",
        "why_features": [
            ("Logistics & port search map", "Ranking cargo agents, customs brokers, and cold storage networks for coastal transit terms."),
            ("Geotagged shipping profiles", "Optimizing Google Business Profiles with verified facilities and port-side imagery."),
            ("Regional authority links", "Securing authority links from shipping forums, global trade catalogs, and logistics portals."),
            ("Voice search for exporters", "Exporters on the move search via voice. We structure FAQ pages to capture mobile voice queries.")
        ],
        "testimonials": {
            "quote": "NEXUS ranked our customs clearance agency near Mangaluru port. Our inbound B2B logistics queries doubled within 90 days of cleaning up our map listing and local schemas.",
            "author": "Satish Kamath",
            "role": "Managing Partner, Kamath Coastal Logistics · Dakshina Kannada",
            "avatar": "SK"
        },
        "pricing_desc_local": "For local clearing brokers, warehouse managers, and seafood suppliers.",
        "pricing_desc_growth": "For regional cargo shippers and logistics firms.",
        "pricing_desc_authority": "For international port operators, large export logistics groups, and shipping lines.",
        "faqs": [
            ("How does local SEO help logistics providers in Mangaluru?", "It lists your business for shipping agents, export houses, and customs clearance seekers looking for local handlers."),
            ("Do you handle reviews management for transport firms?", "Yes, setting up customer reviews feedback loops is a standard part of our campaign.")
        ]
    },
    "agro_spice": {
        "tagline": "Coffee estates · spice processing · sugarcane mills · regional mandis",
        "hero_stat_target": "20",
        "why_features": [
            ("Agro brand topical authority", "We target terms like wholesale coffee supply, spice processing, and crop trade to capture direct buyers."),
            ("Mandi coordinates verified", "Setting up Google maps presence for warehouses, plantations, and trade outlets in rural hubs."),
            ("Bilingual voice schemas", "Agri-buyers search in Kannada and English. We structure content voice schemas to rank in regional speech intents."),
            ("Review loops configuration", "Acquiring direct buyer and dealer trust reviews to boost maps pack placements.")
        ],
        "testimonials": {
            "quote": "Our specialty coffee distribution in Chikkamagaluru was dependent on third-party traders. NEXUS ranked us for premium roasted coffee bulk supply, connecting us directly with cafés across tier-1 cities.",
            "author": "Vikram Hegde",
            "role": "Founder, Hegde Coffee Estates · Chikkamagaluru",
            "avatar": "VH"
        },
        "pricing_desc_local": "For local spice processors, mandi merchants, and independent estates.",
        "pricing_desc_growth": "For regional agro-packers, wholesale crop traders, and mills.",
        "pricing_desc_authority": "For national crop exporters, state cooperatives, and bulk agro-brands.",
        "faqs": [
            ("How does local SEO help Chikkamagaluru coffee estates?", "It ranks your direct sales portal for retail café buyers and wholesale coffee brokers looking for estate sources."),
            ("Do you verify agricultural warehouse map cards?", "Yes, we optimize NAP details for rural coordinates to guarantee map indexation.")
        ]
    },
    "mining_mineral": {
        "tagline": "Iron ore mining · steel mills · granite quarries · industrial transport",
        "hero_stat_target": "16",
        "why_features": [
            ("Industrial mineral buyer queries", "Targeting wholesale bulk keywords (iron ore grades, granite slabs, mining transport) for industrial purchasing agents."),
            ("GBP mapping in mine zones", "Establishing clean map locations in heavy transport and mining zones to guide cargo fleets."),
            ("Trade PR link building", "Securing authority link mentions from steel industry boards, construction journals, and mineral databases."),
            ("Contractor query targeting", "Optimizing content to capture corporate buyers searching for direct mining supply lines.")
        ],
        "testimonials": {
            "quote": "Our steel processing unit in Ballari wanted direct corporate orders. NEXUS ranked our catalog on page-1, helping us bypass brokers and secure contracts from real estate builders directly.",
            "author": "Girish Reddy",
            "role": "Director, Bellary Steel & Minerals · Ballari",
            "avatar": "GR"
        },
        "pricing_desc_local": "For quarry operators, sand suppliers, and mineral transporters.",
        "pricing_desc_growth": "For regional mining suppliers and steel distributors.",
        "pricing_desc_authority": "For national mining conglomerates, large steel mills, and mineral exporters.",
        "faqs": [
            ("How do you target buyers for iron ore and minerals?", "We structure detailed spec sheets, optimize product directory indexes, and build links from construction and metal domains."),
            ("What is the typical maps pack timeline in mining zones?", "Map listing verification and optimization takes 30-45 days to show visibility movement.")
        ]
    },
    "heritage_trade": {
        "tagline": "Heritage tourism · silk weaving hubs · local handlooms · agricultural trade",
        "hero_stat_target": "24",
        "why_features": [
            ("Heritage brand mapping", "Structuring hotel, guide, and cultural tour metadata to capture visitors in tourist hubs like Mysuru & Hampi."),
            ("Mobile voice visitor queries", "Optimizing localized FAQ queries for real-time mobile search (e.g. 'best place to buy Mysore silk')."),
            ("Local artisan link citations", "Securing directories and local portal links to validate handloom and silk brand authority."),
            ("Bilingual tour search", "Optimizing pages in Kannada and English to capture both regional and international tourists.")
        ],
        "testimonials": {
            "quote": "Our silk handloom mill in Mysuru was losing retail walk-ins to modern mall chains. NEXUS optimized our maps coordinates and ranked us for traditional silk sarees, bringing in massive tourist foot traffic.",
            "author": "Madhavan Swamy",
            "role": "Proprietor, Mysore Silk Weavers · Mysuru",
            "avatar": "MS"
        },
        "pricing_desc_local": "For boutique silk shops, heritage homestays, and local tour guides.",
        "pricing_desc_growth": "For regional hotel chains, tour operators, and cooperative handloom societies.",
        "pricing_desc_authority": "For national travel networks, luxury heritage hotels, and state craft corporations.",
        "faqs": [
            ("Can you rank travel guides for Hampi or Mysore tours?", "Yes, we build custom tour activity landing pages and rank them for visitor query terms."),
            ("How does local SEO help Mysore silk shops?", "It puts your retail outlet directly in Google Maps for tourists searching for authentic silk weavers in their vicinity.")
        ]
    }
}
