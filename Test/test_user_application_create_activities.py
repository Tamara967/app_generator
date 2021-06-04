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

from user_application_create_activities import UserApplicationCreateActivitiesPage
from config import *



class UserApplicationCreateActivitiesPageLocators:
    locator_login_send_keys = (By.XPATH, '/html/body/div/div[1]/div/div/div/div/div/div/div/form/div[1]/div/div[1]/div')
    locator_password_send_keys = (By.XPATH, '/html/body/div/div[1]/div/div/div/div/div/div/div/form/div[2]/div/div[1]/div[1]')
    locator_click_login_button = (By.XPATH, "/html/body/div/div[1]/div/div/div/div/div/div/div/form/div[5]/button/span")
    locator_click_drop_doun_manu = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div/button/span/i")
    locator_click_activities_button = (By.XPATH, "/html/body/div/div[1]/div[1]/nav/div[1]/div[2]/div[1]/div/a")
    locator_click_add_new_button = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[1]/main/div/div[2]/div[3]/button/span") 
    locator_send_keys_coustmer_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div/div[1]/div/div/div[1]/div")
    locator_select_instrument_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div/div[3]/div/div/div[1]/div[1]/div/div/i")
    locator_choose_instrument_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[4]/div/div[1]/div/div")
    locator_select_protocol_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div/div[4]/div/div/div[1]/div[1]/div/div/i")
    locator_choose_protocol_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[5]/div/div[2]/div/div")
    locator_select_protocol_version = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div/div[5]/div/div/div[1]/div[1]/div/div/i")
    locator_choose_protocol_version = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[6]/div/div[1]/div/div")
    locator_click_on_the_button_start = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[3]/button[2]/span")


class TestUserApplicationCreateActivitiesPage(UserApplicationCreateActivitiesPage):
    def click_on_the_button_start(self):
        return self.find_element(UserApplicationCreateActivitiesPageLocators.locator_click_on_the_button_start,time=2).click()


    def choose_protocol_version(self):
        return self.find_element(UserApplicationCreateActivitiesPageLocators.locator_choose_protocol_version,time=2).click()


    def select_protocol_version(self):
        return self.find_element(UserApplicationCreateActivitiesPageLocators.locator_select_protocol_version,time=2).click()

 
    def choose_protocol_name(self):
        return self.find_element(UserApplicationCreateActivitiesPageLocators.locator_choose_protocol_name,time=2).click()


    def select_protocol_name(self):
        return self.find_element(UserApplicationCreateActivitiesPageLocators.locator_select_protocol_name,time=2).click()

    def click_drop_doun_manu(self):
        return self.find_element(UserApplicationCreateActivitiesPageLocators.locator_click_drop_doun_manu,time=2).click()

    def send_login(self):
        login_field = self.find_element(UserApplicationCreateActivitiesPageLocators.locator_login_send_keys,time=2)
        search_input = login_field.find_element_by_tag_name("input")
        search_input.send_keys("test@test.org", Keys.ENTER)

    def send_password(self):
        login_field = self.find_element(UserApplicationCreateActivitiesPageLocators.locator_password_send_keys,time=2)
        search_input = login_field.find_element_by_tag_name("input")
        search_input.send_keys("testtestyan", Keys.ENTER)

    def click_on_the_login_button(self):
        return self.find_element(UserApplicationCreateActivitiesPageLocators.locator_click_login_button,time=2).click()

    def click_activities_button(self):
        return self.find_element(UserApplicationCreateActivitiesPageLocators.locator_click_activities_button,time=2).click()

    def click_add_new_button(self):
        return self.find_element(UserApplicationCreateActivitiesPageLocators.locator_click_add_new_button,time=2).click()

    def send_keys_coustmer_name(self):
        login_field = self.find_element(UserApplicationCreateActivitiesPageLocators.locator_send_keys_coustmer_name,time=2)
        search_input = login_field.find_element_by_tag_name("input")
        search_input.send_keys("Test Coustmer", Keys.ENTER)

    def select_instrument_name(self):
        return self.find_element(UserApplicationCreateActivitiesPageLocators.locator_select_instrument_name,time=2).click()

    def choose_instrument_name(self):
        return self.find_element(UserApplicationCreateActivitiesPageLocators.locator_choose_instrument_name,time=2).click()


  
