class MyLocators():

    Driver_Path = "E:\\QAMinds\\WebDrivers\\chromedriver.exe"
    URL = "https://demo.guru99.com/test/newtours/index.php"
    root_Excel = "E:\\QAMinds\\Data\\Test_Matrix.xlsx"

    # Main Page
    name_userName = "userName"
    name_userPassword = "password"
    name_loginButton = "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[4]/td[2]/div/input"
    xPath_LoginMessage = "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/h3"
    xPath_SignOffButton =  "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/a"
    #xPath_SignOffButton = "//a[contains(.,'SIGN-OFF')]"

    # Flights
    xPath_flightsButton = "/html/body/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/a"
    xPath_RoundTrip = "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[2]/td[2]/b/font/input[1]"
    xPath_OneWay = "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[2]/td[2]/b/font/input[2]"
    name_Passengers = "passCount"
    name_Departing = "fromPort"
    name_On_Month = "fromMonth"
    name_On_Day = "fromDay"
    name_Arraiving = "toPort"
    name_Returning_Monthy = "toMonth"
    name_Returning_Day = "toDay"
    xPath_First_Class = "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[9]/td[2]/font/font/input[2]"
    value_Economy_Class = "Coach"
    value_Business_Class = "Business"
    name_Airline = "airline"
    name_FindFlightsButton = "findFlights"
    xPath_FlightMessage = "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td/p/font"
    xPath_BackHomeButton = "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td/a"

    # Tabla de Evidencia
    list_Columns = ["Mensaje"]   