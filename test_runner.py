"""Execute arithmetic test cases and evaluate their outcomes."""
import math
from safe_expression import evaluate_expression
from test_generator import generate_test_cases

def run_tests(expression):
    results = []
    for case in generate_test_cases(expression):
        try:
            actual = evaluate_expression(expression, case.x, case.y)
            if case.expected_error:
                passed = False
                actual_text = f"Returned {actual!r}; expected {case.expected_error}"
            else:
                passed = math.isclose(actual, case.expected, rel_tol=1e-9, abs_tol=1e-9) if isinstance(actual, (int, float)) and isinstance(case.expected, (int, float)) else actual == case.expected
                actual_text = repr(actual)
        except Exception as exc:
            passed = case.expected_error == type(exc).__name__
            actual_text = f"{type(exc).__name__}: {exc}"
        results.append({"id": case.test_id, "input": f"x={case.x}, y={case.y}", "expected": case.expected_error or repr(case.expected), "actual": actual_text, "status": "PASS" if passed else "FAIL"})
    return results
