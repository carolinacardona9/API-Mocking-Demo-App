from playwright.sync_api import Route, expect
from tests.helpers.route_helpers import (
    setup_abort_all_images,
    setup_abort_first_n_images
)


def test_images_load_successfully(browser_page, base_url):
    browser_page.goto(f'{base_url}/images')
    expect(browser_page.locator('.images-container')).to_be_visible()
    image_cards = browser_page.locator('.image-card')
    expect(image_cards).to_have_count(20)
    loaded_images = browser_page.locator('.image-card.loaded')
    expect(loaded_images.first).to_be_visible(timeout=10000)

def test_images_abort_loading(browser_page, base_url):
    import time
    setup_abort_all_images(browser_page)
    start_time = time.time()
    browser_page.goto(f'{base_url}/images')
    load_time = time.time() - start_time
    expect(browser_page.locator('.images-container')).to_be_visible()
    image_cards = browser_page.locator('.image-card')
    expect(image_cards).to_have_count(20)
    loaded_images = browser_page.locator('.image-card.loaded')
    expect(loaded_images).to_have_count(0)
    error_or_loading = browser_page.locator('.error-message, .loading-spinner')
    expect(error_or_loading.first).to_be_visible(timeout=2000)

def test_images_partial_abort(browser_page, base_url):
    setup_abort_first_n_images(browser_page, count=5)
    browser_page.goto(f'{base_url}/images')
    expect(browser_page.locator('.images-container')).to_be_visible()
    browser_page.wait_for_timeout(3000)
    image_cards = browser_page.locator('.image-card')
    expect(image_cards).to_have_count(20)
    error_images = browser_page.locator('.image-card.error, .error-message')
    expect(error_images.first).to_be_visible(timeout=5000)

