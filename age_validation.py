"""Age eligibility validation and test-case generation."""
MINIMUM_AGE = 18
MAXIMUM_AGE = 120

def validate_age(age):
    if isinstance(age, bool) or not isinstance(age, int):
        return "VALIDATION ERROR"
    if age < 0 or age > MAXIMUM_AGE:
        return "INVALID AGE"
    if age >= MINIMUM_AGE:
        return "ELIGIBLE"
    return "NOT ELIGIBLE"

def generate_age_test_cases():
    return [
        ("AG-01", "Adult age", 25, "ELIGIBLE"),
        ("AG-02", "Minimum eligible age", 18, "ELIGIBLE"),
        ("AG-03", "Below eligible age", 17, "NOT ELIGIBLE"),
        ("AG-04", "Young age", 10, "NOT ELIGIBLE"),
        ("AG-05", "Zero age", 0, "NOT ELIGIBLE"),
        ("AG-06", "Negative age", -5, "INVALID AGE"),
        ("AG-07", "Above maximum age", 200, "INVALID AGE"),
        ("AG-08", "Decimal age", 18.5, "VALIDATION ERROR"),
        ("AG-09", "Text input", "abc", "VALIDATION ERROR"),
        ("AG-10", "Empty input", "", "VALIDATION ERROR"),
    ]

def run_age_tests():
    results = []
    for test_id, scenario, age, expected in generate_age_test_cases():
        try:
            value = int(age) if isinstance(age, str) and age.strip() else age
            actual = validate_age(value)
        except (TypeError, ValueError):
            actual = "VALIDATION ERROR"
        results.append({"id": test_id, "scenario": scenario, "input": str(age) if age != "" else "(empty)", "expected": expected, "actual": actual, "status": "PASS" if actual == expected else "FAIL"})
    return results
