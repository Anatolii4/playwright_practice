from playwright.sync_api import Page, expect
import re


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def _open(self, url: str):
        self.page.goto(url)

    def _click_element(self, locator: str):
        self.page.locator(locator).click()

    def _fill_text(self, locator: str, text: str):
        self.page.locator(locator).fill(text)

    def _get_text(self, locator: str):
        return self.page.locator(locator).inner_text()

    def _check_box(self, locator: str):
        self.page.locator(locator).check()