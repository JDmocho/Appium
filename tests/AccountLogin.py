
"""
Test login functionality
Version 1.0
Author Joanna Dmochowska
"""

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
class AccountLogin(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'SH-A500FU'
        desired_caps['app'] = apk_file_path
        desired_caps['udid'] = '192.168.1.12:5555'
        desired_caps['apkPackage'] = 'com.douglas.main'
        desired_caps['apkActivity'] = 'com.douglas.startpage.ui.tabbar.TabbarStartpageActivity'
        desired_caps['noReset'] = False

        # correct email and password
        self.email = ''
        self.password = ''

        # connect to Appium
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        self.driver.is_app_installed('com.douglas.main')
        sleep(5)
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().textContains("ODMÓW")').click()



    def tearDown(self):
        self.driver.quit()


    # TEST CASES

    def test_login_empty_data(self):
        '''Login with empty data should fail'''

        my_douglas_btn = self.driver.find_element_by_id('com.douglas.main:id/actionMyDouglas')
        my_douglas_btn.click()
        sleep(5)
        login_btn = self.driver.find_element_by_id('com.douglas.main:id/loginButton')
        login_btn.click()
        sleep(5)
        fill_email = self.driver.find_element_by_id('com.douglas.main:id/usernameEdit')
        fill_email.send_keys("")
        fill_password = self.driver.find_element_by_id('com.douglas.main:id/passwordEdit')
        fill_password.send_keys("")

        confirm_btn = self.driver.find_element_by_id('com.douglas.main:id/loginButton')
        confirm_btn.click()
        sleep(10)

        # check if email error show up
        error_email = self.driver.find_elements_by_android_uiautomator('new UiSelector().textContains("Proszę wpisać adres e-mail.")')
        self.assertTrue(error_email)

        # check if password error show up
        error_password = self.driver.find_elements_by_android_uiautomator('new UiSelector().textContains("Proszę wpisać hasło.")')
        self.assertTrue(error_password)


    # Get actual DIR
    CUR_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(CUR_DIR, '..', 'data/bad_email_account.csv')

    @data(*GetData.get_data(file_path))
    @unpack

    def test_incorrect_email(self, email, password):
        '''Login with incorrect email should fail'''

        my_douglas_btn = self.driver.find_element_by_id('com.douglas.main:id/actionMyDouglas')
        my_douglas_btn.click()
        sleep(5)
        login_btn = self.driver.find_element_by_id('com.douglas.main:id/loginButton')
        login_btn.click()
        sleep(5)
        fill_email = self.driver.find_element_by_id('com.douglas.main:id/usernameEdit')
        fill_email.send_keys(email)
        fill_password = self.driver.find_element_by_id('com.douglas.main:id/passwordEdit')
        fill_password.send_keys(password)

        confirm_btn = self.driver.find_element_by_id('com.douglas.main:id/loginButton')
        confirm_btn.click()
        sleep(10)

        # check if email error show up
        error_email = self.driver.find_elements_by_android_uiautomator('new UiSelector().textContains("Proszę sprawdzić adres e-mail.")')
        self.assertTrue(error_email)


    # Get actual DIR
    CUR_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(CUR_DIR, '..', 'data/bad_password_account.csv')

    @data(*GetData.get_data(file_path))
    @unpack

    def test_incorrect_password(self, email, password):
        '''Login with incorrect password should fail'''

        my_douglas_btn = self.driver.find_element_by_id('com.douglas.main:id/actionMyDouglas')
        my_douglas_btn.click()
        sleep(5)
        login_btn = self.driver.find_element_by_id('com.douglas.main:id/loginButton')
        login_btn.click()
        sleep(5)
        fill_email = self.driver.find_element_by_id('com.douglas.main:id/usernameEdit')
        fill_email.send_keys(email)
        fill_password = self.driver.find_element_by_id('com.douglas.main:id/passwordEdit')
        fill_password.send_keys(password)

        confirm_btn = self.driver.find_element_by_id('com.douglas.main:id/loginButton')
        confirm_btn.click()
        sleep(10)

        # check if password error show up
        error_password = self.driver.find_elements_by_android_uiautomator('new UiSelector().textContains("Niestety wystąpił błąd. Prosimy spróbować ponownie.")')
        self.assertTrue(error_password)


    def test_correct_data(self):
        '''Logging in with the correct data should be successful'''

        my_douglas_btn = self.driver.find_element_by_id('com.douglas.main:id/actionMyDouglas')
        my_douglas_btn.click()
        sleep(5)
        login_btn = self.driver.find_element_by_id('com.douglas.main:id/loginButton')
        login_btn.click()
        sleep(5)
        fill_email = self.driver.find_element_by_id('com.douglas.main:id/usernameEdit')
        fill_email.send_keys(self.email)
        fill_password = self.driver.find_element_by_id('com.douglas.main:id/passwordEdit')
        fill_password.send_keys(self.password)

        confirm_btn = self.driver.find_element_by_id('com.douglas.main:id/loginButton')
        confirm_btn.click()
        sleep(10)

        # check if a greeting appears
        welcome = self.driver.find_elements_by_android_uiautomator('new UiSelector().textContains("Witaj")')
        self.assertTrue(welcome)

        testerka = self.driver.find_elements_by_android_uiautomator('new UiSelector().textContains("Joanna")')
        self.assertTrue(testerka)


if __name__=="__main__":
    unittest.main(verbosity=2)
