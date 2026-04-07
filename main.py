import csv
import os
from core.driver_setup import setup_driver
from core.handler import WebDriverHandler
from core.phishing_detector import PhishingDetector


def analyze_website(url):
    driver = setup_driver()
    handler = WebDriverHandler(driver, url)

    try:
        handler.open()

        detector = PhishingDetector(handler)
        result = detector.run_all_checks()

        driver.quit()
        return result

    except Exception as e:
        driver.quit()
        return {
            "url": url,
            "error": str(e),
            "verdict": "Error",
            "final_score": 0
        }


def run_bulk_scan(file_name):
    results = []

    # 🔥 Safe path handling
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "data", file_name)

    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return []

    with open(file_path, newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            url = row.get("url")

            if not url:
                continue

            print(f"\n🔍 Scanning: {url}")

            result = analyze_website(url)

            if result:
                results.append(result)

                print("Verdict:", result.get("verdict"))
                print("Score:", result.get("final_score"))
                print("Confidence:", result.get("confidence"))

    return results


if __name__ == "__main__":
    # 🔹 Single URL test
    test_url = "https://example.com"
    result = analyze_website(test_url)

    print("\n=== SINGLE URL RESULT ===")
    print(result)

    # 🔹 Bulk scan (uncomment to use)
    # results = run_bulk_scan("test_urls.csv")