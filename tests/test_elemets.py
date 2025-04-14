import time

from pages.elements.check_box import CheckBox
from pages.elements.buttons import Buttons
from pages.elements.links import Links
from pages.elements.text_box import TextBox
from playwright.sync_api import Page, expect
from data.data_generator import DataGenerator


class TestElements:

    def test_text_box(self, page: Page):
        text_box = TextBox(page)
        text_box.open_page()
        generator = DataGenerator()
        expected_full_name = generator.generate_full_name()
        text_box.fill_name(expected_full_name)
        expected_email = generator.generate_email()
        text_box.fill_email(expected_email)
        expected_current_address = generator.generate_address()
        text_box.fill_current_address(expected_current_address)
        expected_permanent_address = generator.generate_address()
        text_box.fill_permanent_address(expected_permanent_address)
        text_box.submit_form()
        text_box.check_output_info(expected_full_name, expected_email, expected_current_address, expected_permanent_address)

    def test_check_box(self, page: Page):
        check_box = CheckBox(page)
        check_box.open_page()
        chosen_boxes = check_box.click_random_checkbox()
        reflected_boxes = check_box.get_results()

    def test_buttons(self, page: Page):
        buttons = Buttons(page)
        buttons.open_page()
        buttons.click_buttons_and_verify_messages()

    def test_links(self, page: Page):
        links = Links(page)
        links.open_page()
        links.open_new_tab()
        links.verify_url_new_tab()
        links.click_and_verify_broken_link()

    def test_upload_download(self):
        pass
