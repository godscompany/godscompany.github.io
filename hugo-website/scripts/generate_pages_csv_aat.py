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

    keywords = [
        f"{suburb} airport transfer", f"{suburb} to Tullamarine", f"{suburb} to Avalon",
        f"airport taxi {suburb}", f"private airport transfer {suburb}", f"shared ride {suburb}",
        f"{suburb} transfers", f"airport shuttle {suburb}", f"book {suburb} airport taxi",
        f"affordable {suburb} airport transfer", f"{suburb} airport transfer service",
        "airport transfer Geelong", "airport transfer Melbourne", "Melbourne airport taxi",
        "airport transfers Victoria", "Tullamarine airport shuttle", "Avalon airport transfers",
        "Melbourne private transfer", "airport transport services Melbourne"
    ]
    keywords += [
        f"{suburb} to Avalon airport taxi",
        f"Avalon airport pickup from {suburb}",
        f"{suburb} Avalon airport ride",
        f"Avalon airport chauffeur {suburb}",
        f"Avalon airport transport {suburb}",
        f"Avalon airport drop-off from {suburb}",
        f"Avalon airport car hire {suburb}",
        f"cheap Avalon airport transfer from {suburb}",
        f"best Avalon airport shuttle {suburb}",
        f"{suburb} Avalon flight transfer",
        f"{suburb} Avalon taxi fare",
        f"door-to-door Avalon airport {suburb}",
        f"Avalon airport booking {suburb}",
        f"reliable Avalon transfer {suburb}",
        f"Avalon airport service near {suburb}",
        f"{suburb} to Avalon express transfer",
        "Avalon regional airport transfers",
        "private Avalon shuttle Victoria",
        "Avalon taxi from Geelong suburbs"
    ]
    meta_keywords = ', '.join(keywords)

    front_matter = f"""---
title: "Avalon Airport Transfers from {suburb}, {state}"
description: "Reliable and affordable airport transfer service from {suburb} to Avalon Airport and Melbourne Tullamarine. Whether you're heading off on a holiday, a business trip, or picking up a loved one, enjoy a comfortable, door-to-door ride with our trusted local drivers. We offer private and shared airport shuttles, upfront pricing, and timely service — making your journey stress-free every time."
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
## Hassle-Free Airport Transfers from **{suburb}**

Travelling from **{suburb}** to catch a flight has never been easier. Whether you're jetting off on a domestic getaway or embarking on an international adventure, our professional airport transfer services are designed to make your journey to the airport smooth, timely, and completely stress-free. You have two convenient airport options nearby:

- **Avalon Airport** – located just **{dist_avalon} km** away, it's the ideal choice for quick regional and select domestic flights. With its compact size and ease of access, Avalon Airport is a popular alternative for travellers looking to avoid the congestion and longer queues often found at larger airports. From check-in to boarding, the entire process is faster, allowing you to arrive closer to your departure time without stress. Parking is easy, and getting in and out of the terminal is a breeze — especially when you’re dropped off right at the front door with our door-to-door service.

- **Melbourne Tullamarine Airport** – approximately **{dist_tulla} km** from **{suburb}**, it serves as the primary hub for both domestic and international travel across Australia and beyond. Ideal for long-haul flights or when your airline of choice operates exclusively from Tullamarine.

We offer flexible transfer options tailored to suit every traveller’s needs:

- **Shared Ride Services** – a cost-effective and eco-friendly option, with fares starting from just **${price_min}**. Great for solo travellers or those with flexible schedules, our shared rides offer comfortable seating, luggage assistance, and reliable timing.
- **Private Exclusive Transfers** – perfect for individuals, families, or business travellers seeking more space, privacy, and direct service. Prices can go up to **${price_max}** depending on vehicle type and time of day. Choose from premium sedans, SUVs, or people movers — all maintained to high standards for a luxurious ride experience.

All our fares are **upfront, fair, and transparent**, meaning you’ll never be caught off guard with hidden charges. From friendly, professional drivers to clean, modern vehicles equipped with real-time tracking, we prioritize your **safety, comfort, and punctuality**.

Whether your flight departs from Avalon or Tullamarine, let us take the stress out of your travel day. Book your transfer in advance, relax, and enjoy the convenience of a seamless ride from **{suburb}** to the airport.

---
## What Makes **{suburb}** Truly Special?

{attractions}

But beyond its well-known attractions, **{suburb}** is a place where community spirit thrives and everyday life feels just a bit more charming. It’s where you grab your morning coffee from the same smiling barista, where weekend strolls lead to leafy trails and hidden picnic spots by the creek, and where neighbours greet each other by name. Life here is about connection, comfort, and character — and that's exactly what we bring to your airport journey.

Our airport transfer service isn’t just about getting you from point A to point B. It’s about **seamlessly linking the warmth and rhythm of {suburb} life** to your travels, whether you’re catching a red-eye at Tullamarine or a quick hop from Avalon. We take pride in being a part of your routine, your adventures, and everything in between.

When flying out of **Avalon Airport**, you're not just saving time — you're gaining convenience. As a smaller airport located just **{dist_avalon} km** from **{suburb}**, Avalon offers faster check-ins, shorter queues, and easy navigation through the terminal. Our transfers to Avalon are perfectly timed, with door-to-door service that ensures you arrive with plenty of time to spare. It’s ideal for families, business travellers, or those who just want a smooth start to their trip.

Whether you're catching an early flight to Sydney, a budget airline getaway to the Gold Coast, or welcoming someone back home, our Avalon transfers are prompt, reliable, and tailored to your exact needs.

---

## Why Our Airport Transfers Are Perfect for You

### 🚘 Stress-Free Pickups and Drop-offs
Our local drivers are experts on **{suburb}** — they know every shortcut, traffic pattern, and hidden cul-de-sac. With us, you'll never worry about delays or missed turns.

### 💼 Business or Leisure, We’ve Got You Covered
Whether you’re a frequent flyer heading to a business meeting or a family heading off for a long-awaited holiday, our flexible service adapts to your schedule and travel style.

### 🛫 Avalon Airport Specialists
We understand the unique benefits of flying through Avalon — quicker access, regional convenience, and less airport stress. Our drivers are experienced with Avalon schedules, routes, and timing, ensuring a seamless experience every time.

### 💲 Clear, Honest, and Competitive Pricing
No surprises here. We use a **distance-based fare system** combined with flat-rate transparency — offering options for shared rides for those on a budget and private transfers for added comfort and convenience. You always know what you're paying for, and why.

---

## Tips for Travelling from **{suburb}**

- **Book early** to lock in your preferred time, especially during holidays, school breaks, or major events in Geelong and Melbourne.
- **Know your terminal** at Avalon or Tullamarine in advance. While Avalon has fewer terminals, it’s still helpful to check your airline’s instructions beforehand.
- **Leave buffer time**: Avalon is quieter and more streamlined, but it’s still wise to arrive 60–90 minutes before departure to allow for check-in and security.
- **Let us know** if you have extra luggage, bulky items, a pet carrier, or accessibility requirements — we’re more than happy to accommodate your specific travel needs.
- **Flying from Avalon?** Take advantage of its compact design and easy parking. Our transfers drop you right at the terminal entrance, so you can walk straight in without the airport hassle.
- **Check for seasonal flights**: Avalon Airport frequently adds seasonal services to popular destinations like the Gold Coast, Sydney, and Adelaide. If you're planning a getaway, it might be closer and quicker than you think!

---

## Frequently Asked Questions (FAQs)

**Q: Can I share the ride with others to save money?**  
**A:** Yes, definitely! We offer a convenient **shared ride service** designed for passengers who don’t mind traveling with others and want to reduce costs. It’s a great option for solo travellers, students, or anyone looking to save without compromising comfort. You’ll still enjoy a timely and relaxing ride — just at a lower price.

**Q: Are your drivers local to the area?**  
**A:** Absolutely. Our drivers live and work in the region, so they know the local roads, traffic patterns, and shortcuts extremely well. Whether it’s peak hour or an early morning pickup, their local knowledge ensures **fast, reliable, and smooth travel** — no unnecessary delays, no missed turns.

**Q: Can I book last-minute or on short notice?**  
**A:** We understand that travel plans can change in an instant. That’s why we do our best to accommodate **last-minute bookings**. If you need a transfer on short notice, simply give us a call or book through our online portal using the link below — and we’ll do everything we can to get you on your way quickly and stress-free.

**Q: Is Avalon Airport a good option for domestic flights?**  
**A:** Absolutely! Avalon Airport offers an efficient, low-stress alternative for many domestic routes. Its streamlined design means **less walking, faster processing, and shorter queues** — perfect for travellers who want simplicity and speed. Plus, its proximity to **{suburb}** makes it incredibly convenient for quick weekend getaways or work trips.

**Q: Do you offer baby seats or booster seats?**  
**A:** Yes! Safety is a top priority. Please let us know your requirements at the time of booking and we’ll ensure your transfer vehicle is equipped with the appropriate child restraints at no extra cost.

---

## Trusted by Locals

When it comes to airport transfers, trust matters — and our reputation in **{suburb}, {city}, and the surrounding areas** is built on years of dependable service, friendly drivers, and a real connection with the community. We’re more than just a ride; we’re your **neighbours**, your **go-to transport team**, and your **airport specialists**.

Unlike large taxi chains or impersonal ride-hailing apps, we take pride in offering a **personal touch**. From the moment you book until we drop you off at the terminal, we’re focused on one thing: making your journey smooth, safe, and stress-free.

Our regular clients — from busy professionals and retirees to families catching early flights — know they can rely on us for **punctuality**, **clean and comfortable vehicles**, and **drivers who genuinely care**.

Being locally owned and operated means we know the shortcuts, traffic patterns, and how to avoid delays — giving you peace of mind every time you travel.

We’re especially proud of our **Avalon Airport transfer service**. With **{dist_avalon} km** of easy, direct travel between **{suburb}** and Avalon, we’ve helped thousands of locals take full advantage of this convenient regional airport. Whether it’s for a last-minute weekend trip or a routine business commute, Avalon offers a hassle-free flying experience — and we make sure your ride there is just as seamless.

---

## Final Thoughts: Make Your Next Transfer Easy

When it comes to catching a flight or arriving home after a long journey, the last thing you need is uncertainty. Choosing the right airport transfer from **{suburb}** isn’t just a matter of convenience — it’s about starting or ending your trip on the right note.

With our **locally trusted, punctual, and customer-focused service**, you can relax knowing that every detail is handled. From the moment you book to the final drop-off at the terminal or your doorstep, we’re committed to providing a **seamless, stress-free experience** that fits your schedule and budget.

Flying through **Avalon Airport**? You’re choosing an airport that’s **closer, quieter, and faster to navigate** — and with our expert drivers, you can count on arriving with time to spare. We monitor flight schedules, stay ahead of traffic updates, and offer flexible pickup windows to keep your journey smooth from start to finish.

Don't leave your travel day to chance — let us take care of the journey so you can focus on what matters most. Whether you're traveling for business or leisure, our mission is to make every airport transfer **reliable, affordable, and easy**.

---


[📅 **Book Your Airport Ride Now**]({booking_link})  
[📧 **Request a Quick Quote**]({quote_link})

---

## SEO Keywords Used

- **Airport Transfer {suburb}**
- **Tullamarine Taxi from {suburb}**
- **Avalon Airport Shuttle**
- **Melbourne Airport Private Car**
- **Geelong Airport Taxi**
- **Victoria Airport Transfer Services**
- **Chauffeur Transfer to Airport**
- **Reliable Airport Pickups from {suburb}**
- **Book a Ride to Avalon/Tullamarine from {suburb}**
- **{suburb} to Avalon Airport Transfer**
- **{suburb} to Tullamarine Airport Transport**
- **Affordable Airport Shuttle {suburb}**
- **Best Airport Transfer Service {suburb}**
- **Door-to-Door Airport Ride {suburb}**
- **Private Airport Car Hire {suburb}**
- **Luxury Airport Taxi Victoria**
- **Book Airport Chauffeur in {suburb}**
- **{suburb} Airport Drop-off and Pickup**
- **On-Time Airport Ride {suburb}**
- **Flight Transfer Services from {suburb}**
- **Avalon Airport Transport Experts**
- **Quick Shuttle to Avalon Airport**
- **Fast Avalon Transfers from {suburb}**
- **{suburb} to Avalon Direct Shuttle**
- **Local Avalon Airport Car Service**

### Why Avalon is a Great Airport Choice

Avalon Airport is an increasingly popular departure point for travellers across Victoria, thanks to its streamlined layout, minimal wait times, and proximity to **{suburb}**. Whether you're flying with Jetstar, Bonza, or another regional carrier, you'll appreciate:

- **Shorter queues** for check-in and security.
- **Faster boarding** and baggage collection.
- **Easy drop-off and pickup zones** — we’ll get you there quickly and conveniently.
- **Lower stress levels** compared to the hustle of Melbourne Tullamarine.

Choosing Avalon means you’re choosing **simplicity, speed, and convenience** — and with our experienced transfer service, it’s never been easier to get there from **{suburb}**.

We hope this guide has helped you understand everything you need to know about travelling from **{suburb}** to either **Avalon** or **Tullamarine Airport**. Our friendly team looks forward to welcoming you onboard — whether you're headed for a holiday, a work trip, or coming home to Victoria.

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

