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

class TC_2():
    
    def __init__(self, driver):

        self.driver = driver
        self.root_Excel = pd.read_excel(MyLocators.root_Excel, engine = "openpyxl")
        self.list_Columns = MyLocators.list_Columns
        self.xPath_flightsButton = MyLocators.xPath_flightsButton
        self.xPath_RoundTrip = MyLocators.xPath_RoundTrip
        self.xPath_OneWay = MyLocators.xPath_OneWay
        self.name_Passengers = MyLocators.name_Passengers
        self.name_Departing = MyLocators.name_Departing
        self.name_On_Month = MyLocators.name_On_Month
        self.name_On_Day = MyLocators.name_On_Day
        self.name_Arraiving = MyLocators.name_Arraiving
        self.name_Returning_Monthy = MyLocators.name_Returning_Monthy
        self.name_Returning_Day = MyLocators.name_Returning_Day
        self.xPath_First_Class = MyLocators.xPath_First_Class
        self.value_Economy_Class = MyLocators.value_Economy_Class
        self.value_Business_Class = MyLocators.value_Business_Class
        self.name_Airline = MyLocators.name_Airline
        self.name_FindFlightsButton = MyLocators.name_FindFlightsButton
        self.xPath_FlightMessage = MyLocators.xPath_FlightMessage   
        self.xPath_BackHomeButton = MyLocators.xPath_BackHomeButton

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
                    test_Method = getattr(TC_2, method_Name)
                except AttributeError:
                    print("ERROR!!!")
                
                test_Method(self, df)
                
            else:
                pass

        # Escritura del Dataframe a formato CSV
        df.to_csv("E:\\QAMinds\\Evidence\\Vuelos.csv")

    def Test_002(self, df):
        
        print(">>> TC:", self.root_Excel.iloc[i]["ID Test"])

        global int_CurrentRow
        int_CurrentRow = int(copy.copy(i))
        
        self.driver.get(MyLocators.URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.driver.find_element(By.XPATH, self.xPath_flightsButton).click()

        # Screenshoot
        self.driver.save_screenshot("E:\\QAMinds\\Evidence\\image_2.png")

        # Validamos el Tipo de Vuelo
        if self.root_Excel.iloc[i]["Type"] == "One":
            self.driver.find_element(By.XPATH, self.xPath_OneWay).click()
        elif self.root_Excel.iloc[i]["Type"] == "Round":
            self.driver.find_element(By.XPATH, self.xPath_RoundTrip).click()
        else:
            print("Tipo de vuelo INCORRECTO. Favor de Revisar la Matriz.")
        
        # Validamos los Pasajeros
        passengers = Select(self.driver.find_element(By.NAME, self.name_Passengers))
        passengers.select_by_value(str(self.root_Excel.iloc[i]["Passengers"]))

        # Validamos Destino de Salida
        departing = Select(self.driver.find_element(By.NAME, self.name_Departing))
        departing.select_by_value(self.root_Excel.iloc[i]["Departing"])
        
        # Validamos Mes de Salida
        dict_month = {"January": 1, 
                      "February":2,
                      "March": 3,
                      "April": 4,
                      "May": 5,
                      "June": 6,
                      "July": 7,
                      "August": 8,
                      "September": 9,
                      "October" : 10,
                      "November" : 11,
                      "December": 12
                      }
        
        key_month = self.root_Excel.iloc[i]["On_Month"]
        on_month = Select(self.driver.find_element(By.NAME, self.name_On_Month))
        on_month.select_by_value(str(dict_month[key_month]))

        # Validamos Dia de Salida
        on_day = Select(self.driver.find_element(By.NAME, self.name_On_Day))
        on_day.select_by_value(str(self.root_Excel.iloc[i]["On_Day"]))

        # Validamos Destino de Retorno
        arriving = Select(self.driver.find_element(By.NAME, self.name_Arraiving))
        arriving.select_by_value(self.root_Excel.iloc[i]["Arriving"])

        # Validamos Mes de Retorno
        key_month = self.root_Excel.iloc[i]["Returning_Month"]
        returning_month = Select(self.driver.find_element(By.NAME, self.name_Returning_Monthy))
        returning_month.select_by_value(str(dict_month[key_month]))

        # Validamos Dia de Retorno
        returning_day = Select(self.driver.find_element(By.NAME, self.name_Returning_Day)) 
        returning_day.select_by_value(str(self.root_Excel.iloc[i]["Returning_Day"]))

        # Validamos la Clase de Vuelo
        if self.root_Excel.iloc[i]["Class"] == "First":
            self.driver.find_element(By.XPATH, self.xPath_First_Class).click()

        # Validamos la Aerolinea
        airline  = Select(self.driver.find_element(By.NAME, self.name_Airline)) 
        airline.select_by_visible_text(self.root_Excel.iloc[i]["Airline"])

        # Screenshoot
        self.driver.save_screenshot("E:\\QAMinds\\Evidence\\image_3.png")

        # Click en Continuar
        self.driver.find_element(By.NAME, self.name_FindFlightsButton).click()

        try:
            message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.xPath_FlightMessage))
            )

            print(message.text)
            #df.loc[i, "Mensaje"] = message.text
        except:
            print("No se Mostró Respuesta :(")

        # Screenshoot
        self.driver.save_screenshot("E:\\QAMinds\\Evidence\\image.png")

        self.driver.find_element(By.XPATH, self.xPath_BackHomeButton).click()

        print("Registro Exitoso. :)")