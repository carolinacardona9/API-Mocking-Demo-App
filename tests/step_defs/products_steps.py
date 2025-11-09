"""Step definitions for products feature"""
from pytest_bdd import given, when, then, parsers
from playwright.sync_api import expect
from tests.helpers.route_helpers import setup_low_stock_route, setup_delayed_products_route


@given("I mock the API to return products with different stock levels")
def mock_products_stock(browser_page):
    setup_low_stock_route(browser_page)


@given(parsers.parse("I mock the API to have a delay of {seconds:d} seconds"))
def mock_api_delay(browser_page, seconds):
    setup_delayed_products_route(browser_page, seconds)


@given("I navigate to the products page")
@when("I navigate to the products page")
def navigate_products_page(browser_page, base_url):
    browser_page.locator("//a[@href='/products']").click()


@then("I should see products with correct stock background colors")
def verify_stock_colors(browser_page, datatable):
    browser_page.locator("//a[@href='/products']").click()
    expect(browser_page.locator('div.grid-container')).to_be_visible()
    stock_cells = browser_page.locator('.ag-cell[col-id="stock"]').all()
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
def see_loading_spinner(browser_page):
    browser_page.wait_for_selector('div.grid-container', state='visible', timeout=5000)
    spinner = browser_page.locator('app-spinner, .spinner-container').first
    expect(spinner).to_be_visible(timeout=5000)


@then("the grid should eventually load")
def grid_loads(browser_page):
    expect(browser_page.locator('//div[@role="row"]')).to_be_visible(timeout=15000)