"""Batch runner: generates pages for Madhya Pradesh, Chhattisgarh, Odisha, Kerala, and Jharkhand."""
import os, sys, shutil
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '_tools'))
from engine import generate_all, check_links

HERO_SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'haryana', 'images', 'hero.jpg')

# ── Shared category templates ────────────────────────────────────────────────
CAT_ADMIN_IT = lambda capital, area: {
    "tagline": f"State capital IT corridors · corporate services · education hubs · fintech & startups",
    "hero_stat_target": "28",
    "why_features": [
        ("Capital city GBP dominance", f"We optimize Google Business Profiles for coaching centers, IT firms, clinics, and consultancies packed in dense {capital} corridors."),
        ("Competitive B2B SEO", f"We build topical authority and local citations that outrank franchise aggregators for B2B and professional service queries in {capital}."),
        ("Multi-sector schema deployment", f"From hospital schema to legal service markup — we configure JSON-LD structured data tailored to {capital}'s diverse professional sectors."),
        ("Hindi + Hinglish voice intent", f"{capital} buyers search in Hindi and Hinglish. We optimize FAQ schemas, voice queries, and bilingual landing pages for both variants.")
    ],
    "testimonials": {"quote": f"Our IT consultancy in {capital} was invisible online. NEXUS restructured our web presence and ranked us top-3 for IT service queries within 60 days.", "author": "Vikram Sharma", "role": f"Director, Sharma IT Solutions · {capital}", "avatar": "VS"},
    "pricing_desc_local": f"For independent consultants, local coaching centers, and small clinics in {capital}.",
    "pricing_desc_growth": "For expanding coaching chains, mid-size hospitals, and regional IT consultancies.",
    "pricing_desc_authority": "For large hospital networks, enterprise-level brands, and statewide firms.",
    "faqs": [
        (f"How does SEO help IT firms in {capital}?", f"It positions your brand directly in front of corporate clients and decision-makers searching for IT and consulting services in {capital}."),
        (f"Can you rank hospitals in {capital}?", "Yes, we optimize multi-location GBP listings, build medical schema, and target condition-specific long-tail keywords.")
    ]
}

CAT_INDUSTRIAL = lambda hub: {
    "tagline": "Industrial manufacturing · heavy engineering · textile mills · auto parts & fabrication",
    "hero_stat_target": "24",
    "why_features": [
        ("Industrial hub GBP dominance", f"We optimize Google Business Profiles for manufacturers, fabricators, and industrial suppliers in {hub}."),
        ("B2B product catalog SEO", "We target wholesale industrial, auto parts, and engineering keywords to connect manufacturers with national buyers."),
        ("Export keyword targeting", "Industrial hubs export nationally. We optimize for B2B buyer terms, trade directories, and compliance keywords."),
        ("Hindi + English bilingual SEO", "Industrial buyers search in Hindi and English. We build parallel content and schema for both search variants.")
    ],
    "testimonials": {"quote": f"Our manufacturing unit in {hub} was losing orders to online aggregators. NEXUS rebuilt our catalog pages and drove a 3x increase in wholesale inquiries.", "author": "Ajay Mishra", "role": f"Director, Mishra Engineering · {hub}", "avatar": "AM"},
    "pricing_desc_local": "For single-unit workshops, local parts dealers, and small manufacturers.",
    "pricing_desc_growth": "For expanding manufacturing brands, mid-size exporters, and regional distributors.",
    "pricing_desc_authority": "For large industrial conglomerates and national manufacturing brands.",
    "faqs": [
        (f"How does SEO help manufacturers in {hub}?", "It positions your factory directly in front of wholesale buyers and procurement teams searching for direct manufacturers."),
        ("Can you rank industrial suppliers for national queries?", "Yes, we build multilingual product pages and target industrial trade keywords.")
    ]
}

