from test_app_generator_edit_new_organisation import *
from test_app_generator_delate_new_organisation import *
from test_app_generator_login_page import *
from test_app_generator_add_new_organisation import *
from test_app_generator_create_role import *
from test_app_generator_create_user import *
from test_app_generator_create_instrument_pratacol_version import *
from test_app_generator_create_module import *
from test_user_application_login_logout_page import *
from test_user_application_create_activities import *
from test_user_application_activities_copy_activity import *
from test_user_application_activities_complete_activity import *
from test_activities_archive_completed_activity import *
from test_user_appliction_send_to_with_select_review import *
from test_user_appliction_send_to_with_invite_review import *
from test_user_appliction_delete_activites import *
from config import *
import time

def case_1(page_link):
    try:
        home_page_link = get_home_page_link()
        test_app_generator_login_page = TestAppGeneratorLoginLogoutPage(webdriver.Chrome(), page_link)
        test_app_generator_login_page.go_to_site()
        test_app_generator_login_page.send_login()
        test_app_generator_login_page.send_password()
        test_app_generator_login_page.click_on_the_login_button()
        if test_app_generator_login_page.check_login_home(home_page_link):
            test_app_generator_login_page.implicitly_wait()
            test_app_generator_login_page.click_drop_down_menu()
            test_app_generator_login_page.click_on_the_logout_button()
            test_app_generator_login_page.quit_driver()
            print("Test case is passed")
        
    except Exception as err:
        print("Something did not work out, please try again")


def case_2(page_link):
    try:
        test_add_new_organization = TestAppGeneratorAddNewOrganisation(webdriver.Chrome(), page_link)
        test_add_new_organization.go_to_site()
    
        time.sleep(10)
        test_add_new_organization.send_login()
        test_add_new_organization.send_password()
        test_add_new_organization.click_on_the_login_button()
        time.sleep(10)
        test_add_new_organization.click_on_the_organization_button()
        time.sleep(10)
        test_add_new_organization.click_add_new_organization()
        test_add_new_organization.get_all_elements()
        time.sleep(10)
        test_add_new_organization.click_on_the_save_organization_button()
        time.sleep(10)
        print("Test case is passed")

    except Exception as err:
        print("Something did not work out, please try again")


def case_3(page_link):
        test_edit_new_organization = TestAppGeneratorEditNewOrganisation(webdriver.Chrome(), page_link)
        test_edit_new_organization.go_to_site()

        time.sleep(10)
        test_edit_new_organization.send_login()
        test_edit_new_organization.send_password()
        test_edit_new_organization.click_on_the_login_button()
        time.sleep(10)
        test_edit_new_organization.click_on_the_organization_button()
        time.sleep(10)
        print("111") 
        test_edit_new_organization.click_edit_button()       
        #test_edit_new_organization.click_on_the_edit_button()
        time.sleep(10)
        test_edit_new_organization.edit_ful_name()
        time.sleep(25)
        test_edit_new_organization.click_on_the_save_button()
        time.sleep(10)
        test_edit_new_organization.quit_driver()
        time.sleep(4)


def case_4(page_link):
    test_delate_new_organization = TestAppGeneratorDelateNewOrganisation(webdriver.Chrome(), page_link)
    test_delate_new_organization.go_to_site()
    test_delate_new_organization.send_login()
    test_delate_new_organization.send_password()
    test_delate_new_organization.click_on_the_login_button()
    time.sleep(10)

    test_delate_new_organization.click_on_the_organization_button()
    time.sleep(20)
    test_delate_new_organization.click_in_delate_icon()
    time.sleep(15)
    test_delate_new_organization.clik_on_the_button()
    time.sleep(5)
    test_delate_new_organization.quit_driver()

