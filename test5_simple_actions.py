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

    def test_actions_settings(self):
        self.driver.find_element_by_accessibility_id('Graphics').click()
        self.driver.find_element_by_accessibility_id('Arcs').click()
        checktext = self.driver.find_element_by_xpath('//android.widget.TextView[@text="Graphics/Arcs"]').get_attribute(
            'text')
        print(checktext)
        self.assertEqual(checktext, 'Graphics/Arcs', 'wrong title')
        self.driver.press_keycode(2)
        # self.driver.keyevent(4)
        sleep(3)

    def test_graphics_app(self):
        self.driver.find_element_by_accessibility_id('App').click()
        elements = self.driver.find_elements_by_class_name('android.widget.TextView')
        print("Liczba zakładek: " + elements.__len__().__str__())
        print(type(len(elements)))


        for el in elements:
            print("zakładki: " + el.text)

        #self.assertGreaterEqual(elements.__len__().__str__(), '10')
        self.assertGreaterEqual(len(elements), 10)




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)
