import io
import os
import requests
from flask import Flask, jsonify, render_template, request, send_file

app = Flask(__name__)

LOGOS = {
    "Creative Estates": "https://raw.githubusercontent.com/TheBrainCord/Dev/main/invoices/logos/creative_estates.jpg",
    "Sunlight Designings": None,
}

API_KEY = os.environ.get("INVOICE_API_KEY", "")


@app.route("/")
def index():
    return render_template("index.html", companies=list(LOGOS.keys()))


@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    from_company = data.get("from_company", "Creative Estates")

    payload = {
        "from": from_company,
        "to": data["to"],
        "number": data["number"],
        "date": data["date"],
        "payment_terms": data.get("payment_terms", "PayPal"),
        "items": data["items"],
        "fields": {"tax": "%"},
        "tax": float(data.get("tax", 0)),
        "notes": data.get("notes", ""),
        "terms": data.get("terms", ""),
        "currency": "USD",
    }

    logo = LOGOS.get(from_company)
    if logo:
        payload["logo"] = logo

    response = requests.post(
        "https://invoice-generator.com",
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"},
        json=payload,
        timeout=30,
    )

    if response.status_code == 200:
        filename = f"Invoice_{data['number']}_{data['to'].replace(' ', '_')}.pdf"
        return send_file(
            io.BytesIO(response.content),
            mimetype="application/pdf",
            as_attachment=True,
            download_name=filename,
        )

    return jsonify({"error": response.text}), response.status_code


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