def case_5(page_link):
        test_check_and_create_organisation_role = TestAppGeneratorCheckAndCreateOrganisationRole(webdriver.Chrome(), page_link)
        test_check_and_create_organisation_role.go_to_site()

        time.sleep(10)
        test_check_and_create_organisation_role.send_login()
        test_check_and_create_organisation_role.send_password()
        test_check_and_create_organisation_role.click_on_the_login_button()
        time.sleep(10)
        
        test_check_and_create_organisation_role.click_on_the_organization_button()
        time.sleep(10)
        test_check_and_create_organisation_role.click_add_new_organization()
        test_check_and_create_organisation_role.get_all_elements()
        time.sleep(10)
        test_check_and_create_organisation_role.click_on_the_save_organization_button()
        time.sleep(10)
        test_check_and_create_organisation_role.click_drop_doun_manu()
        time.sleep(10)
        test_check_and_create_organisation_role.click_on_the_roles()
        time.sleep(5)
        test_check_and_create_organisation_role.click_on_the_organization_roles() 
        time.sleep(30)
        print(test_check_and_create_organisation_role.assert_test_engineer())
        test_check_and_create_organisation_role.driver_navigate_refresh()
        time.sleep(20)
        test_check_and_create_organisation_role.click_new_role_button()
        time.sleep(15)
        test_check_and_create_organisation_role.select_org_name()    
        time.sleep(5)
        test_check_and_create_organisation_role.click_org_name()
        time.sleep(25)
        test_check_and_create_organisation_role.click_role_name()
        time.sleep(10)
        test_check_and_create_organisation_role.click_on_the_save_button()
        time.sleep(4)
        print("Test case is passed")

def case_6(page_link):     
        current_time = get_current_time()
        test_check_and_create_organisation_user = TestAppGeneratorCheckAndCreateOrganisationUser(webdriver.Chrome(), page_link)
        test_check_and_create_organisation_user.go_to_site()

        time.sleep(10)
        test_check_and_create_organisation_user.send_login()
        test_check_and_create_organisation_user.send_password()
        test_check_and_create_organisation_user.click_on_the_login_button()
        time.sleep(10)
        test_check_and_create_organisation_user.click_on_the_organization_button()
        time.sleep(10)
        test_check_and_create_organisation_user.click_add_new_organization()
        test_check_and_create_organisation_user.get_all_elements()
        time.sleep(10)
        test_check_and_create_organisation_user.click_on_the_save_organization_button()
        time.sleep(10)
        test_check_and_create_organisation_user.click_drop_doun_manu()
        time.sleep(10)
        test_check_and_create_organisation_user.click_on_the_roles()
        time.sleep(5)
        test_check_and_create_organisation_user.click_on_the_organization_roles()
        time.sleep(20)
        print(test_check_and_create_organisation_user.assert_test_engineer())
        time.sleep(20)
        test_check_and_create_organisation_user.driver_navigate_refresh()
        time.sleep(20)
        test_check_and_create_organisation_user.click_new_role_button()
        time.sleep(15)
        test_check_and_create_organisation_user.select_org_name()
        time.sleep(5)
        test_check_and_create_organisation_user.click_org_name()
        time.sleep(25)
    
        test_check_and_create_organisation_user.click_role_name(current_time)
        time.sleep(10)
        test_check_and_create_organisation_user.click_on_the_save_button()
        time.sleep(4)
        
        test_check_and_create_organisation_user.click_drop_doun_manu()
        test_check_and_create_organisation_user.click_on_the_user_button()
        time.sleep(15)
        test_check_and_create_organisation_user.click_organization_user()
        time.sleep(10)
        if test_check_and_create_organisation_user.assert_test_administrator():
            test_check_and_create_organisation_user.click_on_the_add_new_button()
            test_check_and_create_organisation_user.select_organization_name()
            time.sleep(10) 
            test_check_and_create_organisation_user.click_on_the_name()
            time.sleep(10)
            test_check_and_create_organisation_user.send_keys_full_name()
            time.sleep(10)
            test_check_and_create_organisation_user.select_role_name()
            test_check_and_create_organisation_user.click_an_the_role_name()
            time.sleep(15)
            test_check_and_create_organisation_user.send_keys_email_name()
            test_check_and_create_organisation_user.send_keys_email_password()
            time.sleep(5)
            test_check_and_create_organisation_user.click_on_the_save_button()
            print("Test case is passed")

