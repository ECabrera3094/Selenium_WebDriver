import time
import copy
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

# LOCATOR
from Locators.Locators import MyLocators

class TC_1():
    
    def __init__(self, driver):

        self.driver = driver
        self.root_Excel = pd.read_excel(MyLocators.root_Excel, engine = "openpyxl")
        self.name_userName = MyLocators.name_userName
        self.name_userPassword = MyLocators.name_userPassword
        self.name_loginButton = MyLocators.name_loginButton
        self.xPath_LoginMessage = MyLocators.xPath_LoginMessage
        self.xPath_SignOffButton = MyLocators.xPath_SignOffButton
        self.list_Columns = MyLocators.list_Columns

    def start(self):
        # iloc[R][C] - Leer
        # loc[R, C] - Escribir
        global i

        # DataFrame de Almacenamiento
        df = pd.DataFrame(columns=self.list_Columns)

        for i in range(len(self.root_Excel)):
            
            if self.root_Excel.iloc[i]["Y/N"] == "Y":
                method_Name = self.root_Excel.iloc[i]["Nombre"]
                try:
                    test_Method = getattr(TC_1, method_Name)
                except AttributeError:
                    print("ERROR!!!")
                
                test_Method(self, df)
                
            else:
                pass

        # Escritura del Dataframe a formato CSV
        df.to_csv("E:\\QAMinds\\Evidence\\Catalogo.csv")


    def Test_001(self, df):

        print(">>> TC:", self.root_Excel.iloc[i]["ID Test"])

        # DataFrame de Almacenamiento
        #df = pd.DataFrame(columns=self.list_Columns)
        
        global int_CurrentRow
        int_CurrentRow = int(copy.copy(i))
        
        self.driver.get(MyLocators.URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.driver.find_element(By.NAME, self.name_userName).send_keys(self.root_Excel.iloc[i]["Username"])
        self.driver.find_element(By.NAME, self.name_userPassword).send_keys(self.root_Excel.iloc[i]["Password"])
        self.driver.find_element(By.XPATH, self.name_loginButton).click()

        try:
            message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.xPath_LoginMessage))
            )

            #print("Mensaje de Login: ", str(message.text))
            print("Fila: ", int_CurrentRow)

            # Guardamos el Mensaje
            df.loc[int_CurrentRow + 1, "Mensaje"] = message.text

        except TimeoutException as toe:
            print("Error: ", toe)
        
        self.driver.find_element(By.XPATH, self.xPath_SignOffButton).click()

        self.driver.implicitly_wait(5)

        int_CurrentRow +=1

        print("Login Exitoso!!!")