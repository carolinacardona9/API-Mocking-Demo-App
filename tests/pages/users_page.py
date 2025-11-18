class UsersPage:
    # Status colors mapping
    STATUS_COLORS = {
        'Pending': 'rgb(255, 165, 0)',
        'Inactive': 'rgb(255, 0, 0)',
        'Active': 'rgb(0, 128, 0)'
    }
    
    
    def __init__(self):
        self.no_rows_message = 'span.ag-overlay-no-rows-center'
        self.users_grid_container = 'div.grid-wrapper, div.grid-container'
        self.status_column_cells = '.ag-cell[col-id="status"]'
        self.user_rows = '//div[@role="row"]'
        self.users_link = "//a[@href='/users']"
    
    def get_expected_status_color(self, status: str) -> str:
        """Get the expected color for a given status"""
        return self.STATUS_COLORS.get(status, 'rgb(0, 128, 0)')
