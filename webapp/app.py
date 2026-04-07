from flask import Flask, render_template, request, jsonify
from core.driver_setup import setup_driver
from core.handler import UniversalWebHandler
from core.phishing_detector import PhishingDetector

app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    url = data.get("url")

    driver = None  # ensure safe cleanup

    try:
        # 🔹 Setup driver
        driver = setup_driver()
        handler = UniversalWebHandler(driver)

        # 🔹 Open URL
        success = handler.open_url(url)
        if not success:
            return jsonify({"error": "Failed to open URL"})

        # 🔹 Run detection
        detector = PhishingDetector(handler)
        result = detector.run_all_checks()

        return jsonify(result)

    except Exception as e:
        return jsonify({
            "error": str(e)
        })

    finally:
        # 🔹 Always close driver
        if driver:
            driver.quit()


# 🔥 IMPORTANT: keep this (since you're running as module)
app.run(debug=True)