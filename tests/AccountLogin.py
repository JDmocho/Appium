import os
import unittest

from appium import webdriver

# Get actual DIR
CUR_DIR = os.path.dirname(os.path.abspath(__file__))
apk_file_path = os.path.join(CUR_DIR, '..', 'DouglasParfumKosmetik_v7.8.4_apkpure.com.apk')

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

        # connect to Appium
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_login_empty_data(self):
        # login with empty data should fail
        self.driver.is_app_installed('com.douglas.main')


if __name__=="__main__":
    unittest.main(verbosity=2)