CAT_MINING_ENERGY = {
    "tagline": "Coal mining operations · power plants · cement factories · mineral extraction & processing",
    "hero_stat_target": "18",
    "why_features": [
        ("Mining & energy GBP setup", "Optimizing Google Business Profiles for mining companies, power plants, and cement factories in remote industrial zones."),
        ("B2B commodity keyword maps", "We target bulk coal, limestone, cement, and mineral supply keywords to connect producers with national industrial buyers."),
        ("Industrial compliance SEO", "Mining companies need visibility for environmental compliance, safety certifications, and government tender queries."),
        ("Remote location map accuracy", "Mining operations are in remote areas with inaccurate map data. We geolocate and verify all facility coordinates.")
    ],
    "testimonials": {"quote": "Our cement plant was only getting walk-in business. NEXUS optimized our industrial listings and brought in 5 new bulk supply contracts from neighboring states.", "author": "Rakesh Agarwal", "role": "GM, Agarwal Cements", "avatar": "RA"},
    "pricing_desc_local": "For local mining contractors, small quarries, and individual power equipment dealers.",
    "pricing_desc_growth": "For regional cement manufacturers and mid-size mining operations.",
    "pricing_desc_authority": "For large mining corporations, power companies, and national cement brands.",
    "faqs": [
        ("How does SEO help mining companies?", "It connects your mining operation with bulk buyers, construction companies, and government procurement agencies searching online."),
        ("Can you rank cement plants for B2B queries?", "Yes, we build industrial product pages, target construction material keywords, and secure backlinks from trade directories.")
    ]
}

CAT_AGRO = lambda crop_detail: {
    "tagline": f"{crop_detail} · agricultural mandis · dairy cooperatives · food processing",
    "hero_stat_target": "18",
    "why_features": [
        ("Agro commodity keyword mapping", "We target wholesale crop, grain, and produce supply keywords to connect mandis and mills with national buyers."),
        ("Cold storage & mill GBP setup", "Optimizing map listings for cold storages, mills, and processing factories in semi-urban zones with inaccurate coordinates."),
        ("Seasonal crop campaign SEO", "Agricultural trade is seasonal. We plan content calendars around harvest cycles to capture peak-demand search volumes."),
        ("Farmer & dealer review loops", "In agri-commerce, trust is everything. We build structured review acquisition workflows from local dealers and cooperatives.")
    ],
    "testimonials": {"quote": "NEXUS optimized our storage listings, ran seasonal keyword campaigns, and brought in 3 major food processing contracts within 4 months.", "author": "Rajesh Patel", "role": "Director, Patel Agri Services", "avatar": "RP"},
    "pricing_desc_local": "For single-location mills, small dairy cooperatives, and local mandi commission agents.",
    "pricing_desc_growth": "For regional food processing brands and mid-size agricultural distributors.",
    "pricing_desc_authority": "For large crop exporters, national food brands, and statewide dairy corporations.",
    "faqs": [
        ("How does local SEO help agricultural businesses?", "It connects your processing unit directly with wholesale traders, food brands, and government procurement agencies searching online."),
        ("Can you rank seasonal crop businesses?", "Yes, we build seasonal SEO content, optimize GBP with seasonal products, and launch timed campaigns during harvest cycles.")
    ]
}

CAT_HERITAGE_TOURISM = lambda site_detail: {
    "tagline": f"{site_detail} · boutique hospitality · heritage tourism · adventure activities",
    "hero_stat_target": "20",
    "why_features": [
        ("Tourism & heritage schema", "We implement rich hotel, tour package, and attraction schema to secure prominent Google Maps placements."),
        ("Global tourism SEO", "Heritage sites attract international visitors. We rank hospitality brands for English and international travel queries."),
        ("Mobile voice-intent search", "Tourists search using voice. We optimize FAQ content and local listings for quick voice answers about nearby hotels and guides."),
        ("High-authority travel backlinks", "Acquiring organic links from travel publications, tourism portals, and heritage directories to build domain authority.")
    ],
    "testimonials": {"quote": "Our heritage guesthouse was dependent on walk-ins. NEXUS ranked us for direct tourism queries, tripling our direct bookings in one season.", "author": "Priya Devi", "role": "Owner, Heritage Stay", "avatar": "PD"},
    "pricing_desc_local": "For local guesthouses, tour guides, and small travel agents near heritage sites.",
    "pricing_desc_growth": "For regional hotel chains, transport services, and activity booking portals.",
    "pricing_desc_authority": "For luxury heritage resorts, international travel brands, and large hospitality groups.",
    "faqs": [
        ("How does SEO help tourism businesses?", "It captures tourists searching in real-time for rooms, heritage experiences, and guides — allowing them to book directly with you."),
        ("Can you rank my hotel for heritage tourism queries?", "Yes, we design focused landing pages, optimize travel content, and manage local map rankings for tourism keywords.")
    ]
}

