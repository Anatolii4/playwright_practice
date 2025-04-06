import time

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

