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
## Hassle-Free Airport Transfers from **{suburb}**

Travelling from **{suburb}** to catch a flight has never been easier. Whether you're jetting off on a domestic getaway or embarking on an international adventure, our professional airport transfer services are designed to make your journey to the airport smooth, timely, and completely stress-free. You have two convenient airport options nearby:

- **Avalon Airport** – located just **{dist_avalon} km** away, it's the ideal choice for quick regional and some domestic flights.  
- **Melbourne Tullamarine Airport** – approximately **{dist_tulla} km** from **{suburb}**, it serves as the primary hub for both domestic and international travel across Australia and beyond.

We offer flexible transfer options tailored to suit every traveller’s needs:

- **Shared Ride Services** – a cost-effective and eco-friendly option, with fares starting from just **${price_min}**.  
- **Private Exclusive Transfers** – perfect for individuals, families, or business travellers seeking more space and direct service, with prices up to **${price_max}** depending on vehicle type and time of day.

All our fares are **upfront, fair, and transparent**, meaning you’ll never be caught off guard with hidden charges. From friendly drivers to clean, comfortable vehicles, we prioritize your safety, comfort, and punctuality — so you can focus on your journey ahead while we handle the ride.

---

## What Makes **{suburb}** Truly Special?

{attractions}

But beyond its well-known attractions, **{suburb}** is a place where community spirit thrives and everyday life feels just a bit more charming. It’s where you grab your morning coffee from the same smiling barista, where weekend strolls lead to leafy trails and hidden picnic spots by the creek, and where neighbours greet each other by name. Life here is about connection, comfort, and character — and that's exactly what we bring to your airport journey.

Our airport transfer service isn’t just about getting you from point A to point B. It’s about **seamlessly linking the warmth and rhythm of {suburb} life** to your travels, whether you’re catching a red-eye at Tullamarine or a quick hop from Avalon. We take pride in being a part of your routine, your adventures, and everything in between.

---

## Why Our Airport Transfers Are Perfect for You

### 🚘 Stress-Free Pickups and Drop-offs
Our local drivers are experts on **{suburb}** — they know every shortcut, traffic pattern, and hidden cul-de-sac. With us, you'll never worry about delays or missed turns.

### 💼 Business or Leisure, We’ve Got You Covered
Whether you’re a frequent flyer heading to a business meeting or a family heading off for a long-awaited holiday, our flexible service adapts to your schedule and travel style.

### 💲 Clear, Honest, and Competitive Pricing
No surprises here. We use a **distance-based fare system** combined with flat-rate transparency — offering options for shared rides for those on a budget and private transfers for added comfort and convenience. You always know what you're paying for, and why.

---

## Tips for Travelling from {suburb}

- **Book early** to lock in your preferred time, especially during holidays.
- **Know your terminal** at Avalon or Tullamarine in advance.
- **Leave buffer time**: Avalon is quieter, but Tullamarine can get busy.
- **Let us know** if you have extra luggage or special requests — we’re happy to accommodate.

---

## Frequently Asked Questions (FAQs)

**Q: Can I share the ride with others to save money?**  
**A:** Yes, definitely! We offer a convenient **shared ride service** designed for passengers who don’t mind traveling with others and want to reduce costs. It’s a great option for solo travellers, students, or anyone looking to save without compromising comfort. You’ll still enjoy a timely and relaxing ride — just at a lower price.

**Q: Are your drivers local to the area?**  
**A:** Absolutely. Our drivers live and work in the region, so they know the local roads, traffic patterns, and shortcuts extremely well. Whether it’s peak hour or an early morning pickup, their local knowledge ensures **fast, reliable, and smooth travel** — no unnecessary delays, no missed turns.

**Q: Can I book last-minute or on short notice?**  
**A:** We understand that travel plans can change in an instant. That’s why we do our best to accommodate **last-minute bookings**. If you need a transfer on short notice, simply give us a call or book through our online portal using the link below — and we’ll do everything we can to get you on your way quickly and stress-free.

---

## Trusted by Locals

When it comes to airport transfers, trust matters — and our reputation in **{suburb}, {city}, and the surrounding areas** is built on years of dependable service, friendly drivers, and a real connection with the community. We’re more than just a ride; we’re your **neighbours**, your **go-to transport team**, and your **airport specialists**.

Unlike large taxi chains or impersonal ride-hailing apps, we take pride in offering a **personal touch**. From the moment you book until we drop you off at the terminal, we’re focused on one thing: making your journey smooth, safe, and stress-free.

Our regular clients — from busy professionals and retirees to families catching early flights — know they can rely on us for **punctuality**, **clean and comfortable vehicles**, and **drivers who genuinely care**.

Being locally owned and operated means we know the shortcuts, traffic patterns, and how to avoid delays — giving you peace of mind every time you travel.

---

## Final Thoughts: Make Your Next Transfer Easy

When it comes to catching a flight or arriving home after a long journey, the last thing you need is uncertainty. Choosing the right airport transfer from **{suburb}** isn’t just a matter of convenience — it’s about starting or ending your trip on the right note. 

With our **locally trusted, punctual, and customer-focused service**, you can relax knowing that every detail is handled. From the moment you book to the final drop-off at the terminal or your doorstep, we’re committed to providing a **seamless, stress-free experience** that fits your schedule and budget.

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

We hope this guide has helped you understand everything you need to know about travelling from {suburb} to either Avalon or Tullamarine. Our friendly team looks forward to welcoming you onboard!

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

