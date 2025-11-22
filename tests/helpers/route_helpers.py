"""Route interception helpers for image tests"""
from playwright.sync_api import Route, Page
import random

TESTING_SUPPLIER = "Testing supply Inc."

#Images Methods
def setup_abort_all_images(page: Page) -> None:
    def abort_image_requests(route: Route):
        if 'images.unsplash.com' in route.request.url:
            route.abort()  # Don't download the image, test is faster
        else:
            route.continue_()  # Allow other requests (HTML, CSS, JS, etc.)
    # Configure interceptor BEFORE navigating
    page.route('**/*', abort_image_requests)


def setup_abort_first_n_images(page: Page, count: int = 5) -> None:
    abort_count = 0
    def partial_abort(route: Route):
        nonlocal abort_count
        # Abort first N images
        if 'images.unsplash.com' in route.request.url and abort_count < count:
            abort_count += 1
            route.abort()
        else:
            route.continue_()
    page.route('**/*', partial_abort)


#Products Methods
def setup_low_stock_route(page: Page) -> None:
    def low_stock_route(route: Route):
        route.fulfill(
            json={
                "data": [
                    {
                        "id": 1,
                        "name": "Low Stock Test",
                        "category": "Testing tools",
                        "price": 50,
                        "stock": random.randint(0, 9),
                        "supplier": TESTING_SUPPLIER
                    },
                    {
                        "id": 2,
                        "name": "Warning Stock Test",
                        "category": "Testing clothes",
                        "price": 70.24,
                        "stock": random.randint(10, 49),
                        "supplier": TESTING_SUPPLIER
                    },
                    {
                        "id": 3,
                        "name": "High Stock Test",
                        "category": "Testing vehicles",
                        "price": 900,
                        "stock": random.randint(50, 2000),
                        "supplier": TESTING_SUPPLIER
                    }
                ],
                "total": 3,
                "page": 1,
                "pageSize": 10
            }
        )
    page.route('**/api/products**', low_stock_route)


def setup_delayed_products_route(page: Page, seconds: int = 5) -> None:
    def block_route(route: Route):
        pass
    page.route('**/api/products**', block_route)


#Users Methods
def setup_no_records_route(page: Page) -> None:
    def no_records_route(route: Route):
        route.fulfill(
            json={
                "data": [],
                "total": 0,
                "page": 20,
                "pageSize": 10
            }
        )
    page.route('**/api/users**', no_records_route)


def setup_status_color_route(page: Page) -> None:
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
    page.route('**/api/users**', status_color_route)
