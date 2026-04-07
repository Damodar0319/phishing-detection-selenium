import re
from urllib.parse import urlparse


class URLDetector:

    def __init__(self, url):
        self.url = url
        self.parsed = urlparse(url)

    def analyze_url(self):
        url = self.url
        domain = self.parsed.netloc

        suspicious_keywords = ["login", "secure", "verify", "account", "bank"]

        features = {
            "long_url": len(url) > 75,
            "has_ip": bool(re.match(r"\d+\.\d+\.\d+\.\d+", domain)),
            "has_at_symbol": "@" in url,
            "has_hyphen": "-" in domain,
            "too_many_subdomains": domain.count('.') > 3,
            "no_https": not url.startswith("https"),
            "has_suspicious_words": any(word in url.lower() for word in suspicious_keywords),
            "has_suspicious_tld": any(tld in domain for tld in [".xyz", ".info", ".tk"])
        }

        return features

    def get_url_score(self):
        f = self.analyze_url()
        score = 0
        reasons = []

        # 🔥 STRONG signals
        if f["has_ip"]:
            score += 7
            reasons.append("URL uses IP address instead of domain")

        if f["has_at_symbol"]:
            score += 6
            reasons.append("URL contains '@' symbol")

        if f["too_many_subdomains"]:
            score += 3
            reasons.append("Too many subdomains in URL")

        if f["no_https"]:
            score += 3
            reasons.append("Website is not using HTTPS")

        if f["has_suspicious_tld"]:
            score += 3
            reasons.append("Suspicious domain extension used")

        # 🔻 weaker signals
        if f["long_url"]:
            score += 1
            reasons.append("URL is unusually long")

        if f["has_suspicious_words"]:
            score += 2
            reasons.append("Suspicious keywords found in URL")

        # 🔹 KEEP ORIGINAL RETURN (no break)
        return score, f

    # 🔥 NEW (optional, future use)
    def get_detailed_result(self):
        f = self.analyze_url()
        score = 0
        reasons = []

        if f["has_ip"]:
            score += 7
            reasons.append("URL uses IP address instead of domain")

        if f["has_at_symbol"]:
            score += 6
            reasons.append("URL contains '@' symbol")

        if f["too_many_subdomains"]:
            score += 3
            reasons.append("Too many subdomains in URL")

        if f["no_https"]:
            score += 3
            reasons.append("Website is not using HTTPS")

        if f["has_suspicious_tld"]:
            score += 3
            reasons.append("Suspicious domain extension used")

        if f["long_url"]:
            score += 1
            reasons.append("URL is unusually long")

        if f["has_suspicious_words"]:
            score += 2
            reasons.append("Suspicious keywords found in URL")

        return {
            "score": score,
            "reasons": reasons,
            "features": f
        }