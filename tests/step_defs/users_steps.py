"""Step definitions for users feature"""
from pytest_bdd import given, when, then, parsers
from playwright.sync_api import expect
from tests.helpers.route_helpers import setup_no_records_route, setup_status_color_route
from pytest_bdd import parsers


@given("I mock the API to return no users")
def mock_no_users(browser_page):
    setup_no_records_route(browser_page)


@given("I mock the API to return users with different statuses")
def mock_users_with_statuses(browser_page):
    setup_status_color_route(browser_page)


@then(parsers.parse('I should see the message "{message}"'))
def see_message(browser_page, message):
    msg = browser_page.locator('span.ag-overlay-no-rows-center')
    expect(msg).to_have_text(message)


@then("I should see users with correct status colors")
def verify_status_colors(browser_page, datatable):

    grid = browser_page.locator('div.grid-wrapper, div.grid-container')
    expect(grid).to_be_visible()
    
    users_status_cells = browser_page.locator('.ag-cell[col-id="status"]').all()
    assert len(users_status_cells) > 0, "No records were found on the grid"
    # Create color map from datatable
    color_map = {}
    if datatable:
        for row in datatable:
            color_map[row['Status']] = row['Color']
    # Default colors if datatable is not provided
    if not color_map:
        color_map = {
            'Pending': 'rgb(255, 165, 0)',
            'Inactive': 'rgb(255, 0, 0)',
            'Active': 'rgb(0, 128, 0)'
        }
    for cell in users_status_cells:
        cell_text = cell.text_content().strip()
        expected_color = color_map.get(cell_text)
        if expected_color:
            expect(cell).to_have_css('color', expected_color)

