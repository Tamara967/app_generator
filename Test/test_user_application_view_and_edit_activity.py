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

from user_application_view_and_edit_activity import UserAplicatioViewAndEditActivitesPage
from config import *



class UserAplicatioViewAndEditActivitesPageLocators:
    locator_login_send_keys = (By.XPATH, '/html/body/div/div[1]/div/div/div/div/div/div/div/form/div[1]/div/div[1]/div')
    locator_password_send_keys = (By.XPATH, '/html/body/div/div[1]/div/div/div/div/div/div/div/form/div[2]/div/div[1]/div[1]')
    locator_click_login_button = (By.XPATH, "/html/body/div/div[1]/div/div/div/div/div/div/div/form/div[5]/button/span")
    locator_click_drop_down_menu = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div/div[4]/button")
    locator_click_activity_button = (By.XPATH, "/html/body/div/div[1]/div[1]/nav/div[1]/div[2]/div[1]/div/a")   
    locator_click_on_the_edit_icon = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div/main/div/div[3]/div[1]/table/tbody/tr/td[11]/a/button")
    locator_fill_feild = (By.XPATH, '/html/body/div/div[1]/div[2]/div/div/main/div/div[2]/div/form/div[2]/div/div[1]/div[1]/div/div/div/div[2]/div[2]')
    locator_browse_page = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div/main/div/div[3]/div/div/div/div/nav/ul")
    locator_click_on_the_button_save = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div/main/div/button/span")
    locator_click_on_the_generate = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/main/div/div[2]/div/form/div[2]/div/div[2]/input")
    locator_assert_geterate_successful = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/main/div/div[2]/div/form/div[2]/div/div/h4")


class TestUserAplicatioViewAndEditActivitesPage(UserAplicatioViewAndEditActivitesPage):
    def assert_geterate_successful(self):
        check_success_message = "File was successfully generated."
        e_element = self.find_element(UserAplicatioViewAndEditActivitesPageLocators.locator_assert_geterate_successful,time=2)
        text = self.driver.execute_script("return arguments[0].innerText;", e_element)
        if check_success_message in text:
            print("File was successfully generated")

    def click_on_the_generate(self):
        return self.find_element(UserAplicatioViewAndEditActivitesPageLocators.locator_click_on_the_generate,time=2).click()

    def click_on_the_button_save(self):
        return self.find_element(UserAplicatioViewAndEditActivitesPageLocators.locator_click_on_the_button_save,time=2).click()
    
    def fill_feild(self):
        frist_field = self.find_element(UserAplicatioViewAndEditActivitesPageLocators.locator_fill_feild,time=2)
        search_input = frist_field.find_element_by_tag_name("input")
        search_input.send_keys("test", Keys.ENTER)


    def click_on_the_edit_icon(self):
        return self.find_element(UserAplicatioViewAndEditActivitesPageLocators.locator_click_on_the_edit_icon,time=2).click()

    def click_activity_button(self):
        return self.find_element(UserAplicatioViewAndEditActivitesPageLocators.locator_click_activity_button,time=2).click()

    def send_login(self):
        login_field = self.find_element(UserAplicatioViewAndEditActivitesPageLocators.locator_login_send_keys,time=2)
        search_input = login_field.find_element_by_tag_name("input")
        search_input.send_keys("tamara@testorgdom.org", Keys.ENTER)

    def send_password(self):
        login_field = self.find_element(UserAplicatioViewAndEditActivitesPageLocators.locator_password_send_keys,time=2)
        search_input = login_field.find_element_by_tag_name("input")
        search_input.send_keys("tamaratestorgdom.org", Keys.ENTER)

    def click_on_the_login_button(self):
        return self.find_element(UserAplicatioViewAndEditActivitesPageLocators.locator_click_login_button,time=2).click()
    
    def click_drop_down_menu(self):
        return self.find_element(UserAplicatioViewAndEditActivitesPageLocators.locator_click_drop_down_menu,time=2).click()


