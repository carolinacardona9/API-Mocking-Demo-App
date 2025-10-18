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

def test_low_stock_data(page: Page):
    LOW_STOCK_THRESHOLD = 10
    WARNING_STOCK_THRESHOLD = 50

    def get_expected_color(stock_value: int) -> str:
        if stock_value < LOW_STOCK_THRESHOLD:
            return 'low-stock'
        elif stock_value < WARNING_STOCK_THRESHOLD:
            return 'warning-stock'
        return 'high-stock'

    bg_colors = {
        'low-stock': 'rgb(255, 235, 238)',
        'warning-stock': 'rgb(255, 243, 224)',
        'high-stock': 'rgb(232, 245, 233)'
    }
    page.route('**/api/products**', low_stock_route)
    page.goto('http://localhost:4200/products')
    expect(page.locator('div.grid-container')).to_be_visible()

    stock_cells = page.locator('.ag-cell[col-id="stock"]').all()

    assert len(stock_cells) > 0, "No records were found on the grid"
    
    for cell in stock_cells:
        cell_text = cell.text_content()
        try:
            value = int(cell_text)
        except ValueError:
            raise AssertionError(f"Value '{value}' is not a valid number")
        expect(cell).to_have_css('background-color', bg_colors[get_expected_color(value)])
    