CAT_LOCAL_SERVICES = {
    "tagline": "Private clinics & diagnostics · education centers · local retail · small manufacturing",
    "hero_stat_target": "14",
    "why_features": [
        ("Hyperlocal GBP dominance", "In smaller districts, being the #1 Google Maps result is everything. We verify, optimize, and defend your local listing."),
        ("Service area SEO expansion", "We extend your visibility beyond your district into surrounding areas, capturing demand from adjacent markets with no competition."),
        ("Review acquisition & trust", "Local buyers trust reviews more than advertising. We implement structured review workflows that build social proof."),
        ("Mobile-first speed optimization", "Smaller district users are mobile-dependent. We optimize core web vitals, page speed, and mobile UX.")
    ],
    "testimonials": {"quote": "Our diagnostic center had zero online presence. NEXUS set up our GBP, built service pages, and within 3 months we were the top result for lab queries.", "author": "Dr. Priya Kumari", "role": "Director, Local Diagnostics", "avatar": "PK"},
    "pricing_desc_local": "For single-location clinics, tuition centers, small shops, and local service providers.",
    "pricing_desc_growth": "For expanding diagnostic chains, regional coaching centers, and multi-location dealerships.",
    "pricing_desc_authority": "For district-level hospital networks, large educational institutions, and construction firms.",
    "faqs": [
        ("Is SEO worth it for small-town businesses?", "Absolutely. In smaller districts, competition is low — meaning faster rankings, lower cost, and high returns from being #1."),
        ("How quickly can my clinic rank in a small district?", "In low-competition districts, GBP optimization alone can produce top-3 maps rankings within 30 days.")
    ]
}

CAT_TRIBAL_FOREST = {
    "tagline": "Forest produce & bamboo crafts · tribal handicrafts · ecotourism · local healthcare",
    "hero_stat_target": "12",
    "why_features": [
        ("Tribal product catalog SEO", "We optimize handloom, bamboo craft, and forest product catalogs with detailed product schema to rank in niche buyer searches."),
        ("Ecotourism GBP optimization", "We configure tourism listings for jungle lodges, ecotourism camps, and tribal experience tours."),
        ("GI-tagged product authority", "Tribal craft products carry GI tags. We build topical authority around these heritage products for premium buyer keywords."),
        ("Hyperlocal mobile SEO", "In tribal districts, mobile is the only internet. We optimize for slow connections, voice search, and mobile-first discovery.")
    ],
    "testimonials": {"quote": "Our tribal craft cooperative was only selling at local haats. NEXUS built our product pages online and now we receive orders from across India.", "author": "Mangal Singh", "role": "Secretary, Tribal Crafts Cooperative", "avatar": "MS"},
    "pricing_desc_local": "For individual artisans, small craft workshops, and local jungle lodges.",
    "pricing_desc_growth": "For expanding craft cooperatives, mid-size ecotourism operators, and NGOs.",
    "pricing_desc_authority": "For large handicraft export houses, statewide ecotourism brands, and government agencies.",
    "faqs": [
        ("How does SEO help tribal craft businesses?", "It makes your crafts discoverable to collectors, interior designers, and corporate gifting buyers searching online."),
        ("Can you rank ecotourism businesses?", "Yes, we optimize adventure tourism pages, target nature travel keywords, and build backlinks from travel directories.")
    ]
}

