import pytest
from playwright.sync_api import sync_playwright, Page


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="local",
        choices=["local", "prod"],
        help="Environment to run tests against"
    )
    parser.addoption(
        "--slow-mo",
        action="store",
        type=int,
        default=0,
        help="Slow down Playwright operations by specified milliseconds"
    )


@pytest.fixture(scope="session")
def base_url(request):
    """Base URL for the application"""
    env = request.config.getoption("--env")
    urls = {
        "local": "http://localhost:4200",
        "prod": "https://api-mocking-demo-app.netlify.app"
    }
    return urls[env]


@pytest.fixture(scope="session")
def playwright():
    """Playwright instance for the test session"""
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="function")
def browser_page(playwright, request):
    """Browser page fixture for each test"""
    slow_mo = request.config.getoption("--slow-mo")
    browser = playwright.chromium.launch(headless=False, slow_mo=slow_mo)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()
