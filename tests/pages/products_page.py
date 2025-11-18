class ProductsPage:
    # Stock thresholds
    LOW_STOCK_THRESHOLD = 10
    WARNING_STOCK_THRESHOLD = 50
    
    # Stock colors
    STOCK_COLORS = {
        'low': 'rgb(255, 235, 238)',      # < 10
        'warning': 'rgb(255, 243, 224)',  # 10-49
        'normal': 'rgb(232, 245, 233)'    # >= 50
    }
    
    def __init__(self):
        self.products_tab_locator = "//a[@href='/products']"
        self.products_grid_container = 'div.grid-container'
        self.stock_column_cells = '.ag-cell[col-id="stock"]'
        self.loading_spinner = 'app-spinner, .spinner-container'
        self.grid_rows = '//div[@role="row"]'
        self.no_rows_message = 'text=No Rows To Show'
    
    def get_expected_stock_color(self, stock_value: int) -> str:
        """Get the expected background color based on stock value"""
        if stock_value < self.LOW_STOCK_THRESHOLD:
            return self.STOCK_COLORS['low']
        elif stock_value < self.WARNING_STOCK_THRESHOLD:
            return self.STOCK_COLORS['warning']
        return self.STOCK_COLORS['normal']
