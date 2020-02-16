# -*- coding: utf-8 -*-


import os
import unittest
from appium import webdriver
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)

class TestingMobileApp(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'Gigaset GS170'
        desired_caps['app'] =PATH ('ContactManager.apk')
        desired_caps['appPackage'] = 'com.example.android.contactmanager'
        desired_caps['appActivity'] = 'com.example.android.contactmanager.ContactManager'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_fill_contact_manager(self):
        self.driver.find_element_by_id('com.example.android.contactmanager:id/addContactButton').click()
        self.driver.find_element_by_id('com.example.android.contactmanager:id/contactNameEditText').send_keys('Mike')
        self.driver.find_element_by_id('com.example.android.contactmanager:id/contactPhoneEditText').send_keys('123456789')
        self.driver.find_element_by_id('com.example.android.contactmanager:id/contactEmailEditText').send_keys('aaa@aa.aa')
        self.driver.find_element_by_id('com.example.android.contactmanager:id/contactPhoneTypeSpinner').click()
        #self.driver.find_element_by_xpath('//*[@text="Mobile"]').click()
        self.driver.find_element_by_xpath('//android.widget.CheckedTextView[@text="Mobile"]').click()
        self.driver.find_element_by_id('com.example.android.contactmanager:id/contactSaveButton').click()
        sleep(2)
        check = self.driver.find_element_by_id('android:id/alertTitle').get_attribute('text')
        print(check)
        self.assertEqual(check, 'Contact Manager has stopped', 'message incorrect')


#android.widget.ListView[


#com.example.android.contactmanager:id/contactPhoneEditText


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestingMobileApp)
    unittest.TextTestRunner(verbosity=2).run(suite)
