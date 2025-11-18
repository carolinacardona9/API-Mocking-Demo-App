from playwright.sync_api import Page, Route, expect
import time

def test_load_users_successfully(browser_page, base_url):
    """Load users successfully without mocking the API"""
    browser_page.goto(base_url)
    browser_page.locator("//a[@href='/users']").click()
    browser_page.wait_for_load_state("networkidle")
    
    # Verify grid is visible
    grid = browser_page.locator('div.grid-wrapper, div.grid-container')
    expect(grid).to_be_visible()
    
    # Verify that we have at least one user row (excluding header)
    user_rows = browser_page.locator('//div[@role="row"]')
    expect(user_rows.first).to_be_visible(timeout=10000)
    rows = user_rows.all()
    assert len(rows) > 1, "No users were found in the grid"

def no_records_route(route: Route):
    route.fulfill(
        json={
            "data": [],
            "total": 0,
            "page": 20,
            "pageSize": 10
        }
    )

def status_color_route(route: Route):
    route.fulfill(
        json={
            "data": [
                {
                    "id": 1,
                    "name": "Test user pending",
                    "email": "pending@example.com",
                    "role": "Developer",
                    "status": "Pending",
                    "createdAt": "2025-05-20"
                },
                {
                    "id": 2,
                    "name": "Test user active",
                    "email": "active@example.com",
                    "role": "Developer",
                    "status": "Active",
                    "createdAt": "2025-05-20"
                },
                {
                    "id": 3,
                    "name": "Test user inactive",
                    "email": "inactive@example.com",
                    "role": "Developer",
                    "status": "Inactive",
                    "createdAt": "2025-05-20"
                }
            ],
            "total": 3,
            "page": 1,
            "pageSize": 10
        }
    )

def test_users_no_records(browser_page, base_url):
    browser_page.route('**/api/users**', no_records_route)
    browser_page.goto(base_url)
    msg =  browser_page.locator('span.ag-overlay-no-rows-center')
    expect(msg).to_have_text('No Rows To Show')

def test_user_status_color(browser_page, base_url):
    def get_users_status_colors(status: str) -> str:
        if status == 'Pending':
            return 'rgb(255, 165, 0)'
        elif status == 'Inactive':
            return 'rgb(255, 0, 0)'
        return 'rgb(0, 128, 0)'

    browser_page.route('**/api/users**', status_color_route)
    browser_page.goto(base_url)
    expect(browser_page.locator('div.grid-wrapper')).to_be_visible()

    users_status_cells = browser_page.locator('.ag-cell[col-id="status"]').all()

    assert len(users_status_cells) > 0, "No records were found on the grid"

    for cell in users_status_cells:
        cell_text = cell.text_content().strip()
        expect(cell).to_have_css('color', get_users_status_colors(cell_text))
            