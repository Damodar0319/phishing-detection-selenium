class HeuristicEngine:
    def __init__(self, detectors):
        """
        detectors: list of dicts → {"name": str, "result": tuple/dict}
        """
        self.detectors = detectors

    def analyze(self):
        total_score = 0
        all_reasons = []
        details = {}

        for detector in self.detectors:
            name = detector["name"]
            result = detector["result"]

            # 🔹 Handle BOTH old and new formats
            if isinstance(result, tuple):
                score = result[0]
                reasons = []
            elif isinstance(result, dict):
                score = result.get("score", 0)
                reasons = result.get("reasons", [])
            else:
                score = 0
                reasons = []

            total_score += score
            all_reasons.extend(reasons)

            details[name] = {
                "score": score,
                "reasons": reasons
            }

        verdict = self._get_verdict(total_score)
        risk_level = self._get_risk_level(total_score)
        confidence = self._get_confidence(total_score)

        return {
            "total_score": round(total_score, 2),
            "verdict": verdict,
            "risk_level": risk_level,
            "confidence": confidence,
            "reasons": all_reasons,
            "details": details
        }

    def _get_verdict(self, score):
        if score >= 10:
            return "Phishing"
        elif score >= 7:
            return "High Risk"
        elif score >= 4:
            return "Suspicious"
        else:
            return "Safe"

    def _get_risk_level(self, score):
        if score >= 10:
            return "CRITICAL"
        elif score >= 7:
            return "HIGH"
        elif score >= 4:
            return "MEDIUM"
        else:
            return "LOW"

    def _get_confidence(self, score):
        return round(min(score / 10, 1.0), 2)