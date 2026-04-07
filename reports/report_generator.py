class ReportGenerator:
    def __init__(self, url, features, score, classification, extra_reasons=None):
        self.url = url
        self.features = features
        self.score = score
        self.classification = classification
        self.extra_reasons = extra_reasons or []

    def generate(self):
        return {
            "url": self.url,
            "classification": self.classification,
            "score": round(self.score, 2),
            "details": self._generate_details()
        }

    def _generate_details(self):
        reasons = []

        # 🔹 Feature-based explanations (your original logic)
        for feature, value in self.features.items():
            if value:
                explanation = self._explain_feature(feature)
                if explanation:
                    reasons.append(explanation)

        # 🔹 Add extra reasons (from heuristic engine or detectors)
        for reason in self.extra_reasons:
            if reason not in reasons:
                reasons.append(reason)

        # 🔹 If no issues found
        if not reasons:
            reasons.append("No suspicious indicators detected")

        return reasons

    def _explain_feature(self, feature):
        explanations = {
            # 🔗 URL FEATURES
            "long_url": "URL is unusually long (possible obfuscation)",
            "has_ip": "URL uses IP address instead of domain",
            "has_at_symbol": "URL contains '@' symbol (redirect trick)",
            "has_hyphen": "Domain contains hyphen (common in phishing)",
            "too_many_subdomains": "Too many subdomains detected",
            "no_https": "Website is not using HTTPS",
            "has_suspicious_words": "Suspicious keywords found in URL",
            "has_suspicious_tld": "Suspicious domain extension used",

            # 🌐 DOM FEATURES
            "has_iframe": "Page contains iframe (can be used for phishing overlays)",
            "has_hidden_elements": "Hidden elements detected (possible malicious intent)",
            "suspicious_scripts": "Suspicious JavaScript detected",

            # 🔗 LINK FEATURES
            "many_external_links": "Page contains many external links",
            "anchor_mismatch": "Mismatch between link text and actual URL",

            # 📝 FORM FEATURES
            "has_password_field": "Login form detected (possible phishing target)",
            "external_form_action": "Form submits data to external domain",
            "multiple_forms": "Multiple forms detected (unusual behavior)",

            # ⚠️ SYSTEM FEATURES
            "unreachable": "Website could not be reached (inactive or suspicious domain)"
        }

        return explanations.get(feature)