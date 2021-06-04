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

from app_generator_create_instrument_pratacol_version import CreateInstrumentProtocolVersion
from config import *



class TestCreateInstrumentProtocolVersionLocators:
    locator_login_send_keys = (By.XPATH, '//*[@id="input-7"]')
    locator_password_send_keys = (By.XPATH, '//*[@id="input-10"]')
    locator_click_login_button = (By.XPATH, "/html/body/div/div[1]/div/div/div/div/div/div/div/form/div[4]/button/span")
    locator_click_on_the_instrument = (By.XPATH, "/html/body/div/div[1]/div[1]/nav/div[1]/div[2]/div[5]/div/a")   
    locator_create_new_instrument = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div/main/div/div[2]/div[3]/button/span")
    locator_select_organization_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div/div[1]/div/div/div[1]/div[1]/div/div/i")
    locator_choose_organization_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[4]/div/div[1]/div/div")
    locator_send_keys_instrument_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div/div[2]/div/div/div[1]/div")
    locator_click_instrument_save_button = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[3]/button[2]/span")
    locator_click_on_the_drop_douwn_manu = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div/button/span/i")
    locator_click_on_the_protocols_button = (By.XPATH, "/html/body/div/div[1]/div[1]/nav/div[1]/div[2]/div[6]/div/a")
    locator_create_new_protocols = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div/main/div/div[2]/div[3]/button/span") 
    locator_select_org_name_pratacols = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div[1]/div[1]/div/div/div[1]/div[1]/div/div/i")
    locator_choose_org_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[4]/div/div[1]/div/div")
    locator_select_instrument_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div[1]/div[2]/div/div/div[1]/div[1]/div/div/i")
    locator_choose_instrument_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[5]/div/div[1]/div/div")
    locator_send_keys_protocols_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div[2]/div[1]/div/div/div[1]/div")
    locator_click_protocols_save_button = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[3]/button[2]/span")
    locator_click_protocols_version_button = (By.XPATH, "/html/body/div/div[1]/div[1]/nav/div[1]/div[2]/div[7]/div/a")
    locator_create_new_protocols_version = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div/main/div/div[2]/div[3]/button/span")
    locator_select_org_name_in_pro_version = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div/div[1]/div/div/div[1]/div[1]/div/div/i")
    locator_choose_org_name_for_protocol_version = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[4]/div/div[1]/div/div")  
    locator_select_instrument_name_for_protocol_version = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div/div[2]/div/div/div[1]/div[1]/div/div/i")
    locator_choose_ins_name_for_protocol_version = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[5]/div/div[1]/div/div")
    locator_select_protocol_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div/div[3]/div/div/div[1]/div[1]/div/div/i")
    locator_choose_protocol_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[6]/div/div/div/div")
    locator_save_protocol_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[3]/button[2]/span")
    locator_send_keys_protocol_version = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div/div[4]/div/div/div[1]/div")