def case_7(page_link):
    #try:
        current_time = get_current_time()
        test_create_instrument_protocol_version = TestCreateInstrumentProtocolVersion(webdriver.Chrome(), page_link)
        test_create_instrument_protocol_version.go_to_site()

        time.sleep(10)
        test_create_instrument_protocol_version.send_login()
        test_create_instrument_protocol_version.send_password()
        test_create_instrument_protocol_version.click_on_the_login_button()
        time.sleep(15)
       
        test_create_instrument_protocol_version.click_on_the_instrument()
        time.sleep(5)
        test_create_instrument_protocol_version.create_new_instrument()
        test_create_instrument_protocol_version.select_organization_name()
        time.sleep(10)
        test_create_instrument_protocol_version.choose_organization_name()
        test_create_instrument_protocol_version.send_keys_instrument_name(current_time)
        test_create_instrument_protocol_version.click_instrument_save_button()
        time.sleep(10)
        test_create_instrument_protocol_version.click_on_the_drop_douwn_manu()
        time.sleep(5)
        test_create_instrument_protocol_version.click_on_the_protocols_button()
        test_create_instrument_protocol_version.create_new_protocols()
        time.sleep(5)
        test_create_instrument_protocol_version.select_org_name_pratacols()
        time.sleep(10)
        test_create_instrument_protocol_version.choose_org_name()
        time.sleep(5)
        test_create_instrument_protocol_version.select_instrument_name()
        time.sleep(10)
        test_create_instrument_protocol_version.choose_instrument_name()
        test_create_instrument_protocol_version.send_keys_protocols_name(current_time)
        test_create_instrument_protocol_version.click_protocols_save_button()
        time.sleep(10)

        test_create_instrument_protocol_version.click_on_the_drop_douwn_manu()
        time.sleep(10)  
        test_create_instrument_protocol_version.click_protocols_version_button()
        test_create_instrument_protocol_version.create_new_protocols_version()
        time.sleep(10)
        test_create_instrument_protocol_version.select_org_name_in_pro_version()
        time.sleep(5)
        test_create_instrument_protocol_version.choose_org_name_for_protocol_version()
        time.sleep(10)
        test_create_instrument_protocol_version.select_instrument_name_for_protocol_version()
        time.sleep(5)
        test_create_instrument_protocol_version.choose_ins_name_for_protocol_version()
        time.sleep(10)
        test_create_instrument_protocol_version.select_protocol_name()
        time.sleep(5)
        test_create_instrument_protocol_version.choose_protocol_name()
        time.sleep(10)
        test_create_instrument_protocol_version.send_keys_protocol_version(current_time)
        time.sleep(5)
        test_create_instrument_protocol_version.save_protocol_version()
        time.sleep(10)
        print("Test case in passed")

    #except Exception as err:
        print("Something did not work out, please try again")
def case_8(page_link):
        test_create_module = TestAppGeneratorCreateModulePage(webdriver.Chrome(), page_link)
        test_create_module.go_to_site()

        time.sleep(10)
        test_create_module.send_login()
        test_create_module.send_password()
        test_create_module.click_on_the_login_button()
        time.sleep(15)
        test_create_module.click_module_button()
        time.sleep(5) 
        test_create_module.create_new_module()
        time.sleep(10)
        test_create_module.select_organization_name()
        time.sleep(5)
        test_create_module.choose_organization_name()
        time.sleep(10)
        test_create_module.select_instrument_name()
        time.sleep(10)
        test_create_module.choose_instrument_name()
        time.sleep(10)
        test_create_module.select_protocol_name()
        time.sleep(20)
        test_create_module.choose_protocol_name()
        time.sleep(10)
        test_create_module.select_protocol_version_name()
        time.sleep(20)
        test_create_module.choose_protocol_version_name()
        time.sleep(10)
        current_time = get_current_time()
        test_create_module.send_keys_module_name(current_time)
        test_create_module.click_on_the_save_button()
        time.sleep(5)

