import time

from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class Buttons(BasePage):
    __URL = "https://demoqa.com/buttons"
    __RIGHT_CLICK_BUTTON = "#rightClickBtn"
    __RIGHT_CLICK_RESULT = "#rightClickMessage"
    __DOUBLE_CLICK_BUTTON = "#doubleClickBtn"
    __DOUBLE_CLICK_RESULT = "#doubleClickMessage"
    __CLICK_BUTTON = "//button[text()='Click Me']"
    __CLICK_RESULT = "#dynamicClickMessage"

    def __init__(self, page: Page):
        super().__init__(page)

    def open_page(self):
        super()._open(self.__URL)

    def click_buttons_and_verify_messages(self):
        self.page.locator(self.__CLICK_BUTTON).click()
        expect(self.page.locator(self.__CLICK_RESULT)).to_contain_text("You have done a dynamic click")

        self.page.locator(self.__DOUBLE_CLICK_BUTTON).dblclick()
        expect(self.page.locator(self.__DOUBLE_CLICK_RESULT)).to_contain_text("You have done a double click")

        self.page.locator(self.__RIGHT_CLICK_BUTTON).click(button='right')
        expect(self.page.locator(self.__RIGHT_CLICK_RESULT)).to_contain_text("You have done a right click")