# ── STATE CONFIGURATIONS ────────────────────────────────────────────────────
STATES = {
    "madhya-pradesh": {
        "state_name": "Madhya Pradesh", "state_slug": "madhya-pradesh", "state_abbr": "MP",
        "geo_code": "IN-MP", "hub_lat": "23.2599", "hub_lng": "77.4126",
        "primary_city": "Bhopal", "primary_cities": "Bhopal, Indore, Gwalior, and Jabalpur",
        "languages": "Hindi · English", "hub_client_count": "220",
        "categories": {
            "admin_it": CAT_ADMIN_IT("Bhopal", "MP"),
            "industrial": CAT_INDUSTRIAL("Indore"),
            "mining": CAT_MINING_ENERGY,
            "agro": CAT_AGRO("Soybean & wheat mills · opium & garlic mandis · cotton ginning"),
            "heritage": CAT_HERITAGE_TOURISM("Khajuraho temples · Orchha fort · Sanchi Stupa · tiger reserves"),
            "local": CAT_LOCAL_SERVICES,
        },
        "districts": [
            ("agar-malwa","Agar Malwa","23.7100","76.0200","agro"),
            ("alirajpur","Alirajpur","22.3600","74.3500","local"),
            ("anuppur","Anuppur","23.1000","81.6900","mining"),
            ("ashoknagar","Ashoknagar","24.5800","77.7300","agro"),
            ("balaghat","Balaghat","21.8100","80.1900","local"),
            ("barwani","Barwani","22.0400","74.9000","local"),
            ("betul","Betul","21.9100","77.9000","local"),
            ("bhind","Bhind","26.5600","78.7900","agro"),
            ("bhopal","Bhopal","23.2599","77.4126","admin_it"),
            ("burhanpur","Burhanpur","21.3100","76.2300","agro"),
            ("chhatarpur","Chhatarpur","24.9200","79.5900","heritage"),
            ("chhindwara","Chhindwara","22.0600","78.9400","industrial"),
            ("damoh","Damoh","23.8400","79.4400","agro"),
            ("datia","Datia","25.6700","78.4600","agro"),
            ("dewas","Dewas","22.9600","76.0500","industrial"),
            ("dhar","Dhar","22.6000","75.3000","agro"),
            ("dindori","Dindori","22.9500","81.0800","local"),
            ("guna","Guna","24.6500","77.3100","agro"),
            ("gwalior","Gwalior","26.2183","78.1828","industrial"),
            ("harda","Harda","22.3400","77.0900","agro"),
            ("indore","Indore","22.7196","75.8577","admin_it"),
            ("jabalpur","Jabalpur","23.1815","79.9864","industrial"),
            ("jhabua","Jhabua","22.7700","74.5900","local"),
            ("katni","Katni","23.8300","80.4000","mining"),
            ("khandwa","Khandwa","21.8200","76.3500","agro"),
            ("khargone","Khargone","21.8200","75.6100","agro"),
            ("mandla","Mandla","22.6000","80.3800","local"),
            ("mandsaur","Mandsaur","24.0700","75.0700","agro"),
            ("morena","Morena","26.5000","78.0000","agro"),
            ("narsinghpur","Narsinghpur","22.9500","79.1900","agro"),
            ("neemuch","Neemuch","24.4700","74.8700","agro"),
            ("niwari","Niwari","25.1200","78.4000","heritage"),
            ("panna","Panna","24.7200","80.1900","mining"),
            ("raisen","Raisen","23.3300","77.7900","agro"),
            ("rajgarh","Rajgarh","24.0000","76.6200","agro"),
            ("ratlam","Ratlam","23.3300","75.0400","industrial"),
            ("rewa","Rewa","24.5300","81.3000","mining"),
            ("sagar","Sagar","23.8400","78.7400","heritage"),
            ("satna","Satna","24.5800","80.8300","mining"),
            ("sehore","Sehore","23.2000","77.0800","agro"),
            ("seoni","Seoni","22.0900","79.5400","local"),
            ("shahdol","Shahdol","23.3000","81.3600","mining"),
            ("shajapur","Shajapur","23.4300","76.2700","agro"),
            ("sheopur","Sheopur","25.6700","76.7100","agro"),
            ("shivpuri","Shivpuri","25.4300","77.6600","agro"),
            ("sidhi","Sidhi","24.4200","81.8800","mining"),
            ("singrauli","Singrauli","24.2000","82.6700","mining"),
            ("tikamgarh","Tikamgarh","24.7400","78.8300","heritage"),
            ("ujjain","Ujjain","23.1765","75.7885","heritage"),
            ("umaria","Umaria","23.5200","80.8400","mining"),
            ("vidisha","Vidisha","23.5300","77.8100","agro"),
        ]
    },
    "chhattisgarh": {
        "state_name": "Chhattisgarh", "state_slug": "chhattisgarh", "state_abbr": "CG",
        "geo_code": "IN-CT", "hub_lat": "21.2514", "hub_lng": "81.6296",
        "primary_city": "Raipur", "primary_cities": "Raipur, Bilaspur, Durg, and Korba",
        "languages": "Hindi · Chhattisgarhi · English", "hub_client_count": "140",
        "categories": {
            "admin_it": CAT_ADMIN_IT("Raipur", "CG"),
            "industrial": CAT_INDUSTRIAL("Durg-Bhilai"),
            "mining": CAT_MINING_ENERGY,
            "agro": CAT_AGRO("Rice mills · tendu leaf processing · mahua trade"),
            "tribal": CAT_TRIBAL_FOREST,
            "local": CAT_LOCAL_SERVICES,
        },
        "districts": [
            ("balod","Balod","20.7300","81.2000","local"),
            ("baloda-bazar","Baloda Bazar","21.6600","82.1600","agro"),
            ("balrampur","Balrampur","23.6000","83.6000","tribal"),
            ("bastar","Bastar","19.1075","81.9535","tribal"),
            ("bemetara","Bemetara","21.7200","81.5300","agro"),
            ("bijapur","Bijapur","18.8400","80.7700","tribal"),
            ("bilaspur","Bilaspur","22.0797","82.1409","admin_it"),
            ("dantewada","Dantewada","18.9000","81.3500","tribal"),
            ("dhamtari","Dhamtari","20.7100","81.5500","agro"),
            ("durg","Durg","21.1900","81.2800","industrial"),
            ("gariaband","Gariaband","20.6400","82.0600","local"),
            ("gaurela-pendra-marwahi","Gaurela Pendra Marwahi","22.7400","81.6600","local"),
            ("janjgir-champa","Janjgir Champa","22.0100","82.5800","agro"),
            ("jashpur","Jashpur","22.8900","84.1400","tribal"),
            ("kabirdham","Kabirdham","22.0600","81.2500","agro"),
            ("kanker","Kanker","20.2700","81.4900","tribal"),
            ("khairagarh-chhuikhadan-gandai","Khairagarh Chhuikhadan Gandai","21.4200","80.9800","local"),
            ("kondagaon","Kondagaon","19.6000","81.6600","tribal"),
            ("korba","Korba","22.3500","82.6800","mining"),
            ("korea","Korea","23.2100","82.0300","mining"),
            ("mahasamund","Mahasamund","21.1100","82.0900","agro"),
            ("manendragarh-chirmiri-bharatpur","Manendragarh Chirmiri Bharatpur","23.2000","82.2300","mining"),
            ("mohla-manpur-ambagarh-chowki","Mohla Manpur Ambagarh Chowki","21.0800","80.7500","tribal"),
            ("mungeli","Mungeli","22.0700","81.6900","local"),
            ("narayanpur","Narayanpur","19.7300","81.2500","tribal"),
            ("raigarh","Raigarh","21.9000","83.4000","mining"),
            ("raipur","Raipur","21.2514","81.6296","admin_it"),
            ("rajnandgaon","Rajnandgaon","21.1000","81.0300","agro"),
            ("sakti","Sakti","22.0300","82.9600","local"),
            ("sarangarh-bilaigarh","Sarangarh Bilaigarh","21.5900","83.0700","local"),
            ("sukma","Sukma","18.3900","81.6600","tribal"),
            ("surajpur","Surajpur","23.2100","82.8700","mining"),
            ("surguja","Surguja","23.1200","83.1000","mining"),
        ]
    },
    "odisha": {
        "state_name": "Odisha", "state_slug": "odisha", "state_abbr": "OD",
        "geo_code": "IN-OR", "hub_lat": "20.2961", "hub_lng": "85.8245",
        "primary_city": "Bhubaneswar", "primary_cities": "Bhubaneswar, Cuttack, Puri, and Sambalpur",
        "languages": "Odia · Hindi · English", "hub_client_count": "160",
        "categories": {
            "admin_it": CAT_ADMIN_IT("Bhubaneswar", "Odisha"),
            "industrial": CAT_INDUSTRIAL("Rourkela-Sundargarh"),
            "mining": CAT_MINING_ENERGY,
            "agro": CAT_AGRO("Rice & paddy mills · fisheries · cashew processing"),
            "heritage": CAT_HERITAGE_TOURISM("Jagannath Temple Puri · Konark Sun Temple · Chilika Lake · tribal tourism"),
            "local": CAT_LOCAL_SERVICES,
        },
        "districts": [
            ("angul","Angul","20.8400","85.1000","mining"),
            ("balangir","Balangir","20.7200","83.4900","local"),
            ("balasore","Balasore","21.4900","86.9300","agro"),
            ("bargarh","Bargarh","21.3300","83.6200","agro"),
            ("bhadrak","Bhadrak","21.0600","86.5200","agro"),
            ("boudh","Boudh","20.8400","84.3200","local"),
            ("cuttack","Cuttack","20.4625","85.8830","admin_it"),
            ("deogarh","Deogarh","21.5400","84.7300","local"),
            ("dhenkanal","Dhenkanal","20.6600","85.6000","agro"),
            ("gajapati","Gajapati","19.2200","84.1300","local"),
            ("ganjam","Ganjam","19.3900","84.4300","agro"),
            ("jagatsinghpur","Jagatsinghpur","20.2600","86.1700","agro"),
            ("jajpur","Jajpur","20.8500","86.3400","industrial"),
            ("jharsuguda","Jharsuguda","21.8600","84.0100","mining"),
            ("kalahandi","Kalahandi","19.9100","83.1700","local"),
            ("kandhamal","Kandhamal","20.4700","84.2400","local"),
            ("kendrapara","Kendrapara","20.5000","86.4200","agro"),
            ("kendujhar","Kendujhar","21.6300","85.5800","mining"),
            ("khordha","Khordha","20.1800","85.6200","admin_it"),
            ("koraput","Koraput","18.8100","82.7100","local"),
            ("malkangiri","Malkangiri","18.3500","81.8800","local"),
            ("mayurbhanj","Mayurbhanj","21.9400","86.7300","local"),
            ("nabarangpur","Nabarangpur","19.2300","82.5500","local"),
            ("nayagarh","Nayagarh","20.1300","85.1000","local"),
            ("nuapada","Nuapada","20.7800","82.5500","local"),
            ("puri","Puri","19.8135","85.8312","heritage"),
            ("rayagada","Rayagada","19.1700","83.4200","local"),
            ("sambalpur","Sambalpur","21.4669","83.9756","industrial"),
            ("subarnapur","Subarnapur","20.8300","83.8200","local"),
            ("sundargarh","Sundargarh","22.1200","84.0300","industrial"),
        ]
    },
    "kerala": {
        "state_name": "Kerala", "state_slug": "kerala", "state_abbr": "KL",
        "geo_code": "IN-KL", "hub_lat": "10.8505", "hub_lng": "76.2711",
        "primary_city": "Thiruvananthapuram", "primary_cities": "Thiruvananthapuram, Kochi (Ernakulam), Kozhikode, and Thrissur",
        "languages": "Malayalam · English", "hub_client_count": "180",
        "categories": {
            "admin_it": CAT_ADMIN_IT("Thiruvananthapuram-Kochi", "Kerala"),
            "heritage": CAT_HERITAGE_TOURISM("Backwater tourism · Ayurveda wellness · hill station resorts · temple pilgrimages"),
            "agro": CAT_AGRO("Spice plantations · rubber estates · coconut & coir processing · cashew trade"),
            "local": CAT_LOCAL_SERVICES,
        },
        "districts": [
            ("alappuzha","Alappuzha","9.4981","76.3388","heritage"),
            ("ernakulam","Ernakulam","9.9816","76.2999","admin_it"),
            ("idukki","Idukki","9.8500","76.9700","heritage"),
            ("kannur","Kannur","11.8745","75.3704","local"),
            ("kasaragod","Kasaragod","12.4996","74.9869","local"),
            ("kollam","Kollam","8.8932","76.6141","agro"),
            ("kottayam","Kottayam","9.5916","76.5222","agro"),
            ("kozhikode","Kozhikode","11.2588","75.7804","admin_it"),
            ("malappuram","Malappuram","11.0510","76.0711","local"),
            ("palakkad","Palakkad","10.7867","76.6548","agro"),
            ("pathanamthitta","Pathanamthitta","9.2648","76.7870","local"),
            ("thiruvananthapuram","Thiruvananthapuram","8.5241","76.9366","admin_it"),
            ("thrissur","Thrissur","10.5276","76.2144","heritage"),
            ("wayanad","Wayanad","11.6854","76.1320","heritage"),
        ]
    },
    "jharkhand": {
        "state_name": "Jharkhand", "state_slug": "jharkhand", "state_abbr": "JH",
        "geo_code": "IN-JH", "hub_lat": "23.3441", "hub_lng": "85.3096",
        "primary_city": "Ranchi", "primary_cities": "Ranchi, Jamshedpur, Dhanbad, and Bokaro",
        "languages": "Hindi · English", "hub_client_count": "150",
        "categories": {
            "admin_it": CAT_ADMIN_IT("Ranchi", "Jharkhand"),
            "industrial": CAT_INDUSTRIAL("Jamshedpur"),
            "mining": CAT_MINING_ENERGY,
            "tribal": CAT_TRIBAL_FOREST,
            "local": CAT_LOCAL_SERVICES,
        },
        "districts": [
            ("bokaro","Bokaro","23.6693","86.1511","mining"),
            ("chatra","Chatra","24.2100","84.8700","local"),
            ("deoghar","Deoghar","24.4764","86.6932","heritage_local"),
            ("dhanbad","Dhanbad","23.7957","86.4304","mining"),
            ("dumka","Dumka","24.2700","87.2500","local"),
            ("east-singhbhum","East Singhbhum","22.8000","86.2000","industrial"),
            ("garhwa","Garhwa","24.1600","83.8000","local"),
            ("giridih","Giridih","24.1900","86.3000","mining"),
            ("godda","Godda","24.8300","87.2100","local"),
            ("gumla","Gumla","23.0400","84.5400","tribal"),
            ("hazaribagh","Hazaribagh","23.9900","85.3600","mining"),
            ("jamshedpur","Jamshedpur","22.8046","86.2029","industrial"),
            ("jamtara","Jamtara","23.9600","86.8000","local"),
            ("khunti","Khunti","23.0700","85.2800","tribal"),
            ("kodarma","Kodarma","24.4700","85.5900","mining"),
            ("latehar","Latehar","23.7400","84.5000","tribal"),
            ("lohardaga","Lohardaga","23.4400","84.6800","tribal"),
            ("pakur","Pakur","24.6400","87.8400","local"),
            ("palamu","Palamu","24.0300","84.0800","local"),
            ("ramgarh","Ramgarh","23.6300","85.5200","mining"),
            ("ranchi","Ranchi","23.3441","85.3096","admin_it"),
            ("sahibganj","Sahibganj","25.2400","87.6300","local"),
            ("saraikela-kharsawan","Saraikela Kharsawan","22.7000","85.9300","industrial"),
            ("simdega","Simdega","22.6200","84.5100","tribal"),
        ]
    },
    "west-bengal": {
        "state_name": "West Bengal", "state_slug": "west-bengal", "state_abbr": "WB",
        "geo_code": "IN-WB", "hub_lat": "22.5726", "hub_lng": "88.3639",
        "primary_city": "Kolkata", "primary_cities": "Kolkata, Howrah, Darjeeling, and Asansol",
        "languages": "Bengali · English · Hindi", "hub_client_count": "190",
        "categories": {
            "admin_it": CAT_ADMIN_IT("Kolkata", "West Bengal"),
            "industrial": CAT_INDUSTRIAL("Howrah-Asansol"),
            "heritage": CAT_HERITAGE_TOURISM("Darjeeling tea estates · Sundarbans ecotourism · Digha beaches"),
            "agro": CAT_AGRO("Rice & jute mills · tea packaging units · cold storage"),
            "local": CAT_LOCAL_SERVICES,
        },
        "districts": [
            ("alipurduar","Alipurduar","26.4900","89.5200","agro"),
            ("bankura","Bankura","23.2300","87.0700","agro"),
            ("birbhum","Birbhum","23.9100","87.5300","agro"),
            ("cooch-behar","Cooch Behar","26.3400","89.4400","agro"),
            ("dakshin-dinajpur","Dakshin Dinajpur","25.2200","88.7600","agro"),
            ("darjeeling","Darjeeling","27.0360","88.2627","heritage"),
            ("hooghly","Hooghly","22.9000","88.3900","industrial"),
            ("howrah","Howrah","22.5800","88.3100","industrial"),
            ("jalpaiguri","Jalpaiguri","26.5200","88.7200","agro"),
            ("jhargram","Jhargram","22.4500","86.9800","agro"),
            ("kalimpong","Kalimpong","27.0600","88.4700","heritage"),
            ("kolkata","Kolkata","22.5726","88.3639","admin_it"),
            ("malda","Malda","25.0100","88.1400","agro"),
            ("murshidabad","Murshidabad","24.1800","88.2700","agro"),
            ("nadia","Nadia","23.4000","88.5000","agro"),
            ("north-24-parganas","North 24 Parganas","22.7200","88.4800","admin_it"),
            ("paschim-bardhaman","Paschim Bardhaman","23.6800","86.9800","industrial"),
            ("paschim-medinipur","Paschim Medinipur","22.4200","87.3200","industrial"),
            ("purba-bardhaman","Purba Bardhaman","23.2300","87.8600","industrial"),
            ("purba-medinipur","Purba Medinipur","22.3000","87.9200","industrial"),
            ("purulia","Purulia","23.3300","86.3600","agro"),
            ("south-24-parganas","South 24 Parganas","22.1800","88.6700","admin_it"),
            ("uttar-dinajpur","Uttar Dinajpur","25.6300","87.9800","agro"),
        ]
    }
}

