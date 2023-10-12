import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

# Configurar Selenium y el navegador Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ejecutar en modo sin ventana

chrome_service = Service('/usr/lib/chromium-browser/chromedriver')  # Reemplaza con la ruta del chromedriver
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Leer el archivo de Excel
df = pd.read_excel('/home/buho/Descargas/Pruebas2.xlsx', sheet_name='Global News (162)')
columna_enlaces = df['Link']

# Iterar sobre los enlaces
for enlace in columna_enlaces:
    try:
        # Navegar a la página web
        driver.get(enlace)
        time.sleep(5)  # Esperar a que se cargue la página por completo (ajusta este valor según sea necesario)
        # Inicializar las variables con valores vacíos
        fecha = ""
        medio = ""
        titular = ""
        contenido = ""

        # Extraer los elementos necesarios
        fecha_element = driver.find_element(By.CSS_SELECTOR, 'ul.date.datechardin li.bold.ng-binding')
        fecha = fecha_element.text

        medio_element = driver.find_element(By.CSS_SELECTOR, 'span.label.label-info.label-media-name.ng-binding')
        medio = medio_element.text

        titular_element = driver.find_element(By.CSS_SELECTOR, '.title h4 a.datechardin')
        titular = titular_element.text

        contenido_element = driver.find_element(By.CSS_SELECTOR, 'div.media.cf.datechardin.ng-binding')
        contenido = contenido_element.text

        # Imprimir los resultados
        print("Enlace:", enlace)
        print("Fecha:", fecha)
        print("Titular:", titular)
        print("Medio:", medio)
        print("Contenido:", contenido)
        print("------------------------")

    except NoSuchElementException:
        print("Error al cargar el enlace:", enlace)
        print("------------------------")
        continue

# Cerrar el navegador
driver.quit()
