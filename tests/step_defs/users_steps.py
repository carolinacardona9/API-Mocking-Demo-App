"""Step definitions for users feature"""
from pytest_bdd import given, when, then, parsers
from playwright.sync_api import expect
from tests.helpers.route_helpers import setup_no_records_route, setup_status_color_route


@given("I mock the API to return no users")
def mock_no_users(browser_page):
    setup_no_records_route(browser_page)


@given("I mock the API to return users with different statuses")
def mock_users_with_statuses(browser_page):
    setup_status_color_route(browser_page)


@given("I navigate to the users page")
@when("I navigate to the users page")
def navigate_users_page(browser_page, base_url):
    browser_page.locator("//a[@href='/users']").click()


@then(parsers.parse('I should see the message "{message}"'))
def see_message(browser_page, message):
    # Wait for grid to be visible first (even if empty)
    grid = browser_page.locator('div.grid-wrapper, div.grid-container')
    expect(grid).to_be_visible(timeout=10000)
    # Then check for the no rows message
    msg = browser_page.locator('span.ag-overlay-no-rows-center')
    expect(msg).to_have_text(message, timeout=10000)


@then("I should see users in the grid")
def see_users_in_grid(browser_page):
    grid = browser_page.locator('div.grid-wrapper, div.grid-container')
    expect(grid).to_be_visible()
    user_rows = browser_page.locator('//div[@role="row"]')
    expect(user_rows.first).to_be_visible(timeout=10000)
    # Verify that we have at least one user row (excluding header)
    rows = user_rows.all()
    assert len(rows) > 1, "No users were found in the grid"


@then("I should see users with correct status colors")
def verify_status_colors(browser_page):
    """Verify users have correct status colors"""
    def get_users_status_colors(status: str) -> str:
        """Get expected color based on status"""
        if status == 'Pending':
            return 'rgb(255, 165, 0)'
        elif status == 'Inactive':
            return 'rgb(255, 0, 0)'
        return 'rgb(0, 128, 0)'  # Active
    
    grid = browser_page.locator('div.grid-wrapper, div.grid-container')
    expect(grid).to_be_visible()
    
    users_status_cells = browser_page.locator('.ag-cell[col-id="status"]').all()
    assert len(users_status_cells) > 0, "No records were found on the grid"
    
    for cell in users_status_cells:
        cell_text = cell.text_content().strip()
        expected_color = get_users_status_colors(cell_text)
        expect(cell).to_have_css('color', expected_color)

