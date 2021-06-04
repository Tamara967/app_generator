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

from app_generator_create_user import AppGeneratorCheckAndCreateOrganisationUser
from config import *



class AppGeneratorCheckAndCreateOrganisationUserLocators:
    locator_login_send_keys = (By.XPATH, '//*[@id="input-7"]')
    locator_password_send_keys = (By.XPATH, '//*[@id="input-10"]')
    locator_click_login_button = (By.XPATH, "/html/body/div/div[1]/div/div/div/div/div/div/div/form/div[4]/button/span")
    
    locator_click_on_the_organization_button = (By.XPATH, "/html/body/div/div[1]/div[1]/nav/div[1]/div[2]/div[1]/div/a")
    locator_click_add_new_organization = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div/main/div/div[2]/div[3]/button/span")
    locator_click_on_the_save_organization_button = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[3]/button[2]/span")
    locotor_click_drop_doun_manu = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div/button/span/i")
    locator_click_on_the_roles = (By.XPATH, "/html/body/div/div[1]/div[1]/nav/div[1]/div[2]/div[3]/div/div[1]")
    locator_click_on_the_organization_roles = (By.XPATH, "/html/body/div/div[1]/div[1]/nav/div[1]/div[2]/div[3]/div/div[2]/div[1]/div/a")
    locator_assert_test_engineer = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div/main/div/div[3]/div[1]/table/tbody/tr[1]")
    locator_assert_test_manager = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div/main/div/div[3]/div[1]/table/tbody/tr[2]")
    locator_assert_test_administrator = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div/main/div/div[3]/div[1]/table/tbody/tr[3]")
    locator_click_new_role_button = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[1]/main/div/div[2]/div[3]/button/span")
    locator_select_org_name = (By.XPATH, '/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div/div[1]/div/div/div[1]/div[1]/div/div/i') 
    locator_click_org_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[4]/div/div[1]/div/div")
    locator_click_role_name = (By.XPATH, '/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div/div[2]/div/div/div[1]/div')
    locator_click_save_button = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[3]/button[2]/span")
    locator_click_on_the_user_button = (By.XPATH, "/html/body/div/div[1]/div[1]/nav/div[1]/div[2]/div[2]/div/div[1]/div[1]") 
    locator_click_organization_user = (By.XPATH, "/html/body/div/div[1]/div[1]/nav/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/a")
    locator_assert_test_administrator = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div/main/div/div[2]/div[2]/div[1]/table/tbody/tr[1]")
    locator_click_on_the_add_new_button = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div/main/div/div[2]/div[1]/div[3]/button/span")
    locator_select_organization_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div/div[1]/div/div/div[1]/div[1]/div/div/i")
    locator_click_on_the_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[4]/div/div[1]/div/div")
    locator_send_keys_full_name = (By.XPATH, '/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div/div[2]/div/div/div[1]/div')
    locator_select_role_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div/div[3]/div/div/div[1]/div[1]/div/div/i")

    locator_click_an_the_role_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[5]/div/div[1]/div/div")
    locator_send_keys_email_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div/div[4]/div/div/div[1]/div")
    locator_send_keys_email_password = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div/div[5]/div/div/div[1]/div")
    locator_click_on_the_save_button = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[3]/button[2]/span")
   
class TestAppGeneratorCheckAndCreateOrganisationUser(AppGeneratorCheckAndCreateOrganisationUser):

    def send_login(self):
        login_field = self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locator_login_send_keys)
        login_field.send_keys('appgenerator.rm@gmail.com')

    def send_password(self):
        password_field = self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locator_password_send_keys)
        password_field.send_keys('App2020*')

    def click_on_the_login_button(self):
        return self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locator_click_login_button,time=2).click()
    
    def check_login_home(self, load_page_title):
        return True

    def click_on_the_organization_button(self):
        return self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locator_click_on_the_organization_button,time=2).click()

    def click_add_new_organization(self):
        return self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locator_click_add_new_organization,time=2).click()

    def click_on_the_save_organization_button(self):
        return self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locator_click_on_the_save_organization_button,time=2).click()


    def click_drop_doun_manu(self):
        return self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locotor_click_drop_doun_manu,time=2).click()

    def click_on_the_roles(self):
        return self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locator_click_on_the_roles,time=2).click()    

    def click_on_the_organization_roles(self):
        return self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locator_click_on_the_organization_roles,time=2).click()

    def assert_test_engineer(self):
        check_engineer = "Test Engineer"
        e_element = self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locator_assert_test_engineer,time=2)
        text = self.driver.execute_script("return arguments[0].innerText;", e_element)
        if check_engineer in text:
            print("There is a default engineer")
          
        #time.sleep(10)
        check_engineer = "Test Manager"
        m_element = self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locator_assert_test_manager,time=2)
        text = self.driver.execute_script("return arguments[0].innerText;", m_element)
        if check_engineer in text:
            print("There is a default manager")
        #time.sleep(10)

        check_engineer = "Test Administrator"
        a_element = self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locator_assert_test_administrator,time=2)
        text = self.driver.execute_script("return arguments[0].innerText;", a_element)
        if check_engineer in text:
            print("There is a default administrator")
            
        return True   

    def click_new_role_button(self):
        return self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locator_click_new_role_button,time=2).click()

    def select_org_name(self):
        return self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locator_select_org_name,time=2).click() 

    def click_org_name(self):
        return self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locator_click_org_name,time=2).click()

    def click_role_name(self, time):
        element = self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locator_click_role_name,time=10)
        element.click() 
        search = element.find_element_by_tag_name("input")
        search.send_keys("Admin{}".format(time), Keys.ENTER)

    def click_on_the_save_button(self):
        return self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locator_click_save_button,time=2).click()

    def click_on_the_user_button(self):
        return self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locator_click_on_the_user_button,time=2).click()

    def click_organization_user(self):
        return self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locator_click_organization_user,time=2).click()

    def assert_test_administrator(self):
        check_engineer = "Test Administrator"
        e_element = self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locator_assert_test_administrator,time=2)
        text = self.driver.execute_script("return arguments[0].innerText;", e_element)
        if check_engineer in text:
            print("There is a default engineer")
        
        return True

    def click_on_the_add_new_button(self):
        return self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locator_click_on_the_add_new_button,time=2).click()

    def select_organization_name(self):
         return self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locator_select_organization_name,time=2).click()

    def click_on_the_name(self):
         return self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locator_click_on_the_name,time=2).click()
   
    def send_keys_full_name(self):
        element = self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locator_send_keys_full_name,time=2)
        element.click() 
        search = element.find_element_by_tag_name("input")
        search.send_keys("Test Testyan", Keys.ENTER)
    
    def select_role_name(self):
         return self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locator_select_role_name,time=2).click()

    def click_an_the_role_name(self):
         return self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locator_click_an_the_role_name,time=2).click()

    def send_keys_email_name(self):
        element = self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locator_send_keys_email_name,time=2)
        element.click() 
        search = element.find_element_by_tag_name("input")
        search.send_keys("testtest@test.com", Keys.ENTER)

    def send_keys_email_password(self):
        element = self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locator_send_keys_email_password,time=2)
        element.click()
        search = element.find_element_by_tag_name("input")
        search.send_keys("testtesttest", Keys.ENTER)

    def click_on_the_save_button(self):
         return self.find_element(AppGeneratorCheckAndCreateOrganisationUserLocators.locator_click_on_the_save_button,time=2).click()