def case_user_app_1(user_app_page_link):
        test_end_user_app_login_logout = TestUserApplicationLoginLogoutPage(webdriver.Chrome(), user_app_page_link)
        test_end_user_app_login_logout.go_to_site()
        test_end_user_app_login_logout.send_login()
        time.sleep(10)
        test_end_user_app_login_logout.send_password()
        test_end_user_app_login_logout.click_on_the_login_button()
        time.sleep(10)
        test_end_user_app_login_logout.click_drop_down_menu()
        test_end_user_app_login_logout.click_on_the_logout_button()
        time.sleep(10)

def case_user_app_2(user_app_page_link):
        test_create_activities = TestUserApplicationCreateActivitiesPage(webdriver.Chrome(), user_app_page_link)
        test_create_activities.go_to_site()
        test_create_activities.send_login()
        test_create_activities.send_password()
        test_create_activities.click_on_the_login_button()
        time.sleep(10) 
        test_create_activities.click_drop_doun_manu()
        time.sleep(5)
        test_create_activities.click_activities_button()
        test_create_activities.click_add_new_button()
        time.sleep(5)
        test_create_activities.send_keys_coustmer_name()
        time.sleep(5)
        test_create_activities.select_instrument_name()
        time.sleep(20)
        test_create_activities.choose_instrument_name()
        time.sleep(5)
        test_create_activities.select_protocol_name()
        time.sleep(20)
        test_create_activities.choose_protocol_name()
        time.sleep(5)
        test_create_activities.select_protocol_version()
        time.sleep(20)
        test_create_activities.choose_protocol_version()
        time.sleep(5)
        test_create_activities.click_on_the_button_start()
        time.sleep(10)

def case_user_app_3(user_app_page_link):
        test_copy_activity = TestUserApplicationCopyActivityPage(webdriver.Chrome(), user_app_page_link)
        test_copy_activity.go_to_site()
        test_copy_activity.send_login()
        test_copy_activity.send_password()
        test_copy_activity.click_on_the_login_button()
        time.sleep(10)
        test_copy_activity.open_main_manu()
        time.sleep(5)
        test_copy_activity.click_activites_button()
        time.sleep(5)
        test_copy_activity.click_copy_activity_bytton()
        time.sleep(5)
        test_copy_activity.click_ok_button()
        time.sleep(5)

def case_user_app_4(user_app_page_link):
        test_activities_complete_activity = TestUserApplicationCompleteActivityPage(webdriver.Chrome(), user_app_page_link)
        test_activities_complete_activity.go_to_site()
        test_activities_complete_activity.send_login()
        test_activities_complete_activity.send_password()
        time.sleep(10)
        test_activities_complete_activity.click_on_the_login_button()
        time.sleep(5)
        test_activities_complete_activity.open_main_manu()
        time.sleep(5)
        test_activities_complete_activity.click_activites_button()
        time.sleep(5)
        test_activities_complete_activity.click_complete_activity()
        time.sleep(5)
        test_activities_complete_activity.click_ok_button()
        time.sleep(5)
        test_activities_complete_activity.check_complete_ststus()
        time.sleep(5)

def case_user_app_5(user_app_page_link):
        test_delate_activities = TestUserApplicationCompleteActivityPage(webdriver.Chrome(), user_app_page_link)
        test_delate_activities.go_to_site()
        test_delate_activities.send_login()
        test_delate_activities.send_password()
        test_delate_activities.click_on_the_login_button()
        time.sleep(10)
        #test_delate_activities.open_main_manu()
        time.sleep(5)
        test_delate_activities.click_activites_button()
        time.sleep(5)
        test_delate_activities.click_delate_activity_bytton()
        time.sleep(20)
        test_delate_activities.click_ok_button()
        time.sleep(5)

