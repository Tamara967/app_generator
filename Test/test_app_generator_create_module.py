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

from app_generator_create_module import AppGeneratorCreateModulePage
from config import *



class TestAppGeneratorCreateModulePageLocators:
    locator_login_send_keys = (By.XPATH, '//*[@id="input-7"]')
    locator_password_send_keys = (By.XPATH, '//*[@id="input-10"]')
    locator_click_login_button = (By.XPATH, "/html/body/div/div[1]/div/div/div/div/div/div/div/form/div[4]/button/span")
    locator_click_module_button = (By.XPATH, "/html/body/div/div[1]/div[1]/nav/div[1]/div[2]/div[8]/div/a") 
    locator_create_new_module = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[1]/main/div/div[2]/div[3]/button/span")
    locator_select_organization_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div[1]/div[1]/div/div/div[1]/div[1]/div/div/i")
    locator_choose_organization_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[4]/div/div[1]/div/div")
    locator_select_instrument_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div[1]/div[2]/div/div/div[1]/div[1]/div/div/i")
    locator_choose_instrument_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[5]/div/div[1]/div/div")
    locator_select_protocol_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div[2]/div[1]/div/div/div[1]/div[1]/div/div/i")
    locator_choose_protocol_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[6]/div/div[1]/div/div")
    locator_select_protocol_version_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div[2]/div[2]/div/div/div[1]/div[1]/div/div/i")
    locator_choose_protocol_version_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[7]/div/div[1]/div/div")
    locator_send_keys_module_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div[3]/div[1]/div/div/div[1]/div")
    locator_click_on_the_save_button = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[3]/button[2]/span")


class TestAppGeneratorCreateModulePage(AppGeneratorCreateModulePage):
    def click_on_the_save_button(self):
        return self.find_element(TestAppGeneratorCreateModulePageLocators.locator_click_on_the_save_button,time=2).click()


    def send_keys_module_name(self, time):
        
        element = self.find_element(TestAppGeneratorCreateModulePageLocators.locator_send_keys_module_name,time=2)
        element.click()
        search = element.find_element_by_tag_name("input")
        search.send_keys("test_module_name{} ".format(time), Keys.ENTER)

    def choose_protocol_version_name(self):
        return self.find_element(TestAppGeneratorCreateModulePageLocators.locator_choose_protocol_version_name,time=2).click()


    def select_protocol_version_name(self):
        return self.find_element(TestAppGeneratorCreateModulePageLocators.locator_select_protocol_version_name,time=2).click()


    def choose_protocol_name(self):
        return self.find_element(TestAppGeneratorCreateModulePageLocators.locator_choose_protocol_name,time=2).click()


    def select_protocol_name(self):
        return self.find_element(TestAppGeneratorCreateModulePageLocators.locator_select_protocol_name,time=2).click()

    def choose_instrument_name(self):
        return self.find_element(TestAppGeneratorCreateModulePageLocators.locator_choose_instrument_name,time=2).click()


    def select_instrument_name(self):
        return self.find_element(TestAppGeneratorCreateModulePageLocators.locator_select_instrument_name,time=2).click()


    def choose_organization_name(self):
        return self.find_element(TestAppGeneratorCreateModulePageLocators.locator_choose_organization_name,time=2).click()


    def select_organization_name(self):
        return self.find_element(TestAppGeneratorCreateModulePageLocators.locator_select_organization_name,time=2).click()

    def send_login(self):
        login_field = self.find_element(TestAppGeneratorCreateModulePageLocators.locator_login_send_keys)
        login_field.send_keys('appgenerator.rm@gmail.com')

    def send_password(self):
        password_field = self.find_element(TestAppGeneratorCreateModulePageLocators.locator_password_send_keys)
        password_field.send_keys('App2020*')

    def click_on_the_login_button(self):
        return self.find_element(TestAppGeneratorCreateModulePageLocators.locator_click_login_button,time=2).click()

    def click_module_button(self):
        return self.find_element(TestAppGeneratorCreateModulePageLocators.locator_click_module_button,time=2).click()

    def create_new_module(self):
        return self.find_element(TestAppGeneratorCreateModulePageLocators.locator_create_new_module,time=2).click()


