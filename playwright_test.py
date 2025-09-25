# playwright_test.py
# Uses Playwright Python (sync)
# To run:
#   pip install playwright pytest-playwright
#   playwright install
#   pytest -q playwright_test.py

from playwright.sync_api import sync_playwright

def test_search_and_check_buttons():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://rahulshettyacademy.com/AutomationPractice/")
        # Check page title
        assert "Practice Page" in page.title() or "Practice" in page.title()
        # Check checkbox interactions
        checkbox = page.locator("#checkBoxOption1")
        checkbox.check()
        assert checkbox.is_checked()
        checkbox.uncheck()
        assert not checkbox.is_checked()
        # Select dropdown value
        dropdown = page.locator("#dropdown-class-example")
        dropdown.select_option("option2")
        selected = page.locator("#dropdown-class-example").input_value()
        assert selected == "option2"
        # Open new window via open tab link and assert it contains 'qaclickacademy' text
        page.click("#opentab")
        # close browser
        browser.close()

if __name__ == '__main__':
    test_search_and_check_buttons()
