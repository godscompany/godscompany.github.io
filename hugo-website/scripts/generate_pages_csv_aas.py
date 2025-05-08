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
        "Melbourne private transfer", "airport transport services Melbourne",
        f"{suburb} to Avalon Airport taxi", f"Avalon Airport ride from {suburb}",
        f"Avalon Airport private car {suburb}", f"Avalon shuttle from {suburb}",
        f"cheap Avalon Airport transfer", f"Avalon Airport pickup service {suburb}",
        f"{suburb} to Avalon shuttle service", "Avalon Airport transport Geelong",
        "reliable Avalon Airport transfers", "book Avalon Airport taxi online",
        "24/7 Avalon Airport transfer", "Avalon Airport door-to-door service"
    ]

    meta_keywords = ', '.join(keywords)

    front_matter = f"""---
title: "Avalon Airport Transfers from {suburb}, {state}"
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

Getting to your flight on time from **{suburb}** has never been more convenient. Whether you're heading out for a quick weekend getaway, a business trip, or an international vacation, our professional **airport transfer services** are designed to ensure your journey to the airport is smooth, punctual, and completely hassle-free.

You’re well-positioned between two major airports:

- **Avalon Airport** – Just **{dist_avalon} km** from **{suburb}**, Avalon is the go-to option for many regional and domestic flights. With lower foot traffic and quicker check-ins, it’s perfect for those who prefer a more relaxed airport experience. Our dedicated **Avalon Airport transfers from {suburb}** are fast, reliable, and always on time.
  
- **Melbourne Tullamarine Airport** – Located about **{dist_tulla} km** away, Melbourne Airport (Tullamarine) is the main international gateway in Victoria. Whether you're flying across the country or across the globe, we’ve got you covered with **door-to-door transfers** from **{suburb} to Tullamarine Airport**.

We offer tailored ride options for every budget and travel style:

- **Shared Ride Services** – Travel affordably with others going the same way. Our shared shuttles are budget-friendly, starting at just **${price_min}**, and are ideal for solo travellers or those looking to save on transport costs.
  
- **Private Transfers** – For maximum comfort and convenience, book a private car or van. This premium service suits families, groups, or professionals who value privacy and direct routes, with prices up to **${price_max}**, depending on your chosen vehicle and time.

All transfers come with:

- **Transparent pricing** — No surprises or hidden fees.
- **Professional local drivers** — Friendly, punctual, and familiar with {suburb}'s streets.
- **Comfortable, modern vehicles** — Clean, spacious, and well-maintained.
- **24/7 availability** — Early morning flights or late-night arrivals, we’re here whenever you need us.

By booking your **Avalon Airport transfer from {suburb}** with us, you're choosing peace of mind, convenience, and a trusted service that values your time. Let us take the stress out of your airport commute so you can start your journey the right way.

---

## What Makes **{suburb}** Truly Special?

{attractions}

But there’s so much more to **{suburb}** than its standout attractions. It’s the kind of place where community matters — where the local bakery remembers your order, where weekends are spent by the creek with family, and where neighbours wave from their front lawns. The streets are filled with character, and the vibe is laid-back but full of heart. Whether you're new to the area or a lifelong resident, there’s a rhythm to life here that makes every day a little brighter.

At our core, we understand that getting to the airport isn't just about logistics — it’s about maintaining the comfort and flow of your life, even when you're on the move. That’s why we provide more than just a lift to Avalon Airport or Melbourne Tullamarine. We offer a **personalised, community-rooted transfer experience** that begins at your doorstep in **{suburb}** and ends with you arriving safely and on time, ready for your next chapter.

Our Avalon Airport transfer service is ideal for those quick regional flights or weekend getaways. With **{dist_avalon} km** between you and the terminal, it’s a short journey — and with us, it’s a smooth one. Whether it’s a shared ride for a solo traveller or a private transfer for your family, our goal is to make the journey feel effortless, reliable, and pleasant from beginning to end.

---

## Why Our Airport Transfers Are Perfect for You

### 🚘 Stress-Free Pickups and Drop-offs
Our experienced drivers live and work around **{suburb}**, so they know every turn, traffic light, and scenic shortcut. That means **no GPS mishaps or wrong addresses** — just smooth, door-to-door service every time.

### 💼 Business or Leisure, We’ve Got You Covered
Travelling for work? Catching a last-minute flight? Going on a long-awaited family vacation? Whatever the reason, we’ll tailor our airport transport to suit your needs, timeframe, and comfort level.

### 💲 Clear, Honest, and Competitive Pricing
We keep things transparent — no surge pricing, no fine print. Our rates are calculated by distance and travel type, with shared rides offering a **budget-conscious** solution and private options giving you **total control and comfort**. You’ll always know what you’re paying for, and we guarantee excellent value every time.

---

By pairing the warmth of **{suburb}** with a trusted airport transfer service, we’re helping locals stay connected — to business opportunities, family reunions, spontaneous trips, and everything in between. Book your Avalon Airport ride today and experience how effortless travel can really be.


## Tips for Travelling from {suburb} to Avalon Airport

Planning ahead can make a world of difference when catching a flight — especially from a suburb like **{suburb}**, where you’re within easy reach of both Avalon and Tullamarine airports. Here are our top tips to make your airport journey smooth and stress-free:

- **Book Early** – Avalon Airport may be smaller than Tullamarine, but it still gets busy during weekends, school holidays, and special events. Booking in advance ensures you get your preferred time slot and vehicle.
- **Double-Check Your Terminal** – While Avalon is compact and easy to navigate, knowing your airline's terminal helps speed things up and reduces stress. For Tullamarine, this is especially important due to multiple terminals and traffic congestion.
- **Leave Some Buffer Time** – Avalon Airport is known for its shorter queues and smoother check-ins, but it's still smart to plan ahead. We recommend leaving **at least 2 hours** before a domestic flight.
- **Travel Light or Let Us Know** – Carrying sporting equipment, prams, or extra luggage? Let us know at the time of booking. We'll make sure the right vehicle is dispatched and you’re not squeezed for space.
- **Consider Off-Peak Travel** – If your schedule allows, travelling outside peak hours means quicker road travel and a more relaxed airport experience — especially helpful for Avalon, which has limited peak-period access routes.

---

## Frequently Asked Questions (FAQs)

**Q: Can I share the ride with others to save money?**  
**A:** Yes, definitely! We offer a convenient **shared ride service** designed for passengers who don’t mind traveling with others and want to reduce costs. It’s a great option for solo travellers, students, or anyone looking to save without compromising comfort. You’ll still enjoy a timely and relaxing ride — just at a lower price.

**Q: Are your drivers local to the area?**  
**A:** Absolutely. Our drivers live and work in the region, so they know the local roads, traffic patterns, and shortcuts extremely well. Whether it’s peak hour or an early morning pickup, their local knowledge ensures **fast, reliable, and smooth travel** — no unnecessary delays, no missed turns.

**Q: Can I book last-minute or on short notice?**  
**A:** We understand that travel plans can change in an instant. That’s why we do our best to accommodate **last-minute bookings**. If you need a transfer on short notice, simply give us a call or book through our online portal using the link below — and we’ll do everything we can to get you on your way quickly and stress-free.

**Q: How far is Avalon Airport from {suburb}?**  
**A:** Avalon Airport is approximately **{dist_avalon} km** from **{suburb}**, making it a popular choice for travellers in the area. With lighter traffic and quicker check-ins than larger airports, it's often the **faster, more convenient option** — especially with our direct transfer services.

**Q: Can I choose between shared and private rides?**  
**A:** Yes! We provide both **shared rides** (for affordability and sustainability) and **private transfers** (for comfort, privacy, and flexibility). Simply select your preference during booking, and we’ll handle the rest.

---


## Trusted by Locals – The Heart of Our Service

When it comes to airport transfers, **reliability and reputation** are everything. Our service is proudly trusted by residents of **{suburb}, {city}**, and the wider region for one simple reason: we deliver consistent, friendly, and professional transport — every single time.

From early morning flights to late-night arrivals, we’ve been the first choice for:

- **Local families heading off on holiday**
- **Executives catching red-eye business flights**
- **University students flying home during semester breaks**
- **Senior travellers who value a helping hand and a safe, courteous ride**

Our drivers aren't just operators — they’re part of the **local community**, familiar faces who understand the rhythms of life in **{suburb}**. We know the **fastest routes**, the **busiest traffic times**, and how to **get you to Avalon or Tullamarine on time and stress-free**.

Unlike anonymous ride-share apps or rigid shuttle services, we tailor each ride to your needs. Need an extra stop to pick up a family member? Travelling with a pet or special luggage? Just let us know. **We listen, we adapt, and we deliver.**

---

## Final Thoughts – Why Locals Keep Choosing Us

Flying out of Avalon Airport should be easy — and with us, it is.

Whether it’s your first time booking an airport transfer from **{suburb}**, or you’re a long-time customer, our team is here to make every journey seamless. We combine:

- **Local knowledge**
- **Affordable pricing**
- **Flexible ride options**
- **Genuine customer service**

…to bring you a level of care and consistency that big-name companies simply can’t match.

Don’t risk delays, confusion, or impersonal service. With us, **you’re not just a booking — you’re a valued passenger**.

Ready to ride? **Book now** or **get a quote online**, and let’s make your airport journey the easiest part of your travel day.

---

[📅 **Book Your Airport Ride Now**]({booking_link})  
[📧 **Request a Quick Quote**]({quote_link})

---

## SEO Keywords Used

To help travellers like you find our services easily online, we’ve strategically included popular search terms that people use when booking airport transfers from **{suburb}**. These SEO-friendly keywords are chosen to reflect exactly what locals and visitors are looking for — from private airport cars and luxury transfers to affordable shuttles and shared rides to **Avalon** and **Tullamarine Airport**.

So whether you're searching for a **Geelong-based Avalon airport shuttle**, a **chauffeur transfer to Melbourne Airport**, or simply the **best airport ride service from {suburb}**, we've made sure you’ll find us when it matters most.

### Commonly Searched Keywords:
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
- **Avalon Airport Transfers Geelong**
- **Melbourne Airport Shuttle Booking**
- **Pre-booked Airport Taxi {suburb}**
- **Low-cost Airport Transfer Victoria**

---

## Ready to Ride? Let’s Get You There

We hope this guide has helped you understand everything you need to know about travelling from **{suburb}** to either **Avalon** or **Tullamarine Airport**. Whether you're heading out on a long-awaited holiday, a business trip, or just picking up a loved one, our airport transfer service is here to make the journey smooth and stress-free.

From door-to-door pickups and friendly drivers to affordable pricing and flexible scheduling, we’re proud to offer a travel experience you can count on — every single time.

Our friendly local team is always just a message or call away. **We look forward to welcoming you onboard and helping you start your trip the right way — relaxed, on time, and with peace of mind.**

👉 **Book your airport transfer now** and discover why travellers from **{suburb}** choose us as their go-to airport transport partner.

---

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

