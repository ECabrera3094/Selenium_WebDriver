import unittest 
from selenium import webdriver

from TestCases.TestCases import TestCases
from Locators.Locators import Locators

class Carso(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Se Especifican las Opciones de Chrome
        options = webdriver.ChromeOptions()
        # Especificamos la ruta de cualquier Descarga.
        options.add_experimental_option('prefs', {'download.default_directory' : Locators.download_path} )
        cls.driver = webdriver.Chrome(Locators.driver_path, options = options)
        cls.driver.maximize_window()
        cls.driver.get(Locators.url_path)

    def test_Carso(self):
        driver = self.driver
        tc = TestCases(driver)
        tc.DownloadFile()
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()