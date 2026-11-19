"""Generate demonstration login test scenarios."""
from dataclasses import dataclass

@dataclass(frozen=True)
class LoginTestCase:
    test_id: str
    scenario: str
    username: str
    password: str
    expected: str

def generate_login_test_cases():
    return [
        LoginTestCase("LG-01", "Valid username and password", "student", "DemoPass123!", "LOGIN SUCCESS"),
        LoginTestCase("LG-02", "Incorrect password", "student", "WrongPass123!", "LOGIN REJECTED"),
        LoginTestCase("LG-03", "Unknown username", "unknown_user", "DemoPass123!", "LOGIN REJECTED"),
        LoginTestCase("LG-04", "Empty username", "", "DemoPass123!", "VALIDATION ERROR"),
        LoginTestCase("LG-05", "Empty password", "student", "", "VALIDATION ERROR"),
        LoginTestCase("LG-06", "Both fields empty", "", "", "VALIDATION ERROR"),
        LoginTestCase("LG-07", "Incorrect username and password", "wrong_user", "WrongPass123!", "LOGIN REJECTED"),
    ]
