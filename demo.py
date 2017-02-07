#!/usr/bin/env python
import os
import unittest
from appium import webdriver
from time import sleep


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class Demo(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = 'Galaxy S6 edge'
        '''
        desired_caps['appPackage'] = 'com.mobilebtccexchangereactnative'
        desired_caps['appActivity'] = 'MainActivity'
        '''
        desired_caps['appPackage'] = 'com.android.calendar'
        desired_caps['appActivity'] = '.LaunchActivity'
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()


    def test_demo(self):
        try:
          el = self.driver.find_element_by_id("com.android.calendar:id/actionbar_spinner_title_text")
          el.click()
        except:
           pass



        textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        textfields[0].send_keys("Appium User")
        textfields[2].send_keys("someone@appium.io")
        try:
          self.assertEqual('Appium User', textfields[0].text)
          self.assertEqual('someone@appium.io', textfields[2].text)
        except AssertionError as e:
           print e
           print 'Can not find username and password text element'
        '''
        self.driver.find_element_by_name("Save").click()
        # for some reason "save" breaks things
        alert = self.driver.switch_to_alert()

        # no way to handle alerts in Android
        self.driver.find_element_by_android_uiautomator('new UiSelector().clickable(true)').click()

        self.driver.keyevent(3)
        '''
    def test_demo1(self):
        try:
          el = self.driver.find_element_by_id("com.android.calendar:id/action_today")
          el.click()
        except:
          pass



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Demo)
    unittest.TextTestRunner(verbosity=2).run(suite)