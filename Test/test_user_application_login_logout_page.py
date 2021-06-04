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

from user_application_login_logout_page import UserApplicationLoginLogoutPage
from config import *



class UserApplicationLoginLogoutPageLocators:
    locator_login_send_keys = (By.XPATH, '/html/body/div/div[1]/div/div/div/div/div/div/div/form/div[1]/div/div[1]/div')
    locator_password_send_keys = (By.XPATH, '/html/body/div/div[1]/div/div/div/div/div/div/div/form/div[2]/div/div[1]/div[1]')
    locator_click_login_button = (By.XPATH, "/html/body/div/div[1]/div/div/div/div/div/div/div/form/div[5]/button/span")
    locator_click_drop_down_menu = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div/div[4]/button")
    locator_click_logout_button = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div/div[5]/div[3]/div")
   


class TestUserApplicationLoginLogoutPage(UserApplicationLoginLogoutPage):

    def send_login(self):
        login_field = self.find_element(UserApplicationLoginLogoutPageLocators.locator_login_send_keys,time=2)
        search_input = login_field.find_element_by_tag_name("input")
        search_input.send_keys("test@test.org", Keys.ENTER)

    def send_password(self):
        login_field = self.find_element(UserApplicationLoginLogoutPageLocators.locator_password_send_keys,time=2)
        search_input = login_field.find_element_by_tag_name("input")
        search_input.send_keys("testtestyan", Keys.ENTER)

    def click_on_the_login_button(self):
        return self.find_element(UserApplicationLoginLogoutPageLocators.locator_click_login_button,time=2).click()
    
    def click_drop_down_menu(self):
        return self.find_element(UserApplicationLoginLogoutPageLocators.locator_click_drop_down_menu,time=2).click()

    def click_on_the_logout_button(self):
        return self.find_element(UserApplicationLoginLogoutPageLocators.locator_click_logout_button,time=2).click()

