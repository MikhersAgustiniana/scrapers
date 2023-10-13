import webbrowser
import requests
from bs4 import BeautifulSoup

url = 'https://www.ibiza-spotlight.es/magazine/2023/01/ibiza-virgins-guide-melodic-techno'

try:
    response = requests.get(url)

    if response.status_code == 200:
        content = response.text

        soup = BeautifulSoup(content, 'html.parser')

        article_tag = soup.find('main')

        if article_tag:
            article_text = ''

            # Definir etiquetas a omitir
            tags_to_exclude = ['iframe', 'img', 'ul', 'li']

            for element in article_tag.descendants:
                if element.name not in tags_to_exclude:
                    if element.string:
                        article_text += element.string.strip() + '\n'

            with open('output.html', 'w', encoding='utf-8') as file:
                file.write('<!DOCTYPE html>\n<html>')
                file.write('\n<head>\n<title>Contenido del Artículo</title>\n</head>')
                file.write('\n<meta name="color-scheme" content="light dark">')
                file.write('\n<body>\n')
                file.write(f"<pre>\n{article_text.strip()}\n</pre>")
                file.write('\n</body>\n</html>')

            print('El contenido del artículo se ha guardado en "output.html"')
            webbrowser.open('output.html')
        else:
            print('No se encontró la etiqueta "main" en la página.')
    else:
        print(f'La solicitud a {url} falló con el código de estado {response.status_code}')

except requests.exceptions.RequestException as e:
    print(f'Error al hacer la solicitud: {e}')
