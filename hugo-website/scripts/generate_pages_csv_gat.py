import os
import csv
import yaml
from slugify import slugify

# Configuration
CSV_FILE = 'data/aus/vic/geelong_sorted_final.csv'
CONFIG_FILE = 'data/site_config.yaml'
CONTENT_DIR = 'content/australia'
PRICE_MULTIPLIER_MIN = 1.2
PRICE_MULTIPLIER_MAX = 2.4
ADDITIONAL_FARE = 20  # Adding $20 to both the min and max fare

os.makedirs(CONTENT_DIR, exist_ok=True)

# Load config data
with open(CONFIG_FILE, 'r') as config_file:
    config = yaml.safe_load(config_file)

booking_link = config.get('booking_url', '#')
quote_link = config.get('quote_url', '#')


def generate_markdown(state, city, suburb, dist_avalon, dist_tulla, attractions):
    slug = slugify(suburb)
    state_slug = slugify(state)
    city_slug = slugify(city)

    folder = os.path.join(CONTENT_DIR, state_slug, city_slug)
    os.makedirs(folder, exist_ok=True)

    price_min = round(float(dist_tulla) * PRICE_MULTIPLIER_MIN + ADDITIONAL_FARE, 2)
    price_max = round(float(dist_tulla) * PRICE_MULTIPLIER_MAX + ADDITIONAL_FARE, 2)

    filename = os.path.join(folder, f"{slug}.md")

    canonical_url = f"https://laraairportservices.com.au/{state_slug}/{city_slug}/{slug}/"

    suburbs = [
        "Geelong", "Lara", "Corio", "Norlane", "Newtown", "Belmont", "Grovedale", "Highton", "Waurn Ponds",
        "Armstrong Creek", "Charlemont", "Marshall", "Hamlyn Heights", "Herne Hill", "Leopold", "Newcomb",
        "St Albans Park", "Whittington", "Thomson", "Breakwater", "Bell Park", "Bell Post Hill", "Lovely Banks",
        "Bannockburn", "Drysdale", "Clifton Springs", "Ocean Grove", "Barwon Heads", "Torquay", "Anglesea",
        "Winchelsea", "Little River"
    ]

    keywords = [
        "airport transfer Geelong", "airport transfer Melbourne", "Melbourne airport taxi",
        "airport transfers Victoria", "Tullamarine airport shuttle", "Avalon airport transfers",
        "Melbourne private transfer", "airport transport services Melbourne", "Avalon airport taxi", "Tullamarineairport taxi"
    ]

    for suburb in suburbs:
        keywords.extend([
            f"{suburb} airport transfer",
            f"{suburb} to Tullamarine",
            f"{suburb} to Avalon",
            f"airport taxi {suburb}",
            f"private airport transfer {suburb}",
            f"shared ride {suburb}",
            f"{suburb} transfers",
            f"airport shuttle {suburb}",
            f"book {suburb} airport taxi",
            f"affordable {suburb} airport transfer",
            f"{suburb} airport transfer service",
            f"{suburb} Avalon airport transport",
            f"{suburb} Tullamarine airport taxi",
            f"on-time airport pickup {suburb}",
            f"{suburb} airport ride",
            f"door-to-door transfer {suburb}"
        ])

    meta_keywords = ', '.join(keywords)

    front_matter = f"""---
title: "Airport Transfers from {suburb}, {state}"
description: "Personalised airport transfer service from {suburb} to Avalon and Tullamarine airports. Enjoy a smooth, affordable ride with us!"
keywords: "{meta_keywords}"
state: {state}
city: {city}
suburb: {suburb}
distance_to_avalon: {dist_avalon}
distance_to_tullamarine: {dist_tulla}
price_min: {price_min}
price_max: {price_max}
slug: {slug}
canonical_url: "{canonical_url}"
draft: false
---
"""

    body = f"""
## Airport Transfers Across **{suburb}** and Surrounding Suburbs

Looking for a trusted, reliable, and affordable airport transfer service in the Geelong region? Whether you’re based in the heart of the city or in a peaceful surrounding suburb, we’ve got you covered with personalised transfers to both **Avalon Airport** and **Melbourne Tullamarine Airport**.

Our door-to-door service ensures you’re picked up from **your exact location** and dropped off right at the terminal, with no stress, no parking hassles, and no delays. Ideal for families, business travellers, FIFO workers, or holiday-goers — we tailor your experience for comfort and convenience.

We proudly service the following areas:

- **Geelong City & Central**: Geelong, Newtown, Belmont, South Geelong, East Geelong, West Geelong
- **Northern Suburbs**: Corio, Norlane, North Shore, Bell Park, Bell Post Hill, Lovely Banks
- **Western & Inland**: Hamlyn Heights, Herne Hill, Bannockburn, Inverleigh, Winchelsea
- **Southern Corridor**: Highton, Waurn Ponds, Grovedale, Armstrong Creek, Charlemont, Mount Duneed
- **Eastern Suburbs**: Newcomb, Whittington, Thomson, Breakwater, St Albans Park, Leopold
- **Bellarine Peninsula**: Drysdale, Clifton Springs, Ocean Grove, Barwon Heads, Point Lonsdale
- **Surf Coast & Coastal**: Torquay, Jan Juc, Anglesea, Aireys Inlet
- **Outlying Regions**: Lara, Little River, Batesford, Fyansford, Moorabool, Anakie

---

## Hassle-Free Airport Transfers from **{suburb}**

Travelling from **{suburb}** to catch a flight has never been easier. Whether you're jetting off on a domestic getaway or embarking on an international adventure, our professional airport transfer services are designed to make your journey to the airport smooth, timely, and completely stress-free. You have two convenient airport options nearby:

- **Avalon Airport** – located just **{dist_avalon} km** away, it's the ideal choice for quick regional and some domestic flights.
- **Melbourne Tullamarine Airport** – approximately **{dist_tulla} km** from **{suburb}**, it serves as the primary hub for both domestic and international travel across Australia and beyond.

We offer flexible transfer options tailored to suit every traveller’s needs:

- **Shared Ride Services** – a cost-effective and eco-friendly option, with fares starting from just **${price_min}**.
- **Private Exclusive Transfers** – perfect for individuals, families, or business travellers seeking more space and direct service, with prices up to **${price_max}** depending on vehicle type and time of day.

All our fares are **upfront, fair, and transparent**, meaning you’ll never be caught off guard with hidden charges. From friendly drivers to clean, comfortable vehicles, we prioritize your safety, comfort, and punctuality — so you can focus on your journey ahead while we handle the ride.

---

## Why Choose Us for Airport Transfers from **{suburb}**?

- **Reliable, On-Time Service** – Whether it’s Avalon or Tullamarine, you can count on us to get you there on time.
- **Affordable and Flexible Options** – Choose between shared rides, perfect for saving money, or private transfers for more space and comfort.
- **Local Drivers Who Know the Area** – Our team of local drivers ensures that your ride is smooth and fast, taking the best routes to avoid traffic and delays.
- **Stress-Free Booking Process** – Booking your ride is easy and can be done in just a few clicks online or over the phone.

---

## Travel from **{suburb}** with Confidence

Our fleet includes a wide range of vehicles, from sedans for individuals or couples, to larger vehicles for families and groups. All vehicles are well-maintained, comfortable, and climate-controlled, ensuring that your journey is always a pleasant one.

Whether you're heading to a last-minute flight from Avalon or a longer journey to Tullamarine, we’ll make sure you arrive relaxed and on time.

With competitive pricing, an unbeatable level of service, and a deep understanding of the area, we provide the best airport transfer options in the region. **Get in touch today and make your next trip hassle-free!**

---

## What Makes **{suburb}** Truly Special?

**{suburb}** is a vibrant community, full of charm and character, offering both residents and visitors a welcoming atmosphere. From stunning parks and scenic views to local attractions and friendly neighbours, **{suburb}** has something for everyone. Some notable highlights include:

- **{attractions}** – whether it's a family-friendly attraction or a peaceful spot for relaxation, **{suburb}** has plenty to explore. 
- **Scenic Walks and Trails** – ideal for nature lovers, you can wander through lush parks, or enjoy a peaceful day by the creek.
- **Local Markets and Artisan Shops** – where you can find unique handcrafted goods, delicious local produce, and one-of-a-kind treasures.

But beyond its well-known attractions, **{suburb}** is a place where community spirit thrives and everyday life feels just a bit more charming. It’s where you grab your morning coffee from the same smiling barista, where weekend strolls lead to leafy trails and hidden picnic spots by the creek, and where neighbours greet each other by name. Life here is about connection, comfort, and character — and that's exactly what we bring to your airport journey.

Our airport transfer service isn’t just about getting you from point A to point B. It’s about **seamlessly linking the warmth and rhythm of {suburb} life** to your travels, whether you’re catching a red-eye at Tullamarine or a quick hop from Avalon. We take pride in being a part of your routine, your adventures, and everything in between.

---

## Why Our Airport Transfers Are Perfect for You

### 🚘 Stress-Free Pickups and Drop-offs
Our local drivers are experts on **{suburb}** — they know every shortcut, traffic pattern, and hidden cul-de-sac. With us, you'll never worry about delays or missed turns. Whether it's the main streets or lesser-known paths, we ensure a smooth, efficient ride to the airport.

### 💼 Business or Leisure, We’ve Got You Covered
Whether you’re a frequent flyer heading to a business meeting or a family heading off for a long-awaited holiday, our flexible service adapts to your schedule and travel style. Need an early-morning pickup or a late-night drop-off? We’re available to suit all your needs.

### 💲 Clear, Honest, and Competitive Pricing
No surprises here. We use a **distance-based fare system** combined with flat-rate transparency — offering options for shared rides for those on a budget and private transfers for added comfort and convenience. You always know what you're paying for, and why. Whether you're catching a flight from Avalon or Tullamarine, our pricing ensures that you'll get the best value for your trip.

---

## Tips for Travelling from **{suburb}**

- **Book early** to lock in your preferred time, especially during holidays. Geelong can get busy during peak seasons, so reserving your ride in advance ensures a spot when you need it.
- **Know your terminal** at Avalon or Tullamarine in advance. This helps your driver plan the best route and ensures there are no last-minute delays when you arrive.
- **Leave buffer time**: Avalon is quieter, but Tullamarine can get busy, especially during rush hours. Factor in extra time for traffic or security checks.
- **Let us know** if you have extra luggage or special requests — we’re happy to accommodate. Whether it’s a large suitcase, a golf bag, or an additional child seat, we’re prepared to make your ride comfortable and stress-free.

---

## Frequently Asked Questions (FAQs)

**Q: Can I share the ride with others to save money?**  
**A:** Yes, definitely! We offer a convenient **shared ride service** designed for passengers who don’t mind traveling with others and want to reduce costs. It’s a great option for solo travellers, students, or anyone looking to save without compromising comfort. You’ll still enjoy a timely and relaxing ride — just at a lower price.

**Q: Are your drivers local to the area?**  
**A:** Absolutely. Our drivers live and work in the region, so they know the local roads, traffic patterns, and shortcuts extremely well. Whether it’s peak hour or an early morning pickup, their local knowledge ensures **fast, reliable, and smooth travel** — no unnecessary delays, no missed turns. They’re also familiar with popular landmarks and places in **Geelong**, ensuring you have a comfortable ride from start to finish.

**Q: Can I book last-minute or on short notice?**  
**A:** We understand that travel plans can change in an instant. That’s why we do our best to accommodate **last-minute bookings**. If you need a transfer on short notice, simply give us a call or book through our online portal using the link below — and we’ll do everything we can to get you on your way quickly and stress-free. Whether it’s a spontaneous weekend getaway from Geelong or an urgent business trip, we’re here to help.

**Q: Is there a parking fee at Avalon or Tullamarine airports for drop-offs?**  
**A:** No, we take care of parking for you! Our professional drivers will drop you off right at the terminal, so you don’t need to worry about finding parking or paying for it. Whether you’re departing from Avalon or Tullamarine, we aim to make your trip hassle-free right from the start.

**Q: Are your vehicles suitable for large groups or families?**  
**A:** Yes! We have a range of vehicles to suit your needs, from standard sedans for solo travellers to larger vehicles for families or groups. If you need a car with more space for luggage or extra passengers, just let us know when you book, and we’ll provide the best vehicle for your trip.

---

We hope this guide helps you plan your next airport journey from **{suburb}**. If you have any more questions or need assistance with your booking, don't hesitate to reach out to us. Safe travels!

---
## Trusted by Locals

When it comes to airport transfers, there’s one thing that matters most — trust. For years, our reputation in **Geelong**, **Victoria**, and surrounding suburbs has been built on dependable service, friendly drivers, and a deep connection with the community. We’re not just a ride to the airport; we’re your **neighbours**, your **go-to transport team**, and your **trusted airport specialists**.

Unlike the large, impersonal taxi chains or ride-hailing apps, we take great pride in offering a **personal touch** with every trip. From the moment you book your ride, to the moment we drop you off at the terminal, we’re dedicated to making your airport journey smooth, safe, and stress-free.

Our loyal clients — whether they’re busy professionals rushing to catch a flight, retirees enjoying a relaxed trip, or families heading on a long-awaited vacation — rely on us for **punctuality**, **clean, well-maintained vehicles**, and **drivers who truly care** about providing exceptional service.

Being locally owned and operated means that our drivers are more than just employees — they’re **local experts**. They know the roads, the shortcuts, and the best routes to avoid delays. Whether it’s navigating through **Geelong**’s streets or driving to Avalon or Tullamarine Airport, we ensure that you’re always in safe, capable hands.

For our clients, that means peace of mind every time they travel. Whether you’re catching an early morning flight, arriving back home after a long trip, or simply heading to the airport with no worries, we’re here to make sure your experience is seamless and stress-free.

---

## Final Thoughts: Make Your Next Transfer Easy

When it comes to catching a flight or arriving home after a long journey, the last thing you want to worry about is your transport. The key to a smooth start or finish to your trip lies in choosing the right airport transfer from **Geelong**. It’s not just about getting from point A to point B — it’s about starting or ending your journey on the right note.

With our **locally trusted**, **punctual**, and **customer-focused service**, you can rest easy knowing that every detail is taken care of. From the moment you book to the final drop-off at your terminal or doorstep, we are committed to providing a **seamless, stress-free experience** that works with your schedule and budget.

Don’t leave your travel day to chance. Let us take care of the journey so you can focus on what matters most. Whether you’re traveling for business or leisure, we are here to make every airport transfer **reliable**, **affordable**, and **easy**. After all, you deserve a comfortable and dependable journey, every time.

---

[📅 **Book Your Airport Ride Now**]({booking_link})  
[📧 **Request a Quick Quote**]({quote_link})

---
## SEO Keywords Used
- **Airport Transfer Geelong**
- **Tullamarine Taxi from Geelong**
- **Avalon Airport Shuttle Geelong**
- **Melbourne Airport Private Car Geelong**
- **Geelong Airport Taxi**
- **Victoria Airport Transfer Services**
- **Chauffeur Transfer to Airport Geelong**
- **Reliable Airport Pickups from Geelong**
- **Book a Ride to Avalon/Tullamarine from Geelong**
- **Geelong to Avalon Airport Transfer**
- **Geelong to Tullamarine Airport Transport**
- **Affordable Airport Shuttle Geelong**
- **Best Airport Transfer Service Geelong**
- **Door-to-Door Airport Ride Geelong**
- **Private Airport Car Hire Geelong**
- **Luxury Airport Taxi Victoria**
- **Book Airport Chauffeur in Geelong**
- **Geelong Airport Drop-off and Pickup**
- **On-Time Airport Ride Geelong**
- **Flight Transfer Services from Geelong**

### Surrounding Suburbs:
- **Airport Transfer Lara**
- **Tullamarine Taxi from Lara**
- **Avalon Airport Shuttle Lara**
- **Melbourne Airport Private Car Lara**
- **Lara Airport Taxi**
- **Victoria Airport Transfer Services Lara**
- **Chauffeur Transfer to Airport Lara**
- **Reliable Airport Pickups from Lara**
- **Book a Ride to Avalon/Tullamarine from Lara**
- **Lara to Avalon Airport Transfer**
- **Lara to Tullamarine Airport Transport**
- **Affordable Airport Shuttle Lara**
- **Best Airport Transfer Service Lara**
- **Door-to-Door Airport Ride Lara**
- **Private Airport Car Hire Lara**
- **Luxury Airport Taxi Victoria**
- **Book Airport Chauffeur in Lara**
- **Lara Airport Drop-off and Pickup**
- **On-Time Airport Ride Lara**
- **Flight Transfer Services from Lara**

- **Airport Transfer Bell Park**
- **Tullamarine Taxi from Bell Park**
- **Avalon Airport Shuttle Bell Park**
- **Melbourne Airport Private Car Bell Park**
- **Bell Park Airport Taxi**
- **Victoria Airport Transfer Services Bell Park**
- **Chauffeur Transfer to Airport Bell Park**
- **Reliable Airport Pickups from Bell Park**
- **Book a Ride to Avalon/Tullamarine from Bell Park**
- **Bell Park to Avalon Airport Transfer**
- **Bell Park to Tullamarine Airport Transport**
- **Affordable Airport Shuttle Bell Park**
- **Best Airport Transfer Service Bell Park**
- **Door-to-Door Airport Ride Bell Park**
- **Private Airport Car Hire Bell Park**
- **Luxury Airport Taxi Victoria**
- **Book Airport Chauffeur in Bell Park**
- **Bell Park Airport Drop-off and Pickup**
- **On-Time Airport Ride Bell Park**
- **Flight Transfer Services from Bell Park**

- **Airport Transfer Highton**
- **Tullamarine Taxi from Highton**
- **Avalon Airport Shuttle Highton**
- **Melbourne Airport Private Car Highton**
- **Highton Airport Taxi**
- **Victoria Airport Transfer Services Highton**
- **Chauffeur Transfer to Airport Highton**
- **Reliable Airport Pickups from Highton**
- **Book a Ride to Avalon/Tullamarine from Highton**
- **Highton to Avalon Airport Transfer**
- **Highton to Tullamarine Airport Transport**
- **Affordable Airport Shuttle Highton**
- **Best Airport Transfer Service Highton**
- **Door-to-Door Airport Ride Highton**
- **Private Airport Car Hire Highton**
- **Luxury Airport Taxi Victoria**
- **Book Airport Chauffeur in Highton**
- **Highton Airport Drop-off and Pickup**
- **On-Time Airport Ride Highton**
- **Flight Transfer Services from Highton**

- **Airport Transfer Newtown**
- **Tullamarine Taxi from Newtown**
- **Avalon Airport Shuttle Newtown**
- **Melbourne Airport Private Car Newtown**
- **Newtown Airport Taxi**
- **Victoria Airport Transfer Services Newtown**
- **Chauffeur Transfer to Airport Newtown**
- **Reliable Airport Pickups from Newtown**
- **Book a Ride to Avalon/Tullamarine from Newtown**
- **Newtown to Avalon Airport Transfer**
- **Newtown to Tullamarine Airport Transport**
- **Affordable Airport Shuttle Newtown**
- **Best Airport Transfer Service Newtown**
- **Door-to-Door Airport Ride Newtown**
- **Private Airport Car Hire Newtown**
- **Luxury Airport Taxi Victoria**
- **Book Airport Chauffeur in Newtown**
- **Newtown Airport Drop-off and Pickup**
- **On-Time Airport Ride Newtown**
- **Flight Transfer Services from Newtown**

- **Airport Transfer Corio**
- **Tullamarine Taxi from Corio**
- **Avalon Airport Shuttle Corio**
- **Melbourne Airport Private Car Corio**
- **Corio Airport Taxi**
- **Victoria Airport Transfer Services Corio**
- **Chauffeur Transfer to Airport Corio**
- **Reliable Airport Pickups from Corio**
- **Book a Ride to Avalon/Tullamarine from Corio**
- **Corio to Avalon Airport Transfer**
- **Corio to Tullamarine Airport Transport**
- **Affordable Airport Shuttle Corio**
- **Best Airport Transfer Service Corio**
- **Door-to-Door Airport Ride Corio**
- **Private Airport Car Hire Corio**
- **Luxury Airport Taxi Victoria**
- **Book Airport Chauffeur in Corio**
- **Corio Airport Drop-off and Pickup**
- **On-Time Airport Ride Corio**
- **Flight Transfer Services from Corio**

- **Airport Transfer Belmont**
- **Tullamarine Taxi from Belmont**
- **Avalon Airport Shuttle Belmont**
- **Melbourne Airport Private Car Belmont**
- **Belmont Airport Taxi**
- **Victoria Airport Transfer Services Belmont**
- **Chauffeur Transfer to Airport Belmont**
- **Reliable Airport Pickups from Belmont**
- **Book a Ride to Avalon/Tullamarine from Belmont**
- **Belmont to Avalon Airport Transfer**
- **Belmont to Tullamarine Airport Transport**
- **Affordable Airport Shuttle Belmont**
- **Best Airport Transfer Service Belmont**
- **Door-to-Door Airport Ride Belmont**
- **Private Airport Car Hire Belmont**
- **Luxury Airport Taxi Victoria**
- **Book Airport Chauffeur in Belmont**
- **Belmont Airport Drop-off and Pickup**
- **On-Time Airport Ride Belmont**
- **Flight Transfer Services from Belmont**

---
"""

    with open(filename, 'w', encoding='utf-8', errors='replace') as f:
        f.write(front_matter)
        f.write(body)

    print(f"Generated: {filename}")


# Load and process the CSV
with open(CSV_FILE, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        generate_markdown(
            row['State'],
            row['City'],
            row['Suburb'],
            row['DistanceToAvalon'],
            row['DistanceToTullamarine'],
            row['Attractions']
        )

