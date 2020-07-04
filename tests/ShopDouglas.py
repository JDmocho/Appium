
"""
Check if product price in cart is the same as on product page
Version 1.0
Author Joanna Dmochowska
"""

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
        desired_caps['noReset'] = False

        # connect to Appium
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        self.driver.is_app_installed('com.douglas.main')
        sleep(5)
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().textContains("ODMÓW")').click()

    def tearDown(self):
        self.driver.quit()


    # TEST CASES

    def test_add_product_from_menu(self):
        """Price product should be identical as in the cart"""

        buy_btn = self.driver.find_element_by_id('com.douglas.main:id/actionSearch')
        buy_btn.click()
        sleep(4)
        makeup_btn = self.driver.find_element_by_xpath("//*[@resource-id='com.douglas.main:id/container' and @index=2]")
        makeup_btn.click()
        sleep(4)
        face_btn = self.driver.find_element_by_xpath("//*[@resource-id='com.douglas.main:id/container' and @index=1]")
        face_btn.click()
        sleep(4)
        menu_face_btn = self.driver.find_element_by_id('com.douglas.main:id/productFilter')
        menu_face_btn.click()
        sleep(4)
        menu_face_btn_1 = self.driver.find_element_by_xpath("//*[@resource-id='com.douglas.main:id/name' and @text='Twarz']")
        menu_face_btn_1.click()
        sleep(4)
        recycler = self.driver.find_element_by_id('com.douglas.main:id/recycler')
        recycler.find_element_by_android_uiautomator('new UiSelector().textContains("Podkłady")').click()
        sleep(4)

        # pobieramy cene
        self.driver.swipe(50, 1000, 50, 250, 1000)

        el_price =self.driver.find_element_by_id('com.douglas.main:id/actualPrice')

        price = el_price.text
        print(price)
        price = price.split(' / ')
        print(price)
        print(price[0])
        price = price[0].split(' ')
        price = price[0]
        print(price)


        el_price.click()
        sleep(30)
        #cookies = self.driver.find_elements_by_xpath("//*[@resource-id='uc-btn-accept-banner']")
        cookies = self.driver.find_elements_by_class_name('android.app.Dialog')
        print(len(cookies))

        add_to_cart = self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector()).scrollIntoView('
            +'new UiSelector().textContains("DO KOSZYKA"))')

        add_to_cart.click()
        sleep(2)
        add_to_cart.click()


        sleep(15)
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("KOSZYK I KASA")').click()
        sleep(5)

        price_in_cart =self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector()).scrollIntoView('
            +'new UiSelector().textContains("'+price+'"))')


        self.assertTrue(price_in_cart)



if __name__=="__main__":
    unittest.main(verbosity=2)