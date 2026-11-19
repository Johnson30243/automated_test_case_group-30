"""Generate representative arithmetic test inputs."""
from dataclasses import dataclass
from safe_expression import reference_result

@dataclass
class TestCase:
    test_id: str
    x: float
    y: float
    expected: object = None
    expected_error: str = ""

def generate_test_cases(expression):
    scenarios = [
        ("NORMAL", 8, 2), ("ZERO_X", 0, 5), ("ZERO_Y", 7, 0),
        ("NEGATIVE_X", -6, 3), ("BOTH_NEGATIVE", -4, -2),
        ("LARGE_VALUES", 100000, 250), ("DECIMAL_VALUES", 2.5, 0.5),
    ]
    cases = []
    for number, (label, x, y) in enumerate(scenarios, 1):
        try:
            expected = reference_result(expression, x, y)
            cases.append(TestCase(f"TC-{number:02d}-{label}", x, y, expected))
        except ZeroDivisionError:
            cases.append(TestCase(f"TC-{number:02d}-{label}", x, y, None, "ZeroDivisionError"))
        except (OverflowError, ArithmeticError) as exc:
            cases.append(TestCase(f"TC-{number:02d}-{label}", x, y, None, type(exc).__name__))
    return cases
