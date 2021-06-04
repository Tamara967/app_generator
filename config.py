import datetime


def get_page_link():
    return "http://35.234.81.128/login"

def get_home_page_link():
    return "http://35.234.81.128/dashboard?title=Dashboard"

def get_current_time():
        x = datetime.datetime.now()

        replace_current_time = str(x).replace(" ","")
        current_date_and_time = replace_current_time.replace(":","")
        cur_date_and_time = current_date_and_time.replace('-',"")
        test_run_date_and_time = cur_date_and_time.replace('.',"")

        return test_run_date_and_time 


def get_end_user_app_page_link():
    return "http://35.234.81.128/yYXAVOIZfwXLhP0qJToR/login"


#test_user_application_activities_copy_activity.py
#test_user_application_create_activities.py
#test_user_application_activities_complete_activity.py
#test_user_application_login_logout_page.py

