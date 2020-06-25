import os
import unittest

from appium import webdriver
from time import sleep
from library import GetData
from ddt import ddt, data, unpack

# Get actual DIR
CUR_DIR = os.path.dirname(os.path.abspath(__file__))
apk_file_path = os.path.join(CUR_DIR, '..', 'DouglasParfumKosmetik_v7.8.4_apkpure.com.apk')

@ddt
class RegistrationForm(unittest.TestCase):
    '''Testing the registration form.'''
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'SH-A500FU'
        desired_caps['app'] = apk_file_path
        desired_caps['udid'] = '192.168.1.12:5555'
        desired_caps['apkPackage'] = 'com.douglas.main'
        desired_caps['apkActivity'] = 'com.douglas.startpage.ui.tabbar.TabbarStartpageActivity'
        desired_caps['noReset'] = True

        # connect to Appium
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    # TEST CASES

    def test_empty_registration_form(self):
        '''Login with empty data should fail'''

        self.driver.is_app_installed('com.douglas.main')

        sleep(5)
        my_douglas_btn = self.driver.find_element_by_id('com.douglas.main:id/actionMyDouglas')
        my_douglas_btn.click()
        sleep(5)
        put_on_btn = self.driver.find_element_by_id('com.douglas.main:id/registerButton')
        put_on_btn.click()
        sleep(5)

        fill_name = self.driver.find_element_by_id('com.douglas.main:id/firstNameEdit')
        fill_name.send_keys("")
        fill_surname = self.driver.find_element_by_id('com.douglas.main:id/lastNameEdit')
        fill_surname.send_keys("")
        fill_email = self.driver.find_element_by_id('com.douglas.main:id/emailEdit')
        fill_email.send_keys("")
        fill_password = self.driver.find_element_by_id('com.douglas.main:id/passwordEdit')
        fill_password.send_keys("")
        fill_repassword = self.driver.find_element_by_id('com.douglas.main:id/passwordRepeatEdit')
        fill_repassword.send_keys("")


        # scroll down
        self.driver.swipe(50,600,50,250,1000)

        create_btn =  self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("Załóż konto")')
        create_btn.click()
        sleep(5)

        # check if empty data show up
        error_name = self.driver.find_elements_by_android_uiautomator('new UiSelector().textContains("Proszę wpisać imię.")')
        self.assertTrue(error_name)
        error_surname = self.driver.find_elements_by_android_uiautomator('new UiSelector().textContains("Proszę wpisać nazwisko.")')
        self.assertTrue(error_surname)
        error_email = self.driver.find_elements_by_android_uiautomator('new UiSelector().textContains("Proszę wpisać adres e-mail.")')
        self.assertTrue(error_email)
        error_password = self.driver.find_elements_by_android_uiautomator('new UiSelector().textContains("Proszę wpisać hasło.")')
        self.assertTrue(error_password)
        error_repassword = self.driver.find_elements_by_android_uiautomator('new UiSelector().textContains("Proszę wpisać hasło.")')
        self.assertTrue(error_repassword)



    CUR_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(CUR_DIR, '..', 'data/incorrect_email_registration.csv')

    @data(*GetData.get_data(file_path))
    @unpack
    def test_incorrect_email(self,email):
        """Login with incorrect pemail should fail"""

        self.driver.is_app_installed('com.douglas.main')

        sleep(5)
        my_douglas_btn = self.driver.find_element_by_id('com.douglas.main:id/actionMyDouglas')
        my_douglas_btn.click()
        sleep(5)
        put_on_btn = self.driver.find_element_by_id('com.douglas.main:id/registerButton')
        put_on_btn.click()
        sleep(5)

        fill_name = self.driver.find_element_by_id('com.douglas.main:id/firstNameEdit')
        fill_name.send_keys("Joanna")
        fill_surname = self.driver.find_element_by_id('com.douglas.main:id/lastNameEdit')
        fill_surname.send_keys("Hejka")
        fill_email = self.driver.find_element_by_id('com.douglas.main:id/emailEdit')
        fill_email.send_keys(email)
        fill_password = self.driver.find_element_by_id('com.douglas.main:id/passwordEdit')
        fill_password.send_keys("Tester1234")
        fill_repassword = self.driver.find_element_by_id('com.douglas.main:id/passwordRepeatEdit')
        fill_repassword.send_keys("Tester1234")

        # scroll down
        self.driver.swipe(50, 600, 50, 250, 1000)

        create_btn = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("Załóż konto")')
        create_btn.click()
        sleep(5)

        # check if incorrect error show up
        error_email = self.driver.find_elements_by_android_uiautomator('new UiSelector().textContains("Proszę sprawdzić adres e-mail.")')
        self.assertTrue(error_email)


    CUR_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(CUR_DIR, '..', 'data/incorrect_password_registration.csv')

    @data(*GetData.get_data(file_path))
    @unpack
    def test_incorrect_password(self, password, repassword):
        '''Login with incorrect password should fail'''

        self.driver.is_app_installed('com.douglas.main')

        sleep(5)
        my_douglas_btn = self.driver.find_element_by_id('com.douglas.main:id/actionMyDouglas')
        my_douglas_btn.click()
        sleep(5)
        put_on_btn = self.driver.find_element_by_id('com.douglas.main:id/registerButton')
        put_on_btn.click()
        sleep(5)

        fill_name = self.driver.find_element_by_id('com.douglas.main:id/firstNameEdit')
        fill_name.send_keys("Joanna")
        fill_surname = self.driver.find_element_by_id('com.douglas.main:id/lastNameEdit')
        fill_surname.send_keys("Hejka")
        fill_email = self.driver.find_element_by_id('com.douglas.main:id/emailEdit')
        fill_email.send_keys("tester@tester.pl")
        fill_password = self.driver.find_element_by_id('com.douglas.main:id/passwordEdit')
        fill_password.send_keys(password)
        fill_repassword = self.driver.find_element_by_id('com.douglas.main:id/passwordRepeatEdit')
        fill_repassword.send_keys(repassword)

        # scroll down
        self.driver.swipe(50, 600, 50, 250, 1000)

        create_btn = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("Załóż konto")')
        create_btn.click()
        sleep(5)

        # check if errors show up
        error_check_1 = self.driver.find_elements_by_android_uiautomator('new UiSelector().textContains("Wpisane hasła nie są zgodne.")')
        error_check_2 = self.driver.find_elements_by_android_uiautomator('new UiSelector().textContains("Ze względów bezpieczeństwa, prosimy o wprowadzenie dłuższego hasła, min. 6 znaków.")')
        error_check_3 = self.driver.find_elements_by_android_uiautomator('new UiSelector().textContains("Proszę wpisać hasło.")')

        if error_check_1 or error_check_2 or error_check_3:
            errors = True
        else:
            errors = False

        self.assertTrue(errors)


if __name__=="__main__":
    unittest.main(verbosity=2)