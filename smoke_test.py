"""Run a quick command-line verification of the four test modules."""
from test_runner import run_tests
from login_test_runner import run_login_tests
from student_grading import run_grading_tests
from age_validation import run_age_tests

def check(name, rows):
    passed = sum(row["status"] == "PASS" for row in rows)
    failed = len(rows) - passed
    print(f"{name}: {passed}/{len(rows)} PASS, {failed} FAIL")
    for row in rows:
        if row["status"] != "PASS":
            print("  FAILED:", row)
    return failed == 0

if __name__ == "__main__":
    checks = [
        check("Arithmetic (x + y)", run_tests("x + y")),
        check("Login", run_login_tests()),
        check("Student grading", run_grading_tests()),
        check("Age validation", run_age_tests()),
    ]
    print("\nOVERALL:", "ALL CHECKS PASSED" if all(checks) else "SOME CHECKS FAILED")
    raise SystemExit(0 if all(checks) else 1)
