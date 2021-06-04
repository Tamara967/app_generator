from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import ast
import datetime

class AppGeneratorAddNewOrganisation():

    def __init__(self, driver, page_link):
        self.driver = driver
        self.page_link = page_link

    def find_element(self, locator,time = 20):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                          message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time = 20):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
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

    def get_driver_max(self):
        return self.driver.maximize_window()
  
    def get_all_elements(self):
        all_elem = self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[3]")
        input_item = all_elem.find_elements_by_tag_name("input")
        clik_okta = self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div/div/div")
        


        file = open("json_data.py", "r+")
        contents = file.read()
        data_keys = ast.literal_eval(contents)
        file.close()

        x = datetime.datetime.now()

        replace_current_time = str(x).replace(" ","")
        current_date_and_time = replace_current_time.replace(":","")
        cur_date_and_time = current_date_and_time.replace('-',"")
        test_run_date_and_time = cur_date_and_time.replace('.',"")
       
        
        for keys in range(0, len(data_keys)):
            if keys <= 1 :
                data_keys[keys] = test_run_date_and_time + data_keys[keys]
            if keys > 1 and keys % 3 == 0:
                data_keys[keys] = data_keys[keys] + data_keys[1]
      
        result = []
        data = {}
        for elem in input_item:
            el = elem.get_attribute("required")
            text = elem.get_attribute("type")
            if el and text == "text":
                result.append(elem)
       
        for i in range(0, len(result)):
            for j in range(0, len(data_keys)):
                data[result[i]] = data_keys[i]

        for key, value in data.items():
            key.send_keys(value)
