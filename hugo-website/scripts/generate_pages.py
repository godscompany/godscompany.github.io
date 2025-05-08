import yaml
import subprocess
from pathlib import Path

with open("data/suburbs.yaml") as f:
    suburbs = yaml.safe_load(f)

output_dir = Path("content/suburb")
output_dir.mkdir(parents=True, exist_ok=True)

template = """---
title: "Airport Transfer from {name} to Melbourne Airport"
slug: "{slug}"
name: "{name}"
description: "Book a reliable private airport transfer from {name} to Melbourne Airport. Fixed pricing, on-time service, professional drivers."
keywords:
  - "{name} airport transfer"
  - "{name} to Melbourne Airport"
  - "private cab from {name}"
  - "airport taxi in {name}"
  - "{name} to Avalon Airport"
  - "{name} taxi estimate"
---

## Why Choose Us for Your {name} Airport Transfers?

- Professional drivers with local knowledge
- On-time pickups and drop-offs
- Affordable shared or exclusive ride options

## Suburb Highlights

{highlights}

## Major Attractions in {name}

{attractions}

## Distance to Airports

- **Avalon Airport**: {distance_to_avalon} km
- **Tullamarine Airport**: {distance_to_tullamarine} km

## Fare Estimate

- **To Avalon Airport**: AUD ${avalon_min:.2f} – ${avalon_max:.2f}
- **To Tullamarine Airport**: AUD ${tulla_min:.2f} – ${tulla_max:.2f}

> *Note: Prices are estimates based on distance and vary by ride type (shared/private). Final quote available via [Get a Quote](https://laraairportservices.square.site/contact-us).*

[📅 Book Now](https://laraairportservices.square.site/s/appointments)

[✉️ Get a Quote](https://laraairportservices.square.site/contact-us)

---
"""

def format_list(lst):
    return "\n".join([f"- {item}" for item in lst])

for suburb in suburbs:
    # Fare estimates
    avalon_min = suburb['distance_to_avalon'] * 1.2 + 10
    avalon_max = suburb['distance_to_avalon'] * 2.4 + 10
    tulla_min = suburb['distance_to_tullamarine'] * 1.2 + 10
    tulla_max = suburb['distance_to_tullamarine'] * 2.4 + 10

    md = template.format(
        name=suburb["name"],
        slug=suburb["slug"],
        highlights=format_list(suburb["highlights"]),
        attractions=format_list(suburb["attractions"]),
        distance_to_avalon=suburb["distance_to_avalon"],
        distance_to_tullamarine=suburb["distance_to_tullamarine"],
        avalon_min=avalon_min,
        avalon_max=avalon_max,
        tulla_min=tulla_min,
        tulla_max=tulla_max
    )

    with open(output_dir / f"{suburb['slug']}.md", "w") as f:
        f.write(md)

# Run Hugo
try:
    subprocess.run(["hugo", "-D"], check=True)
    print("✅ Site generated successfully.")
except subprocess.CalledProcessError as e:
    print(f"❌ Error generating site: {e}")

