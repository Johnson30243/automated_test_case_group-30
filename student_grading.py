"""Student score validation and grading test generation."""

def grade_score(score):
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        return "VALIDATION ERROR"
    if score < 0 or score > 100:
        return "INVALID SCORE"
    if score >= 70: return "A"
    if score >= 60: return "B"
    if score >= 50: return "C"
    if score >= 45: return "D"
    if score >= 40: return "E"
    return "F"

def generate_grading_test_cases():
    scenarios = [
        ("GR-01", "Excellent score", 85, "A"),
        ("GR-02", "A lower boundary", 70, "A"),
        ("GR-03", "B grade", 65, "B"),
        ("GR-04", "C grade", 55, "C"),
        ("GR-05", "D grade", 47, "D"),
        ("GR-06", "E grade", 42, "E"),
        ("GR-07", "Failing score", 25, "F"),
        ("GR-08", "Minimum valid score", 0, "F"),
        ("GR-09", "Maximum valid score", 100, "A"),
        ("GR-10", "Score above maximum", 105, "INVALID SCORE"),
        ("GR-11", "Negative score", -5, "INVALID SCORE"),
        ("GR-12", "Decimal score", 59.5, "C"),
        ("GR-13", "Text input", "abc", "VALIDATION ERROR"),
        ("GR-14", "Empty input", "", "VALIDATION ERROR"),
    ]
    return scenarios

def run_grading_tests():
    results = []
    for test_id, scenario, score, expected in generate_grading_test_cases():
        try:
            value = float(score) if isinstance(score, str) and score.strip() else score
            actual = grade_score(value)
        except (TypeError, ValueError):
            actual = "VALIDATION ERROR"
        results.append({"id": test_id, "scenario": scenario, "input": str(score) if score != "" else "(empty)", "expected": expected, "actual": actual, "status": "PASS" if actual == expected else "FAIL"})
    return results
