import os
import unittest

from appium import webdriver
from time import sleep


# Get actual DIR
CUR_DIR = os.path.dirname(os.path.abspath(__file__))
apk_file_path = os.path.join(CUR_DIR, '..', 'DouglasParfumKosmetik_v7.8.4_apkpure.com.apk')


class ShopDouglas(unittest.TestCase):
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

    def test_add_product_from_menu(self):

        self.driver.is_app_installed('com.douglas.main')
        sleep(2)
        buy_btn = self.driver.find_element_by_id('com.douglas.main:id/actionSearch')
        buy_btn.click()
        sleep(2)
        makeup_btn = self.driver.find_element_by_xpath("//*[@resource-id='com.douglas.main:id/container' and @index=2]")
        makeup_btn.click()


if __name__=="__main__":
    unittest.main(verbosity=2)