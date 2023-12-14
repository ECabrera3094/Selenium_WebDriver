import time
import unittest 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Reporte HTML
import HtmlTestRunner

# LOCATOR
from Locators.Locators import MyLocators

# TestCases
from TestCases.TC_1 import TC_1
from TestCases.TC_2 import TC_2

class QAMinds(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("INICIO DE LA PRUEBA")
        miServicio = Service(MyLocators.Driver_Path)
        cls.driver = webdriver.Chrome(service = miServicio)
        time.sleep(5)
    
    def test_QAMinds(self):
        driver = self.driver
        tc_2 = TC_2(driver)
        tc_2.start()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("\nFIN DE LA PRUEBA")

if __name__ == '__main__':
    #unittest.main() 
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='E:\\QAMinds\\Evidence\\Reporte_1.html'))