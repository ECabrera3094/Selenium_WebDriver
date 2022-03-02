import time
import unittest
from selenium import webdriver
from TestCases.TestCases import TestCases_Maquiladora

from Locators.Locators import MyLocators

class Maquiladora(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(MyLocators.Driver_Path)
        cls.driver.get(MyLocators.URL)
        cls.driver.maximize_window()
        time.sleep(5)

    def test_Maquiladora(self):
        driver = self.driver 
        maquiladora = TestCases_Maquiladora(driver)
        maquiladora.start_TestCases()
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
    #https://industriamaquiladora.com/maquiladoras.php
    #Usuario: marketing@mediafactory.studio
    #P/W: abc2021