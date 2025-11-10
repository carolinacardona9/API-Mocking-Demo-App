from playwright.sync_api import expect
from tests.helpers.route_helpers import setup_low_stock_route, setup_delayed_products_route

def test_low_stock_data(browser_page, base_url):
    LOW_STOCK_THRESHOLD = 10
    WARNING_STOCK_THRESHOLD = 50

    def get_expected_color(stock_value: int) -> str:
        if stock_value < LOW_STOCK_THRESHOLD:
            return 'rgb(255, 235, 238)'
        elif stock_value < WARNING_STOCK_THRESHOLD:
            return 'rgb(255, 243, 224)'
        return 'rgb(232, 245, 233)'
    
    setup_low_stock_route(browser_page)
    browser_page.goto(base_url)
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
        expect(cell).to_have_css('background-color', get_expected_color(value))
    

def test_loading_indicator(browser_page, base_url):
    setup_delayed_products_route(browser_page, seconds=10)
    browser_page.goto(base_url)
    browser_page.locator("//a[@href='/products']").click()
    # Wait for component to mount
    expect(browser_page.locator('div.grid-container')).to_be_visible()
    # Wait for spinner - use the Angular component selector or its internal container
    spinner = browser_page.locator('app-spinner, .spinner-container').first
    expect(spinner).to_be_visible(timeout=5000)
    # Verify that "No Rows To Show" message is NOT visible while loading
    no_rows_message = browser_page.locator('text=No Rows To Show')
    expect(no_rows_message).not_to_be_visible()
    # Wait for grid to eventually load after API responds (10 seconds delay + processing)
    expect(browser_page.locator('//div[@role="row"]')).to_be_visible(timeout=15000)
    