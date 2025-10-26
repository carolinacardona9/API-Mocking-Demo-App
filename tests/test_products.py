from playwright.sync_api import Page, Route, expect
import time
import random

def low_stock_route(route: Route):
    route.fulfill(
        json={
            "data": [
                {
                    "id": 1,
                    "name": "Low Stock Test",
                    "category": "Testing tools",
                    "price": 50,
                    "stock": random.randint(0, 9),
                    "supplier": "Testing supply Inc."
                },
                {
                    "id": 2,
                    "name": "Warning Stock Test",
                    "category": "Testing clothes",
                    "price": 70.24,
                    "stock": random.randint(10, 49),
                    "supplier": "Testing supply Inc."
                },
                {
                    "id": 3,
                    "name": "High Stock Test",
                    "category": "Testing vehicles",
                    "price": 900,
                    "stock": random.randint(50,2000),
                    "supplier": "Testing supply Inc."
                }
            ],
            "total": 3,
            "page": 1,
            "pageSize": 10
        }
    )

def response_delay_route(route: Route):
    time.sleep(3)
    route.continue_()

def test_low_stock_data(browser_page, base_url):
    LOW_STOCK_THRESHOLD = 10
    WARNING_STOCK_THRESHOLD = 50

    def get_expected_color(stock_value: int) -> str:
        if stock_value < LOW_STOCK_THRESHOLD:
            return 'rgb(255, 235, 238)'
        elif stock_value < WARNING_STOCK_THRESHOLD:
            return 'rgb(255, 243, 224)'
        return 'rgb(232, 245, 233)'
    
    browser_page.route('**/api/products**', low_stock_route)
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
    browser_page.route('**/api/products**', response_delay_route)
    browser_page.goto(base_url)
    browser_page.locator("//a[@href='/products']").click()
    expect(browser_page.locator('div.grid-container')).to_be_visible()
    expect(browser_page.locator('div.spinner')).to_be_visible()
    expect(browser_page.locator('//div[@role="row"]')).to_be_visible()
    