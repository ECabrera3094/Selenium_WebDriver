import os
import time
import zipfile
import pyarrow
import datetime
import unittest 
import itertools
import pandas as pd
from pyarrow import csv
import pyarrow.parquet as pq
import pyarrow.parquet
from tqdm import tqdm
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

# Locators
from Locators.locators_validation_TXT_CV import Locators_validation_TXT_CV

class TestCases_validation_TXT_CV():

    def __init__(self):
        self.Drivers_path  = Locators_validation_TXT_CV.Drivers_path 

        self.Loocker_URL = Locators_validation_TXT_CV.Loocker_URL
        self.Loocker_user = Locators_validation_TXT_CV.Loocker_user 
        self.Loocker_password = Locators_validation_TXT_CV.Loocker_password
        self.list_Countries = Locators_validation_TXT_CV.list_Countries
        self.list_TXT_Operations_Files = Locators_validation_TXT_CV.list_TXT_Operations_Files

        self.id_textbox_user = Locators_validation_TXT_CV.id_textbox_user 
        self.id_textbox_password  = Locators_validation_TXT_CV.id_textbox_password 
        self.id_loging_button = Locators_validation_TXT_CV.id_loging_button
        self.xpath_main_page_logo = Locators_validation_TXT_CV.xpath_main_page_logo
        self.xpath_dashboard_claro_video_link = Locators_validation_TXT_CV.xpath_dashboard_claro_video_link
        self.xpath_produccion_link = Locators_validation_TXT_CV.xpath_produccion_link
        self.xpath_reportes_homologados_link = Locators_validation_TXT_CV.xpath_reportes_homologados_link
        self.xpath_claro_video_link = Locators_validation_TXT_CV.xpath_claro_video_link
        self.xpath_archivos_txt_link = Locators_validation_TXT_CV.xpath_archivos_txt_link
        self.xpath_archivos_operaciones_cv_link = Locators_validation_TXT_CV.xpath_archivos_operaciones_cv_link
        self.xpath_pais_button = Locators_validation_TXT_CV.xpath_pais_button
        self.xpath_close_pais = Locators_validation_TXT_CV.xpath_close_pais
        self.xpath_listbox_pais = Locators_validation_TXT_CV.xpath_listbox_pais
        self.xpath_actualizar_button = Locators_validation_TXT_CV.xpath_actualizar_button
        self.xpath_descargar_archivo_button = Locators_validation_TXT_CV.xpath_descargar_archivo_button

        self.Download_path = Locators_validation_TXT_CV.Download_path
        self.Usuarios_CSV_File_path = Locators_validation_TXT_CV.Usuarios_CSV_File_path
        self.Usuarios_CTL_File_path = Locators_validation_TXT_CV.Usuarios_CTL_File_path
        self.Usuarios_Parquet_File_path = Locators_validation_TXT_CV.Usuarios_Parquet_File_path

    def start(self):
        self.download_Compressed_Files()
        self.unzip_Compressed_Files()
        #self.convert_CSV_to_Parquet(self.Usuarios_CSV_File_path, self.Usuarios_Parquet_File_path)

    def download_Compressed_Files(self):

        # Specify Services as Driver Path
        service = Service(executable_path = self.Drivers_path)
        # Specify Chrome Options
        options = webdriver.ChromeOptions()
        # Specify the Path of any Download
        options.add_experimental_option('prefs', {'download.default_directory' : self.Download_path} )
        driver = webdriver.Chrome(service = service, options = options)
        driver.maximize_window()
        driver.get(self.Loocker_URL)
        #driver.delete_all_cookies()
        # Validate the Login Page based on the User Textbox
        try:
            WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.ID, self.id_textbox_user))
            )
        except TimeoutException as toe:
            print("Timeout Error on Loading Page: ", toe)
        # Enter Username
        driver.find_element(By.ID, self.id_textbox_user).send_keys(self.Loocker_user)
        # Enter Password
        driver.find_element(By.ID, self.id_textbox_password).send_keys(self.Loocker_password)
        # Click Login Button
        driver.find_element(By.ID, self.id_loging_button).click()
        # Validate the Main Page based on the Dashboard Claro Video Link
        try:
            WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.xpath_dashboard_claro_video_link))
            )
        except TimeoutException as toe:
            print("Timeout Error on Loading Page: ", toe)
        # Click on "Dashboards Claro" Link
        driver.find_element(By.XPATH, self.xpath_dashboard_claro_video_link).click()
        time.sleep(2)
        # Click on "Produccion" Link
        driver.find_element(By.XPATH, self.xpath_produccion_link).click()
        time.sleep(2)
        # Click on "Reportes Homologados" Link
        driver.find_element(By.XPATH, self.xpath_reportes_homologados_link).click()
        time.sleep(2)
        # Click on "Claro Video" Link
        driver.find_element(By.XPATH, self.xpath_claro_video_link).click()
        time.sleep(2)
        # Click on "Archivos TXT" Link
        driver.find_element(By.XPATH, self.xpath_archivos_txt_link).click()
        time.sleep(2)
        # Click on "Archivos de Operaciones CV" Link
        driver.find_element(By.XPATH, self.xpath_archivos_operaciones_cv_link).click()
        time.sleep(10) # <-----
        # --------------------------------
        # Start the Loop of Countries
        # === Start on Argentin and ends of Uruguay.
        i = 1
        for _ in itertools.repeat(None, 16):
            # Click on "Pais" Button
            driver.find_element(By.XPATH, self.xpath_pais_button).click()
            time.sleep(2)
            # Click on "X" if you have already a Countrie on the Field.
            try:
                driver.find_element(By.XPATH, self.xpath_close_pais ).click()
            except:
                pass
            # Click on the Listbox
            driver.find_element(By.XPATH, self.xpath_listbox_pais).click() 
            time.sleep(2)
            # Choose a Countrie
            driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div/ul/li["+str(i)+"]/div/div").click() # !!!
            time.sleep(2)
            # Clik on "Actualizar" Button
            driver.find_element(By.XPATH, self.xpath_actualizar_button).click() 
            time.sleep(10)
            # Click on "Descargar Archivo" Button
            driver.find_element(By.XPATH, self.xpath_descargar_archivo_button).click()
            time.sleep(15)
            # Count +1
            i += 1
        # --------------------------------
        # Checking the Download Process
        wait = True

        while(wait == True):
            # Returns an Array with the Full Path of each element inside.
            chrome_temp_file = sorted(Path(self.Download_path).glob('*.crdownload'))
            firefox_temp_file = sorted(Path(self.Download_path).glob('*.part'))
            print("Array: ", len(chrome_temp_file))
            # If the Array contains more than one .crdownload File, we have to wait
            if (len(chrome_temp_file) >= 1 or len(firefox_temp_file) >= 1):
                print('downloading files ...')
                time.sleep(30)
            else:
                # Break the Loop.
                wait = False
        print('Finished Downloading All Files ...')
        # --------------------------------
        # End of Session
        driver.close()
        driver.quit()

    def convert_CSV_to_Parquet(self, csv_file_path, parquet_file_path):
        # Symbol that Delimit each Element of the Frame
        delmt = '|' 
        table = csv.read_csv(csv_file_path, parse_options = csv.ParseOptions(delimiter = delmt))
        # Save the Parquet File
        pyarrow.parquet.write_table(table, parquet_file_path)

    def unzip_Compressed_Files(self):
        
        # Obtain the DateTime and Replace the "-" symbol. 
        today = str(datetime.date.today()).replace("-","")
        #today = str(20240602)
        # ----- Enter the Zip File
        # Validate the 16 Countries
        for country in self.list_Countries:
            try: 
                # Create a New Directory where the Files will be Extracted
                new_Download_Directory = self.Download_path + '\\txt_' + country + '_' + today
                os.mkdir(new_Download_Directory) 
                # Descargamos los Archivos según su País y Carpeta
                # loading the temp.zip and creating a zip object 
                with zipfile.ZipFile(self.Download_path + '\\txt_' + country + '_' + today +'.zip', 'r') as zipObject:
                    zipObject.extractall(path = new_Download_Directory)
            except:
                pass
            print("Pais: ", country, " OK")

        # Validate the 16 Countries
        for country in self.list_Countries:
            # Read again the Download Path
            new_Download_Directory = self.Download_path + '\\txt_' + country + '_' + today
            # ----- Read earch TXT File
            for title_Operation in self.list_TXT_Operations_Files:
                try:

                    # ----- CSV
                    # Convert CSV to Paruet File
                    csv_file_path = new_Download_Directory + '\\' + title_Operation + '_' +  country + '_' + today + ".csv"
                    parquet_file_path = new_Download_Directory + '\\' + title_Operation + '_' +  country + '_' + today + ".parquet"
                    self.convert_CSV_to_Parquet(csv_file_path, parquet_file_path)
                    csv_file = pd.read_parquet(parquet_file_path, engine='pyarrow')
                    #print(len(csv_file))

                    # ----- CTL
                    # Open CTL File
                    ctl_file = open(new_Download_Directory + '\\' + title_Operation + '_' +  country + '_' + today + ".ctl", "rb")
                    # Read CTL File
                    ctl_value = int(ctl_file.read()) # <-- Converto CTL to Int. 
                    # Close CTL File
                    ctl_file.close()

                    print('CSV - CTL {0} {1} OK'.format(country, title_Operation) if len(csv_file) == ctl_value else 'CSV - CTL {0} {1} FAIL'.format(country, title_Operation))

                    # ----- MD5
                    # Open MD5 File
                    md5_file = open(new_Download_Directory + '\\' + title_Operation + '_' +  country + '_' + today + ".md5_", "rb")
                    # Read MD5 File
                    md5_value = md5_file.read()
                    print("Archivo MD5 PASS" if len(md5_value) == 32 else "Archivo MD5 FAIL")
                    # Close MD5 File
                    md5_file.close()
                except:
                    pass
'''
- validar que exista el archivo en el zip
- validar que el csv no venga vacio
- validar que el bionario sea de una linea o no venga vacio
- saber crear un nuevo reporte HTML.

Visualizaciones_ARGENTINA_20240527
'''

'''
        #df = pd.DataFrame()
        df = pd.read_csv(csv_file_path, engine = 'python', header = 0, sep='|', encoding='utf-8')
        print(len(table))
        #df.to_parquet(parquet_file_path)
        table = pa.Table.from_pandas(df)
        pq.write_table(table, parquet_file_path)
        print(len(table))
        #return df
'''