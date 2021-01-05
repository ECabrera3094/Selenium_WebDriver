import unittest
from selenium import webdriver

from TestCases.TestCases import TestCases


class Mercury(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:/Users/everis/Downloads/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(1)
        cls.driver.get("http://demo.guru99.com/test/newtours/index.php")

    def test_Mercury(self):
        driver = self.driver

        tc = TestCases(driver)
        tc.Register()
        tc.Flights()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()