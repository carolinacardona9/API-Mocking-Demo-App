"""Common step definitions for all features"""
from pytest_bdd import given, when, then, parsers
from playwright.sync_api import Route, expect
import pytest


@given("the application is running")
def application_running(browser_page, base_url):
    browser_page.goto(base_url)
    expect(browser_page.locator('h1')).to_contain_text('Demo Playwright Mocking')


@given(parsers.parse("I navigate to the {page_name} page"))
def navigate_to_page(browser_page, base_url, page_name):
    page_map = {
        "users": "/users",
        "products": "/products",
        "images": "/images"
    }
    url = f"{base_url}{page_map.get(page_name.lower(), f'/{page_name}')}"
    browser_page.goto(url)


@when("the page loads")
def page_loads(browser_page):
    browser_page.wait_for_load_state("networkidle")

