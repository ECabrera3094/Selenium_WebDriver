class Locators_validation_TXT_CV():
    
    Loocker_URL = "https://amco.cloud.looker.com/login"
    Loocker_user = "datos_qa.cmx@clarovideotv.com"
    Loocker_password = "@#C1aR-9qA_"
    list_Countries = ['ARGENTINA',
                    'BRASIL',
                    'CHILE',
                    'COLOMBIA',
                    'COSTARICA',
                    'DOMINICANA',
                    'ECUADOR',
                    'ELSALVADOR',
                    'GUATEMALA',
                    'HONDURAS',
                    'MEXICO',
                    'NICARAGUA',
                    'PANAMA',
                    'PARAGUAY',
                    'PERU',
                    'URUGUAY']

    list_TXT_Operations_Files = ['Catalogo',
                    'Suscripciones',
                    'SuscripcionesDiarias',
                    'Temporada',
                    'Transacciones',
                    'Usuarios',
                    'Usuarios_Eliminados',
                    'UsuariosInactivos',
                    'UsuariosSinCustomerId',
                    'Visualizaciones']

    id_textbox_user = "login-email"
    id_textbox_password = "login-password"
    id_loging_button = "login-submit"
    xpath_main_page_logo = "/html/body/div[2]/div/div/div/header/div/div[1]/a/div/svg"
    xpath_dashboard_claro_video_link = "/html/body/div[2]/div/div/div/div/section/div/div[1]/div/a/span"
    xpath_produccion_link = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[1]/div/div[1]/lk-breadcrumbs/div/ul/li[2]/a"
    xpath_reportes_homologados_link = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[3]/div/div/lk-folder-children-section/div/div[2]/a[5]/div/div"
    xpath_claro_video_link = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[3]/div/div/lk-folder-children-section/div/div[2]/a[3]/div/div"
    xpath_archivos_txt_link = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[3]/div/div/lk-folder-children-section/div/div[2]/a[2]/div/div"
    xpath_archivos_operaciones_cv_link = "/html/body/div[2]/div/div/div/div/section/folders-subrouter/div/div/lk-folder/div/div[3]/div/div/lk-browse-table[1]/table/tbody/tr[1]/td[3]/div/a/div[1]"
    xpath_pais_button = "/html/body/div[2]/div/div/div/div/section/div/div[1]/div/div[2]/section/div/div/div/span/span"
    xpath_close_pais = "/html/body/div[3]/div/div/div/div/div/div/div/div/div[2]/button/div[2]"
    xpath_listbox_pais = "/html/body/div[3]/div/div/div/div/div/div/div/div/div[1]/input[2]"
    xpath_actualizar_button = "/html/body/div[2]/div/div/div/div/section/div/div[1]/div/div[1]/div[2]/div/div/button"                
    xpath_descargar_archivo_button = "/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[2]/div/section/div/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[4]/div/span/div/div/span/span/a/button"

    Download_path = "C:\\Automation\\Claro\\Downloads"
    Evidence_path = "C:\\Automation\\Claro\\Evidence\\Reporte.html"
    Drivers_path = "C:\\Automation\\Claro\\Drivers\\chromedriver.exe"
    Usuarios_CSV_File_path = "C:\\Users\\Emiliano Cabrera P\\Desktop\\Visualizaciones_ARGENTINA_20240527.csv"
    Usuarios_CTL_File_path  = "C:\\Users\\Emiliano Cabrera P\\Desktop\\Usuarios_MEXICO_20240521.ctl"
    Usuarios_Parquet_File_path  = "C:\\Users\\Emiliano Cabrera P\\Desktop\\Visualizaciones_ARGENTINA_20240527.parquet"





