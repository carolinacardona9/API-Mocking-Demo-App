"""Step definitions for products feature"""
from pytest_bdd import given, when, then, parsers
from playwright.sync_api import expect
from tests.helpers.route_helpers import setup_low_stock_route, setup_delayed_products_route
from tests.pages.products_page import ProductsPage


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


@then("I should see products in the grid")
def see_products_in_grid(browser_page, products_page: ProductsPage):
    expect(browser_page.locator(products_page.products_grid_container)).to_be_visible()
    product_rows = browser_page.locator(products_page.grid_rows)
    expect(product_rows.first).to_be_visible(timeout=10000)
    rows = product_rows.all()
    assert len(rows) > 1, "No products were found in the grid"


@then("I should see products with correct stock background colors")
def verify_stock_colors(browser_page,  products_page: ProductsPage):
    browser_page.locator(products_page.products_tab_locator).click()
    expect(browser_page.locator(products_page.products_grid_container)).to_be_visible()
    stock_cells = browser_page.locator(products_page.stock_column_cells).all()
    assert len(stock_cells) > 0, "No records were found on the grid"
    
    for cell in stock_cells:
        cell_text = cell.text_content().strip()
        try:
            value = int(cell_text)
        except ValueError:
            raise AssertionError(f"Value '{cell_text}' is not a valid number")
        expected_color = products_page.get_expected_stock_color(value)
        expect(cell).to_have_css('background-color', expected_color)


@then("I should see a loading spinner")
def see_loading_spinner(browser_page, products_page: ProductsPage):
    browser_page.wait_for_selector(products_page.products_grid_container, state='visible', timeout=5000)
    spinner = browser_page.locator(products_page.loading_spinner).first
    expect(spinner).to_be_visible(timeout=5000)
    # Verify that "No Rows To Show" message is NOT visible while loading
    no_rows_message = browser_page.locator('text=No Rows To Show')
    expect(no_rows_message).not_to_be_visible()


@then("the grid should eventually load")
def grid_loads(browser_page, products_page: ProductsPage):
    expect(browser_page.locator(products_page.grid_rows)).to_be_visible(timeout=15000)