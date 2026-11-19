"""Local demonstration authentication only; not production security."""
DEMO_USERNAME = "student"
DEMO_PASSWORD = "DemoPass123!"

def authenticate(username: str, password: str) -> bool:
    if not isinstance(username, str) or not isinstance(password, str):
        return False
    if not username.strip() or not password:
        return False
    return username == DEMO_USERNAME and password == DEMO_PASSWORD
