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

from user_appliction_send_to_review import ActivitiesSendToReviewPage
from config import *



class ActivitiesSendToReviewPageLocators:
    locator_login_send_keys = (By.XPATH, '/html/body/div/div[1]/div/div/div/div/div/div/div/form/div[1]/div/div[1]/div')
    locator_password_send_keys = (By.XPATH, '/html/body/div/div[1]/div/div/div/div/div/div/div/form/div[2]/div/div[1]/div[1]')
    locator_click_login_button = (By.XPATH, "/html/body/div/div[1]/div/div/div/div/div/div/div/form/div[5]/button/span")
    locator_open_main_manu = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div/button/span/i")
    locator_click_activites_button = (By.XPATH, "/html/body/div/div[1]/div[1]/nav/div[1]/div[2]/div[1]/div/a")
    locator_click_send_to_review_button = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div/main/div/div[3]/div[1]/table/tbody/tr/td[11]/button[4]")    
    locator_click_section_reason_field = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div/div[1]/div/div/div[1]/div[1]")
    locator_click_reason_name = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[4]/div/div[1]/div/div")
    locator_select_review_field = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/form/div/div[3]/div/div/div[1]/div[1]/div[2]/div/i")
    locator_select_reviewer = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[5]/div/div/div/div")
    locator_click_send_button = (By.XPATH, "/html/body/div/div[1]/div[2]/div/div[3]/div/div/div[3]/button[2]/span")
 
class TestActivitiesSendToReviewPage(ActivitiesSendToReviewPage):
    def click_send_button(self):
        return self.find_element(ActivitiesSendToReviewPageLocators.locator_click_send_button,time=2).click()

    def click_reason_name(self):
        return self.find_element(ActivitiesSendToReviewPageLocators.locator_click_reason_name,time=2).click()


    def select_reviewer(self):
        return self.find_element(ActivitiesSendToReviewPageLocators.locator_select_reviewer,time=2).click()

    def select_review_field(self):
        return self.find_element(ActivitiesSendToReviewPageLocators.locator_select_review_field,time=2).click()

    def click_section_reason_field(self):
        return self.find_element(ActivitiesSendToReviewPageLocators.locator_click_section_reason_field,time=2).click()

    def click_send_to_review_button(self):
        return self.find_element(ActivitiesSendToReviewPageLocators.locator_click_send_to_review_button,time=2).click()

    def click_activites_button(self):
        return self.find_element(ActivitiesSendToReviewPageLocators.locator_click_activites_button,time=2).click()


    def open_main_manu(self):
        return self.find_element(ActivitiesSendToReviewPageLocators.locator_open_main_manu,time=2).click()

    def send_login(self):
        login_field = self.find_element(ActivitiesSendToReviewPageLocators.locator_login_send_keys,time=2)
        search_input = login_field.find_element_by_tag_name("input")
        search_input.send_keys("testtest@test.org", Keys.ENTER)

    def send_password(self):
        login_field = self.find_element(ActivitiesSendToReviewPageLocators.locator_password_send_keys,time=2)
        search_input = login_field.find_element_by_tag_name("input")
        search_input.send_keys("testtest", Keys.ENTER)

    def click_on_the_login_button(self):
        return self.find_element(ActivitiesSendToReviewPageLocators.locator_click_login_button,time=2).click()



