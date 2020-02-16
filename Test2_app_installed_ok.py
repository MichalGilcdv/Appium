# -*- coding: utf-8 -*-


import os
import unittest
from appium import webdriver
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestingMobileApp(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'Gigaset GS170'
        desired_caps['app'] = PATH('ApiDemos-debug.apk')
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()



    def test_clicking_on(self):
        self.driver.find_element_by_accessibility_id('Preference').click()
        self.driver.back()
        self.driver.keyevent(4)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingMobileApp)
    unittest.TextTestRunner(verbosity=2).run(suite)
