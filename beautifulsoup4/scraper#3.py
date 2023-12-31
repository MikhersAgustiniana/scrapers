import webbrowser
import requests
from bs4 import BeautifulSoup

url = 'https://www.eltiempo.com/justicia/delitos/emilio-tapia-es-declarado-exento-de-responsabilidad-fiscal-en-caso-de-centros-poblados-815563'

try:
    response = requests.get(url)

    if response.status_code == 200:
        content = response.text

        soup = BeautifulSoup(content, 'html.parser')

        # Encontrar la etiqueta "article" y extraer su contenido
        article_tag = soup.find('article')

        if article_tag:
            article_text = ''

            for element in article_tag.stripped_strings:
                if str(element) == ".":
                    del element
                else:
                    article_text += element + '\n\n'

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
            print('No se encontró la etiqueta "article" en la página.')
    else:
        print(f'La solicitud a {url} falló con el código de estado {response.status_code}')

except requests.exceptions.RequestException as e:
    print(f'Error al hacer la solicitud: {e}')
