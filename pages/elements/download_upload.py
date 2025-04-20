import time

from playwright.sync_api import Page

from pages.base_page import BasePage
import os
import base64
from datetime import datetime

class DownloadUpload(BasePage):
    __URL = "https://demoqa.com/upload-download"
    __DOWNLOAD_BUTTON = "//h1[text()='Upload and Download']/following-sibling::div//a[text()='Download']"
    __UPLOAD_DOWNLOAD_BUTTON = "#uploadFile"
    __UPLOADED_FILE_PATH = "#uploadedFilePath"
    def __init__(self, page: Page):
        super().__init__(page)

    def open_page(self):
        super()._open(self.__URL)

    def download_file(self):

        with self.page.expect_download() as download_file:
            super()._click_element(self.__DOWNLOAD_BUTTON)
            download = download_file.value
            file_name = download.suggested_filename
            download_path = rf"C:\Users\48788\PycharmProjects\playwright_practice\downloaded_files\{file_name}"
            download.save_as(download_path)
            assert file_name == "sampleFile.jpeg", "The name of the downloaded file is not correct"
            error = download.failure()
            assert error is None, f"File has not been downloaded: {error}"

    def upload_file(self):
        file_path = r"C:\Users\48788\PycharmProjects\playwright_practice\data\Screenshot_1.png"
        self.page.set_input_files(self.__UPLOAD_DOWNLOAD_BUTTON, file_path )
        actual_uploaded_file = super()._get_text(self.__UPLOADED_FILE_PATH)
        return actual_uploaded_file
    