from playwright.sync_api import Page, expect


def test_valid_login_shows_products(page: Page):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_text("Products")).to_be_visible()