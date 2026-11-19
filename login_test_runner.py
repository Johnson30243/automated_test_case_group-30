"""Execute generated login test scenarios."""
from login_auth import authenticate
from login_test_generator import generate_login_test_cases

def run_login_tests():
    results = []
    for case in generate_login_test_cases():
        if not case.username.strip() or not case.password:
            actual = "VALIDATION ERROR"
        elif authenticate(case.username, case.password):
            actual = "LOGIN SUCCESS"
        else:
            actual = "LOGIN REJECTED"
        results.append({"id": case.test_id, "scenario": case.scenario, "username": case.username or "(empty)", "expected": case.expected, "actual": actual, "status": "PASS" if actual == case.expected else "FAIL"})
    return results
