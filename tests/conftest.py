import pytest
from playwright.sync_api import Playwright


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="prod",
        choices=["local", "prod"]
    )

@pytest.fixture(scope="session")
def base_url(request):
    env = request.config.getoption("--env")
    urls = {
        "local": "http://localhost:4200",
        "prod": "https://api-mocking-demo-app.netlify.app"
    }
    return urls[env]


@pytest.fixture(scope="function")
def browser_page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()
