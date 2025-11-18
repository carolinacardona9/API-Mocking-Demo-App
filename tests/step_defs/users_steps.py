"""Step definitions for users feature"""
from pytest_bdd import given, when, then, parsers
from playwright.sync_api import expect
from tests.helpers.route_helpers import setup_no_records_route, setup_status_color_route
from tests.pages.users_page import UsersPage


@given("I mock the API to return no users")
def mock_no_users(browser_page):
    setup_no_records_route(browser_page)


@given("I mock the API to return users with different statuses")
def mock_users_with_statuses(browser_page):
    setup_status_color_route(browser_page)


@given("I navigate to the users page")
@when("I navigate to the users page")
def navigate_users_page(browser_page, base_url, users_page: UsersPage):
    browser_page.locator(users_page.users_link).click()


@then("I should see users in the grid")
def see_users_in_grid(browser_page, users_page: UsersPage):
    expect(browser_page.locator(users_page.users_grid_container)).to_be_visible()
    user_rows = browser_page.locator(users_page.user_rows)
    expect(user_rows.first).to_be_visible(timeout=10000)
    rows = user_rows.all()
    assert len(rows) > 1, "No users were found in the grid"


@then(parsers.parse('I should see the message "{message}"'))
def see_message(browser_page, message, users_page: UsersPage):
    msg = browser_page.locator(users_page.no_rows_message)
    expect(msg).to_have_text(message)


@then("I should see users with correct status colors")
def verify_status_colors(browser_page, users_page: UsersPage):
    grid = browser_page.locator(users_page.users_grid_container)
    expect(grid).to_be_visible()
    
    users_status_cells = browser_page.locator(users_page.status_column_cells).all()
    assert len(users_status_cells) > 0, "No records were found on the grid"
    
    for cell in users_status_cells:
        cell_text = cell.text_content().strip()
        expected_color = users_page.get_expected_status_color(cell_text)
        expect(cell).to_have_css('color', expected_color)

