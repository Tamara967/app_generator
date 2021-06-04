from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import os

def get_path(path):
    os.chdir(path)
    sys.path.insert(0,path)


get_path("/home/erida-employee/Desktop/ssh/page_class/App_Gnerator/Page")
get_path("/home/erida-employee/Desktop/ssh/page_class/App_Gnerator")

from app_generator_add_new_organisation import AppGeneratorAddNewOrganisation
from config import *



class AppGeneratorAddNewOrganisationLocator:
    locator_login_send_keys = (By.XPATH, '//*[@id="input-7"]')
    locator_password_send_keys = (By.XPATH, '//*[@id="input-10"]')
    locator_click_login_button = (By.XPATH, "/html/body/div/div[1]/div/div/div/div/div/div/div/form/div[4]/button/span")
    locator_click_on_the_organization_button = (By.XPATH, "/html/body/div/div[1]/div[1]/nav/div[1]/div[2]/div[1]/div/a")
    locator_click_add_new_button = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div/main/div/div[2]/div[3]/button/span")
    locator_add_new_organization = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div/div[1]")
    locator_all_input_name = (By.CLASS_NAME, "v-dialog__content v-dialog__content--active")
    locator_find_input_field = (By.TAG_NAME, "input")
    locator_click_on_the_save_organization_button = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[3]/button[2]")
    

class TestAppGeneratorAddNewOrganisation(AppGeneratorAddNewOrganisation):

    def send_login(self):
        login_field = self.find_element(AppGeneratorAddNewOrganisationLocator.locator_login_send_keys)
        login_field.send_keys('appgenerator.rm@gmail.com')

    def send_password(self):
        password_field = self.find_element(AppGeneratorAddNewOrganisationLocator.locator_password_send_keys)
        password_field.send_keys('App2020*')

    def click_on_the_login_button(self):
        return self.find_element(AppGeneratorAddNewOrganisationLocator.locator_click_login_button,time=2).click()
    
    def check_login_home(self, load_page_title):
        return True

    def click_on_the_save_organization_button(self):
        return self.find_element(AppGeneratorAddNewOrganisationLocator.locator_click_on_the_save_organization_button,time=2).click()
 
    def click_on_the_organization_button(self):
        return self.find_element(AppGeneratorAddNewOrganisationLocator.locator_click_on_the_organization_button,time=2).click()

    def click_add_new_organization(self):
        return self.find_element(AppGeneratorAddNewOrganisationLocator.locator_click_add_new_button,time=2).click()


