class TestCreateInstrumentProtocolVersion(CreateInstrumentProtocolVersion):

    def send_login(self):
        login_field = self.find_element(TestCreateInstrumentProtocolVersionLocators.locator_login_send_keys)
        login_field.send_keys('appgenerator.rm@gmail.com')

    def send_password(self):
        password_field = self.find_element(TestCreateInstrumentProtocolVersionLocators.locator_password_send_keys)
        password_field.send_keys('App2020*')

    def click_on_the_login_button(self):
        return self.find_element(TestCreateInstrumentProtocolVersionLocators.locator_click_login_button,time=2).click()

    def click_on_the_instrument(self):
        return self.find_element(TestCreateInstrumentProtocolVersionLocators.locator_click_on_the_instrument,time=2).click()

    def create_new_instrument(self):
        return self.find_element(TestCreateInstrumentProtocolVersionLocators.locator_create_new_instrument,time=2).click()

    def select_organization_name(self):
        return self.find_element(TestCreateInstrumentProtocolVersionLocators.locator_select_organization_name,time=2).click()

    def choose_organization_name(self):
        return self.find_element(TestCreateInstrumentProtocolVersionLocators.locator_choose_organization_name,time=2).click()

    def send_keys_instrument_name(self, time):
        element = self.find_element(TestCreateInstrumentProtocolVersionLocators.locator_send_keys_instrument_name,time=2)
        element.click()
        search = element.find_element_by_tag_name("input")
        search.send_keys("test_instrument{}".format(time), Keys.ENTER)

    def click_instrument_save_button(self):
        return self.find_element(TestCreateInstrumentProtocolVersionLocators.locator_click_instrument_save_button,time=2).click()

    def click_on_the_drop_douwn_manu(self):
        return self.find_element(TestCreateInstrumentProtocolVersionLocators.locator_click_on_the_drop_douwn_manu,time=2).click()
 
    def click_on_the_protocols_button(self):
        return self.find_element(TestCreateInstrumentProtocolVersionLocators.locator_click_on_the_protocols_button,time=2).click()
    
    def create_new_protocols(self):
        return self.find_element(TestCreateInstrumentProtocolVersionLocators.locator_create_new_protocols,time=2).click()

    def select_org_name_pratacols(self):
        return self.find_element(TestCreateInstrumentProtocolVersionLocators.locator_select_org_name_pratacols,time=2).click()

    def choose_org_name(self):
        return self.find_element(TestCreateInstrumentProtocolVersionLocators.locator_choose_org_name,time=2).click()

    def select_instrument_name(self):
        return self.find_element(TestCreateInstrumentProtocolVersionLocators.locator_select_instrument_name,time=2).click()

    def choose_instrument_name(self):
        return self.find_element(TestCreateInstrumentProtocolVersionLocators.locator_choose_instrument_name,time=2).click()

    def send_keys_protocols_name(self, time):
        element =  self.find_element(TestCreateInstrumentProtocolVersionLocators.locator_send_keys_protocols_name,time=2)
        element.click()
        search = element.find_element_by_tag_name("input")
        search.send_keys("test_prtocol{}".format(time), Keys.ENTER)

    def click_protocols_save_button(self):
        return self.find_element(TestCreateInstrumentProtocolVersionLocators.locator_click_protocols_save_button,time=2).click()

    def click_protocols_version_button(self):
        return self.find_element(TestCreateInstrumentProtocolVersionLocators.locator_click_protocols_version_button,time=2).click()

    def create_new_protocols_version(self):
        return self.find_element(TestCreateInstrumentProtocolVersionLocators.locator_create_new_protocols_version,time=2).click()

    def select_org_name_in_pro_version(self):
        return self.find_element(TestCreateInstrumentProtocolVersionLocators.locator_select_org_name_in_pro_version,time=2).click()

    def choose_org_name_for_protocol_version(self):
        return self.find_element(TestCreateInstrumentProtocolVersionLocators.locator_choose_org_name_for_protocol_version,time=2).click()

    def select_instrument_name_for_protocol_version(self):
        return self.find_element(TestCreateInstrumentProtocolVersionLocators.locator_select_instrument_name_for_protocol_version,time=2).click()

    def choose_ins_name_for_protocol_version(self):
        return self.find_element(TestCreateInstrumentProtocolVersionLocators.locator_choose_ins_name_for_protocol_version,time=2).click()

    def select_protocol_name(self):
        return self.find_element(TestCreateInstrumentProtocolVersionLocators.locator_select_protocol_name,time=2).click()

    def choose_protocol_name(self):
        return self.find_element(TestCreateInstrumentProtocolVersionLocators.locator_choose_protocol_name,time=2).click()

    def save_protocol_version(self):
        return self.find_element(TestCreateInstrumentProtocolVersionLocators.locator_save_protocol_name,time=2).click()
    
    def send_keys_protocol_version(self, time):
        element =  self.find_element(TestCreateInstrumentProtocolVersionLocators.locator_send_keys_protocol_version,time=2)
        element.click()
        search = element.find_element_by_tag_name("input")
        search.send_keys("test_prtocol_version{}".format(time), Keys.ENTER)







