import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

from Locators.Locators import MyLocators

class TestCases_Maquiladora():

    def __init__(self, driver):
        self.driver = driver
        self.XPath_Subscription_Message = MyLocators.XPath_Subscription_Message
        self.excelFile = pd.read_excel(MyLocators.root_Excel, engine = "openpyxl")
        self.href_MiCuenta = MyLocators.href_MiCuenta
        self.Name_User = MyLocators.Name_User
        self.Name_Password  = MyLocators.Name_Password 
        self.XPath_Enter_Button = MyLocators.XPath_Enter_Button
        self.Link_Directorio = MyLocators.Link_Directorio
        self.list_Columns = MyLocators.list_Columns

        self.XPath_Maquiladoras = MyLocators.XPath_Maquiladoras
        self.XPath_Table_Maquiladora = MyLocators.XPath_Table_Maquiladora
        self.XPath_Table_insideMaquiladora = MyLocators.XPath_Table_insideMaquiladora

        self.XPath_Razon_Social = MyLocators.XPath_Razon_Social
        self.XPath_Direccion = MyLocators.XPath_Direccion
        self.XPath_Parque_Industrial = MyLocators.XPath_Parque_Industrial
        self.XPath_Ciudad = MyLocators.XPath_Ciudad
        self.XPath_Telefono = MyLocators.XPath_Telefono
        self.XPath_Correo = MyLocators.XPath_Correo
        self.XPath_Sitio_Web = MyLocators.XPath_Sitio_Web

        self.XPath_Recursos_Humanos = MyLocators.XPath_Recursos_Humanos
        self.XPath_Compras = MyLocators.XPath_Compras
        self.XPath_Mantenimiento = MyLocators.XPath_Mantenimiento
        self.XPath_Control_Calidad = MyLocators.XPath_Control_Calidad

        self.XPath_Medio_Ambiente = MyLocators.XPath_Medio_Ambiente
        self.XPath_Sistemas = MyLocators.XPath_Sistemas
        self.XPath_Imports_Exports = MyLocators.XPath_Imports_Exports

    def start_TestCases(self):
        # iloc[R][C] - Read
        # loc[R,C] - Write
        global i
        for i in range(len(self.excelFile)):
            if self.excelFile.iloc[i]["Y/N"] == "Y":
                method_Name = self.excelFile.iloc[i]["Nombre"]
                try:
                    test_Method = getattr(TestCases_Maquiladora, method_Name)
                except AttributeError:
                    print("ERROR!")
                
                # Execute the Method.
                test_Method(self)
            else:
                pass
    
    def login(self):
        
        self.driver.find_element_by_xpath("//a[contains(@href, '" + self.href_MiCuenta + "')]").click()
        time.sleep(1)
        self.driver.find_element_by_name(self.Name_User).send_keys(self.excelFile.iloc[i]["Username"])
        self.driver.find_element_by_name(self.Name_Password).send_keys(self.excelFile.iloc[i]["Password"])
        self.driver.find_element_by_xpath(self.XPath_Enter_Button).click()

    def Test_001(self):

        # Creamos el DataFrame que será el Catalogo.
        df = pd.DataFrame(columns=self.list_Columns)

        # Validamos Mensaje de Suscripcion en caso de que Existe.
        try:
            self.driver.find_element_by_css_selector(".close > svg").click()
        except:
            pass
        
        self.login()

        # Click en DIRECTORIO
        element_to_hover_over = self.driver.find_element_by_link_text(self.Link_Directorio)
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.XPath_Maquiladoras).click()
        time.sleep(3)

        # Obtenemos la Tabla de Maquiladora
        interestingDivs_Maquiladoras = self.driver.find_elements_by_xpath(self.XPath_Table_Maquiladora)

        # Contamos la Cantidad de Elementos dentro de la Tabla de Maquiladoras.
        int_TotalDivs_Maquiladoras = 1 # Inicia necesariamente en 1.
        for each in interestingDivs_Maquiladoras:
            int_TotalDivs_Maquiladoras +=1

        # Definimos la Actual Fila que mantendra el Control en el Frame.
        global int_CurrectRow # Los Headers estan en la Fila 1.
        int_CurrectRow = 2
        
        # Leemos cada Elemento dentro de la Tabla de Maquiladoras.
        # int_TotalDivs_Maquiladoras
        for each_element in range(13, 25): # La Tabla de Maquiladoras empieza en 1.

            str_element_Maquiladora = self.driver.find_element_by_xpath(self.XPath_Table_Maquiladora + "[" + str(each_element) + "]").text

            # Guardamos el Elemento dentro del DataFrame.
            df.loc[int_CurrectRow, 'Categoria'] = str_element_Maquiladora

            # Ingresamos a cada Elemento de la Tabla de Maquiladoras.
            self.driver.find_element_by_xpath(self.XPath_Table_Maquiladora + "[" + str(each_element) + "]").click()

            # ---------- ----------

            # Tabla: Dentro del Elemento
            interestingDivs_insideMaquiladoras = self.driver.find_elements_by_xpath(self.XPath_Table_insideMaquiladora)

            # Contamos la Cantidad de Elementos dentro de la Nueva Tabla de Maquiladoras.
            int_TotalDivs_insideMaquiladoras = 1 # Inicia necesariamente en 1.
            for each in interestingDivs_insideMaquiladoras:
                int_TotalDivs_insideMaquiladoras += 1

            # Leemos cada elemento dentro de la Nueva Tabla de Maquiladoras.
            for each_elementInside in range(1, int_TotalDivs_insideMaquiladoras):

                str_element_insideMaquiladora = self.driver.find_element_by_xpath(self.XPath_Table_insideMaquiladora + "[" + str(each_elementInside) + "]").text

                # Ingresamos a los Datos Generales del Proveedor.
                self.driver.find_element_by_xpath(self.XPath_Table_insideMaquiladora + "[" + str(each_elementInside) + "]").click()

                # ---------- ---------- ----------

                # Ya adentro tomamos los Datos de cada Proveedor.
                # Guardamos el Elemento dentro del DataFrame.
                df.loc[int_CurrectRow, "Nombre"] = str_element_insideMaquiladora

                df.loc[int_CurrectRow, "Razon_Social"] = self.driver.find_element_by_xpath(self.XPath_Razon_Social).text

                df.loc[int_CurrectRow, "Direccion"] = self.driver.find_element_by_xpath(self.XPath_Direccion).text

                df.loc[int_CurrectRow, "Parque_Industrial"] = self.driver.find_element_by_xpath(self.XPath_Parque_Industrial).text

                df.loc[int_CurrectRow, "Ciudad"] = self.driver.find_element_by_xpath(self.XPath_Ciudad).text

                df.loc[int_CurrectRow, "Telefono"] = self.driver.find_element_by_xpath(self.XPath_Telefono).text

                df.loc[int_CurrectRow, "Correo"] = self.driver.find_element_by_xpath(self.XPath_Correo).text

                df.loc[int_CurrectRow, "Sitio_Web"] = self.driver.find_element_by_xpath(self.XPath_Sitio_Web).text

                # Obtenemos el Correo Personal de Cada Encargado de Departamento.
                email_Recursos_Humanos = self.driver.find_element_by_xpath(self.XPath_Recursos_Humanos+"/a").get_attribute('href')
                email_Recursos_Humanos = email_Recursos_Humanos.replace('mailto:', '')
                df.loc[int_CurrectRow, "Recursos_Humanos"] = self.driver.find_element_by_xpath(self.XPath_Recursos_Humanos).text + " - Email: " + email_Recursos_Humanos
                df.loc[int_CurrectRow, "Correo_RH"] = email_Recursos_Humanos

                email_Compras = self.driver.find_element_by_xpath(self.XPath_Compras+"/a").get_attribute('href')
                email_Compras = email_Compras.replace('mailto:', '')
                df.loc[int_CurrectRow, "Compras"] = self.driver.find_element_by_xpath(self.XPath_Compras).text + " - Email: " + email_Compras
                df.loc[int_CurrectRow, "Correo_Compras"] = email_Compras

                email_Mantenimiento = self.driver.find_element_by_xpath(self.XPath_Mantenimiento+"/a").get_attribute('href')
                email_Mantenimiento = email_Mantenimiento.replace('mailto:', '')
                df.loc[int_CurrectRow, "Mantenimiento"] = self.driver.find_element_by_xpath(self.XPath_Mantenimiento).text + " - Email: " + email_Mantenimiento
                df.loc[int_CurrectRow, "Correo_Mantenimiento"] = email_Mantenimiento

                email_Control_Calidad = self.driver.find_element_by_xpath(self.XPath_Control_Calidad+"/a").get_attribute('href')
                email_Control_Calidad = email_Control_Calidad.replace('mailto:', '')
                df.loc[int_CurrectRow, "Control_Calidad"] = self.driver.find_element_by_xpath(self.XPath_Control_Calidad).text + " - Email: " + email_Control_Calidad
                df.loc[int_CurrectRow, "Correo_Control_Calidad"] = email_Control_Calidad

                email_Medio_Ambiente = self.driver.find_element_by_xpath(self.XPath_Medio_Ambiente+"/a").get_attribute('href')
                email_Medio_Ambiente = email_Medio_Ambiente.replace('mailto:', '')
                df.loc[int_CurrectRow, "Medio_Ambiente"] = self.driver.find_element_by_xpath(self.XPath_Medio_Ambiente).text + " - Email: " + email_Medio_Ambiente
                df.loc[int_CurrectRow, "Correo_Medio_Ambiente"] = email_Medio_Ambiente

                email_Sistemas = self.driver.find_element_by_xpath(self.XPath_Sistemas+"/a").get_attribute('href')
                email_Sistemas = email_Sistemas.replace('mailto:', '')
                df.loc[int_CurrectRow, "Sistemas"] = self.driver.find_element_by_xpath(self.XPath_Sistemas).text + " - Email: " + email_Sistemas
                df.loc[int_CurrectRow, "Correo_Sistemas"] = email_Sistemas

                email_Imports_Exports = self.driver.find_element_by_xpath(self.XPath_Imports_Exports+"/a").get_attribute('href')
                email_Imports_Exports = email_Imports_Exports.replace('mailto:', '')
                df.loc[int_CurrectRow, "Imports/Exports"] = self.driver.find_element_by_xpath(self.XPath_Imports_Exports).text + " - Email: " + email_Imports_Exports
                df.loc[int_CurrectRow, "Correo_Imports_Exports"] = email_Imports_Exports

                int_CurrectRow += 1

                # Regresamos al Pag. de los Proveedores.
                self.driver.execute_script("window.history.go(-1)")

                time.sleep(1)

                # ---------- ---------- ----------

            # ---------- ----------

            # Regresamos al Pag. de la Tabla de Maquiladora.
            self.driver.execute_script("window.history.go(-1)")

            time.sleep(1)

            int_CurrectRow += 1

        print(df)

        df.to_excel("/Users/EmilianoCabreraPerez/Desktop/Maquiladora/Results/Catalogo.xlsx")