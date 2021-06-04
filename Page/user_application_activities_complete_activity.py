from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



class UserApplicationCompleteActivityPage():

    def __init__(self, driver, page_link):
        self.driver = driver
        self.page_link = page_link

    def find_element(self, locator,time=20):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                          message=f"Can't find element by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.page_link)
    
    def assert_driver_title(self, load_page_title):
        if driver.title == load_page_title:
            return self.assertEqual(driver.title, load_page_title)    
        else:
            print("WebPage Failed to load")

    def implicitly_wait(self):
        return self.driver.implicitly_wait(10)

    def quit_driver(self):
        return self.driver.close()

