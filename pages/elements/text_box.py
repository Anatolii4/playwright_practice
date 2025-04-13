from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class TextBox(BasePage):
    __URL = "https://demoqa.com/text-box"
    __NAME = "#userName"
    __EMAIL = "#userEmail"
    __CURRENT_ADDRESS = "#currentAddress"
    __PERMANENT_ADDRESS = "#permanentAddress"
    __SUBMIT_BUTTON = "#submit"
    __OUTPUT_NAME = "//div[@id='output']//div//p[@id='name']"
    __OUTPUT_EMAIL = "//div[@id='output']//div//p[@id='email']"
    __OUTPUT_CURRENT_ADDRESS = "//div[@id='output']//div//p[@id='currentAddress']"
    __OUTPUT_PERMANENT_ADDRESS = "//div[@id='output']//div//p[@id='permanentAddress']"

    def __init__(self, page: Page):
        super().__init__(page)

    def open_page(self):
        super()._open(self.__URL)

    def fill_name(self, full_name: str):
        super()._fill_text(self.__NAME, full_name)

    def fill_email(self, email: str):
        super()._fill_text(self.__EMAIL, email)

    def fill_current_address(self, address: str):
        super()._fill_text(self.__CURRENT_ADDRESS, address)

    def fill_permanent_address(self, address: str):
        super()._fill_text(self.__PERMANENT_ADDRESS, address)

    def submit_form(self):
        super()._click_element(self.__SUBMIT_BUTTON)

    def check_output_info(self, name, email, current_address, permanent_address):
        expect(self.page.locator(self.__OUTPUT_NAME)).to_contain_text(name)
        expect(self.page.locator(self.__OUTPUT_EMAIL)).to_contain_text(email)
        expect(self.page.locator(self.__OUTPUT_CURRENT_ADDRESS)).to_contain_text(current_address)
        expect(self.page.locator(self.__OUTPUT_PERMANENT_ADDRESS)).to_contain_text(permanent_address)

