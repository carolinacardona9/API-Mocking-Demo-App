"""Step definitions for products feature"""
from pytest_bdd import given, when, then, parsers
from playwright.sync_api import expect
from tests.helpers.route_helpers import setup_low_stock_route, setup_delayed_products_route
from pages.products_page import ProductsPage


@given("I mock the API to return products with different stock levels")
def mock_products_stock(browser_page):
    setup_low_stock_route(browser_page)


@given(parsers.parse("I mock the API to have a delay of {seconds:d} seconds"))
def mock_api_delay(browser_page, seconds):
    setup_delayed_products_route(browser_page, seconds)


@given("I navigate to the products page")
@when("I navigate to the products page")
def navigate_products_page(browser_page, base_url, products_page: ProductsPage):
    browser_page.locator(products_page.products_tab_locator).click()
    


@then("I should see products with correct stock background colors")
def verify_stock_colors(browser_page, datatable, products_page: ProductsPage):
    browser_page.locator(products_page.products_tab_locator).click()
    expect(browser_page.locator(products_page.products_grid_container)).to_be_visible()
    stock_cells = browser_page.locator(products_page.stock_column_cells).all()
    assert len(stock_cells) > 0, "No records were found on the grid"
    # Create color map from datatable
    color_map = {}
    for row in datatable:
        stock_range = row['Stock Range']
        if '-' in stock_range:
            color_map[stock_range] = row['Color']
    for cell in stock_cells:
        cell_text = cell.text_content().strip()
        try:
            value = int(cell_text)
        except ValueError:
            raise AssertionError(f"Value '{cell_text}' is not a valid number")
        expected_color = None
        if value < 10:
            expected_color = color_map.get('0-9')
        elif value < 50:
            expected_color = color_map.get('10-49')
        else:
            expected_color = color_map.get('50+')
        if expected_color:
            expect(cell).to_have_css('background-color', expected_color)


@then("I should see a loading spinner")
def see_loading_spinner(browser_page, products_page: ProductsPage):
    browser_page.wait_for_selector(products_page.products_grid_container, state='visible', timeout=5000)
    spinner = browser_page.locator(products_page.loading_spinner).first
    expect(spinner).to_be_visible(timeout=5000)


@then("the grid should eventually load")
def grid_loads(browser_page, products_page: ProductsPage):
    expect(browser_page.locator(products_page.grid_rows)).to_be_visible(timeout=15000)