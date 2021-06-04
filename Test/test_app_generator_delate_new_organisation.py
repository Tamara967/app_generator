from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import os

def get_path(path):
    os.chdir(path)
    sys.path.insert(0,path)


get_path("/home/erida-employee/Desktop/ssh/page_class/App_Gnerator/Page")
get_path("/home/erida-employee/Desktop/ssh/page_class/App_Gnerator")

from app_generator_delate_new_organisation import AppGeneratorDelateNewOrganisation
from config import *



class AppGeneratorDelateNewOrganisationLocator:
    locator_login_send_keys = (By.XPATH, '//*[@id="input-7"]')
    locator_password_send_keys = (By.XPATH, '//*[@id="input-10"]')
    locator_click_login_button = (By.XPATH, "/html/body/div/div[1]/div/div/div/div/div/div/div/form/div[4]/button/span")
    locator_click_on_the_organization_button = (By.XPATH, "/html/body/div/div[1]/div[1]/nav/div[1]/div[2]/div[1]/div/a")
    locator_click_in_delate_icon = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div/main/div/div[3]/div[1]/table/tbody/tr[1]/td[12]/button[3]")    
    locator_clik_on_the_button = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[3]/button[2]/span")    


class TestAppGeneratorDelateNewOrganisation(AppGeneratorDelateNewOrganisation):
    def send_login(self):
        login_field = self.find_element(AppGeneratorDelateNewOrganisationLocator.locator_login_send_keys)
        login_field.send_keys('appgenerator.rm@gmail.com')

    def send_password(self):
        password_field = self.find_element(AppGeneratorDelateNewOrganisationLocator.locator_password_send_keys)
        password_field.send_keys('App2020*')

    def click_on_the_login_button(self):
        return self.find_element(AppGeneratorDelateNewOrganisationLocator.locator_click_login_button,time=2).click()

    def click_on_the_organization_button(self):
        return self.find_element(AppGeneratorDelateNewOrganisationLocator.locator_click_on_the_organization_button,time=2).click()

    def click_in_delate_icon(self):
        return self.find_element(AppGeneratorDelateNewOrganisationLocator.locator_click_in_delate_icon,time=2).click()

    def clik_on_the_button(self):
        return self.find_element(AppGeneratorDelateNewOrganisationLocator.locator_clik_on_the_button,time=2).click()
