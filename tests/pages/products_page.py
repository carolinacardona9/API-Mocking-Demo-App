class ProductsPage:
    def __init__(self):
        self.products_tab_locator = "//a[@href='/products']"
        self.products_grid_container = 'div.grid-container'
        self.stock_column_cells = '.ag-cell[col-id="stock"]'
        self.loading_spinner = 'app-spinner, .spinner-container'
        self.grid_rows = '//div[@role="row"]'
