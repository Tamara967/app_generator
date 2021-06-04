from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



class UserAplicatioViewAndEditActivitesPage():

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
   
    def find_elements(self):
        locator =  "/html/body/div/div[1]/div[2]/div/div/main/div/div[3]/div/div/div/div/nav/ul"
        elements = self.driver.find_element_by_xpath(locator)
        elem_li = elements.find_elements_by_tag_name("li")
        for elem in elem_li:
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            elem.click()
            time.sleep(5)
  

