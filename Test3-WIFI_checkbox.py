import os
import unittest
from appium import webdriver
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestowanieAplikacji(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platfomVersion'] = '7.0'
        desired_caps['deviceName'] = 'Gigaset GS170'
        desired_caps['app'] = PATH('ApiDemos-debug.apk')
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()


    def test_wifi_settings(self):
        self.driver.find_element_by_accessibility_id("Preference").click()
        self.driver.find_element_by_accessibility_id("3. Preference dependencies").click()
        self.driver.find_element_by_id('android:id/checkbox').click()
        self.driver.back()
        self.driver.find_element_by_accessibility_id("3. Preference dependencies").click()
        self.driver.find_element_by_id('android:id/checkbox').click()



        # is_checked = self.driver.find_element_by_class_name("android.widget.CheckBox").get_attribute("checked")
        # print(is_checked)
        # if is_checked == False:
        #     self.driver.find_element_by_class_name("android.widget.CheckBox").click()
        # self.assertTrue("Checkbox is checked", is_checked=="true")
        # sleep(3)
        # print(is_checked)

        # is_checked = self.driver.find_element_by_class_name("android.widget.CheckBox").get_attribute("checked")
        # print(is_checked)
        # if is_checked == "false":
        #     self.driver.find_element_by_class_name("android.widget.CheckBox").click()
        #     check2 = self.driver.find_element_by_class_name("android.widget.CheckBox").get_attribute("checked")
        #     if check2 =="true":
        #          is_checked = True
        #     print(is_checked)
        # print(is_checked)
        # self.assertTrue("Checkbox is checked", is_checked == 'true')
        # sleep(3)
        # print(is_checked)

       # - Rozwiązanie GM:

        # Rozwiązanie GM(1):
        # self.driver.find_element_by_accessibility_id("Preference").click()
        # self.driver.find_element_by_accessibility_id("3. Preference dependencies").click()
        # self.driver.find_element_by_android_uiautomator('new UiSelector().checkable(true)').click() # zmiana na zaznaczony
        # self.driver.back()
        # self.driver.find_element_by_accessibility_id("3. Preference dependencies").click()
        # self.driver.find_element_by_android_uiautomator('new UiSelector().checkable(true)').click()


        # Rozwiązanie GM(2):
        #self.driver.find_element_by_accessibility_id("Preference").click()
        #self.driver.find_element_by_accessibility_id("3. Preference dependencies").click()
        checkboxes = self.driver.find_elements_by_android_uiautomator('new UiSelector().checkable(true)')
        amount_of_checkboxes = len(checkboxes)

        # dydaktycznie printy:
        print("Liczba checkboxow: ")
        print(amount_of_checkboxes)

        # pętla po checkboxach, która zaznacza wszystkie checkboxy

        for el in checkboxes:
            el.click()

        for el in checkboxes:
            is_checked_value = self.driver.find_element_by_class_name("android.widget.CheckBox").get_attribute(
                "checked")
            if is_checked_value == 'true':
                print("Wszystkie checkboxy są zaznaczone")

        #self.driver.find_element_by_xpath('//*[@text="WiFi settings"]').click()
        #self.driver.find_element_by_xpath('//android.widget.RelativeLayout[2]').click()
        self.driver.find_elements_by_class_name('android.widget.RelativeLayout')[1].click()
        self.driver.find_element_by_id('android:id/edit').send_keys('1234')
        checkpassword = self.driver.find_element_by_id('android:id/edit').get_attribute('text')

        print(checkpassword)
        self.driver.back()
        self.assertEqual('1235',checkpassword,'pass is incorrect')
        self.driver.find_element_by_id('android:id/button1').click()
        #self.driver.back()
        #self.driver.back()
        self.driver.keyevent(4)
        sleep(3)




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)
