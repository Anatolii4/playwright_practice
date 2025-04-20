from playwright.sync_api import Page

from pages.base_page import BasePage


class DatesPicker(BasePage):

    __URL = "https://demoqa.com/date-picker"
    def __init(self, page: Page):
        super().__init__(page)

    def open_page(self):
        super()._open(self.__URL)