from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Locators.Locators import MyLocators


class TestCases():

    def __init__(self, driver):
        self.driver = driver

        self.name_Username = MyLocators.name_Username
        self.link_Text_Home = MyLocators.link_Text_Home
        self.link_text_Register = MyLocators.link_Text_Register
        self.link_Text_Flights = MyLocators.link_Text_Flights

        # Register
        self.name_FirstName = MyLocators.name_FirstName
        self.name_LastName = MyLocators.name_LastName
        self.name_Phone = MyLocators.name_Phone
        self.name_Email = MyLocators.name_Email
        self.name_Address = MyLocators.name_Address
        self.name_City = MyLocators.name_City
        self.name_State = MyLocators.name_State
        self.name_PostalCode = MyLocators.name_PostalCode
        self.name_Country = MyLocators.name_Country
        self.id_Email = MyLocators.id_Email
        self.name_Password = MyLocators.name_Password
        self.name_ConfirmPassword = MyLocators.name_ConfirmPassword
        self.name_Submit = MyLocators.name_Submit
        self.xpath_message = MyLocators.xpath_message

        # Flights
        self.name_TripType = MyLocators.name_TripType
        self.xpath_RoundTripe = MyLocators.xpath_RoundTripe
        self.xpath_OneWay = MyLocators.xpath_OneWay
        self.name_Passengers = MyLocators.name_Passengers
        self.name_Departing_From = MyLocators.name_Departing_From
        self.name_From_Month = MyLocators.name_From_Month
        self.name_From_Day = MyLocators.name_From_Day
        self.name_Arriving = MyLocators.name_Arriving
        self.name_Returning_Month = MyLocators.name_Returning_Month
        self.name_Returning_Day = MyLocators.name_Returning_Day
        self.xpath_Economy_Class = MyLocators.xpath_Economy_Class
        self.xpath_Business_Class = MyLocators.xpath_Business_Class
        self.xpath_First_Class = MyLocators.xpath_First_Class
        self.name_Airline = MyLocators.name_Airline
        self.name_Continue = MyLocators.name_Continue
        self.xpath_message_2 = MyLocators.xpath_message_2

    def Register(self):

        self.driver.find_element_by_link_text(self.link_Text_Home).click()

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.NAME, self.name_Username))
        )

        self.driver.find_element_by_link_text(self.link_text_Register).click()

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.NAME, self.name_FirstName))
        )

        self.driver.find_element_by_name(self.name_FirstName).send_keys("Emiliano")
        self.driver.find_element_by_name(self.name_LastName).send_keys("Cabrera")
        self.driver.find_element_by_name(self.name_Phone).send_keys("5545045186")
        self.driver.find_element_by_name(self.name_Email).send_keys("cabrerapereze@hotmail.com")
        self.driver.find_element_by_name(self.name_Address).send_keys("Pino #16")
        self.driver.find_element_by_name(self.name_City).send_keys("CDMX")
        self.driver.find_element_by_name(self.name_State).send_keys("Xochimilco")
        self.driver.find_element_by_name(self.name_PostalCode).send_keys("16030")
        strCountry = Select(self.driver.find_element_by_name(self.name_Country))
        strCountry.select_by_visible_text("MEXICO")
        self.driver.find_element_by_id(self.id_Email).send_keys("cabrerapereze@hotmail.com")
        self.driver.find_element_by_name(self.name_Password).send_keys("admin")
        self.driver.find_element_by_name(self.name_ConfirmPassword).send_keys("admin")
        self.driver.find_element_by_name(self.name_Submit).click()

        wait = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.xpath_message))
        )

    def Flights(self):
        self.driver.find_element_by_link_text(self.link_Text_Home).click()

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.NAME, self.name_Username))
        )

        self.driver.find_element_by_link_text(self.link_Text_Flights).click()

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.NAME, self.name_TripType))
        )

        self.driver.find_element_by_xpath(self.xpath_OneWay).click()

        Select(self.driver.find_element_by_name(self.name_Passengers)).select_by_visible_text("4")

        Select(self.driver.find_element_by_name(self.name_Departing_From)).select_by_visible_text("New York")

        Select(self.driver.find_element_by_name(self.name_From_Month)).select_by_visible_text("April")

        Select(self.driver.find_element_by_name(self.name_From_Day)).select_by_visible_text("25")

        Select(self.driver.find_element_by_name(self.name_Arriving)).select_by_visible_text("Paris")

        Select(self.driver.find_element_by_name(self.name_Returning_Month)).select_by_visible_text("April")

        Select(self.driver.find_element_by_name(self.name_Returning_Day)).select_by_visible_text("30")

        self.driver.find_element_by_xpath(self.xpath_Business_Class).click()

        Select(self.driver.find_element_by_name(self.name_Airline)).select_by_visible_text("Unified Airlines")

        self.driver.find_element_by_name(self.name_Continue).click()

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.xpath_message_2))
        )