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
    bg_colors = {
        'low-stock': 'rgb(255, 235, 238)',
        'warning-stock': 'rgb(255, 243, 224)',
        'high-stock': 'rgb(232, 245, 233)'
    }
    page.route('**/api/products**', low_stock_route)
    page.goto('http://localhost:4200/products')
    expect(page.locator('div.grid-container')).to_be_visible()
    stock_cells = page.locator('.ag-cell[col-id="stock"]').all()
    stock_values = [int(cell.text_content()) for cell in stock_cells]
    breakpoint()
    for i,cell in enumerate(stock_cells):
        value = stock_values[i]
        expected_color = 'high-stock'
        if value < 10:
            expected_color = 'low-stock'
        elif value < 50:
            expected_color = 'warning-stock'
        expect(cell).to_have_css('background-color', bg_colors[expected_color])
    