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
def verify_stock_colors(browser_page):
    """Verify products have correct stock background colors based on stock levels"""
    LOW_STOCK_THRESHOLD = 10
    WARNING_STOCK_THRESHOLD = 50
    
    def get_expected_color(stock_value: int) -> str:
        """Get expected color based on stock value"""
        if stock_value < LOW_STOCK_THRESHOLD:
            return 'rgb(255, 235, 238)'
        elif stock_value < WARNING_STOCK_THRESHOLD:
            return 'rgb(255, 243, 224)'
        return 'rgb(232, 245, 233)'
    
    browser_page.locator("//a[@href='/products']").click()
    expect(browser_page.locator('div.grid-container')).to_be_visible()
    stock_cells = browser_page.locator('.ag-cell[col-id="stock"]').all()
    assert len(stock_cells) > 0, "No records were found on the grid"
    
    for cell in stock_cells:
        cell_text = cell.text_content().strip()
        try:
            value = int(cell_text)
        except ValueError:
            raise AssertionError(f"Value '{cell_text}' is not a valid number")
        expected_color = get_expected_color(value)
        expect(cell).to_have_css('background-color', expected_color)


@then("I should see a loading spinner")
def see_loading_spinner(browser_page):
    # Wait for component to mount (same as test_loading_indicator)
    expect(browser_page.locator('div.grid-container')).to_be_visible(timeout=5000)
    # Wait for spinner - use the Angular component selector or its internal container
    spinner = browser_page.locator('app-spinner, .spinner-container').first
    expect(spinner).to_be_visible(timeout=5000)
    # Verify that "No Rows To Show" message is NOT visible while loading
    no_rows_message = browser_page.locator('text=No Rows To Show')
    expect(no_rows_message).not_to_be_visible()


@then("the grid should eventually load")
def grid_loads(browser_page):
    expect(browser_page.locator('//div[@role="row"]')).to_be_visible(timeout=15000)


@then("I should see products in the grid")
def see_products_in_grid(browser_page):
    expect(browser_page.locator('div.grid-container')).to_be_visible()
    product_rows = browser_page.locator('//div[@role="row"]')
    expect(product_rows.first).to_be_visible(timeout=10000)
    # Verify that we have at least one product row (excluding header)
    rows = product_rows.all()
    assert len(rows) > 1, "No products were found in the grid"