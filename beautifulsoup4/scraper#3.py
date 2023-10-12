import webbrowser
import requests
from bs4 import BeautifulSoup

# URL del sitio web que deseas obtener
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

        # Encontrar la etiqueta "article" y extraer su contenido
        article_tag = soup.find('article')

        if article_tag:
            # Inicializar una cadena para almacenar el contenido con saltos de línea
            article_text = ''

            # Iterar sobre los elementos de texto dentro de "article"
            for element in article_tag.descendants:
                if isinstance(element, str):
                    article_text += element + '\n'

            # Imprimir el contenido del "article" con saltos de línea
            with open('output.html', 'w', encoding='utf-8') as file:
                file.write('<!DOCTYPE html>\n<html>')
                file.write('\n<head>\n<title>Contenido del Artículo</title>\n</head>')
                file.write('\n<meta name="color-scheme" content="light dark">')
                file.write('\n<body>\n')
                file.write(f"<pre>\n{article_text.strip()}\n</pre>")
                file.write('\n</body>\n</html>')

            print('El contenido del artículo se ha guardado en "output.html"')
            webbrowser.open('output.html')
            print(article_text.strip())
        else:
            print('No se encontró la etiqueta "article" en la página.')
    else:
        print(f'La solicitud a {url} falló con el código de estado {response.status_code}')

except requests.exceptions.RequestException as e:
    print(f'Error al hacer la solicitud: {e}')
