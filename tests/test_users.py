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

def test_users_no_records(page: Page):
    page.route('**/api/users**', no_records_route)
    page.goto('http://localhost:4200/users')
    msg = page.locator('span.ag-overlay-no-rows-center')
    expect(msg).to_have_text('No Rows To Show')

def test_user_status_color(page: Page):
    def get_users_status_colors(status: str) -> str:
        if status == 'Pending':
            return 'rgb(255, 165, 0)'
        elif status == 'Inactive':
            return 'rgb(255, 0, 0)'
        return 'rgb(0, 128, 0)'

    page.route('**/api/users**', status_color_route)
    page.goto('http://localhost:4200/users')
    expect(page.locator('div.grid-container')).to_be_visible()

    users_status_cells = page.locator('.ag-cell[col-id="status"]').all()

    assert len(users_status_cells) > 0, "No records were found on the grid"

    for cell in users_status_cells:
        cell_text = cell.text_content().strip()
        expect(cell).to_have_css('color', get_users_status_colors(cell_text))
            