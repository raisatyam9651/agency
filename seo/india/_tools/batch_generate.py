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
    },
    "assam": {
        "state_name": "Assam", "state_slug": "assam", "state_abbr": "AS",
        "geo_code": "IN-AS", "hub_lat": "26.1445", "hub_lng": "91.7362",
        "primary_city": "Guwahati", "primary_cities": "Guwahati, Dibrugarh, Jorhat, and Silchar",
        "languages": "Assamese · Bengali · Bodo · English", "hub_client_count": "110",
        "categories": {
            "admin_it": CAT_ADMIN_IT("Guwahati", "Assam"),
            "industrial": CAT_INDUSTRIAL("Dibrugarh-Digboi"),
            "heritage": CAT_HERITAGE_TOURISM("Kaziranga National Park · Sivasagar monuments · Majuli island"),
            "agro": CAT_AGRO("Tea plantations & packaging · mustard oil & rice mills"),
            "tribal": CAT_TRIBAL_FOREST,
            "local": CAT_LOCAL_SERVICES,
        },
        "districts": [
            ("bajali","Bajali","26.3300","91.1700","local"),
            ("baksa","Baksa","26.6900","91.3800","tribal"),
            ("barpeta","Barpeta","26.3200","90.9800","agro"),
            ("biswanath","Biswanath","26.7300","93.1500","agro"),
            ("bongaigaon","Bongaigaon","26.4700","90.5600","industrial"),
            ("cachar","Cachar","24.8100","92.8000","local"),
            ("charaideo","Charaideo","26.9000","94.9000","heritage"),
            ("chirang","Chirang","26.5300","90.5200","tribal"),
            ("darrang","Darrang","26.4500","92.0300","agro"),
            ("dhemaji","Dhemaji","27.4800","94.5700","agro"),
            ("dhubri","Dhubri","26.0200","89.9700","local"),
            ("dibrugarh","Dibrugarh","27.4722","94.9125","industrial"),
            ("dima-hasao","Dima Hasao","25.1800","93.0300","heritage"),
            ("goalpara","Goalpara","26.1700","90.6200","local"),
            ("golaghat","Golaghat","26.5200","93.9700","heritage"),
            ("hailakandi","Hailakandi","24.6800","92.5600","local"),
            ("hojai","Hojai","26.0000","92.8500","agro"),
            ("jorhat","Jorhat","26.7509","94.2037","admin_it"),
            ("kamrup","Kamrup","26.3000","91.6000","local"),
            ("kamrup-metropolitan","Kamrup Metropolitan","26.1445","91.7362","admin_it"),
            ("karbi-anglong","Karbi Anglong","25.8500","93.5000","tribal"),
            ("karimganj","Karimganj","24.8700","92.3600","local"),
            ("kokrajhar","Kokrajhar","26.4000","90.2700","tribal"),
            ("lakhimpur","Lakhimpur","27.2300","94.1000","agro"),
            ("majuli","Majuli","26.9500","94.1700","heritage"),
            ("morigaon","Morigaon","26.2500","92.2600","agro"),
            ("nagaon","Nagaon","26.3500","92.6800","admin_it"),
            ("nalbari","Nalbari","26.4500","91.4300","agro"),
            ("sivasagar","Sivasagar","26.9833","94.6333","heritage"),
            ("sonitpur","Sonitpur","26.6300","92.7900","heritage"),
            ("south-salmara-mankachar","South Salmara Mankachar","25.6600","89.8800","local"),
            ("tamulpur","Tamulpur","26.6300","91.5700","tribal"),
            ("tinsukia","Tinsukia","27.5000","95.3600","industrial"),
            ("udalguri","Udalguri","26.7400","92.1300","tribal"),
            ("west-karbi-anglong","West Karbi Anglong","25.8000","92.5000","tribal"),
        ]
    },
    "uttarakhand": {
        "state_name": "Uttarakhand", "state_slug": "uttarakhand", "state_abbr": "UK",
        "geo_code": "IN-UT", "hub_lat": "30.3165", "hub_lng": "78.0322",
        "primary_city": "Dehradun", "primary_cities": "Dehradun, Haridwar, Haldwani, and Roorkee",
        "languages": "Hindi · Garhwali · Kumaoni · English", "hub_client_count": "90",
        "categories": {
            "admin_it": CAT_ADMIN_IT("Dehradun", "Uttarakhand"),
            "industrial": CAT_INDUSTRIAL("Haridwar-Pantnagar"),
            "heritage": CAT_HERITAGE_TOURISM("Nainital resorts · Haridwar-Rishikesh pilgrimage · Char Dham travel"),
            "agro": CAT_AGRO("Horticulture & organic farms · basmati rice processing"),
            "local": CAT_LOCAL_SERVICES,
        },
        "districts": [
            ("almora","Almora","29.5871","79.6467","heritage"),
            ("bageshwar","Bageshwar","29.8400","79.7700","local"),
            ("chamoli","Chamoli","30.4000","79.3300","heritage"),
            ("champawat","Champawat","29.3300","80.0800","local"),
            ("dehradun","Dehradun","30.3165","78.0322","admin_it"),
            ("haridwar","Haridwar","29.9457","78.1642","industrial"),
            ("nainital","Nainital","29.3800","79.4500","heritage"),
            ("pauri-garhwal","Pauri Garhwal","30.1500","78.7800","heritage"),
            ("pithoragarh","Pithoragarh","29.5800","80.2200","local"),
            ("rudraprayag","Rudraprayag","30.2800","78.9800","heritage"),
            ("tehri-garhwal","Tehri Garhwal","30.3800","78.4800","heritage"),
            ("udham-singh-nagar","Udham Singh Nagar","29.0200","79.4900","industrial"),
            ("uttarkashi","Uttarkashi","30.7300","78.4500","heritage"),
        ]
    },
    "himachal-pradesh": {
        "state_name": "Himachal Pradesh", "state_slug": "himachal-pradesh", "state_abbr": "HP",
        "geo_code": "IN-HP", "hub_lat": "31.1048", "hub_lng": "77.1734",
        "primary_city": "Shimla", "primary_cities": "Shimla, Dharamshala, Solan, and Mandi",
        "languages": "Hindi · Pahari · English", "hub_client_count": "80",
        "categories": {
            "admin_it": CAT_ADMIN_IT("Shimla", "Himachal Pradesh"),
            "industrial": CAT_INDUSTRIAL("Baddi-Solan"),
            "heritage": CAT_HERITAGE_TOURISM("Manali adventure resorts · Shimla heritage hotels · Dharamshala retreats"),
            "agro": CAT_AGRO("Apple packaging and transport · tea plantation estates"),
            "local": CAT_LOCAL_SERVICES,
        },
        "districts": [
            ("bilaspur","Bilaspur","31.3300","76.7600","local"),
            ("chamba","Chamba","32.5500","76.1300","heritage"),
            ("hamirpur","Hamirpur","31.6800","76.5200","local"),
            ("kangra","Kangra","32.1000","76.2700","heritage"),
            ("kinnaur","Kinnaur","31.6500","78.4700","heritage"),
            ("kullu","Kullu","31.9600","77.1100","heritage"),
            ("lahaul-and-spiti","Lahaul and Spiti","32.3000","77.5000","heritage"),
            ("mandi","Mandi","31.7100","76.9300","local"),
            ("shimla","Shimla","31.1048","77.1734","admin_it"),
            ("sirmaur","Sirmaur","30.5500","77.3000","industrial"),
            ("solan","Solan","30.9200","77.1200","industrial"),
            ("una","Una","31.4700","76.2700","industrial"),
        ]
    },
    "jammu-and-kashmir": {
        "state_name": "Jammu and Kashmir", "state_slug": "jammu-and-kashmir", "state_abbr": "JK",
        "geo_code": "IN-JK", "hub_lat": "34.0837", "hub_lng": "74.7973",
        "primary_city": "Srinagar", "primary_cities": "Srinagar, Jammu, Anantnag, and Kathua",
        "languages": "Urdu · Kashmiri · Dogri · Hindi · English", "hub_client_count": "70",
        "categories": {
            "admin_it": CAT_ADMIN_IT("Srinagar & Jammu", "Jammu and Kashmir"),
            "industrial": CAT_INDUSTRIAL("Kathua-Samba"),
            "heritage": CAT_HERITAGE_TOURISM("Gulmarg & Pahalgam adventure resorts · Srinagar houseboats · Vaishno Devi pilgrimage travel"),
            "agro": CAT_AGRO("Apple & walnut packaging · saffron trade & spice mills"),
            "local": CAT_LOCAL_SERVICES,
        },
        "districts": [
            ("anantnag","Anantnag","33.7300","75.1500","heritage"),
            ("bandipora","Bandipora","34.4200","74.6500","local"),
            ("baramulla","Baramulla","34.2000","74.3500","agro"),
            ("budgam","Budgam","34.0200","74.7200","local"),
            ("doda","Doda","33.1400","75.5700","local"),
            ("ganderbal","Ganderbal","34.2300","74.7800","heritage"),
            ("jammu","Jammu","32.7266","74.8570","admin_it"),
            ("kathua","Kathua","32.3800","75.5200","industrial"),
            ("kishtwar","Kishtwar","33.3100","75.7600","local"),
            ("kulgam","Kulgam","33.6500","75.0200","agro"),
            ("kupwara","Kupwara","34.5200","74.2500","local"),
            ("poonch","Poonch","33.7700","74.1000","local"),
            ("pulwama","Pulwama","33.8800","74.9000","agro"),
            ("rajouri","Rajouri","33.3800","74.3000","local"),
            ("ramban","Ramban","33.2500","75.2500","local"),
            ("reasi","Reasi","33.0800","74.8300","heritage"),
            ("samba","Samba","32.5600","75.1200","industrial"),
            ("shopian","Shopian","33.7200","74.8300","agro"),
            ("srinagar","Srinagar","34.0837","74.7973","admin_it"),
            ("udhampur","Udhampur","32.9300","75.1300","local"),
        ]
    },
    "goa": {
        "state_name": "Goa", "state_slug": "goa", "state_abbr": "GA",
        "geo_code": "IN-GA", "hub_lat": "15.4909", "hub_lng": "73.8278",
        "primary_city": "Panaji", "primary_cities": "Panaji, Margao, Mapusa, and Vasco da Gama",
        "languages": "Konkani · Marathi · English", "hub_client_count": "50",
        "categories": {
            "admin_it": CAT_ADMIN_IT("Panaji", "Goa"),
            "heritage": CAT_HERITAGE_TOURISM("Calangute & Baga beach resorts · Old Goa heritage churches · water sports"),
            "local": CAT_LOCAL_SERVICES,
        },
        "districts": [
            ("north-goa","North Goa","15.4989","73.8278","heritage"),
            ("south-goa","South Goa","15.2736","73.9580","heritage"),
        ]
    },
    "arunachal-pradesh": {
        "state_name": "Arunachal Pradesh", "state_slug": "arunachal-pradesh", "state_abbr": "AR",
        "geo_code": "IN-AR", "hub_lat": "27.1000", "hub_lng": "93.6200",
        "primary_city": "Itanagar", "primary_cities": "Itanagar, Pasighat, Namsai, and Tawang",
        "languages": "English · Hindi · Nyishi · Adi", "hub_client_count": "40",
        "categories": {
            "admin_it": CAT_ADMIN_IT("Itanagar", "Arunachal Pradesh"),
            "heritage": CAT_HERITAGE_TOURISM("Tawang monastery tours · Ziro Valley ecotourism · Namdapha national park adventure"),
            "agro": CAT_AGRO("Horticulture & fruit packaging · bamboo & wood craft mills"),
            "tribal": CAT_TRIBAL_FOREST,
            "local": CAT_LOCAL_SERVICES,
        },
        "districts": [
            ("anjaw","Anjaw","28.0000","96.5000","tribal"),
            ("changlang","Changlang","27.1200","95.7400","agro"),
            ("dibang-valley","Dibang Valley","28.8000","95.9000","heritage"),
            ("east-kameng","East Kameng","27.3000","93.0000","tribal"),
            ("east-siang","East Siang","28.0700","95.3300","agro"),
            ("kamle","Kamle","27.6000","93.8000","tribal"),
            ("kra-daadi","Kra Daadi","27.9000","93.5000","tribal"),
            ("kurung-kumey","Kurung Kumey","27.9000","93.3000","tribal"),
            ("lepa-rada","Lepa Rada","27.8000","94.7000","tribal"),
            ("lohit","Lohit","27.9200","96.1700","agro"),
            ("longding","Longding","26.8500","95.4000","tribal"),
            ("lower-dibang-valley","Lower Dibang Valley","28.1400","95.8300","heritage"),
            ("lower-siang","Lower Siang","27.7000","94.6000","tribal"),
            ("lower-subansiri","Lower Subansiri","27.5300","93.8400","heritage"),
            ("namsai","Namsai","27.6700","95.8700","heritage"),
            ("pakke-kessang","Pakke Kessang","27.1000","93.1000","tribal"),
            ("papum-pare","Papum Pare","27.1000","93.6200","admin_it"),
            ("shi-yomi","Shi Yomi","28.5000","94.2000","tribal"),
            ("siang","Siang","28.2000","94.8000","tribal"),
            ("tawang","Tawang","27.5800","91.8600","heritage"),
            ("tirap","Tirap","27.0000","95.5000","tribal"),
            ("upper-siang","Upper Siang","28.6000","94.9000","tribal"),
            ("upper-subansiri","Upper Subansiri","28.0000","94.1000","tribal"),
            ("west-kameng","West Kameng","27.2600","92.4200","heritage"),
            ("west-siang","West Siang","28.1700","94.8000","agro"),
        ]
    },
    "sikkim": {
        "state_name": "Sikkim", "state_slug": "sikkim", "state_abbr": "SK",
        "geo_code": "IN-SK", "hub_lat": "27.3300", "hub_lng": "88.6100",
        "primary_city": "Gangtok", "primary_cities": "Gangtok, Namchi, Mangan, and Soreng",
        "languages": "Nepali · Sikkimese · Lepcha · English", "hub_client_count": "30",
        "categories": {
            "admin_it": CAT_ADMIN_IT("Gangtok", "Sikkim"),
            "heritage": CAT_HERITAGE_TOURISM("Gangtok resorts · Rumtek monastery tours · organic farm tourism"),
            "agro": CAT_AGRO("Organic farming & cardamon packaging · tea garden packaging mills"),
            "local": CAT_LOCAL_SERVICES,
        },
        "districts": [
            ("gangtok","Gangtok","27.3314","88.6138","admin_it"),
            ("mangan","Mangan","27.5000","88.5300","heritage"),
            ("namchi","Namchi","27.1700","88.3500","heritage"),
            ("soreng","Soreng","27.1700","88.2000","agro"),
        ]
    },
    "meghalaya": {
        "state_name": "Meghalaya", "state_slug": "meghalaya", "state_abbr": "ML",
        "geo_code": "IN-ML", "hub_lat": "25.5700", "hub_lng": "91.8800",
        "primary_city": "Shillong", "primary_cities": "Shillong, Tura, Nongpoh, and Jowai",
        "languages": "Khasi · Garo · English", "hub_client_count": "45",
        "categories": {
            "admin_it": CAT_ADMIN_IT("Shillong", "Meghalaya"),
            "industrial": CAT_INDUSTRIAL("Byrnihat-Ri Bhoi"),
            "mining": CAT_MINING_ENERGY,
            "heritage": CAT_HERITAGE_TOURISM("Cherrapunji waterfalls travel · Shillong peak resorts · Mawlynnong village ecotourism"),
            "agro": CAT_AGRO("Lakadong turmeric & spice mills · organic horticulture packaging"),
            "local": CAT_LOCAL_SERVICES,
        },
        "districts": [
            ("east-garo-hills","East Garo Hills","25.6600","90.5800","local"),
            ("east-jaintia-hills","East Jaintia Hills","25.3000","92.4000","mining"),
            ("east-khasi-hills","East Khasi Hills","25.5700","91.8800","admin_it"),
            ("eastern-west-khasi-hills","Eastern West Khasi Hills","25.5000","91.5000","local"),
            ("north-garo-hills","North Garo Hills","25.9000","90.6000","local"),
            ("ri-bhoi","Ri Bhoi","25.9000","91.8800","industrial"),
            ("south-garo-hills","South Garo Hills","25.2800","90.6300","local"),
            ("south-west-garo-hills","South West Garo Hills","25.5000","89.9000","local"),
            ("south-west-khasi-hills","South West Khasi Hills","25.3000","91.2000","local"),
            ("west-garo-hills","West Garo Hills","25.5200","90.2200","agro"),
            ("west-jaintia-hills","West Jaintia Hills","25.4500","92.2000","agro"),
            ("west-khasi-hills","West Khasi Hills","25.5200","91.2600","local"),
        ]
    },
    "mizoram": {
        "state_name": "Mizoram", "state_slug": "mizoram", "state_abbr": "MZ",
        "geo_code": "IN-MZ", "hub_lat": "23.7300", "hub_lng": "92.7200",
        "primary_city": "Aizawl", "primary_cities": "Aizawl, Lunglei, Champhai, and Serchhip",
        "languages": "Mizo · English · Hindi", "hub_client_count": "25",
        "categories": {
            "admin_it": CAT_ADMIN_IT("Aizawl", "Mizoram"),
            "heritage": CAT_HERITAGE_TOURISM("Aizawl hill resorts · Reiek tourism packages · Phawngpui adventure travel"),
            "agro": CAT_AGRO("Bamboo craft mills & handlooms · organic fruit packaging"),
            "local": CAT_LOCAL_SERVICES,
        },
        "districts": [
            ("aizawl","Aizawl","23.7300","92.7200","admin_it"),
            ("champhai","Champhai","23.4700","93.3300","agro"),
            ("hnahthial","Hnahthial","22.9600","92.9300","local"),
            ("khawzawl","Khawzawl","23.5300","93.1800","local"),
            ("kolasib","Kolasib","24.2200","92.6800","agro"),
            ("lawngtlai","Lawngtlai","22.5300","92.9000","local"),
            ("lunglei","Lunglei","22.8800","92.7300","heritage"),
            ("mamit","Mamit","23.9300","92.4800","local"),
            ("saiha","Saiha","22.4800","92.9800","local"),
            ("serchhip","Serchhip","23.3000","92.8300","agro"),
        ]
    },
    "manipur": {
        "state_name": "Manipur", "state_slug": "manipur", "state_abbr": "MN",
        "geo_code": "IN-MN", "hub_lat": "24.8174", "hub_lng": "93.9368",
        "primary_city": "Imphal", "primary_cities": "Imphal, Thoubal, Bishnupur, and Ukhrul",
        "languages": "Manipuri (Meitei) · English · Hindi", "hub_client_count": "35",
        "categories": {
            "admin_it": CAT_ADMIN_IT("Imphal", "Manipur"),
            "heritage": CAT_HERITAGE_TOURISM("Loktak Lake ecotourism · Kangla Fort heritage tours · Sirohi National Park adventure"),
            "agro": CAT_AGRO("Horticulture & pineapple packaging · handloom weavers & craft mills"),
            "local": CAT_LOCAL_SERVICES,
        },
        "districts": [
            ("bishnupur","Bishnupur","24.6300","93.7600","heritage"),
            ("chandel","Chandel","24.3200","94.0200","local"),
            ("churachandpur","Churachandpur","24.3300","93.6800","local"),
            ("imphal-east","Imphal East","24.8000","93.9800","admin_it"),
            ("imphal-west","Imphal West","24.8174","93.9368","admin_it"),
            ("jiribam","Jiribam","24.8000","93.1200","local"),
            ("kakching","Kakching","24.4800","93.9800","agro"),
            ("kamjong","Kamjong","24.8000","94.3000","local"),
            ("kangpokpi","Kangpokpi","25.1500","93.9800","local"),
            ("nenglong","Nenglong","24.8500","93.6000","local"),
            ("pherzawl","Pherzawl","24.2800","93.2000","local"),
            ("senapati","Senapati","25.2600","94.0100","agro"),
            ("tamenglong","Tamenglong","24.9800","93.5000","agro"),
            ("tengnoupal","Tengnoupal","24.3800","94.1500","local"),
            ("thoubal","Thoubal","24.6400","94.0200","local"),
            ("ukhrul","Ukhrul","25.1200","94.3600","heritage"),
        ]
    },
    "nagaland": {
        "state_name": "Nagaland", "state_slug": "nagaland", "state_abbr": "NL",
        "geo_code": "IN-NL", "hub_lat": "25.6700", "hub_lng": "94.1200",
        "primary_city": "Kohima", "primary_cities": "Kohima, Dimapur, Mokokchung, and Wokha",
        "languages": "English · Nagamese · Hindi", "hub_client_count": "20",
        "categories": {
            "admin_it": CAT_ADMIN_IT("Kohima", "Nagaland"),
            "industrial": CAT_INDUSTRIAL("Dimapur"),
            "heritage": CAT_HERITAGE_TOURISM("Hornbill Festival tourism · Kohima heritage stays · Mokokchung cultural tours"),
            "agro": CAT_AGRO("Spices & honey packaging · organic bamboo & wood crafts"),
            "local": CAT_LOCAL_SERVICES,
        },
        "districts": [
            ("chumoukedima","Chumoukedima","25.8300","93.7800","industrial"),
            ("dimapur","Dimapur","25.9000","93.7300","industrial"),
            ("kiphire","Kiphire","25.9000","94.7800","local"),
            ("kohima","Kohima","25.6700","94.1200","admin_it"),
            ("longleng","Longleng","26.4700","94.8200","local"),
            ("mokokchung","Mokokchung","26.3300","94.5200","heritage"),
            ("mon","Mon","26.7500","95.0600","local"),
            ("niuland","Niuland","25.9500","93.9000","agro"),
            ("noklak","Noklak","26.2000","95.0000","local"),
            ("peraen","Peraen","25.5200","93.5800","local"),
            ("phek","Phek","25.6700","94.5000","agro"),
            ("shamator","Shamator","26.0500","94.9000","local"),
            ("tuensang","Tuensang","26.2800","94.8300","local"),
            ("wokha","Wokha","26.0900","94.2600","agro"),
            ("zunheboto","Zunheboto","25.9700","94.5200","local"),
            ("tseminyu","Tseminyu","25.9000","94.2000","local"),
        ]
    },
    "tripura": {
        "state_name": "Tripura", "state_slug": "tripura", "state_abbr": "TR",
        "geo_code": "IN-TR", "hub_lat": "23.8400", "hub_lng": "91.2800",
        "primary_city": "Agartala", "primary_cities": "Agartala, Udaipur, Dharmanagar, and Kailasahar",
        "languages": "Bengali · Kokborok · English", "hub_client_count": "30",
        "categories": {
            "admin_it": CAT_ADMIN_IT("Agartala", "Tripura"),
            "heritage": CAT_HERITAGE_TOURISM("Unakoti rock carvings · Neermahal water palace · Ujjayanta Palace tours"),
            "agro": CAT_AGRO("Rubber processing & sheet packaging · bamboo craft mills"),
            "local": CAT_LOCAL_SERVICES,
        },
        "districts": [
            ("dhalai","Dhalai","24.0300","91.8800","local"),
            ("gomati","Gomati","23.5300","91.4800","heritage"),
            ("khowai","Khowai","24.0600","91.6000","agro"),
            ("north-tripura","North Tripura","24.2600","92.1700","agro"),
            ("sepahijala","Sepahijala","23.6300","91.3200","heritage"),
            ("south-tripura","South Tripura","23.1200","91.5000","agro"),
            ("unakoti","Unakoti","24.2400","92.0200","heritage"),
            ("west-tripura","West Tripura","23.8400","91.2800","admin_it"),
        ]
    },
    "lakshadweep": {
        "state_name": "Lakshadweep", "state_slug": "lakshadweep", "state_abbr": "LD",
        "geo_code": "IN-LD", "hub_lat": "10.5700", "hub_lng": "72.6400",
        "primary_city": "Kavaratti", "primary_cities": "Kavaratti, Agatti, and Minicoy",
        "languages": "Malayalam · Jeseri · English", "hub_client_count": "10",
        "categories": {
            "admin_it": CAT_ADMIN_IT("Kavaratti", "Lakshadweep"),
            "heritage": CAT_HERITAGE_TOURISM("Bangaram & Agatti coral reef resorts · water sports & scuba diving packages"),
            "agro": CAT_AGRO("Coir & coconut processing · tuna fish packaging & cold storage"),
            "local": CAT_LOCAL_SERVICES,
        },
        "districts": [
            ("lakshadweep","Lakshadweep","10.5700","72.6400","heritage"),
        ]
    },
    "puducherry": {
        "state_name": "Puducherry", "state_slug": "puducherry", "state_abbr": "PY",
        "geo_code": "IN-PY", "hub_lat": "11.9416", "hub_lng": "79.8083",
        "primary_city": "Puducherry", "primary_cities": "Puducherry, Karaikal, Mahe, and Yanam",
        "languages": "Tamil · French · Telugu · Malayalam · English", "hub_client_count": "20",
        "categories": {
            "admin_it": CAT_ADMIN_IT("Puducherry", "Puducherry"),
            "heritage": CAT_HERITAGE_TOURISM("Auroville spiritual tourism · French Quarter guesthouses · beach resorts"),
            "agro": CAT_AGRO("Rice mills & food processing · coconut product packaging"),
            "local": CAT_LOCAL_SERVICES,
        },
        "districts": [
            ("karaikal","Karaikal","10.9200","79.8300","local"),
            ("mahe","Mahe","11.7000","75.5300","local"),
            ("puducherry","Puducherry","11.9416","79.8083","admin_it"),
            ("yanam","Yanam","16.7300","82.2100","local"),
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
