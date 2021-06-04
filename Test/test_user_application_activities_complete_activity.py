from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import sys
import os
import time

def get_path(path):
    os.chdir(path)
    sys.path.insert(0,path)


get_path("/home/erida-employee/Desktop/ssh/page_class/App_Gnerator/Page")
get_path("/home/erida-employee/Desktop/ssh/page_class/App_Gnerator")

from user_application_activities_complete_activity import UserApplicationCompleteActivityPage
from config import *



class UserApplicationCompleteActivityPageLocators:
    locator_login_send_keys = (By.XPATH, '/html/body/div/div[1]/div/div/div/div/div/div/div/form/div[1]/div/div[1]/div')
    locator_password_send_keys = (By.XPATH, '/html/body/div/div[1]/div/div/div/div/div/div/div/form/div[2]/div/div[1]/div[1]')
    locator_click_login_button = (By.XPATH, "/html/body/div/div[1]/div/div/div/div/div/div/div/form/div[5]/button/span")
    locator_click_drop_doun_manu = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div/button/span/i")
    locator_open_main_manu = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div/button/span/i")
    locator_click_activites_button = (By.XPATH, "/html/body/div/div[1]/div[1]/nav/div[1]/div[2]/div[1]/div/a")
    locator_click_complete_activity = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div/main/div/div[3]/div[1]/table/tbody/tr[1]/td[11]/button[2]")
    locator_click_ok_button = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[3]/button[2]/span")
    locator_check_complete_ststus = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[1]/main/div/div[3]/div[1]/table/tbody")

class TestUserApplicationCompleteActivityPage(UserApplicationCompleteActivityPage):
    def check_complete_ststus(self):
        check_status = "Closed"
        e_element = self.find_element(UserApplicationCompleteActivityPageLocators.locator_check_complete_ststus,time=2)
        text = self.driver.execute_script("return arguments[0].innerText;", e_element)
        if check_status in text:
            print("Status is changed")

    def click_ok_button(self):
        return self.find_element(UserApplicationCompleteActivityPageLocators.locator_click_ok_button,time=2).click()

    def click_complete_activity(self):
        return self.find_element(UserApplicationCompleteActivityPageLocators.locator_click_complete_activity,time=2).click()

    def click_activites_button(self):
        return self.find_element(UserApplicationCompleteActivityPageLocators.locator_click_activites_button,time=2).click()


    def open_main_manu(self):
        return self.find_element(UserApplicationCompleteActivityPageLocators.locator_open_main_manu,time=2).click()

    def send_login(self):
        login_field = self.find_element(UserApplicationCompleteActivityPageLocators.locator_login_send_keys,time=2)
        search_input = login_field.find_element_by_tag_name("input")
        search_input.send_keys("test@test.org", Keys.ENTER)

    def send_password(self):
        login_field = self.find_element(UserApplicationCompleteActivityPageLocators.locator_password_send_keys,time=2)
        search_input = login_field.find_element_by_tag_name("input")
        search_input.send_keys("testtestyan", Keys.ENTER)

    def click_on_the_login_button(self):
        return self.find_element(UserApplicationCompleteActivityPageLocators.locator_click_login_button,time=2).click()



