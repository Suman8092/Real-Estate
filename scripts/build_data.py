import json
import os

properties = [
    # --- DEMO2 PROPERTIES ---
    {
        "id": "vrindaan",
        "slug": "project-vrindaan",
        "name": "Vrindaan",
        "developer": "Vrindaan Developers",
        "city": "Vrindavan",
        "state": "Uttar Pradesh",
        "locality": "Raal Road",
        "address": "Raal Road, Vrindavan, Mathura, Uttar Pradesh – 281121",
        "propertyType": "Residential Plots & Signature Villas",
        "category": "residential",
        "status": "Ready to Move / Ongoing",
        "startingPrice": "₹45 Lakh*",
        "maximumPrice": "₹1.85 Cr*",
        "priceDisplay": "₹45 Lakh – ₹1.85 Cr*",
        "priceNote": "Starting price for 145 sq. yd. residential plots. Villa pricing includes 4 BHK + servant room.",
        "bhkConfig": "Plots (145, 180, 230 sq. yd.) & 4 BHK Villas",
        "bhkOptions": ["Plots", "4 BHK"],
        "carpetArea": "145 – 350 sq. yd.",
        "superArea": "2,950 sq. ft. (Signature Villa)",
        "possessionDate": "Ready for Possession",
        "reraNumber": "UPRERAPRM495523",
        "image": "images/1.jpg",
        "gallery": ["images/1.jpg", "images/2.jpg", "images/pro1-516x360.jpg"],
        "overview": "Vrindaan is an exclusive residential township situated in the sacred heart of Braj on Raal Road, Vrindavan. The development seamlessly integrates plotted residential spaces, signature luxury villas, spiritual centres, and lush landscaped open parks.",
        "description": "A tranquil haven combining traditional ethos with modern luxury. Designed for seekers of serenity and discerning homeowners, Vrindaan provides wide tree-lined boulevards, dedicated meditation zones, herbal gardens, and 24/7 gated security.",
        "highlights": [
            "Prime location on Raal Road, Vrindavan with swift connection to NH-19 and Bhaktivedanta Swami Marg.",
            "Signature 4 BHK villas with private servant quarters and 2,950 sq. ft. super area.",
            "Dedicated spiritual retreats, meditation enclosures, and fragrant herbal flora.",
            "Fully approved gated community with underground cabling and 24/7 water supply."
        ],
        "specifications": [
            "Plot Sizes: 145, 180 and 230 sq. yd.",
            "Signature Villa: 350 sq. yd. plot; 4 BHK + servant room; ~2,950 sq. ft. super area.",
            "Road Infrastructure: 30 ft and 40 ft wide black-top paved avenues.",
            "Water & Power: Dual overhead storage tanks and dedicated 33kV feeder line."
        ],
        "amenities": [
            "5-star managed suites", "Spiritual meditation centre", "Herbal garden & organic orchard",
            "Clubhouse & wellness gym", "Swimming pool & sun deck", "Play school & daycare plots",
            "Private clinic & healthcare spaces", "24/7 security with perimeter CCTV"
        ],
        "locationAdvantages": [
            "10 minutes from Prem Mandir & ISKCON Vrindavan",
            "15 minutes from Bankey Bihari Temple",
            "Direct access to NH-19 (Delhi-Agra Expressway)",
            "30 minutes from Mathura Junction railway station"
        ],
        "paymentPlan": "Flexible construction-linked payment plan: 10% booking, 40% over 6 months, 50% upon possession.",
        "isDemo2": True,
        "isTopProject": True,
        "isFeatured": True
    },
    {
        "id": "lifestyle-central",
        "slug": "project-lifestyle-central",
        "name": "Lifestyle Central",
        "developer": "BNX Group",
        "city": "Greater Noida",
        "state": "Uttar Pradesh",
        "locality": "Delta 2",
        "address": "8/G/2, Delta 2, Greater Noida, Uttar Pradesh – 201310",
        "propertyType": "Boutique Retail & Hotel Suites",
        "category": "commercial",
        "status": "Under Construction",
        "startingPrice": "₹65 Lakh*",
        "maximumPrice": "₹2.5 Cr*",
        "priceDisplay": "₹65 Lakh – ₹2.5 Cr*",
        "priceNote": "Starting price for premium lockable suites. Retail spaces available with pre-leased guarantee.",
        "bhkConfig": "Luxury Studio Suites & Retail Shops",
        "bhkOptions": ["Studio", "Commercial Retail"],
        "carpetArea": "420 – 1,180 sq. ft.",
        "superArea": "645 – 1,615 sq. ft.",
        "possessionDate": "December 2026",
        "reraNumber": "UPRERAPRJ764512",
        "image": "images/lifestyle-central-updated-cover.webp",
        "gallery": [
            "images/lifestyle-central-updated-cover.webp",
            "images/lifestyle-central-updated-tower.webp",
            "images/lifestyle-central-updated-retail-render.webp",
            "images/lifestyle-central-updated-hotel-suite.webp",
            "images/lifestyle-central-updated-leisure-plan.webp"
        ],
        "overview": "Lifestyle Central by BNX Group is Greater Noida's marquee commercial and hospitality landmark located in Delta 2. It integrates high-street luxury retail, serviced hotel suites, banquet facilities, and a panoramic rooftop leisure club.",
        "description": "Rising 18 storeys high, Lifestyle Central redefines urban leisure and business. With lower levels catering to high-end global retail brands and dining, the upper floors feature 133 fully serviced boutique suites operated under global hospitality standards.",
        "highlights": [
            "Ground to 2nd Floor: High-street retail promenades and international gourmet dining.",
            "3rd Floor: Grand banquet hall catering for 500+ guests for conferences and celebrations.",
            "9th to 17th Floor: 133 luxury studio suites with hotel-grade concierge and housekeeping.",
            "18th Floor Rooftop: Signature infinity pool, open sky lounge, and cocktail bar."
        ],
        "specifications": [
            "Structure: Earthquake-resistant RCC frame with high acoustic performance.",
            "Parking: Mechanical multi-level automated car parking spanning 4 levels.",
            "Elevators: 6 high-speed smart destination-controlled passenger elevators.",
            "Power Backup: 100% full load redundant DG power backup."
        ],
        "amenities": [
            "Rooftop infinity swimming pool", "Sky lounge & sunset bar", "Grand 500-capacity banquet hall",
            "Mechanical multi-level parking", "High-street retail boulevard", "Concierge & bell desk services",
            "24/7 security with smart access", "Central VRV air-conditioning"
        ],
        "locationAdvantages": [
            "Walking distance from Delta 1 Metro Station (Aqua Line)",
            "5 minutes from Pari Chowk, Greater Noida",
            "Direct connectivity to Yamuna Expressway & Noida-Greater Noida Expressway",
            "Surrounded by established residential sectors and IT parks"
        ],
        "paymentPlan": "Assured rental investment plan: 50:25:25 or customized milestone plan with 12% return commitments.",
        "isDemo2": True,
        "isTopProject": True,
        "isFeatured": True
    },
    {
        "id": "casa-corbett",
        "slug": "project-casa-corbett",
        "name": "Casa Corbett",
        "developer": "AGF Group",
        "city": "Kalagarh",
        "state": "Uttar Pradesh",
        "locality": "Corbett Buffer Region",
        "address": "Kalagarh, Near Jim Corbett National Park Foothills, Uttar Pradesh – 246142",
        "propertyType": "Holiday-home, Villa & Farmhouse Plots",
        "category": "farmhouse",
        "status": "Ready for Possession",
        "startingPrice": "₹35 Lakh*",
        "maximumPrice": "₹1.4 Cr*",
        "priceDisplay": "₹35 Lakh – ₹1.4 Cr*",
        "priceNote": "Plots starting at 500 sq. yd. Custom resort villa construction available upon request.",
        "bhkConfig": "Farmhouse Plots (500, 1000, 2000 sq. yd.) & Resort Villas",
        "bhkOptions": ["Plots", "3 BHK", "4 BHK"],
        "carpetArea": "500 – 2,000 sq. yd.",
        "superArea": "2,200 – 4,800 sq. ft. (Villas)",
        "possessionDate": "Immediate / Ongoing",
        "reraNumber": "UPRERAPRM881923",
        "image": "images/casa-corbett-updated-cover.webp",
        "gallery": [
            "images/casa-corbett-updated-cover.webp",
            "images/casa-corbett-updated-plot-fields.webp",
            "images/casa-corbett-updated-philosophy-river.webp",
            "images/casa-corbett-updated-plot-types.webp",
            "images/casa-corbett-updated-resort-villa.webp"
        ],
        "overview": "Casa Corbett by AGF Group is an idyllic resort-living sanctuary nestled against the lush foothills of Kalagarh near Corbett National Park. It offers pristine farmhouse plots and bespoke resort cottages.",
        "description": "Escape the pollution of the metropolis and reconnect with nature. Casa Corbett features riverside trails, private organic orchards, wellness pavilions, and unobstructed views of the Shivalik ranges.",
        "highlights": [
            "Scenic location in the pristine ecological corridor near Corbett Tiger Reserve.",
            "Spacious plotted layouts from 500 sq. yd. up to 2,000 sq. yd.",
            "Dedicated riverfront promenade and wellness meditation meadows.",
            "Resort-style club facilities with concierge management for absentee owners."
        ],
        "specifications": [
            "Plot Sizes: 500, 1,000, 1,500 and 2,000 sq. yd.",
            "Internal Access: 35 ft and 45 ft wide paved nature-aligned roads.",
            "Fencing: Biosensitive solar-powered boundary fencing.",
            "Power & Water: Solar street-lighting and deep groundwater boring connection."
        ],
        "amenities": [
            "Resort club & swimming pool", "Riverfront jogging track", "Organic farming & fruit groves",
            "Outdoor yoga & wellness deck", "Bonfire & celebration lawn", "24/7 manned security checkposts",
            "Rental management support", "Children's eco playground"
        ],
        "locationAdvantages": [
            "Bordering the Ramganga river and Corbett buffer forest",
            "20 minutes from Kalagarh Dam panoramic viewpoint",
            "Easy driving route from Delhi NCR via Moradabad-Kashipur highway",
            "Close proximity to luxury safari eco-resorts"
        ],
        "paymentPlan": "20% booking advance, 50% within 45 days, 30% upon registry and boundary handover.",
        "isDemo2": True,
        "isTopProject": True,
        "isFeatured": True
    },
    {
        "id": "anantara",
        "slug": "project-anantara",
        "name": "Anantara",
        "developer": "AGF Group",
        "city": "Kalagarh",
        "state": "Uttar Pradesh",
        "locality": "Near Kalagarh Dam, Amangarh region",
        "address": "Near Kalagarh Dam, Amangarh Tiger Corridor, Uttar Pradesh – 246142",
        "propertyType": "AgriForest Plots & Nature Cottages",
        "category": "farmhouse",
        "status": "Ongoing Development",
        "startingPrice": "₹15 Lakh*",
        "maximumPrice": "₹65 Lakh*",
        "priceDisplay": "₹15 Lakh – ₹65 Lakh*",
        "priceNote": "Modular cottage construction: ₹8–15 lakh*. Farm plots from ₹15 lakh*. Development charges separate.",
        "bhkConfig": "AgriForest Plots & 1/2 BHK Nature Cottages",
        "bhkOptions": ["Plots", "1 BHK", "2 BHK"],
        "carpetArea": "250 – 1,200 sq. yd.",
        "superArea": "650 – 1,450 sq. ft. (Cottages)",
        "possessionDate": "March 2026",
        "reraNumber": "UPRERAPRM632145",
        "image": "images/anantara-updated-07.webp",
        "gallery": [
            "images/anantara-updated-07.webp",
            "images/anantara-updated-12.webp",
            "images/anantara-updated-06.webp",
            "images/anantara-updated-10.webp",
            "images/anantara-updated-00.webp"
        ],
        "overview": "Anantara is an expansive 23.25-acre AgriForest community located adjacent to the Kalagarh Dam and Amangarh wildlife corridor. It integrates sustainable agro-forestry with eco-cottages.",
        "description": "Anantara offers an authentic country living experience where every plot owner benefits from shared fruit plantations, medicinal flora, and professionally maintained sustainable farming practices.",
        "highlights": [
            "23.25-acre masterplanned agro-forestry township.",
            "Affordable modular cottages starting from ₹8–15 lakh*.",
            "Managed plantation including teak, mango, and medicinal herbs.",
            "Zero carbon footprint development ethos with solar backup."
        ],
        "specifications": [
            "Total Land Area: 23.25 contiguous acres.",
            "Plot Dimensions: 250, 500, and 1,000 sq. yd.",
            "Cottage Build: Prefab insulated sustainable timber-frame modular cottages.",
            "Water Source: Natural rainwater harvesting canals and natural aquifers."
        ],
        "amenities": [
            "AgriForest plantation & orchards", "Eco-friendly modular cottages", "Forest walking trails",
            "Community retreat clubhouse", "Organic vegetable farm", "Stargazing observatory deck",
            "Solar boundary protection", "24/7 security & caretaker staff"
        ],
        "locationAdvantages": [
            "Adjacent to Kalagarh Dam and Amangarh Tiger Corridor",
            "Unspoilt green forest belt with high biodiversity",
            "Direct road access connecting to Najibabad and Kotdwar",
            "Under 4 hours drive from Central Delhi"
        ],
        "paymentPlan": "Convenient flexi plan: 25% down payment, 50% over 12 equal monthly installments, 25% on possession.",
        "isDemo2": True,
        "isTopProject": True,
        "isFeatured": True
    },
    {
        "id": "vantara-heritage",
        "slug": "project-vantara-heritage",
        "name": "Vantara Heritage",
        "developer": "AGF Group",
        "city": "Garhmukteshwar",
        "state": "Uttar Pradesh",
        "locality": "Brijghat, Hapur",
        "address": "Brijghat, Garhmukteshwar, Hapur District, Uttar Pradesh – 245205",
        "propertyType": "Villa & Farmhouse Plots",
        "category": "residential",
        "status": "Ongoing / Booking Open",
        "startingPrice": "₹14,999 / sq. yd.*",
        "maximumPrice": "₹95 Lakh*",
        "priceDisplay": "From ₹14,999 / sq. yd.*",
        "priceNote": "Brochure starting price ₹14,999/sq.yd. 10% PLC applicable on corner/park-facing plots.",
        "bhkConfig": "Township Villa & Farmhouse Plots",
        "bhkOptions": ["Plots", "3 BHK", "4 BHK"],
        "carpetArea": "150 – 1,000 sq. yd.",
        "superArea": "Customized Villa Layouts",
        "possessionDate": "June 2026",
        "reraNumber": "UPRERAPRM419082",
        "image": "images/vantara-heritage-cover.webp",
        "gallery": [
            "images/vantara-heritage-cover.webp",
            "images/vantara-heritage-overview.webp",
            "images/vantara-heritage-plot.webp",
            "images/vantara-heritage-farmhouse.webp",
            "images/vantara-heritage-location-art.webp"
        ],
        "overview": "Vantara Heritage is a prestigious 55+ acre gated mega-township situated at Brijghat, Garhmukteshwar. It blends the holy heritage of the Ganges with high-specification villa and farmhouse plots.",
        "description": "Offering world-class living just an hour's drive from Delhi NCR on NH-9, Vantara Heritage provides wide asphalt roads, private artificial lakes, grand entry gates, and resort-grade amenities.",
        "highlights": [
            "Expansive 55+ acre gated township with grand royal entry arches.",
            "Dual options: Residential villa plots and spacious farmhouse plots.",
            "Wide 30 ft and 40 ft paved internal road network with street lighting.",
            "Prime highway frontage on the Delhi-Lucknow Highway (NH-9)."
        ],
        "specifications": [
            "Township Extent: 55+ acres fully walled development.",
            "Plot Sizes: 150, 200, 300, 500 and 1,000 sq. yd.",
            "Electrification: Government power grid substation connectivity.",
            "Drainage: Underground storm water and treated sewage pipelines."
        ],
        "amenities": [
            "Grand clubhouse & wellness spa", "Swimming pool & splash deck", "Scenic artificial lake & promenade",
            "Jogging & cycling tracks", "Kids adventure park & senior citizens lounge", "Badminton & basketball courts",
            "24/7 multi-tier security & surveillance", "Underground cabling & streetlights"
        ],
        "locationAdvantages": [
            "Located directly on NH-9 (Delhi-Garhmukteshwar Highway)",
            "5 minutes from Brijghat Ganga Ghats",
            "45 minutes from Noida and Ghaziabad via Delhi-Meerut Expressway",
            "Upcoming industrial and tourism corridor node"
        ],
        "paymentPlan": "Special inaugural plan: 10% booking, 40% in 30 days, 50% spread over development milestones.",
        "isDemo2": True,
        "isTopProject": True,
        "isFeatured": True
    },
    {
        "id": "aurya-city",
        "slug": "project-aurya-city",
        "name": "Aurya City",
        "developer": "AGF Group",
        "city": "Dholera",
        "state": "Gujarat",
        "locality": "Near Dholera SIR",
        "address": "Near Dholera SIR Activation Zone, Dholera Smart City, Gujarat – 382455",
        "propertyType": "Residential Plots & Smart Living",
        "category": "residential",
        "status": "Upcoming / New Launch",
        "startingPrice": "₹18 Lakh*",
        "maximumPrice": "₹60 Lakh*",
        "priceDisplay": "₹18 Lakh – ₹60 Lakh*",
        "priceNote": "Early investor pricing in India's first greenfield industrial smart city.",
        "bhkConfig": "Smart City Residential Plots",
        "bhkOptions": ["Plots"],
        "carpetArea": "120 – 500 sq. yd.",
        "superArea": "1,080 – 4,500 sq. ft.",
        "possessionDate": "December 2026",
        "reraNumber": "PR/GJ/AHMEDABAD/DHOLERA/RAA11029",
        "image": "images/aurya-city-updated-20.webp",
        "gallery": [
            "images/aurya-city-updated-20.webp",
            "images/aurya-city-updated-16.webp",
            "images/aurya-city-updated-22.webp",
            "images/aurya-city-updated-26.webp",
            "images/aurya-city-updated-17.webp"
        ],
        "overview": "Aurya City is an ambitious 250-acre master-planned residential township located right adjacent to India's first semiconductor and manufacturing smart hub, Dholera Special Investment Region (SIR).",
        "description": "Positioned for unprecedented capital appreciation, Aurya City combines high-grade urban planning, ICT-enabled utility networks, tree-lined avenues, and complete clear-title documentation.",
        "highlights": [
            "250-acre planned smart township inside the immediate Dholera SIR influence zone.",
            "Walking distance from planned commercial shopping and entertainment hubs.",
            "High investment potential backed by Dholera International Airport & Expressway.",
            "Guaranteed clear title with immediate registration readiness."
        ],
        "specifications": [
            "Total Land Parcel: 250 acres master development.",
            "Plot Categories: 120, 150, 200, 300, and 500 sq. yd.",
            "Smart Infrastructure: Smart metering, underground drainage, and optical fiber.",
            "Road Width: 12-meter and 18-meter wide sector arterial roads."
        ],
        "amenities": [
            "Smart clubhouse & banquet hall", "Commercial shopping complexes", "Sports academy & tennis courts",
            "Healthcare clinic spaces", "Educational academy zone", "Landscaped sensory parks",
            "24/7 CCTV surveillance & gated entry", "EV charging parking stations"
        ],
        "locationAdvantages": [
            "Adjacent to Dholera SIR Activation Area",
            "15 minutes from upcoming Dholera International Airport",
            "Direct access to Ahmedabad-Dholera Expressway (109 km)",
            "Close to upcoming Tata Semiconductor Fab unit"
        ],
        "paymentPlan": "10% booking advance, 40% within 15 days, balance 50% within 30 days or bank loan.",
        "isDemo2": True,
        "isTopProject": True,
        "isFeatured": True
    },
    {
        "id": "bnx-group",
        "slug": "project-bnx-group",
        "name": "BNX Group (Pride Plaza)",
        "developer": "BNX Group",
        "city": "Greater Noida",
        "state": "Uttar Pradesh",
        "locality": "Delta 2",
        "address": "8/G/2, Delta 2, Greater Noida, Uttar Pradesh – 201310",
        "propertyType": "Studios, Retail & Hospitality",
        "category": "commercial",
        "status": "Under Construction",
        "startingPrice": "₹55 Lakh*",
        "maximumPrice": "₹2.2 Cr*",
        "priceDisplay": "₹55 Lakh – ₹2.2 Cr*",
        "priceNote": "High ROI commercial and studio apartments with attractive lease-back options.",
        "bhkConfig": "Luxury Studio Suites, Retail, & Office Spaces",
        "bhkOptions": ["Studio", "1 BHK", "Commercial"],
        "carpetArea": "380 – 1,200 sq. ft.",
        "superArea": "550 – 1,850 sq. ft.",
        "possessionDate": "October 2026",
        "reraNumber": "UPRERAPRJ882415",
        "image": "images/bnx-group-tower.webp",
        "gallery": [
            "images/bnx-group-tower.webp",
            "images/bnx-group-tower-detail.webp",
            "images/bnx-group-hotel.webp",
            "images/bnx-group-commercial.webp",
            "images/bnx-group-industries.webp"
        ],
        "overview": "Pride Plaza / Lifestyle Central by BNX Group represents the pinnacle of multi-faceted commercial real estate in Greater Noida, featuring hospitality suites, retail showrooms, and corporate workspaces.",
        "description": "Engineered for maximum investment return and customer footfall, BNX Group brings world-class construction, intelligent space planning, and premium amenities under one iconic architectural roof.",
        "highlights": [
            "Integrated destination combining retail, hospitality, banquet, and rooftop dining.",
            "Strategic frontage in prime Delta 2 commercial corridor.",
            "High rental yields driven by Greater Noida university and industrial belt.",
            "Turnkey furnished suites with high-grade European fixtures."
        ],
        "specifications": [
            "Building Height: Ground + 18 commercial and hospitality levels.",
            "Floors 4–7: Advanced robotic mechanical car parking.",
            "Floor 3: Grand 500-guest ballroom with pre-function atrium.",
            "HVAC: Central water-cooled chiller air-conditioning plant."
        ],
        "amenities": [
            "Hotel suites managed by hospitality partners", "Mechanical multi-level parking",
            "High-street branded retail shops", "Fine dining restaurants & food court", "Infinity pool & sky terrace",
            "High-speed passenger & service elevators", "24/7 security with access controls", "Power backup 100%"
        ],
        "locationAdvantages": [
            "Direct metro connectivity via Aqua Line Delta 1 Station",
            "Direct connection to Yamuna Expressway & FNG corridor",
            "Close proximity to Knowledge Park institutional cluster",
            "Surrounded by high-density residential sectors"
        ],
        "paymentPlan": "Special investor plan: 50% on booking, 25% on structure completion, 25% on offer of possession.",
        "isDemo2": True,
        "isTopProject": True,
        "isFeatured": True
    },
    {
        "id": "godrej-tropical-isle",
        "slug": "project-godrej-tropical-isle",
        "name": "Godrej Tropical Isle",
        "developer": "Godrej Properties",
        "city": "Noida",
        "state": "Uttar Pradesh",
        "locality": "Sector 44",
        "address": "Plot No GH-01, Sector 44, Noida Expressway, Noida, UP – 201303",
        "propertyType": "Luxury Island-Themed Residences",
        "category": "residential",
        "status": "Under Construction",
        "startingPrice": "₹3.2 Cr*",
        "maximumPrice": "₹6.8 Cr*",
        "priceDisplay": "₹3.2 Cr – ₹6.8 Cr*",
        "priceNote": "Ultra-luxury 3 and 4 BHK island-inspired apartments with private elevator access.",
        "bhkConfig": "3 BHK & 4 BHK Luxury Residences",
        "bhkOptions": ["3 BHK", "4 BHK"],
        "carpetArea": "1,450 – 2,450 sq. ft.",
        "superArea": "1,800 – 3,250 sq. ft.",
        "possessionDate": "February 2028",
        "reraNumber": "UPRERAPRJ446589",
        "image": "images/godrej-tropical-isle.webp",
        "gallery": [
            "images/godrej-tropical-isle.webp",
            "images/selected-building-illustration.png",
            "images/pro1-516x360.jpg"
        ],
        "overview": "Godrej Tropical Isle in Sector 44 Noida brings ultra-luxury island resort-style living to the heart of Noida. Featuring island-inspired architecture, floating cabanas, private decks, and air purification systems.",
        "description": "Strategically positioned at Sector 44 right at the start of the Noida-Greater Noida Expressway, Godrej Tropical Isle offers seamless access to South Delhi and Central Noida while enveloping residents in lush tropical greenery.",
        "highlights": [
            "Prime Sector 44 location — just 2 minutes from South Delhi via Kalindi Kunj and DND.",
            "Tropical resort aesthetic with water pavilions, floating cabanas, and beach-edge pool.",
            "Exclusive low-density masterplan with wide central greens and panoramic views.",
            "Air purification technology in every apartment unit and common areas."
        ],
        "specifications": [
            "Towers: Iconic high-rises with double-height designer arrival lobbies.",
            "Air Conditioning: VRV/VRF air conditioning in living, dining, and bedrooms.",
            "Flooring: Imported Italian marble in living and dining; laminated wooden in master bedroom.",
            "Kitchen: Fully fitted modular kitchen with European hob, chimney, and dishwasher."
        ],
        "amenities": [
            "Grand tropical clubhouse", "Beach-edge swimming pool & floating cabanas", "Indoor temperature-controlled pool",
            "Tennis, squash & badminton courts", "State-of-the-art gymnasium & Pilates studio", "Private cinema screening lounge",
            "Dedicated concierge desk", "5-tier smart security & video intercom"
        ],
        "locationAdvantages": [
            "Direct connectivity to DND Flyway & Kalindi Kunj (5 mins to Delhi)",
            "3 minutes from Botanical Garden Metro Interchange",
            "Close proximity to Golf Course Noida & Max Super Speciality Hospital",
            "Top schools (Amity, Lotus Valley, Step by Step) within 10 minutes"
        ],
        "paymentPlan": "Construction-linked milestone plan: 10% on booking, 15% on foundation, balance linked to floor slabs.",
        "isDemo2": True,
        "isTopProject": True,
        "isFeatured": True
    },
    {
        "id": "eon-fairfox",
        "slug": "project-eon-fairfox",
        "name": "EON Fairfox",
        "developer": "Fairfox IT Infra",
        "city": "Noida",
        "state": "Uttar Pradesh",
        "locality": "Sector 140A",
        "address": "EON, Plot No-01A, Sector 140A, Noida, Uttar Pradesh – 201304",
        "propertyType": "Commercial Office Spaces & Retail",
        "category": "commercial",
        "status": "Under Construction / Pre-Leased Options",
        "startingPrice": "₹42 Lakh*",
        "maximumPrice": "₹3.5 Cr*",
        "priceDisplay": "₹42 Lakh – ₹3.5 Cr*",
        "priceNote": "Lockable office units and high-street retail spaces with attractive lease assistance.",
        "bhkConfig": "Lockable IT/ITeS Offices & Retail Showrooms",
        "bhkOptions": ["Commercial Office", "Commercial Retail"],
        "carpetArea": "250 – 1,800 sq. ft.",
        "superArea": "350 – 2,500 sq. ft.",
        "possessionDate": "December 2026",
        "reraNumber": "UPRERAPRJ211016",
        "image": "images/eon-fairfox.jpeg",
        "gallery": [
            "images/eon-fairfox.jpeg",
            "images/building_image_in_organic_template-optimized.webp",
            "images/about-commercial-building.webp"
        ],
        "overview": "Fairfox Eye of Noida (EON) is an iconic 13.5-acre IGBC Gold certified commercial development situated at Sector 140A Noida Expressway. It sets a new benchmark in sustainable corporate workspaces and lifestyle retail.",
        "description": "Featuring pedestrian-friendly multi-level skywalks, expansive central green courtyards, international dining zones, and high-tech lockable workspaces, EON is the epicenter of business along the Expressway.",
        "highlights": [
            "Massive 13.5-acre development in Noida's premier high-tech institutional sector.",
            "IGBC Gold certified green building design minimizing operational overheads.",
            "43-meter wide arterial road frontage with dedicated multi-level entry and exit gates.",
            "High-street retail boulevard with 84-meter central pedestrian plaza."
        ],
        "specifications": [
            "Structure: Grade-A high-efficiency earthquake-resistant steel-concrete frame.",
            "Elevators: 24 high-speed destination-dispatch elevators.",
            "Ceiling Heights: 4.2-meter clear floor-to-ceiling heights in offices.",
            "Power: 100% redundant DG power backup with automated load sharing."
        ],
        "amenities": [
            "Grade-A lockable corporate office suites", "Skywalk interconnected retail promenades",
            "Grand central water courtyards & food court", "Multi-tier automated basement parking",
            "Conference halls & business meeting rooms", "24/7 security with thermal screening & BMS",
            "EV charging infrastructure", "High-speed optical fiber connectivity"
        ],
        "locationAdvantages": [
            "Located at Sector 140A, Noida-Greater Noida Expressway",
            "2 minutes from Sector 137 Metro Station (Aqua Line)",
            "Immediate connectivity to FNG (Faridabad-Noida-Ghaziabad) Expressway",
            "Surrounded by over 50,000 residential families within a 3 km radius"
        ],
        "paymentPlan": "Attractive 50:25:25 investment plan or flexi construction-linked schedule with lease guarantee.",
        "isDemo2": True,
        "isTopProject": True,
        "isFeatured": True
    },

    # --- PROPERTYPISTOL TOP PROJECTS: DELHI ---
    {
        "id": "godrej-south-estate",
        "slug": "project-godrej-south-estate",
        "name": "Godrej South Estate - Prima",
        "developer": "Godrej Properties",
        "city": "Delhi",
        "state": "Delhi",
        "locality": "Okhla Phase 1, South Delhi",
        "address": "Plot No 3, Okhla Industrial Area Phase 1, South Delhi, Delhi – 110020",
        "propertyType": "Super Luxury Residential High-Rise",
        "category": "residential",
        "status": "Under Construction",
        "startingPrice": "₹4.8 Cr*",
        "maximumPrice": "₹12 Cr*",
        "priceDisplay": "₹4.8 Cr – ₹12 Cr*",
        "priceNote": "Luxury 2, 3 and 4 BHK residences with copper crowns and air purification systems.",
        "bhkConfig": "2, 3 & 4 BHK Luxury Residences",
        "bhkOptions": ["2 BHK", "3 BHK", "4 BHK"],
        "carpetArea": "1,050 – 2,750 sq. ft.",
        "superArea": "1,500 – 3,850 sq. ft.",
        "possessionDate": "June 2026",
        "reraNumber": "DLRERA2019P0003",
        "image": "images/pro1-516x360.jpg",
        "gallery": ["images/pro1-516x360.jpg", "images/p13-516x360.jpg", "images/pro2-516x360.jpg"],
        "overview": "Godrej South Estate is Delhi's landmark high-rise luxury residential development located in South Delhi. Designed with bespoke copper crowns, 5-tier security, and state-of-the-art common area air purification.",
        "description": "The first gated high-rise enclave in South Delhi by Godrej Properties, featuring grand manicured gardens, hotel-style concierge services, and private heated indoor pool facilities.",
        "highlights": [
            "Prestigious South Delhi address with rapid connection to Greater Kailash and Nehru Place.",
            "Advanced air purification technology delivering clean alpine-quality air.",
            "Stunning architectural facade with copper stone cladding and floor-to-ceiling glazing.",
            "Exclusive low-density gated compound with resort-level club amenities."
        ],
        "specifications": [
            "Structure: Tallest residential towers in South Delhi with shear-wall construction.",
            "Interiors: Italian marble flooring, VRV air conditioning, and bespoke joinery.",
            "Kitchen: Imported German modular kitchen with built-in appliances.",
            "Balconies: Deep landscaped balconies offering panoramic city skyline views."
        ],
        "amenities": [
            "Heated indoor swimming pool", "Boutique spa & wellness salon", "Private cinema lounge",
            "State-of-the-art fitness centre", "Banquet salon & private dining room", "Tennis & squash courts",
            "5-tier biometric access security", "Concierge and valet parking services"
        ],
        "locationAdvantages": [
            "5 minutes from Greater Kailash (GK-1 & GK-2)",
            "8 minutes from Nehru Place business district",
            "Direct signal-free connectivity to Faridabad and Noida",
            "25 minutes from Indira Gandhi International Airport"
        ],
        "paymentPlan": "25:25:25:25 construction linked milestone plan.",
        "isDemo2": False,
        "isTopProject": True,
        "isFeatured": True
    },
    {
        "id": "garur-golf-island",
        "slug": "project-garur-golf-island",
        "name": "Garur Golf Island",
        "developer": "Garur Group",
        "city": "Delhi",
        "state": "Delhi",
        "locality": "Sector 19B, Dwarka",
        "address": "Sector 19B, Dwarka, South West Delhi, Delhi – 110075",
        "propertyType": "Ultra-Luxury Golf Facing Residences",
        "category": "residential",
        "status": "Under Construction",
        "startingPrice": "₹7.5 Cr*",
        "maximumPrice": "₹14 Cr*",
        "priceDisplay": "₹7.5 Cr – ₹14 Cr*",
        "priceNote": "Expansive 4 BHK golf-front homes with private elevators and panoramic fairway vistas.",
        "bhkConfig": "4 BHK Golf Residences + Servant Room",
        "bhkOptions": ["4 BHK"],
        "carpetArea": "2,600 – 3,950 sq. ft.",
        "superArea": "3,500 – 5,200 sq. ft.",
        "possessionDate": "December 2026",
        "reraNumber": "DLRERA2023P0012",
        "image": "images/pro2-516x360.jpg",
        "gallery": ["images/pro2-516x360.jpg", "images/p15-516x360.jpg", "images/pro3-516x360.jpg"],
        "overview": "Directly overlooking the international 18-hole DDA Golf Course in Sector 19B Dwarka, Golf Island represents the pinnacle of golf-resort living in the National Capital.",
        "description": "Featuring ultra-spacious 4 BHK residences with private entrance foyers, smart home automation, expansive panoramic decks, and exclusive access to a world-class clubhouse.",
        "highlights": [
            "Uninterrupted views of the 18-hole championship Dwarka Golf Course.",
            "Private lift access opening directly into each palatial residence.",
            "Smart home automation with app-controlled lighting, climate, and security.",
            "Located in Delhi's fastest appreciating micro-market near Yashobhoomi (IICC)."
        ],
        "specifications": [
            "Living Spaces: 11 ft clear floor-to-ceiling heights with triple glazed acoustic windows.",
            "Bathrooms: Premium Kohler / Toto fixtures with glass cubicles and jacuzzi in master suite.",
            "Security: Smart card access, video door phones, and 24/7 round-the-clock guards."
        ],
        "amenities": [
            "Golf putting green & golf simulator", "Infinity-edge sky pool", "Grand banquet & ballroom",
            "Squash & badminton courts", "Spa, steam & sauna rooms", "Kids play zone & creche",
            "Multi-level basement parking with EV points", "24/7 security with CCTV monitoring"
        ],
        "locationAdvantages": [
            "Overlooking Sector 19B 18-Hole DDA Golf Course",
            "5 minutes from Yashobhoomi (IICC) & Delhi Metro",
            "10 minutes from Indira Gandhi International Airport (Terminal 3)",
            "Direct access to Dwarka Expressway & Urban Extension Road (UER II)"
        ],
        "paymentPlan": "Customized 30:40:30 plan with construction progress benchmarks.",
        "isDemo2": False,
        "isTopProject": True,
        "isFeatured": True
    },
    {
        "id": "tarc-tripundra",
        "slug": "project-tarc-tripundra",
        "name": "Tarc Tripundra",
        "developer": "TARC",
        "city": "Delhi",
        "state": "Delhi",
        "locality": "Bijwasan Road, Pushpanjali",
        "address": "Main Bijwasan Road, Near Pushpanjali Greens, New Delhi – 110061",
        "propertyType": "Boutique Luxury Residences",
        "category": "residential",
        "status": "Under Construction",
        "startingPrice": "₹4.2 Cr*",
        "maximumPrice": "₹8.5 Cr*",
        "priceDisplay": "₹4.2 Cr – ₹8.5 Cr*",
        "priceNote": "3 and 4 BHK boutique residences immersed in natural farm greenery.",
        "bhkConfig": "3 & 4 BHK Luxury Suites",
        "bhkOptions": ["3 BHK", "4 BHK"],
        "carpetArea": "1,650 – 2,400 sq. ft.",
        "superArea": "2,200 – 3,150 sq. ft.",
        "possessionDate": "November 2026",
        "reraNumber": "DLRERA2022P0007",
        "image": "images/pro3-516x360.jpg",
        "gallery": ["images/pro3-516x360.jpg", "images/p16-516x360.jpg", "images/pro4-516x360.jpg"],
        "overview": "Set amidst 3 acres of tranquil greenery on Bijwasan Road near Pushpanjali Farms, TARC Tripundra brings private boutique living to New Delhi with exceptional attention to craftsmanship.",
        "description": "Carefully planned with 7-tier air filtration, indoor heated saltwater pools, starlit terrace lounges, and bespoke organic finishes.",
        "highlights": [
            "Boutique low-density living in South West Delhi's prime farm belt.",
            "Indoor temperature-controlled saltwater pool for year-round recreation.",
            "Hospitality-driven concierge, housekeeping, and private chef services.",
            "Minutes from Aerocity and IGI Airport."
        ],
        "specifications": [
            "Air Quality: 7-tier mechanical and electrostatic air filtration.",
            "Flooring: Imported polished marble and engineered hardwood.",
            "Windows: German acoustic sound-insulating double glazed fenestration."
        ],
        "amenities": [
            "Saltwater indoor heated swimming pool", "Rooftop starlit leisure lounge", "Private mini-theatre",
            "Fitness studio & yoga pavilion", "Sensory herb gardens", "Kids play enclave",
            "Multi-tier security & valet service", "100% power backup"
        ],
        "locationAdvantages": [
            "5 minutes from Aerocity Worldmark dining and retail hub",
            "10 minutes from IGI Airport T3",
            "Seamless access to Vasant Kunj and Gurgaon Cyber City",
            "Surrounded by elite farmhouse developments"
        ],
        "paymentPlan": "Flexible 20% on booking, 70% in milestones, 10% on possession.",
        "isDemo2": False,
        "isTopProject": True,
        "isFeatured": True
    },
    {
        "id": "godrej-connaught-one",
        "slug": "project-godrej-connaught-one",
        "name": "Godrej Connaught One",
        "developer": "Godrej Properties",
        "city": "Delhi",
        "state": "Delhi",
        "locality": "Connaught Place / Central Delhi",
        "address": "Shaheed Bhagat Singh Marg, Near Connaught Place, Central Delhi, Delhi – 110001",
        "propertyType": "Heritage Elite Luxury Residences",
        "category": "residential",
        "status": "Under Construction",
        "startingPrice": "₹18 Cr*",
        "maximumPrice": "₹32 Cr*",
        "priceDisplay": "₹18 Cr – ₹32 Cr*",
        "priceNote": "Ultra-exclusive Central Delhi residences in a once-in-a-lifetime heritage address.",
        "bhkConfig": "3 & 4 BHK Palatial Residences",
        "bhkOptions": ["3 BHK", "4 BHK"],
        "carpetArea": "1,900 – 3,450 sq. ft.",
        "superArea": "2,500 – 4,500 sq. ft.",
        "possessionDate": "December 2027",
        "reraNumber": "DLRERA2022P0001",
        "image": "images/pro4-516x360.jpg",
        "gallery": ["images/pro4-516x360.jpg", "images/p17-516x360.jpg", "images/pro5-516x360.jpg"],
        "overview": "Godrej Connaught One is Delhi's most prestigious urban residential address, situated on Shaheed Bhagat Singh Marg just steps from Connaught Place in Lutyens' vicinity.",
        "description": "Crafted for royalty, diplomats, and industrialists, this iconic development offers private butler service, temperature-controlled indoor pools, and unmatched status in Central Delhi.",
        "highlights": [
            "Rare opportunity to own freehold luxury residences in Central Delhi.",
            "Moments away from Connaught Place, Shivaji Stadium, and India Gate.",
            "Unrivalled 7-star personalized concierge and private butler services.",
            "Contemporary architectural marvel meeting heritage aesthetic elegance."
        ],
        "specifications": [
            "Structure: Special Grade-A high-density core engineering.",
            "Finishes: Master suites finished in rare book-matched Italian marble.",
            "Smart Living: Fully automated IoT lighting, shading, and climate control."
        ],
        "amenities": [
            "Private butler & 7-star concierge desk", "Temperature-controlled swimming pool",
            "Executive business salon & boardroom", "State-of-the-art wellness club & gym", "Fine-dining private chef kitchen",
            "Multi-level secure basement with chauffeur lounge", "Biometric multi-tier security", "24/7 dedicated facility team"
        ],
        "locationAdvantages": [
            "2 minutes from Connaught Place Central Circle",
            "3 minutes from Shivaji Stadium Metro Station (Airport Express)",
            "10 minutes from Rashtrapati Bhavan & India Gate",
            "Surrounded by top cultural hubs, five-star hotels, and embassies"
        ],
        "paymentPlan": "Special bespoke milestone plan tailored for ultra-high-net-worth investors.",
        "isDemo2": False,
        "isTopProject": True,
        "isFeatured": True
    },
    {
        "id": "sawasdee-lodhi-greens",
        "slug": "project-sawasdee-lodhi-greens",
        "name": "Sawasdee Lodhi Greens",
        "developer": "Sawasdee Group",
        "city": "Delhi",
        "state": "Delhi",
        "locality": "Lodhi Colony, Central Delhi",
        "address": "Near Lodhi Colony, Central Delhi, Delhi – 110003",
        "propertyType": "Prime Central Delhi Boutique Homes",
        "category": "residential",
        "status": "Ready to Move",
        "startingPrice": "₹3.5 Cr*",
        "maximumPrice": "₹6.8 Cr*",
        "priceDisplay": "₹3.5 Cr – ₹6.8 Cr*",
        "priceNote": "Ready to move in luxury apartments adjacent to Khan Market and Lodhi Gardens.",
        "bhkConfig": "2 & 3 BHK Luxury Apartments",
        "bhkOptions": ["2 BHK", "3 BHK"],
        "carpetArea": "950 – 1,600 sq. ft.",
        "superArea": "1,250 – 2,100 sq. ft.",
        "possessionDate": "Ready to Move",
        "reraNumber": "DLRERA2020P0009",
        "image": "images/pro5-516x360.jpg",
        "gallery": ["images/pro5-516x360.jpg", "images/p18-516x360.jpg", "images/d1.jpg"],
        "overview": "Sawasdee Lodhi Greens offers an exclusive boutique residential experience right in the heritage greenery of Central Delhi, close to Lodhi Gardens and Khan Market.",
        "description": "Ready-to-move-in luxury homes designed for high-ranking professionals and connoisseurs of refined urban living, complete with manicured gardens and quiet residential surrounds.",
        "highlights": [
            "Direct proximity to Lodhi Art District, Khan Market, and India Habitat Centre.",
            "Ready-to-move-in boutique luxury apartments with immediate registration.",
            "Private underground parking and green terrace lounges.",
            "Surrounded by mature neem and amaltas trees in Delhi's greenest zone."
        ],
        "specifications": [
            "Finishes: Premium hardwood timber flooring in bedrooms; vitrified tiles in utility.",
            "Fixtures: Premium Grohe bath fittings and imported sanitaryware.",
            "Power: 100% generator power backup for uninterrupted comfort."
        ],
        "amenities": [
            "Landscaped rooftop terrace", "Resident lounge & reading library", "Secure underground parking",
            "Fitness studio with modern cardio equipment", "CCTV surveillance & intercom", "Power backup 100%"
        ],
        "locationAdvantages": [
            "5 minutes from Lodhi Gardens and India Habitat Centre",
            "7 minutes from Khan Market & Golf Links",
            "Quick access to Ring Road, Barapullah Flyover & Mathura Road",
            "Walking distance from JLN Stadium Metro Station"
        ],
        "paymentPlan": "Ready-to-move instant payment plan with bank home loan approvals.",
        "isDemo2": False,
        "isTopProject": True,
        "isFeatured": True
    },
    {
        "id": "risland-sky-mansion",
        "slug": "project-risland-sky-mansion",
        "name": "Risland Sky Mansion",
        "developer": "Risland India",
        "city": "Delhi",
        "state": "Delhi",
        "locality": "Chattarpur, South Delhi",
        "address": "Chattarpur Farms, South Delhi, Delhi – 110074",
        "propertyType": "Ultra-Luxury Penthouse & Mansions",
        "category": "residential",
        "status": "Ready to Move",
        "startingPrice": "₹6.9 Cr*",
        "maximumPrice": "₹25 Cr*",
        "priceDisplay": "₹6.9 Cr – ₹25 Cr*",
        "priceNote": "Delhi's tallest landmark 100-meter luxury towers overlooking Asola Wildlife Sanctuary.",
        "bhkConfig": "3, 4 BHK & Sky Penthouses",
        "bhkOptions": ["3 BHK", "4 BHK", "Penthouse"],
        "carpetArea": "2,450 – 8,500 sq. ft.",
        "superArea": "3,300 – 11,000 sq. ft.",
        "possessionDate": "Ready to Move",
        "reraNumber": "DLRERA2018P0014",
        "image": "images/risland-sky-mansion.jpg",
        "gallery": ["images/risland-sky-mansion.jpg", "images/d2.jpg", "images/d3.jpg"],
        "overview": "Soaring 100 meters above the prestigious farmhouse belt of Chattarpur, Risland Sky Mansion is Delhi's premier skyscraper development offering uninterrupted 360-degree sanctuary views.",
        "description": "With just 2 mansions per core and private elevators, Sky Mansion offers palatial ceiling heights, a 33,000 sq. ft. club, Olympic-standard lap pool, and lush curated forest landscapes.",
        "highlights": [
            "Delhi's tallest residential building standing 100 meters high.",
            "Panoramic views over 20,000 acres of Asola Wildlife Sanctuary greenery.",
            "Lavish 33,000 sq. ft. five-star clubhouse with international leisure.",
            "Ready-to-move luxury apartments with immediate deed execution."
        ],
        "specifications": [
            "Ceiling Heights: 11.8 ft palatial clear ceiling heights.",
            "Elevators: Dedicated high-speed private elevator foyer per apartment.",
            "Security: 5-level intelligent security system with infrared boundary detection."
        ],
        "amenities": [
            "33,000 sq. ft. mega clubhouse", "Olympic-size lap swimming pool", "Tennis court & squash court",
            "2 km winding forest jogging path", "Private rooftop helipad access", "Kids fantasy wonderland playground",
            "Chauffeur lounge & multi-level basement", "Round-the-clock concierge"
        ],
        "locationAdvantages": [
            "Nestled in the elite Chattarpur and Asola farmhouse enclave",
            "10 minutes from Qutub Minar and Mehrauli Heritage Park",
            "15 minutes from Vasant Kunj luxury malls (DLF Emporio, Promenade)",
            "Direct link to MG Road connecting Delhi and Gurugram"
        ],
        "paymentPlan": "Ready to move in: 10% booking, 90% upon registry and possession.",
        "isDemo2": False,
        "isTopProject": True,
        "isFeatured": True
    },

    # --- PROPERTYPISTOL TOP PROJECTS: NOIDA & GREATER NOIDA ---
    {
        "id": "ats-le-grandiose",
        "slug": "project-ats-le-grandiose",
        "name": "ATS Le Grandiose",
        "developer": "ATS Infrastructure",
        "city": "Noida",
        "state": "Uttar Pradesh",
        "locality": "Sector 150",
        "address": "Sector 150, Noida-Greater Noida Expressway, Noida, UP – 201310",
        "propertyType": "Eco-Luxury Spanish Residences",
        "category": "residential",
        "status": "Ready to Move / Resale",
        "startingPrice": "₹1.6 Cr*",
        "maximumPrice": "₹3.8 Cr*",
        "priceDisplay": "₹1.6 Cr – ₹3.8 Cr*",
        "priceNote": "Spanish-inspired luxury apartments in NCR's greenest low-density sector.",
        "bhkConfig": "3 & 4 BHK Luxury Apartments",
        "bhkOptions": ["3 BHK", "4 BHK"],
        "carpetArea": "1,180 – 2,350 sq. ft.",
        "superArea": "1,625 – 3,200 sq. ft.",
        "possessionDate": "Ready to Move",
        "reraNumber": "UPRERAPRJ3254",
        "image": "images/d3.jpg",
        "gallery": ["images/d3.jpg", "images/d4.jpg", "images/v1.jpg"],
        "overview": "Located in Sector 150, Noida's greenest and first overhead wire-free sector, ATS Le Grandiose showcases classical Spanish arches, clay-tiled roofs, and low-density open spaces.",
        "description": "Boasting an expansive central green courtyard, Olympic athletic facilities, and direct expressway connectivity, it is one of Noida's most desirable residential societies.",
        "highlights": [
            "Situated in 80% green Sector 150, close to Shaheed Bhagat Singh Sports City.",
            "Distinctive Spanish colonial architecture with red tile roofs and terracotta finishes.",
            "Low-density living with only 2 apartments per floor in select towers.",
            "Immediate connectivity to Noida-Greater Noida Expressway and Yamuna Expressway."
        ],
        "specifications": [
            "Structure: Earthquake-resistant RCC frame meeting Zone-IV seismic codes.",
            "Flooring: Wooden flooring in master suite; premium imported vitrified tiles in living.",
            "Fittings: Concealed plumbing with Jaquar / Kohler CP fittings."
        ],
        "amenities": [
            "Spanish architecture clubhouse", "Squash & badminton courts", "Swimming pool with toddler splash",
            "Cricket pitch & basketball court", "Open-air amphitheatre", "Fully equipped gym & yoga room",
            "24/7 security with perimeter sensor beams", "Power backup 100%"
        ],
        "locationAdvantages": [
            "Right off the Noida-Greater Noida Expressway in Sector 150",
            "10 minutes from Pari Chowk & upcoming Jewar Airport route",
            "Near upcoming Sector 148 Aqua Line Metro Station",
            "Surrounded by international golf courses and sports facilities"
        ],
        "paymentPlan": "Ready-to-move resale and builder transfer plans available.",
        "isDemo2": False,
        "isTopProject": True,
        "isFeatured": True
    },
    {
        "id": "eldeco-ballads-of-bliss",
        "slug": "project-eldeco-ballads-of-bliss",
        "name": "Eldeco Ballads of Bliss",
        "developer": "Eldeco Group",
        "city": "Noida",
        "state": "Uttar Pradesh",
        "locality": "Sector 12, Greater Noida West",
        "address": "Sector 12, Greater Noida West (Noida Extension), Uttar Pradesh – 201306",
        "propertyType": "Premium High-Rise Residences",
        "category": "residential",
        "status": "Under Construction",
        "startingPrice": "₹1.1 Cr*",
        "maximumPrice": "₹2.2 Cr*",
        "priceDisplay": "₹1.1 Cr – ₹2.2 Cr*",
        "priceNote": "Modern 2 and 3 BHK homes with music-themed landscapes and open parks.",
        "bhkConfig": "2 & 3 BHK Contemporary Homes",
        "bhkOptions": ["2 BHK", "3 BHK"],
        "carpetArea": "850 – 1,420 sq. ft.",
        "superArea": "1,150 – 1,850 sq. ft.",
        "possessionDate": "July 2027",
        "reraNumber": "UPRERAPRJ954128",
        "image": "images/eldeco-ballads-of-bliss.jpg",
        "gallery": ["images/eldeco-ballads-of-bliss.jpg", "images/v2.jpg", "images/v3.jpg"],
        "overview": "Eldeco Ballads of Bliss is an inspired residential enclave in Sector 12, Greater Noida West. Designed with harmonious music-themed gardens, expansive balconies, and seamless metro access.",
        "description": "Constructed with Eldeco's 40-year legacy of engineering excellence, this gated society features vaastu-compliant homes, dedicated sports arenas, and family recreational spaces.",
        "highlights": [
            "Strategic Sector 12 Greater Noida West location with planned metro station outside.",
            "75% open landscaped greenery with musical themed garden pavilions.",
            "Vaastu-compliant corner apartments with 3-sided ventilation.",
            "Eldeco's trusted brand delivery and high construction standards."
        ],
        "specifications": [
            "Structure: Monolithic aluminum formwork (Mivan) construction.",
            "Lobbies: Air-conditioned double-height ground entrance lobbies.",
            "Windows: Powder-coated aluminum sliding windows with mosquito mesh."
        ],
        "amenities": [
            "Grand leisure clubhouse", "Rooftop leisure pavilion & observatory", "Swimming pool & sun loungers",
            "Badminton & squash indoor courts", "Kids musical play park", "Yoga & meditation lawn",
            "Multi-tier security with mobile access", "100% power backup"
        ],
        "locationAdvantages": [
            "Adjacent to the upcoming Greater Noida West Metro corridor",
            "10 minutes from Gaur City Mall and Crossing Republik",
            "15 minutes from Sector 52/71 Noida metro junction",
            "Quick access to NH-24 / Delhi-Meerut Expressway"
        ],
        "paymentPlan": "Standard 10% booking, 40% in milestones, 50% on completion.",
        "isDemo2": False,
        "isTopProject": True,
        "isFeatured": True
    },
    {
        "id": "express-astra",
        "slug": "project-express-astra",
        "name": "Express Astra",
        "developer": "Express Builders",
        "city": "Noida",
        "state": "Uttar Pradesh",
        "locality": "Sector 1, Greater Noida West",
        "address": "Plot No GH-05B, Sector 1, Greater Noida West, UP – 201306",
        "propertyType": "Eco-Friendly Modern Residences",
        "category": "residential",
        "status": "Under Construction",
        "startingPrice": "₹85 Lakh*",
        "maximumPrice": "₹1.75 Cr*",
        "priceDisplay": "₹85 Lakh – ₹1.75 Cr*",
        "priceNote": "Vaastu-compliant residences with 75% green open spaces in prime Sector 1.",
        "bhkConfig": "2, 3 & 4 BHK Eco-Homes",
        "bhkOptions": ["2 BHK", "3 BHK", "4 BHK"],
        "carpetArea": "820 – 1,550 sq. ft.",
        "superArea": "1,150 – 2,005 sq. ft.",
        "possessionDate": "March 2026",
        "reraNumber": "UPRERAPRJ4796",
        "image": "images/v3.jpg",
        "gallery": ["images/v3.jpg", "images/v4.jpg", "images/h41.jpg"],
        "overview": "Express Astra in Sector 1 Greater Noida West offers 3-side open residences surrounded by lush zen gardens and panoramic views of Hindon green belt.",
        "description": "Engineered for sustainable urban families, Express Astra incorporates rainwater recharging, solar-assisted common illumination, and ultra-spacious layouts.",
        "highlights": [
            "Sector 1 Greater Noida West — closest sector to Central Noida.",
            "3-side open apartments maximizing natural breeze and sunlight.",
            "Zero vehicular movement on the podium level for child safety.",
            "Over 75% open landscaped space with zen gazebos."
        ],
        "specifications": [
            "Structure: Earthquake-resistant RCC frame structure.",
            "Kitchen: Granite counter-top with stainless steel sink and ceramic tiles.",
            "Flooring: Vitrified tiles in drawing/dining and wooden finish in bedrooms."
        ],
        "amenities": [
            "Zen meditation gardens", "Swimming pool with kids splash pool", "Well-equipped health gym",
            "Indoor games room with table tennis & billiards", "Jogging & roller skating track",
            "Children's play apparatus", "24/7 security with digital surveillance", "Full power backup"
        ],
        "locationAdvantages": [
            "Closest Greater Noida West sector to Central Noida (Sector 78/79 bridge)",
            "5 minutes from FNG Expressway entry point",
            "10 minutes from Noida City Centre metro station",
            "Reputed schools and multi-speciality hospitals within 2 km"
        ],
        "paymentPlan": "20% down payment, 70% construction-linked installments, 10% on possession.",
        "isDemo2": False,
        "isTopProject": True,
        "isFeatured": True
    },
    {
        "id": "ace-starlit",
        "slug": "project-ace-starlit",
        "name": "ACE Starlit",
        "developer": "ACE Group",
        "city": "Noida",
        "state": "Uttar Pradesh",
        "locality": "Sector 152",
        "address": "Plot No SC-01/01, Sector 152, Noida Expressway, Noida – 201310",
        "propertyType": "Signature Expressway High-Rise",
        "category": "residential",
        "status": "Under Construction",
        "startingPrice": "₹1.45 Cr*",
        "maximumPrice": "₹3.1 Cr*",
        "priceDisplay": "₹1.45 Cr – ₹3.1 Cr*",
        "priceNote": "Iconic glass-facade towers on Noida Expressway with panoramic views.",
        "bhkConfig": "2 & 3 BHK Luxury Residences",
        "bhkOptions": ["2 BHK", "3 BHK"],
        "carpetArea": "980 – 1,320 sq. ft.",
        "superArea": "1,350 – 1,775 sq. ft.",
        "possessionDate": "June 2027",
        "reraNumber": "UPRERAPRJ677297",
        "image": "images/ace-starlit-updated-cover.webp",
        "gallery": ["images/ace-starlit-updated-cover.webp", "images/h42.jpg", "images/h44.jpg"],
        "overview": "ACE Starlit is an iconic architectural masterpiece located on the Noida Expressway in Sector 152. Known for its signature glass facade, grand arrival court, and luxury club.",
        "description": "Combining contemporary aesthetics with thoughtful privacy, ACE Starlit offers corner-facing apartments with deep balconies overlooking expressway greens and golf courses.",
        "highlights": [
            "Corner plot location on Noida Expressway with 45-meter wide access roads.",
            "Contemporary reflective glass facade with double-height entrance lobbies.",
            "Exclusive clubhouse with all-weather indoor temperature-controlled pool.",
            "Close proximity to upcoming international cricket stadium in Sector 152."
        ],
        "specifications": [
            "Facade: High-performance double-glazed solar reflective glass panels.",
            "Finishes: Premium marble flooring in foyer and drawing areas.",
            "Air Conditioning: Pre-installed energy-efficient inverter ACs."
        ],
        "amenities": [
            "Grand signature clubhouse", "All-weather indoor temperature regulated pool", "Outdoor leisure pool & sun deck",
            "Tennis & basketball courts", "Banquet hall & party lawn", "Fitness centre with spinning studio",
            "Multi-tier 24/7 security with ANPR car entry", "100% power backup"
        ],
        "locationAdvantages": [
            "Prime frontage on Noida-Greater Noida Expressway",
            "2 minutes from Sector 148 Aqua Line Metro Station",
            "Direct route to Noida International Airport at Jewar",
            "Opposite upcoming international cricket stadium & commercial sector"
        ],
        "paymentPlan": "30:40:30 linked payment schedule.",
        "isDemo2": False,
        "isTopProject": True,
        "isFeatured": True
    },
    {
        "id": "crc-maesta",
        "slug": "project-crc-maesta",
        "name": "CRC Maesta",
        "developer": "CRC Group",
        "city": "Noida",
        "state": "Uttar Pradesh",
        "locality": "Sector 1, Greater Noida West",
        "address": "Plot No GH-02C, Sector 1, Greater Noida West, UP – 201306",
        "propertyType": "Ultra-Modern High-Rise Living",
        "category": "residential",
        "status": "Under Construction",
        "startingPrice": "₹1.25 Cr*",
        "maximumPrice": "₹2.6 Cr*",
        "priceDisplay": "₹1.25 Cr – ₹2.6 Cr*",
        "priceNote": "Ultra-spacious balconies and imported marble finishes in prime Sector 1.",
        "bhkConfig": "3 & 4 BHK Luxury Residences",
        "bhkOptions": ["3 BHK", "4 BHK"],
        "carpetArea": "1,220 – 1,950 sq. ft.",
        "superArea": "1,720 – 2,690 sq. ft.",
        "possessionDate": "September 2027",
        "reraNumber": "UPRERAPRJ719468",
        "image": "images/crc-maesta-updated-cover.webp",
        "gallery": ["images/crc-maesta-updated-cover.webp", "images/h45.jpg", "images/h48.jpg"],
        "overview": "CRC Maesta is a modern luxury high-rise development in Sector 1 Greater Noida West, offering thoughtfully planned 3 and 4 BHK residences with deep running balconies.",
        "description": "Designed by renowned Hafeez Contractor, CRC Maesta features a sky club, panoramic observation decks, sports academies, and high-efficiency floor plates.",
        "highlights": [
            "Architect Hafeez Contractor design with continuous curvilinear balconies.",
            "Dedicated Sky Lounge at high altitude offering 360-degree skyline views.",
            "Low-density four apartments per core configuration with 3 high-speed lifts.",
            "Minutes from Central Noida via the operational Hindon bridge."
        ],
        "specifications": [
            "Balconies: 6 ft wide continuous running balconies with toughened glass railings.",
            "Elevators: 3 high-speed OTIS / Schindler elevators per tower.",
            "Plumbing: Low-noise CPVC piping and water softening filtration."
        ],
        "amenities": [
            "Sky club & observatory deck", "Heated indoor pool & outdoor leisure pool", "Steam, sauna & wellness spa",
            "Indoor squash & badminton arena", "Banquet ballroom with pre-function foyer", "Dedicated visitor car parking",
            "5-tier security surveillance with guard patrol", "100% DG power backup"
        ],
        "locationAdvantages": [
            "Sector 1 Greater Noida West, immediately adjoining Central Noida",
            "5 minutes from Sector 78 and Sector 101 Noida metro stations",
            "Direct access to FNG Corridor and NH-24",
            "Leading international schools (Lotus Valley, DPS) in immediate vicinity"
        ],
        "paymentPlan": "Construction milestone plan: 10% booking, 40% structure, 50% on finishes.",
        "isDemo2": False,
        "isTopProject": True,
        "isFeatured": True
    },

    # --- PROPERTYPISTOL TOP PROJECTS: PUNE ---
    {
        "id": "godrej-woodsville",
        "slug": "project-godrej-woodsville",
        "name": "Godrej Woodsville",
        "developer": "Godrej Properties",
        "city": "Pune",
        "state": "Maharashtra",
        "locality": "Hinjawadi Phase 1",
        "address": "Maan Road, Hinjawadi Phase 1, Pune, Maharashtra – 411057",
        "propertyType": "Forest-Themed Smart Living",
        "category": "residential",
        "status": "Under Construction",
        "startingPrice": "₹62 Lakh*",
        "maximumPrice": "₹1.35 Cr*",
        "priceDisplay": "₹62 Lakh – ₹1.35 Cr*",
        "priceNote": "Smart 1, 2 and 3 BHK forest-themed homes in Hinjawadi IT corridor.",
        "bhkConfig": "1, 2 & 3 BHK Smart Homes",
        "bhkOptions": ["1 BHK", "2 BHK", "3 BHK"],
        "carpetArea": "471 – 968 sq. ft.",
        "superArea": "650 – 1,320 sq. ft.",
        "possessionDate": "December 2026",
        "reraNumber": "P52100046729",
        "image": "images/p13-516x360.jpg",
        "gallery": ["images/p13-516x360.jpg", "images/pro1-516x360.jpg", "images/p15-516x360.jpg"],
        "overview": "Godrej Woodsville in Hinjawadi Phase 1 brings forest-inspired living to Pune's premier IT hub. Featuring 400+ mature trees, canopy walkways, and smart home automation.",
        "description": "Designed for tech professionals, Godrej Woodsville integrates co-working lounges with high-speed WiFi, sky decks, and wellness trails within a secure 4-acre community.",
        "highlights": [
            "Prime Hinjawadi Phase 1 location — walk to Rajiv Gandhi Infotech Park.",
            "Over 400 trees with elevated canopy boardwalks and fresh nature air.",
            "Dedicated co-working pods and business meeting rooms on-site.",
            "Smart home features with voice-controlled switches and digital door locks."
        ],
        "specifications": [
            "Automation: Smart lighting, geyser, and AC control via smartphone app.",
            "Flooring: Vitrified tiles in all rooms; anti-skid ceramic tiles in bathrooms.",
            "Safety: Video door phone, smoke detector, and gas leak sensor in kitchen."
        ],
        "amenities": [
            "400+ tree forest plantation & skywalk", "Sky lounge with star observatory", "Swimming pool & pool-side cabanas",
            "Co-working business pods with high-speed WiFi", "Fitness gym & aerobics studio", "Children's adventure playground",
            "Multi-tier 24/7 security with smart boom barriers", "100% power backup for common zones"
        ],
        "locationAdvantages": [
            "Located in Hinjawadi Phase 1 near Wipro, Infosys, and Cognizant campuses",
            "3 minutes from upcoming Pune Metro Line 3 (Maan Station)",
            "10 minutes from Mumbai-Pune Expressway exit",
            "Top international schools and healthcare centres within 3 km"
        ],
        "paymentPlan": "Special 10:90 subvention and flexi milestone plans.",
        "isDemo2": False,
        "isTopProject": True,
        "isFeatured": True
    },
    {
        "id": "kohinoor-presidentia",
        "slug": "project-kohinoor-presidentia",
        "name": "Kohinoor Presidentia",
        "developer": "Kohinoor Group",
        "city": "Pune",
        "state": "Maharashtra",
        "locality": "Kharadi",
        "address": "New Kharadi, Near EON IT Park, Pune, Maharashtra – 411014",
        "propertyType": "Sophisticated Urban High-Rise",
        "category": "residential",
        "status": "Under Construction",
        "startingPrice": "₹82 Lakh*",
        "maximumPrice": "₹1.7 Cr*",
        "priceDisplay": "₹82 Lakh – ₹1.7 Cr*",
        "priceNote": "2 and 3 BHK premium apartments in Pune's eastern IT epicentre.",
        "bhkConfig": "2 & 3 BHK High-Rise Apartments",
        "bhkOptions": ["2 BHK", "3 BHK"],
        "carpetArea": "725 – 1,120 sq. ft.",
        "superArea": "980 – 1,510 sq. ft.",
        "possessionDate": "March 2026",
        "reraNumber": "P52100030509",
        "image": "images/p15-516x360.jpg",
        "gallery": ["images/p15-516x360.jpg", "images/pro2-516x360.jpg", "images/p16-516x360.jpg"],
        "overview": "Kohinoor Presidentia is a premier residential landmark in Kharadi, Pune, offering luxury high-rise apartments equipped with over 30 modern lifestyle amenities.",
        "description": "Situated minutes away from EON Free Zone and World Trade Center Pune, Kohinoor Presidentia offers infinity pools, rooftop barbecue terraces, and spacious family layouts.",
        "highlights": [
            "Located in Kharadi — Pune's premier eastern IT and residential growth corridor.",
            "Over 30 world-class amenities across ground and rooftop leisure decks.",
            "Grand 25,000 sq. ft. multi-tier clubhouse with sports courts.",
            "Minutes from World Trade Center, EON IT Park, and Zensar Technologies."
        ],
        "specifications": [
            "Structure: Aluminum formwork shear wall earthquake-resistant construction.",
            "Doors: Laminated designer flush doors with digital mortise locks.",
            "Kitchen: Granite platform with stainless steel sink and water purifier point."
        ],
        "amenities": [
            "Infinity-edge swimming pool", "25,000 sq. ft. luxury clubhouse", "Rooftop barbecue & star gazing terrace",
            "Aerobics & Zumba studio", "Indoor badminton & squash courts", "Children's themed play area",
            "24/7 security with CCTV monitoring", "Full generator power backup"
        ],
        "locationAdvantages": [
            "5 minutes from World Trade Center (WTC) & EON IT Park",
            "10 minutes from Viman Nagar and Phoenix Marketcity",
            "15 minutes from Pune International Airport (Lohegaon)",
            "Direct connectivity to Nagar Road and Solapur Highway"
        ],
        "paymentPlan": "Flexible construction-linked payment schedule with bank pre-approvals.",
        "isDemo2": False,
        "isTopProject": True,
        "isFeatured": True
    },
    {
        "id": "kolte-patil-life-republic",
        "slug": "project-kolte-patil-life-republic",
        "name": "Kolte Patil Life Republic",
        "developer": "Kolte-Patil Developers",
        "city": "Pune",
        "state": "Maharashtra",
        "locality": "Hinjawadi-Marunji",
        "address": "Survey No. 74, Marunji, Hinjawadi IT Corridor, Pune – 411057",
        "propertyType": "390-Acre Integrated Township",
        "category": "residential",
        "status": "Ready to Move / Ongoing",
        "startingPrice": "₹45 Lakh*",
        "maximumPrice": "₹1.5 Cr*",
        "priceDisplay": "₹45 Lakh – ₹1.5 Cr*",
        "priceNote": "1, 2, 3 BHK homes and duplex villas in Pune's largest operational township.",
        "bhkConfig": "1, 2, 3 BHK & Duplex Villas",
        "bhkOptions": ["1 BHK", "2 BHK", "3 BHK", "Villa"],
        "carpetArea": "450 – 1,450 sq. ft.",
        "superArea": "620 – 1,980 sq. ft.",
        "possessionDate": "Ready to Move / Phased 2026",
        "reraNumber": "P52100027629",
        "image": "images/p16-516x360.jpg",
        "gallery": ["images/p16-516x360.jpg", "images/pro3-516x360.jpg", "images/p17-516x360.jpg"],
        "overview": "Life Republic by Kolte-Patil is a celebrated 390-acre integrated township in Hinjawadi, Pune. Housing thousands of happy families with operational schools, sports complexes, and nature lakes.",
        "description": "With internal 150-ft wide spine roads, functioning international schools, high-street shopping, and multiple clubhouses, Life Republic is a self-sustaining city within a city.",
        "highlights": [
            "Massive 390-acre gated township with operational social infrastructure.",
            "Operational Anisha Global School and multi-speciality medical clinic inside.",
            "Natural lake with botanical walking trails and sports stadiums.",
            "5 operational clubhouses with multiple swimming pools and gymnasiums."
        ],
        "specifications": [
            "Infrastructure: 150 ft wide main access roads and underground storm drainage.",
            "Water Management: In-house water treatment plant and 100% sewage recycling.",
            "Construction: Quality earthquake-resistant RCC structures by Kolte-Patil."
        ],
        "amenities": [
            "5 grand operational clubhouses", "Multiple Olympic-size swimming pools", "Multi-sports academy & football ground",
            "Operational Anisha Global School", "High-street retail & daily convenience marts", "Nature lake & botanical gardens",
            "Township security with patrol vehicles & central command", "100% power backup for essentials"
        ],
        "locationAdvantages": [
            "Direct 5-minute drive to Hinjawadi IT Park Phase 1 & 2",
            "Quick access to Mumbai-Pune Expressway via Wakad/Punawale",
            "Close to upcoming Hinjawadi-Shivajinagar Metro Line",
            "Surrounded by natural hills and clean green atmosphere"
        ],
        "paymentPlan": "Ready to move in and under-construction customized milestone options.",
        "isDemo2": False,
        "isTopProject": True,
        "isFeatured": True
    },
    {
        "id": "vtp-sierra",
        "slug": "project-vtp-sierra",
        "name": "VTP Sierra",
        "developer": "VTP Realty",
        "city": "Pune",
        "state": "Maharashtra",
        "locality": "Baner-Sus",
        "address": "Sus-Pashan Link Road, Near Baner, Pune, Maharashtra – 411021",
        "propertyType": "Maximum Livable Area Residences",
        "category": "residential",
        "status": "Under Construction",
        "startingPrice": "₹74 Lakh*",
        "maximumPrice": "₹1.4 Cr*",
        "priceDisplay": "₹74 Lakh – ₹1.4 Cr*",
        "priceNote": "Zero-wastage MLA apartments nestled against Baner hills.",
        "bhkConfig": "2 & 3 BHK MLA Residences",
        "bhkOptions": ["2 BHK", "3 BHK"],
        "carpetArea": "680 – 1,020 sq. ft.",
        "superArea": "920 – 1,380 sq. ft.",
        "possessionDate": "June 2026",
        "reraNumber": "P52100026772",
        "image": "images/p17-516x360.jpg",
        "gallery": ["images/p17-516x360.jpg", "images/pro4-516x360.jpg", "images/p18-516x360.jpg"],
        "overview": "VTP Sierra in Baner-Sus brings VTP Realty's patented Maximum Livable Area (MLA) design philosophy to West Pune, delivering zero corridor wastage and maximum usable floor space.",
        "description": "Perched with backdrop views of the Baner hills, VTP Sierra features hill-facing infinity pools, a 3-tier clubhouse, and rapid connectivity to Mumbai-Pune Expressway and Balewadi High Street.",
        "highlights": [
            "Maximum Livable Area (MLA) philosophy: larger living rooms and zero wasted space.",
            "Stunning hill backdrop with fresh airflow and unblocked nature horizons.",
            "High-street retail plaza at ground level for day-to-day shopping convenience.",
            "Minutes from Balewadi High Street entertainment hub and Baner IT corridor."
        ],
        "specifications": [
            "Design: Zero dead-space floor planning with large utility balconies.",
            "Fixtures: Premium branded sanitary fittings from American Standard / Grohe.",
            "Structure: Advanced ALU-form shuttering for superior concrete finish."
        ],
        "amenities": [
            "Hill-facing infinity swimming pool", "3-tier recreational clubhouse", "Badminton & squash indoor courts",
            "Acupressure reflexology pathway", "Children's fun pool & adventure play zone", "Yoga & meditation hall",
            "3-tier digital security with boom barriers", "100% power backup for elevators & common areas"
        ],
        "locationAdvantages": [
            "5 minutes from Balewadi High Street dining and shopping",
            "7 minutes from Baner commercial hub and Mumbai-Bengaluru Highway",
            "12 minutes from Hinjawadi IT Park",
            "Surrounded by premier schools (Orchid, VIBGYOR, Symbiosis)"
        ],
        "paymentPlan": "Special 20:80 bank-subsidized scheme or milestone payment plan.",
        "isDemo2": False,
        "isTopProject": True,
        "isFeatured": True
    },
    {
        "id": "shapoorji-joyville-sensorium",
        "slug": "project-shapoorji-joyville-sensorium",
        "name": "Shapoorji Joyville Sensorium",
        "developer": "Shapoorji Pallonji Real Estate",
        "city": "Pune",
        "state": "Maharashtra",
        "locality": "Hinjawadi Phase 1",
        "address": "Near Mula River, Hinjawadi Phase 1, Pune, Maharashtra – 411057",
        "propertyType": "Biophilic Tech-Enabled Living",
        "category": "residential",
        "status": "Under Construction",
        "startingPrice": "₹69 Lakh*",
        "maximumPrice": "₹1.28 Cr*",
        "priceDisplay": "₹69 Lakh – ₹1.28 Cr*",
        "priceNote": "2 and 3 BHK biophilic residences spread across 10.5 acres with 75% green open area.",
        "bhkConfig": "2 & 3 BHK Biophilic Homes",
        "bhkOptions": ["2 BHK", "3 BHK"],
        "carpetArea": "611 – 890 sq. ft.",
        "superArea": "830 – 1,220 sq. ft.",
        "possessionDate": "November 2026",
        "reraNumber": "P52100027244",
        "image": "images/p18-516x360.jpg",
        "gallery": ["images/p18-516x360.jpg", "images/pro5-516x360.jpg", "images/p19-516x360.jpg"],
        "overview": "Shapoorji Pallonji Joyville Sensorium in Hinjawadi Phase 1 is a 10.5-acre biophilic sanctuary with 75% open spaces, 2.8-acre sunken garden, and riverside green promenades.",
        "description": "Imbued with sensory reflexology paths, aroma gardens, infinity swimming pools, and smart app automation, it provides peace and vitality for modern IT families.",
        "highlights": [
            "Backed by the 150-year construction heritage of Shapoorji Pallonji.",
            "Expansive 2.8-acre multi-level sunken garden with riverside view.",
            "Over 75% green open spaces creating a fresh micro-climate.",
            "Walk-to-work convenience for major IT tech companies in Hinjawadi."
        ],
        "specifications": [
            "Biophilic Elements: Vertical green walls, aroma flora, and sensory walkways.",
            "Security: Integrated Smart Visitor Management and perimeter beams.",
            "Water Quality: Centralized water treatment and rainwater percolation pits."
        ],
        "amenities": [
            "2.8-acre multi-level sunken garden", "Riverside walking promenade", "Electric vehicle fast-charging bays",
            "Infinity-edge swimming pool & sundeck", "Fitness pavilion & outdoor gym", "Herb & aroma sensory gardens",
            "Smart intercom & CCTV security", "100% power backup"
        ],
        "locationAdvantages": [
            "Located on Mula River waterfront, Hinjawadi Phase 1",
            "5 minutes from Infosys, TCS, and Tech Mahindra campuses",
            "Direct link to Mumbai-Pune Expressway bypass",
            "Near upcoming Hinjawadi Metro Station"
        ],
        "paymentPlan": "Subvention and construction-linked 10:90 and 20:80 plans.",
        "isDemo2": False,
        "isTopProject": True,
        "isFeatured": True
    },
    {
        "id": "pride-world-city",
        "slug": "project-pride-world-city",
        "name": "Pride World City - Wellington",
        "developer": "Pride Group",
        "city": "Pune",
        "state": "Maharashtra",
        "locality": "Charholi Budruk, Near Dhanori",
        "address": "Pride World City, Charholi Budruk, Near Dhanori, Pune – 412105",
        "propertyType": "400-Acre Mega Township",
        "category": "residential",
        "status": "Under Construction",
        "startingPrice": "₹58 Lakh*",
        "maximumPrice": "₹1.45 Cr*",
        "priceDisplay": "₹58 Lakh – ₹1.45 Cr*",
        "priceNote": "2, 3 and 4 BHK residences within Pune's largest waterfront global township.",
        "bhkConfig": "2, 3 & 4 BHK Township Homes",
        "bhkOptions": ["2 BHK", "3 BHK", "4 BHK"],
        "carpetArea": "690 – 1,520 sq. ft.",
        "superArea": "940 – 2,050 sq. ft.",
        "possessionDate": "December 2026",
        "reraNumber": "P52100019682",
        "image": "images/p19-516x360.jpg",
        "gallery": ["images/p19-516x360.jpg", "images/d1.jpg", "images/d2.jpg"],
        "overview": "Wellington is a premier residential sector within the monumental 400-acre Pride World City mega-township in Charholi, Pune. Featuring waterfront views, grand clubhouses, and central lakes.",
        "description": "Enjoy a self-contained lifestyle with top schools, shopping malls, business parks, and medical hubs all integrated within the secure township perimeter.",
        "highlights": [
            "Part of the world-class 400-acre Pride World City master township.",
            "Waterfront promenades and natural lakes integrated into daily living.",
            "Operational international school and daily convenience stores within walking reach.",
            "Strategic location just 15 minutes from Pune International Airport."
        ],
        "specifications": [
            "Township Infrastructure: 80 ft and 100 ft wide concrete avenues.",
            "Finishes: Anti-skid ceramic tiles in balconies; vitrified tiles in all rooms.",
            "Safety: Fire-fighting sprinkler systems and 24/7 central security monitoring."
        ],
        "amenities": [
            "Club Wellington with swimming pool & spa", "Waterfront jogging promenade & central lake",
            "Open-air amphitheatre for cultural events", "Dedicated cycling & rollerblading tracks",
            "Multi-purpose sports courts", "Children's interactive play gardens",
            "Township central command security", "100% power backup"
        ],
        "locationAdvantages": [
            "Located at Charholi Budruk, directly connected to Ring Road and BRTS",
            "10 minutes from Dhanori and Vishrantwadi",
            "15 minutes from Pune International Airport (Lohegaon)",
            "20 minutes from Kalyani Nagar and Koregaon Park"
        ],
        "paymentPlan": "20% booking, 70% in stage-wise slabs, 10% on possession.",
        "isDemo2": False,
        "isTopProject": True,
        "isFeatured": True
    },

    # --- PROPERTYPISTOL TOP PROJECTS: GURUGRAM ---
    {
        "id": "signature-global-twin-tower",
        "slug": "project-signature-global-twin-tower",
        "name": "Signature Global Twin Tower DXP",
        "developer": "Signature Global",
        "city": "Gurugram",
        "state": "Haryana",
        "locality": "Sector 37D, Dwarka Expressway",
        "address": "Sector 37D, Dwarka Expressway, Gurugram, Haryana – 122001",
        "propertyType": "Ultra-Luxury High-Rise Enclave",
        "category": "residential",
        "status": "New Launch / Under Construction",
        "startingPrice": "₹3.2 Cr*",
        "maximumPrice": "₹5.8 Cr*",
        "priceDisplay": "₹3.2 Cr – ₹5.8 Cr*",
        "priceNote": "Signature Global's flagship ultra-luxury twin towers directly on Dwarka Expressway.",
        "bhkConfig": "3 & 4 BHK Sky Residences",
        "bhkOptions": ["3 BHK", "4 BHK"],
        "carpetArea": "1,550 – 2,550 sq. ft.",
        "superArea": "2,100 – 3,400 sq. ft.",
        "possessionDate": "July 2028",
        "reraNumber": "RC/REP/HARERA/GGM/812/544/2024/39",
        "image": "images/d2.jpg",
        "gallery": ["images/d2.jpg", "images/d3.jpg", "images/d4.jpg"],
        "overview": "Signature Global Twin Tower DXP in Sector 37D Gurugram represents an architectural tour-de-force directly facing the Dwarka Expressway. Featuring sky deck lounges at 100 meters, Olympic pools, and private elevators.",
        "description": "Designed for discerning global citizens, the Twin Towers offer floor-to-ceiling double-glazed glass facades, expansive sundecks, high-speed elevators, and five-star wellness infrastructure.",
        "highlights": [
            "Signature twin towers standing tall directly along Dwarka Expressway corridor.",
            "Exclusive Sky Deck Lounge at 100m height with panoramic skyline horizons.",
            "Private elevator foyers providing absolute exclusivity for each resident.",
            "Olympic-size lap swimming pool and resort-style cabanas."
        ],
        "specifications": [
            "Living Spaces: 11.5 ft clear floor heights with floor-to-ceiling glass fenestration.",
            "Flooring: Imported Italian marble in all entertainment zones; engineered wood in suites.",
            "Climate Control: Central VRV air-conditioning with air-purification filters."
        ],
        "amenities": [
            "100m high Sky Deck Lounge", "Olympic-size lap swimming pool", "Private elevator access per residence",
            "State-of-the-art health club & spa", "Concierge reception & business lounge", "Squash & tennis courts",
            "Multi-tier biometric security", "100% power backup"
        ],
        "locationAdvantages": [
            "Located directly on Dwarka Expressway (NH-248BB)",
            "15 minutes from Delhi Border and Yashobhoomi (IICC)",
            "20 minutes from Indira Gandhi International Airport (T3)",
            "Direct link to Central Peripheral Road (CPR) and NH-48"
        ],
        "paymentPlan": "Special 25:25:25:25 construction linked milestone plan.",
        "isDemo2": False,
        "isTopProject": True,
        "isFeatured": True
    },
    {
        "id": "bptp-the-amaario",
        "slug": "project-bptp-the-amaario",
        "name": "BPTP The Amaario",
        "developer": "BPTP Limited",
        "city": "Gurugram",
        "state": "Haryana",
        "locality": "Sector 37D, Dwarka Expressway",
        "address": "Sector 37D, Off Dwarka Expressway, Gurugram, Haryana – 122001",
        "propertyType": "Club-Centric Opulent Residences",
        "category": "residential",
        "status": "Under Construction",
        "startingPrice": "₹4.5 Cr*",
        "maximumPrice": "₹7.2 Cr*",
        "priceDisplay": "₹4.5 Cr – ₹7.2 Cr*",
        "priceNote": "Ultra-luxury 4 BHK residences with massive 70,000 sq. ft. clubhouse.",
        "bhkConfig": "4 BHK + Servant Room Luxury Residences",
        "bhkOptions": ["4 BHK"],
        "carpetArea": "2,400 – 2,950 sq. ft.",
        "superArea": "3,200 – 3,900 sq. ft.",
        "possessionDate": "October 2028",
        "reraNumber": "RC/REP/HARERA/GGM/816/548/2024/43",
        "image": "images/bptp-the-amaario.jpg",
        "gallery": ["images/bptp-the-amaario.jpg", "images/v1.jpg", "images/v2.jpg"],
        "overview": "BPTP The Amaario in Sector 37D Gurugram offers super-exclusive 4 BHK residences centered around an unprecedented 70,000 sq. ft. club palace, heated indoor pool, and private fine-dining salons.",
        "description": "With just 2 apartments per core, 3 parking slots per home, and 12-ft wide continuous sundecks, The Amaario is engineered for connoisseurs of generous, private residential architecture.",
        "highlights": [
            "Low-density configuration: Only 2 residences per floor with private elevators.",
            "Grand 70,000 sq. ft. luxury clubhouse — one of the largest on Dwarka Expressway.",
            "Heated indoor swimming pool and outdoor resort pool with sunken lounge.",
            "3 dedicated car parking slots with individual EV charging provision."
        ],
        "specifications": [
            "Deck Balconies: 12-ft deep running balconies with zero-obstruction glass railings.",
            "Kitchen: Poggenpohl / equivalent modular kitchen with Miele built-in appliances.",
            "Security: Smart card access, biometric scan, and 24/7 dedicated control room."
        ],
        "amenities": [
            "70,000 sq. ft. palace clubhouse", "Heated indoor swimming pool", "Private cinema screening room",
            "Bowling alley & virtual golf simulator", "Fine dining private banquet hall", "Tennis, squash & badminton courts",
            "Multi-tier 24/7 security with patrol", "100% full DG power backup"
        ],
        "locationAdvantages": [
            "Direct access to Dwarka Expressway via Sector 37D arterial spine",
            "10 minutes from Hero Honda Chowk and Subhash Chowk",
            "20 minutes from Cyber City and Ambience Mall",
            "Surrounded by top healthcare and educational institutions"
        ],
        "paymentPlan": "Convenient 30:40:30 milestone plan.",
        "isDemo2": False,
        "isTopProject": True,
        "isFeatured": True
    },
    {
        "id": "elan-the-presidential",
        "slug": "project-elan-the-presidential",
        "name": "Elan The Presidential",
        "developer": "Elan Group",
        "city": "Gurugram",
        "state": "Haryana",
        "locality": "Sector 106, Dwarka Expressway",
        "address": "Sector 106, Dwarka Expressway, Gurugram, Haryana – 122006",
        "propertyType": "Presidential Luxury Residences",
        "category": "residential",
        "status": "Under Construction",
        "startingPrice": "₹4.1 Cr*",
        "maximumPrice": "₹9.5 Cr*",
        "priceDisplay": "₹4.1 Cr – ₹9.5 Cr*",
        "priceNote": "Presidential suites with golf putting, horse riding track, and triple-height lobbies.",
        "bhkConfig": "3, 4 & 5 BHK Presidential Suites",
        "bhkOptions": ["3 BHK", "4 BHK", "5 BHK"],
        "carpetArea": "1,850 – 3,450 sq. ft.",
        "superArea": "2,450 – 4,500 sq. ft.",
        "possessionDate": "November 2027",
        "reraNumber": "RC/REP/HARERA/GGM/641/373/2022/116",
        "image": "images/v2.jpg",
        "gallery": ["images/v2.jpg", "images/v3.jpg", "images/v4.jpg"],
        "overview": "Elan The Presidential in Sector 106 Gurugram is spread over 30 contiguous acres right on the Dwarka Expressway. It boasts an 8-hole golf putting green, horse riding track, and 3 lavish clubhouses.",
        "description": "Featuring futuristic aerodynamic tower designs, Olympic lap pools, dedicated butler service, and crystal lagoons, it sets a global gold standard in luxury living.",
        "highlights": [
            "Massive 30-acre ultra-luxury development right on the 8-lane Dwarka Expressway.",
            "Exclusive 8-hole golf putting green and horse riding trail inside.",
            "Three grand designer clubhouses catering to wellness, sports, and fine dining.",
            "Triple-height grand entrance arrival lobbies with waterfall cascades."
        ],
        "specifications": [
            "Architecture: Futuristic aerodynamic glass and steel towers designed by international architects.",
            "Balconies: Continuous cantilevered floating sundecks with outdoor jacuzzi points.",
            "HVAC: VRF central air-conditioning with UV-C germicidal air treatment."
        ],
        "amenities": [
            "3 grand designer clubhouses", "Olympic-size swimming pool", "8-hole golf putting green & horse track",
            "Dedicated butler & concierge desk", "Private screening mini-theatre", "Tennis, squash & pickleball courts",
            "5-tier biometric & AI security", "100% power backup"
        ],
        "locationAdvantages": [
            "Zero distance from Dwarka Expressway in Sector 106",
            "10 minutes from Delhi-Gurgaon Border and Yashobhoomi",
            "15 minutes from IGI Airport Terminal 3",
            "Swift connectivity to DLF Cyber Hub via upcoming expressway bypass"
        ],
        "paymentPlan": "25:25:25:25 linked payment schedule.",
        "isDemo2": False,
        "isTopProject": True,
        "isFeatured": True
    },
    {
        "id": "whiteland-the-aspen",
        "slug": "project-whiteland-the-aspen",
        "name": "Whiteland The Aspen",
        "developer": "Whiteland Corporation",
        "city": "Gurugram",
        "state": "Haryana",
        "locality": "Sector 76, SPR",
        "address": "Sector 76, Southern Peripheral Road (SPR), Gurugram, Haryana – 122004",
        "propertyType": "Resort-Style Forest High-Rise",
        "category": "residential",
        "status": "Under Construction",
        "startingPrice": "₹3.3 Cr*",
        "maximumPrice": "₹6.5 Cr*",
        "priceDisplay": "₹3.3 Cr – ₹6.5 Cr*",
        "priceNote": "Overlooking the pristine Aravalli range with 70% open green expanses.",
        "bhkConfig": "3 & 4 BHK Resort Residences",
        "bhkOptions": ["3 BHK", "4 BHK"],
        "carpetArea": "1,720 – 2,750 sq. ft.",
        "superArea": "2,290 – 3,600 sq. ft.",
        "possessionDate": "June 2027",
        "reraNumber": "RC/REP/HARERA/GGM/677/409/2023/21",
        "image": "images/v4.jpg",
        "gallery": ["images/v4.jpg", "images/h41.jpg", "images/h42.jpg"],
        "overview": "Whiteland The Aspen in Sector 76 Gurugram delivers resort-style forest living along the Southern Peripheral Road (SPR), framed by the dramatic ridgeline of the Aravalli hills.",
        "description": "Featuring private plunge pools, organic herbal sanctuaries, temperature-controlled swimming pools, and seamless highway access to NH-48 and Cyber City.",
        "highlights": [
            "Spectacular views of the lush green Aravalli mountain range.",
            "Over 70% open landscape with curated forest groves and bird pavilions.",
            "Corner apartments with private plunge pools in select signature penthouses.",
            "Direct connectivity to NH-48 and Golf Course Extension Road."
        ],
        "specifications": [
            "Decks: Deep sun-shade balconies offering natural mountain air circulation.",
            "Finishes: Polished Italian marble and imported oak-finish laminated flooring.",
            "Green Building: IGBC Platinum standard design with solar thermal heating."
        ],
        "amenities": [
            "Resort clubhouse & temperature controlled pool", "Aravalli viewing sky decks", "Kids water splash fun park",
            "Organic herb & spice gardens", "Indoor squash, badminton & gym", "Multi-tier 5-level security",
            "Electric vehicle charging stations", "100% power backup"
        ],
        "locationAdvantages": [
            "Located on Southern Peripheral Road (SPR) in Sector 76",
            "5 minutes from NH-48 (Delhi-Jaipur Expressway) Cloverleaf",
            "10 minutes from Golf Course Extension Road",
            "Close proximity to leading corporate campuses (TCS, Amdocs, American Express)"
        ],
        "paymentPlan": "Special 30:40:30 flexible installment plan.",
        "isDemo2": False,
        "isTopProject": True,
        "isFeatured": True
    },
    {
        "id": "krisumi-waterfall",
        "slug": "project-krisumi-waterfall",
        "name": "Krisumi Waterfall Residences",
        "developer": "Krisumi Corporation",
        "city": "Gurugram",
        "state": "Haryana",
        "locality": "Sector 36A, CPR",
        "address": "Sector 36A, Off Dwarka Expressway & CPR, Gurugram, Haryana – 122004",
        "propertyType": "Indo-Japanese Craftsmanship Living",
        "category": "residential",
        "status": "Ready to Move / Resale",
        "startingPrice": "₹2.2 Cr*",
        "maximumPrice": "₹4.5 Cr*",
        "priceDisplay": "₹2.2 Cr – ₹4.5 Cr*",
        "priceNote": "Japanese precision engineering by Sumitomo Corporation with onsen spa and Zen gardens.",
        "bhkConfig": "2 & 3 BHK Luxury Suites",
        "bhkOptions": ["2 BHK", "3 BHK"],
        "carpetArea": "1,080 – 1,920 sq. ft.",
        "superArea": "1,448 – 2,538 sq. ft.",
        "possessionDate": "Ready to Move / Resale",
        "reraNumber": "RC/REP/HARERA/GGM/2018/03",
        "image": "images/h42.jpg",
        "gallery": ["images/h42.jpg", "images/h44.jpg", "images/h45.jpg"],
        "overview": "Krisumi Waterfall Residences in Sector 36A is a historic collaboration between Fortune 500 Japanese giant Sumitomo Corporation and Krishna Group. Combining Japanese precision and Zen aesthetics.",
        "description": "Boasting a 36,000 sq. ft. clubhouse, authentic Japanese onsen bath and spa, fine Kaiseki dining, and stepped waterfall gardens, it delivers tranquility and peerless quality.",
        "highlights": [
            "Joint venture between Japan's Fortune 500 Sumitomo Corp and Krishna Group.",
            "Authentic Japanese onsen spa, sauna, and zen meditation pavilions.",
            "Superb Sector 36A location connecting Dwarka Expressway, CPR, and NH-48.",
            "Ready-to-move luxury suites with Japanese minimalist interior fixtures."
        ],
        "specifications": [
            "Engineering: Japanese Nikken Sekkei architectural and seismic design.",
            "Bathrooms: Japanese Toto washlets and smart electronic vanity controls.",
            "Joinery: Engineered acoustic doors with seamless magnetic latches."
        ],
        "amenities": [
            "36,000 sq. ft. Japanese clubhouse", "Traditional Japanese onsen spa & sauna", "Fine Kaiseki & Teppanyaki restaurant",
            "Olympic lap swimming pool", "State-of-the-art TechnoGym fitness centre", "Cascading waterfall zen gardens",
            "24/7 concierge & multilingual desk", "100% full power backup"
        ],
        "locationAdvantages": [
            "Direct junction of Dwarka Expressway, CPR (Central Peripheral Road), and NH-48",
            "10 minutes from Rajiv Chowk Gurugram and Cyber City via NH-48",
            "20 minutes from IGI Airport via Dwarka Expressway",
            "Adjoining upcoming Global City mega hub"
        ],
        "paymentPlan": "Ready-to-move immediate handover and bank loan options.",
        "isDemo2": False,
        "isTopProject": True,
        "isFeatured": True
    },
    {
        "id": "sobha-city",
        "slug": "project-sobha-city",
        "name": "Sobha City",
        "developer": "Sobha Limited",
        "city": "Gurugram",
        "state": "Haryana",
        "locality": "Sector 108, Dwarka Expressway",
        "address": "Sector 108, Dwarka Expressway, Gurugram, Haryana – 122017",
        "propertyType": "39-Acre Urban Park Oasis",
        "category": "residential",
        "status": "Under Construction / Ready to Move",
        "startingPrice": "₹2.4 Cr*",
        "maximumPrice": "₹5.2 Cr*",
        "priceDisplay": "₹2.4 Cr – ₹5.2 Cr*",
        "priceNote": "39 acres of urban park living with two 40,000 sq. ft. clubhouses and a half-acre lakelet.",
        "bhkConfig": "2 & 3 BHK Luxury Residences",
        "bhkOptions": ["2 BHK", "3 BHK"],
        "carpetArea": "1,020 – 1,780 sq. ft.",
        "superArea": "1,381 – 2,343 sq. ft.",
        "possessionDate": "Phased 2026 / Ready to Move",
        "reraNumber": "RC/REP/HARERA/GGM/2016/16",
        "image": "images/h45.jpg",
        "gallery": ["images/h45.jpg", "images/h48.jpg", "images/h41.jpg"],
        "overview": "Sobha City in Sector 108 Gurugram spans 39 contiguous acres right next to the Delhi border on the Dwarka Expressway. It features 8.5 acres of continuous urban park, two 40,000 sq. ft. clubhouses, and a half-acre lakelet.",
        "description": "Constructed with Sobha's industry-reputed in-house backward integration model, Sobha City offers Olympic-size swimming pools, full cricket grounds, and exceptional German-finish build quality.",
        "highlights": [
            "39-acre master development with over 8.5 acres of continuous central urban park.",
            "Half-acre resort-style natural lakelet with white sand beach and deck.",
            "Two massive 40,000 sq. ft. clubhouses (Club Oval and Club Viva).",
            "Full-size 90-meter diameter cricket pitch with professional pavilion."
        ],
        "specifications": [
            "Construction: Sobha backward integration ensuring millimeter-level precision.",
            "Finishes: Sobha-manufactured solid timber doors, double-glazed soundproof windows.",
            "Water: 100% treated potable water system with rainwater recharge."
        ],
        "amenities": [
            "Two 40,000 sq. ft. luxury clubhouses", "Half-acre lakelet with sandy beach", "90m diameter cricket pitch & pavilion",
            "Olympic-size swimming pool & covered indoor pool", "Squash, tennis & multi-sport courts",
            "3 km jogging and walking trail", "Biometric 3-tier security with 24/7 patrol", "100% full power backup"
        ],
        "locationAdvantages": [
            "Located right on Dwarka Expressway in Sector 108",
            "Just 15 minutes from Terminal 3 of Indira Gandhi International Airport",
            "10 minutes from Yashobhoomi (IICC) in Dwarka",
            "Adjoining Delhi border with zero traffic bottlenecks"
        ],
        "paymentPlan": "Special 20:80 and construction-linked milestone payment schemes.",
        "isDemo2": False,
        "isTopProject": True,
        "isFeatured": True
    }
]

os.makedirs('data', exist_ok=True)
with open('data/properties.json', 'w', encoding='utf-8') as f:
    json.dump(properties, f, indent=2, ensure_ascii=False)

print(f"Successfully generated data/properties.json with {len(properties)} properties.")

