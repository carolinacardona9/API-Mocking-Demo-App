from playwright.sync_api import Page, Route, expect
import time

def no_records_route(route: Route):
    route.fulfill(
        json={
            "data": [],
            "total": 0,
            "page": 20,
            "pageSize": 10
        }
    )

def test_users_no_records(page: Page):
    page.route('**/api/users**',no_records_route)
    page.goto('http://localhost:4200/users')
    msg = page.locator('span.ag-overlay-no-rows-center')
    expect(msg).to_have_text('No Rows To Show')