# Fix: Jharkhand deoghar uses a category not in its categories dict
# Add heritage_local as alias to local
for state_key, state_cfg in STATES.items():
    for slug, name, lat, lng, cat in state_cfg["districts"]:
        if cat not in state_cfg["categories"]:
            # Map unknown to local
            state_cfg["categories"][cat] = CAT_LOCAL_SERVICES

def run():
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
    for state_key, config in STATES.items():
        print(f"\n{'='*60}")
        print(f"GENERATING: {config['state_name']} ({len(config['districts'])} districts)")
        print(f"{'='*60}")

        # Ensure images directory and copy hero
        img_dir = os.path.join(base_dir, state_key, 'images')
        os.makedirs(img_dir, exist_ok=True)
        hero_dest = os.path.join(img_dir, 'hero.jpg')
        if not os.path.exists(hero_dest):
            shutil.copy2(HERO_SRC, hero_dest)
            print(f"  Copied hero.jpg to {state_key}/images/")

        generate_all(config)

        # Run link check
        state_dir = os.path.join(base_dir, state_key)
        ok = check_links(state_dir)
        status = "✅ PASS" if ok else "❌ FAIL"
        print(f"  Link check: {status}")

    print(f"\n{'='*60}")
    print("ALL STATES COMPLETE!")
    print(f"{'='*60}")

if __name__ == "__main__":
    run()
