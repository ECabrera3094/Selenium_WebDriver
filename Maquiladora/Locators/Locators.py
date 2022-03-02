class MyLocators():

    Driver_Path = "/Users/EmilianoCabreraPerez/Downloads/chromedriver"
    URL = "https://industriamaquiladora.com/index.php"
    root_Excel = "/Users/EmilianoCabreraPerez/Desktop/Maquiladora/Test_Matrix.xlsx"

    XPath_Subscription_Message = "//*[@id='mbr-popup-cp']/div/div/div[1]/button/svg"
    href_MiCuenta = "acceso.php"
    Name_User = "usuario"
    Name_Password = "clave"
    XPath_Enter_Button = "//*[@id='extForm20-6h']/div/div/div[2]/form/div/div[4]/button"
    Link_Directorio = "DIRECTORIO"
    XPath_Maquiladoras = "//*[@id='navbarSupportedContent']/ul/li[5]/div/a[1]"
    XPath_Table_Maquiladora = "//*[@id='content12-2m']/div/div/div[1]/div"
    XPath_Table_insideMaquiladora = "//*[@id='content12-2e']/div/div/div[2]/div/div"
    
    XPath_Razon_Social      = "//*[@id='extFooter2-2u']/div/div/div[1]/div/div[1]/div[2]"
    XPath_Direccion         = "//*[@id='extFooter2-2u']/div/div/div[1]/div/div[2]/div[2]"
    XPath_Parque_Industrial = "//*[@id='extFooter2-2u']/div/div/div[1]/div/div[3]/div[2]"
    XPath_Ciudad            = "//*[@id='extFooter2-2u']/div/div/div[1]/div/div[4]/div[2]"
    XPath_Telefono          = "//*[@id='extFooter2-2u']/div/div/div[1]/div/div[5]/div[2]"
    XPath_Correo            = "//*[@id='extFooter2-2u']/div/div/div[1]/div/div[6]/div[2]"
    XPath_Sitio_Web         = "//*[@id='extFooter2-2u']/div/div/div[1]/div/div[7]/div[2]"

    XPath_Recursos_Humanos  = "//*[@id='content13-31']/div/div/div[1]/div[1]"
    XPath_Compras           = "//*[@id='content13-31']/div/div/div[1]/div[2]"
    XPath_Mantenimiento     = "//*[@id='content13-31']/div/div/div[1]/div[3]"
    XPath_Control_Calidad   = "//*[@id='content13-31']/div/div/div[1]/div[4]"

    XPath_Medio_Ambiente    = "//*[@id='contactos2']/div[1]"
    XPath_Sistemas          = "//*[@id='contactos2']/div[2]"
    XPath_Imports_Exports   = "//*[@id='contactos2']/div[3]"

    list_Columns = ["Categoria", "Nombre", "Razon_Social", "Direccion", "Parque_Industrial", "Ciudad", "Telefono", "Correo", "Sitio_Web", 
                    "Recursos_Humanos", "Correo_RH", "Compras", "Correo_Compras", "Mantenimiento", "Correo_Mantenimiento","Control_Calidad", "Correo_Control_Calidad"
                    "Medio_Ambiente", "Correo_Medio_Ambiente", "Sistemas", "Correo_Sistemas" ,"Imports/Exports", "Correo_Imports_Exports"]