def case_user_app_6(user_app_page_link):
        test_send_to_review = TestActivitiesSendToReviewPage(webdriver.Chrome(), user_app_page_link)
        test_send_to_review.go_to_site()
        test_send_to_review.send_login()
        test_send_to_review.send_password()
        test_send_to_review.click_on_the_login_button()
        time.sleep(10)
        test_send_to_review.open_main_manu()
        time.sleep(5)
        test_send_to_review.click_activites_button()
        time.sleep(5)
        test_send_to_review.click_send_to_review_button()
        time.sleep(5)
        test_send_to_review.click_section_reason_field()
        time.sleep(10)
        test_send_to_review.click_reason_name()
        time.sleep(5)
        test_send_to_review.select_review_field()
        time.sleep(10)
        test_send_to_review.select_reviewer()
        time.sleep(10)
        test_send_to_review.scroll_down_to_window()
        time.sleep(10)
        test_send_to_review.click_send_button()
        time.sleep(10)

def case_user_app_7(user_app_page_link):
        test_send_to_review_with_invite = TestActivitiesSendToReviewPage(webdriver.Chrome(), user_app_page_link)
        test_send_to_review_with_invite.go_to_site()
        test_send_to_review_with_invite.send_login()
        test_send_to_review_with_invite.send_password()
        test_send_to_review_with_invite.click_on_the_login_button()
        time.sleep(10)
        test_send_to_review_with_invite.open_main_manu()
        time.sleep(5)
        test_send_to_review_with_invite.click_activites_button()
        time.sleep(5)
        test_send_to_review_with_invite.click_send_to_review_button()
        time.sleep(5)
        test_send_to_review_with_invite.click_section_reason_field()
        time.sleep(10)
        test_send_to_review_with_invite.click_reason_name()
        time.sleep(5)
        test_send_to_review_with_invite.click_invite_reviewer_select()
        time.sleep(5)
        test_send_to_review_with_invite.type_revier_field()
        time.sleep(5)
        test_send_to_review_with_invite.scroll_down_to_window()
        time.sleep(10)
        test_send_to_review_with_invite.click_send_button()
        time.sleep(10)
        test_send_to_review_with_invite.check_activities_status()
        time.sleep(10) 

def case_user_app_8(user_app_page_link):
        test_user_application_delete_activity_page = TestUserApplicationDeleteActivityPage(webdriver.Chrome(), user_app_page_link)
        test_user_application_delete_activity_page.go_to_site()
        test_user_application_delete_activity_page.send_login()
        test_user_application_delete_activity_page.send_password()
        test_user_application_delete_activity_page.click_on_the_login_button()
        time.sleep(10)
        test_user_application_delete_activity_page.open_main_manu()
        time.sleep(5)
        test_user_application_delete_activity_page.click_activites_button()
        time.sleep(5)
        test_user_application_delete_activity_page.click_delate_button()
        time.sleep(5)
        test_user_application_delete_activity_page.click_ok_button()
        time.sleep(10) 

page_link = get_page_link()
user_app_page_link = get_end_user_app_page_link()
#case_1(page_link)
#case_2(page_link)
#case_3(page_link)
#case_4(page_link)
#case_5(page_link)
#case_6(page_link)
#case_7(page_link)
#case_8(page_link)
#case_user_app_1(user_app_page_link)
#case_user_app_2(user_app_page_link)
#case_user_app_3(user_app_page_link)
#case_user_app_4(user_app_page_link)
#case_user_app_5(user_app_page_link)
#case_user_app_6(user_app_page_link)
#case_user_app_7(user_app_page_link)
case_user_app_8(user_app_page_link)

