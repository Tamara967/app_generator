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

from app_generator_login_page import AppGeneratorLoginLogoutPage
from config import *



class TestAppGeneratorLoginLogoutPageLocators:
    locator_login_send_keys = (By.XPATH, '//*[@id="input-7"]')
    locator_password_send_keys = (By.XPATH, '//*[@id="input-10"]')
    locator_click_login_button = (By.XPATH, "/html/body/div/div[1]/div/div/div/div/div/div/div/form/div[4]/button/span")
    locator_click_drop_down_menu = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div/div[4]/button")
    locator_click_logout_button = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div/div[5]/div[4]/div")
   


class TestAppGeneratorLoginLogoutPage(AppGeneratorLoginLogoutPage):

    def send_login(self):
        login_field = self.find_element(TestAppGeneratorLoginLogoutPageLocators.locator_login_send_keys)
        login_field.send_keys('appgenerator.rm@gmail.com')

    def send_password(self):
        password_field = self.find_element(TestAppGeneratorLoginLogoutPageLocators.locator_password_send_keys)
        password_field.send_keys('App2020*')

    def click_on_the_login_button(self):
        return self.find_element(TestAppGeneratorLoginLogoutPageLocators.locator_click_login_button,time=2).click()
    
    def check_login_home(self, load_page_title):
        return True
    def click_drop_down_menu(self):
        return self.find_element(TestAppGeneratorLoginLogoutPageLocators.locator_click_drop_down_menu,time=2).click()

    def click_on_the_logout_button(self):
        return self.find_element(TestAppGeneratorLoginLogoutPageLocators.locator_click_logout_button,time=2).click()

