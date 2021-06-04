from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import os

def get_path(path):
    os.chdir(path)
    sys.path.insert(0,path)


get_path("/home/erida-employee/Desktop/ssh/page_class/App_Gnerator/Page")
get_path("/home/erida-employee/Desktop/ssh/page_class/App_Gnerator")

from app_generator_edit_new_organisation import AppGeneratorEditNewOrganisation
from config import *



class AppGeneratorEditNewOrganisationLocator:
    locator_login_send_keys = (By.XPATH, '//*[@id="input-7"]')
    locator_password_send_keys = (By.XPATH, '//*[@id="input-10"]')
    locator_click_login_button = (By.XPATH, "/html/body/div/div[1]/div/div/div/div/div/div/div/form/div[4]/button/span")
    locator_click_on_the_organization_button = (By.XPATH, "/html/body/div/div[1]/div[1]/nav/div[1]/div[2]/div[1]/div/a")
    locator_click_edit_button = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[1]/main/div/div[3]/div[1]/table/tbody/tr[1]/td[12]/button[1]")
    locator_edit_ful_name = (By.XPATH, '//*[@id="input-229"]')
    locator_click_on_the_save_button = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[3]/button[2]/span")


class TestAppGeneratorEditNewOrganisation(AppGeneratorEditNewOrganisation):

    def send_login(self):
        login_field = self.find_element(AppGeneratorEditNewOrganisationLocator.locator_login_send_keys)
        login_field.send_keys('appgenerator.rm@gmail.com')

    def send_password(self):
        password_field = self.find_element(AppGeneratorEditNewOrganisationLocator.locator_password_send_keys)
        password_field.send_keys('App2020*')

    def click_on_the_login_button(self):
        return self.find_element(AppGeneratorEditNewOrganisationLocator.locator_click_login_button,time=2).click() 
 
    def click_on_the_organization_button(self):
        return self.find_element(AppGeneratorEditNewOrganisationLocator.locator_click_on_the_organization_button,time=2).click()

    def click_edit_button(self):
        return self.find_element(AppGeneratorEditNewOrganisationLocator.locator_click_edit_button,time=2).click()

    def edit_ful_name(self):
        full_name =  self.find_element(AppGeneratorEditNewOrganisationLocator.locator_edit_ful_name,time=2)
        full_name.click()
        full_name.clear()
        full_name.send_keys("fagag")

    def click_on_the_save_button(self):
        return self.find_element(AppGeneratorEditNewOrganisationLocator.locator_click_on_the_save_button,time=2).click()















