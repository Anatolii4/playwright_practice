import time
import random

from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class CheckBox(BasePage):
    __URL = "https://demoqa.com/checkbox"
    __CHECKBOX = "//span[@class='rct-checkbox']"
    __CHECKBOX_TITLES = "//span[@class='rct-title']"
    __EXPAND_BUTTON = "Expand all"
    __RESULTS = "//div[@id='result']//span[@class='text-success']"
    __CHECKED_BOX_TITLE_LOCATOR = ".//ancestor::span[@class='rct-text']"
    def __init__(self, page: Page):
        super().__init__(page)

    def open_page(self):
        super()._open(self.__URL)

    def click_random_checkbox(self):
        self.page.get_by_title(self.__EXPAND_BUTTON).click()
        self.page.wait_for_selector(self.__CHECKBOX)
        checkboxes = self.page.locator(self.__CHECKBOX)
        titles = self.page.locator(self.__CHECKED_BOX_TITLE_LOCATOR)
        count_of_checkboxes = checkboxes.count()
        number_to_click = random.randint(1, 5)
        random_index = random.sample(range(count_of_checkboxes), number_to_click)
        clicked_boxes = []
        for index in random_index:
            choose_box = checkboxes.nth(index)
            choose_box.click()
            title_of_checkboxes = titles.nth(index).inner_text()
            clicked_boxes.append(title_of_checkboxes)
        modified_list = [item.lower() for item in clicked_boxes]
        print(modified_list)
        return modified_list

    def get_results(self):
        title_of_checked_boxes = []
        boxes_result = self.page.locator(self.__RESULTS)
        count_checked_boxes = boxes_result.count()
        for index in range(count_checked_boxes):
            title = boxes_result.nth(index).inner_text()
            title_of_checked_boxes.append(title)
        return title_of_checked_boxes
