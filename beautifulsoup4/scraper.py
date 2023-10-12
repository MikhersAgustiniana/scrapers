import requests
from bs4 import BeautifulSoup
import re

# URL del sitio web que deseas obtener
# url = 'https://www.xataka.com/basics/como-ver-version-antigua-web-cache-google-archive-org'
url = 'https://www.ibiza-spotlight.es/magazine/2023/01/ibiza-virgins-guide-melodic-techno'

try:
    # Realizar una solicitud GET a la URL
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Obtener el contenido de la página web
        content = response.text

        # Crear un objeto BeautifulSoup para analizar el HTML
        soup = BeautifulSoup(content, 'html.parser')

        # Extraer el texto de los elementos HTML
        text = soup.get_text()

        # Utilizar una expresión regular para eliminar espacios en blanco adicionales
        cleaned_text = re.sub(r'\s+', ' ', text).strip()

        # Imprimir el contenido de texto sin etiquetas y sin espacios en blanco adicionales
        print(cleaned_text)
    else:
        print(f'La solicitud a {url} falló con el código de estado {response.status_code}')

except requests.exceptions.RequestException as e:
    print(f'Error al hacer la solicitud: {e}')
