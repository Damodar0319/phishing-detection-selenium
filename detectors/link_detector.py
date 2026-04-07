from selenium.webdriver.common.by import By
from urllib.parse import urlparse


class LinkDetector:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.base_domain = urlparse(base_url).netloc

    def extract_links(self):
        elements = self.driver.find_elements(By.TAG_NAME, "a")

        links = []
        for el in elements:
            href = el.get_attribute("href")
            if href:
                links.append(href)

        return links

    def analyze_links(self):
        elements = self.driver.find_elements(By.TAG_NAME, "a")

        internal = 0
        external = 0
        suspicious = 0
        anchor_mismatch = 0
        empty_links = 0

        for el in elements:
            href = el.get_attribute("href")
            text = el.text.strip()

            if not href:
                empty_links += 1
                suspicious += 1
                continue

            if href.startswith("#") or href.startswith("javascript"):
                empty_links += 1
                suspicious += 1
                continue

            parsed = urlparse(href)

            if self.base_domain in parsed.netloc:
                internal += 1
            else:
                external += 1

            if text and parsed.netloc not in text:
                anchor_mismatch += 1

        total = len(elements) if elements else 1

        return {
            "total_links": total,
            "internal": internal,
            "external": external,
            "suspicious": suspicious,
            "anchor_mismatch": anchor_mismatch,
            "empty_links": empty_links,
            "external_ratio": external / total
        }

    def get_link_score(self):
        data = self.analyze_links()
        score = 0
        reasons = []

        if data["external_ratio"] > 0.8:
            score += 1
            reasons.append("High number of external links")

        if data["anchor_mismatch"] > 10:
            score += 2
            reasons.append("Many anchor text mismatches")

        if data["empty_links"] > 10:
            score += 1
            reasons.append("Many empty or JavaScript links detected")

        # 🔹 KEEP ORIGINAL RETURN (no break)
        return score, data

    # 🔥 NEW (optional, future use)
    def get_detailed_result(self):
        data = self.analyze_links()
        score = 0
        reasons = []

        if data["external_ratio"] > 0.8:
            score += 1
            reasons.append("High number of external links")

        if data["anchor_mismatch"] > 10:
            score += 2
            reasons.append("Many anchor text mismatches")

        if data["empty_links"] > 10:
            score += 1
            reasons.append("Many empty or JavaScript links detected")

        return {
            "score": score,
            "reasons": reasons,
            "data": data
        }