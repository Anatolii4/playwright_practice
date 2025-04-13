import time

from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class Links(BasePage):
    __URL = "https://demoqa.com/links"
    __URL_BROKEN_LINKS = "https://demoqa.com/broken"
    __HOME_LINK = "#simpleLink"
    __BROKEN_LINK = "//a[text()='Click Here for Valid Link']"

    def __init__(self, page: Page):
        super().__init__(page)

    def open_page(self):
        super()._open(self.__URL)

    def open_new_tab(self):
        super()._click_element(self.__HOME_LINK)

    def verify_url_new_tab(self):
        with self.page.expect_popup() as popup_info:
            new_tab = popup_info.value
            expect(new_tab).to_have_url("https://demoqa.com/")
            new_tab.close()

    def click_and_verify_broken_link(self):
        super()._open(self.__URL_BROKEN_LINKS)
        super()._click_element(self.__BROKEN_LINK)
        expect(self.page).to_have_url("https://demoqa.com/")