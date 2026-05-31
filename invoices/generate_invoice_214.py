import json, os, requests

items = [
    {"name": "16-05-2026 124 Wendover Cir", "quantity": 44, "unit_cost": 0.70},
    {"name": "16-05-2026 26 Lindale Ln", "quantity": 30, "unit_cost": 0.70},
    {"name": "16-05-2026 142 Forest View Dr", "quantity": 31, "unit_cost": 0.70},
    {"name": "16-05-2026 127 Wilbourn Dr", "quantity": 35, "unit_cost": 0.70},
    {"name": "16-05-2026 127 Wilbourn Dr _remove the piece of furniture in the living room & small piece of furniture in the smaller bedroom", "quantity": 5, "unit_cost": 0.50},
    {"name": "16-05-2026 770 Estate Lp", "quantity": 1, "unit_cost": 0.70},
    {"name": "19-05-2026 1452 Model Farm Rd", "quantity": 38, "unit_cost": 0.70},
    {"name": "19-05-2026 210 Creekview Ct", "quantity": 31, "unit_cost": 0.70},
    {"name": "19-05-2026 154 Lynhurst Dr", "quantity": 70, "unit_cost": 0.70},
    {"name": "19-05-2026 249 Colby Cir", "quantity": 38, "unit_cost": 0.70},
    {"name": "19-05-2026 249 Colby Cir _can you remove the RV from the front of the house", "quantity": 8, "unit_cost": 0.75},
    {"name": "19-05-2026 131 Berkshire Lp New", "quantity": 30, "unit_cost": 0.70},
    {"name": "20-05-2026 371 Storie Ave", "quantity": 30, "unit_cost": 0.70},
    {"name": "20-05-2026 159 Holly Tree Dr", "quantity": 45, "unit_cost": 0.70},
    {"name": "20-05-2026 188 Bent Tree Dr", "quantity": 34, "unit_cost": 0.70},
    {"name": "20-05-2026 188 Bent Tree Dr _remove the flag on the front of the house that's messed up", "quantity": 7, "unit_cost": 0.50},
    {"name": "20-05-2026 4455 Jonesville Hwy", "quantity": 49, "unit_cost": 0.70},
    {"name": "20-05-2026 598 Ted Brooks", "quantity": 54, "unit_cost": 0.70},
    {"name": "20-05-2026 30 Laurel Cir", "quantity": 19, "unit_cost": 0.70},
    {"name": "21-05-2026 502 Rector Rd", "quantity": 38, "unit_cost": 0.70},
    {"name": "21-05-2026 384 Woodgate Dr Exteriors", "quantity": 10, "unit_cost": 0.70},
    {"name": "21-05-2026 188 Davis St", "quantity": 28, "unit_cost": 0.70},
    {"name": "21-05-2026 35 Pineridge Ct", "quantity": 52, "unit_cost": 0.70},
    {"name": "22-05-2026 402 Charit Trl", "quantity": 80, "unit_cost": 0.70},
    {"name": "22-05-2026 402 Charit Trl _If you see any cats or dogs in the photos please remove them", "quantity": 5, "unit_cost": 0.50},
    {"name": "22-05-2026 3643 S York Hwy", "quantity": 34, "unit_cost": 0.70},
    {"name": "22-05-2026 3643 S York Hwy _Just remove the woman from the living room shot and her chair", "quantity": 1, "unit_cost": 1.00},
    {"name": "22-05-2026 1421 Taylor Place", "quantity": 37, "unit_cost": 0.70},
    {"name": "22-05-2026 163 Underpass Dr", "quantity": 42, "unit_cost": 0.70},
    {"name": "22-05-2026 89 Crockett Cir", "quantity": 34, "unit_cost": 0.70},
    {"name": "24-05-2026 231 Tuttle", "quantity": 40, "unit_cost": 0.70},
    {"name": "24-05-2026 231 Tuttle _remove the sign & the sprinkler sticking up and the tractors in the back yard", "quantity": 12, "unit_cost": 0.50},
    {"name": "24-05-2026 41 Hickory Cove Ln", "quantity": 35, "unit_cost": 0.70},
    {"name": "24-05-2026 30 Laurel Circle", "quantity": 32, "unit_cost": 0.70},
    {"name": "24-05-2026 8424 Cherokee Trl", "quantity": 16, "unit_cost": 0.70},
    {"name": "24-05-2026 1072 Belmont Dr", "quantity": 40, "unit_cost": 0.70},
    {"name": "25-05-2026 6911 Lindal Rd", "quantity": 47, "unit_cost": 0.70},
    {"name": "25-05-2026 315 Harper Village", "quantity": 37, "unit_cost": 0.70},
    {"name": "25-05-2026 130 Shubert St", "quantity": 36, "unit_cost": 0.70},
    {"name": "26-05-2026 239 Rotherham Dr", "quantity": 44, "unit_cost": 0.70},
    {"name": "26-05-2026 197 Markham New Photos", "quantity": 10, "unit_cost": 0.70},
    {"name": "26-05-2026 809 Buffalo Trl", "quantity": 45, "unit_cost": 0.70},
    {"name": "26-05-2026 1 Eagle Bluff Lots", "quantity": 34, "unit_cost": 0.70},
    {"name": "26-05-2026 100 S Ridge Ave", "quantity": 44, "unit_cost": 0.70},
    {"name": "27-05-2026 82 Hwy 70 E", "quantity": 19, "unit_cost": 0.70},
    {"name": "27-05-2026 8429 Hwy 127 S Cover Photo", "quantity": 1, "unit_cost": 0.70},
    {"name": "27-05-2026 8424 Cherokee Trl Interiors", "quantity": 28, "unit_cost": 0.70},
    {"name": "27-05-2026 1019 Taylors Chapel", "quantity": 6, "unit_cost": 0.70},
    {"name": "27-05-2026 116 Joe Voiles", "quantity": 12, "unit_cost": 0.70},
    {"name": "27-05-2026 538 Harding Rd", "quantity": 31, "unit_cost": 0.70},
    {"name": "28-05-2026 134 Lakeside Dr", "quantity": 35, "unit_cost": 0.70},
    {"name": "28-05-2026 3070 Nocatee Trace", "quantity": 45, "unit_cost": 0.70},
]

payload = {
    "from": "Creative Estates",
    "to": "Allen Hall Photography",
    "number": "214",
    "date": "June 1, 2026",
    "payment_terms": "PayPal",
    "items": items,
    "fields": {"tax": "%"},
    "tax": 7.5,
    "notes": "Its really great working with you. We are looking forward to continuing with more services.",
    "terms": "Invoice included the PayPal and cross border charges.",
    "currency": "USD"
}

api_key = os.environ.get("INVOICE_API_KEY", "sk_OuwFKmA6rklfHfzyTMuqyN4eR8MEck5H")
output_dir = os.environ.get("OUTPUT_DIR", os.path.join(os.path.dirname(__file__), "output"))
os.makedirs(output_dir, exist_ok=True)

response = requests.post(
    "https://invoice-generator.com",
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    },
    json=payload
)

filename = "Invoice_214_Allen_Hall_May2ndHalf.pdf"
if response.status_code == 200:
    out_path = os.path.join(output_dir, filename)
    with open(out_path, "wb") as f:
        f.write(response.content)
    print(f"✅ Invoice saved: {out_path}")
else:
    print(f"❌ Error {response.status_code}: {response.text}")
