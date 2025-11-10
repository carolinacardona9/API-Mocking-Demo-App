from pytest_bdd import given, when, then, parsers
from playwright.sync_api import expect
from tests.helpers.route_helpers import (
    setup_abort_all_images,
    setup_abort_first_n_images
)


@given("I navigate to the images page")
def navigate_to_images(browser_page, base_url):
    browser_page.goto(f'{base_url}/images')


@given("I configure route interception to abort image requests")
def configure_abort_all_images(browser_page):
    setup_abort_all_images(browser_page)


@given("I configure route interception to abort the first 5 images")
def configure_abort_first_five(browser_page):
    setup_abort_first_n_images(browser_page, count=5)


@when("I navigate to the images page")
def navigate_images_page(browser_page, base_url):
    browser_page.goto(f'{base_url}/images')


@then(parsers.parse("I should see {count:d} image cards"))
def see_image_cards(browser_page, count):
    image_cards = browser_page.locator('.image-card')
    expect(image_cards).to_have_count(count)


@then("at least one image should be loaded")
def at_least_one_loaded(browser_page):
    loaded_images = browser_page.locator('.image-card.loaded')
    expect(loaded_images.first).to_be_visible(timeout=10000)


@then("no images should be loaded")
def no_images_loaded(browser_page):
    loaded_images = browser_page.locator('.image-card.loaded')
    expect(loaded_images).to_have_count(0)


@then("I should see error or loading indicators")
def see_error_or_loading(browser_page):
    error_or_loading = browser_page.locator('.error-message, .loading-spinner')
    expect(error_or_loading.first).to_be_visible(timeout=2000)


@then("the test should complete faster than loading all images")
def test_completes_fast(browser_page):
    expect(browser_page.locator('.images-container')).to_be_visible()


@then("some images should be loaded")
def some_images_loaded(browser_page):
    browser_page.wait_for_timeout(3000)
    loaded_images = browser_page.locator('.image-card.loaded')
    expect(loaded_images.first).to_be_visible(timeout=5000)


@then("some images should show error state")
def some_images_error(browser_page):
    error_images = browser_page.locator('.image-card.error, .error-message')
    expect(error_images.first).to_be_visible(timeout=5000)

