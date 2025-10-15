from playwright.sync_api import Page, Route, expect
import time

def low_stock_route(route: Route):
    route.fulfill(
        json={
            "data": [{
                "id": 1,
                "name": "Product test",
                "category": "Testing tools",
                "price": 70.24,
                "stock": 2,
                "supplier": "Testing supply Inc."
            }],
            "total": 1,
            "page": 1,
            "pageSize": 10
        }
    )

def test_low_stock_data(page: Page):
    page.route('**/api/products**', low_stock_route)
    page.goto('http://localhost:4200/users')
    breakpoint()
    page.locator("//a[@href='/products']").click()
    breakpoint()
    stock_cell = page.locator('.ag-cell[col-id="stock"]')
    expect(stock_cell).to_have_css('background-color', 'rgb(255, 235, 238)')
    