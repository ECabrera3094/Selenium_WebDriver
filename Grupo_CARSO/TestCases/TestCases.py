import time
import unittest 
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

from Locators.Locators import Locators

class TestCases():

    def __init__(self, driver):
        self.driver = driver
        self.id_SearchBox = Locators.id_SearchBox
        self.xpath_SearchButton = Locators.xpath_SearchButton
        self.xpath_CSVFileDownload = Locators.xpath_CSVFileDownload

    def DownloadFile(self):

        print("INICIO DE LA PRUEBA")

        try:
            WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.ID, self.id_SearchBox)))
        except TimeoutException as toe:
            print("Error: ", toe)

        self.driver.find_element(By.ID, self.id_SearchBox).send_keys("electric car")

        time.sleep(3)

        self.driver.find_element(By.XPATH, self.xpath_SearchButton).click()

        time.sleep(3)

        # Click en Descarga.
        self.driver.find_element(By.XPATH, self.xpath_CSVFileDownload).click()

        time.sleep(50)

        # Abrimos el CSV y Filtramos.
        df = pd.read_csv("/Users/EmilianoCabreraPerez/Downloads/Electric_Vehicle_Population_Data.csv")

        column = 'Make'

        search = 'TESLA'

        filtered_value = df[df[column] == search]

        count = len(filtered_value)

        print("Cantidad Total de {0}: {1}".format(search, count))

        print("FIN DE LA PRUEBA")
