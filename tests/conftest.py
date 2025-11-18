import pytest
from playwright.sync_api import sync_playwright, Page

# Register step definitions globally for pytest-bdd
pytest_plugins = [
    'tests.step_defs.common_steps',
    'tests.step_defs.products_steps',
    'tests.step_defs.users_steps',
    'tests.step_defs.images_steps',
]

from tests.pages.products_page import ProductsPage
from tests.pages.users_page import UsersPage
from tests.pages.images_page import ImagesPage

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


@pytest.fixture(scope="session")
def products_page():
    return ProductsPage()


@pytest.fixture(scope="session")
def users_page():
    return UsersPage()


@pytest.fixture(scope="session")
def images_page():
    return ImagesPage()
