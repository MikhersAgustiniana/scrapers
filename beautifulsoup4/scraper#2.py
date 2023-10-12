import requests
from bs4 import BeautifulSoup
import re
import webbrowser

url = 'https://www.ibiza-spotlight.es/magazine/2023/01/ibiza-virgins-guide-melodic-techno'

try:
    response = requests.get(url)

    if response.status_code == 200:
        content = response.text

        soup = BeautifulSoup(content, 'html.parser')

        # article_h1 = soup.find('h1')
        article_tag = soup.find('article')

        # if article_h1:
        #     article_h1_text = article_h1.get_text()

        #     cleaned_h1_text = re.sub(r'\s+', ' ', article_h1_text).strip()

        #     print(cleaned_h1_text)
        # else:
        #     print('No se encontró la etiqueta "h1" en la página.')
        
        if article_tag:
            # article_text = article_tag.get_text()
            article_text = ' '.join(article_tag.stripped_strings)

            cleaned_article_text = re.sub(r'\s+', ' ', article_text).strip()

            with open('output.html', 'w', encoding='utf-8') as file:
                file.write('<!DOCTYPE html>\n<html>\n<head>\n<title>Contenido del Artículo</title>\n</head>\n<body>\n')
                file.write(str(article_text))
                file.write('\n</body>\n</html>')

            print('El contenido del artículo se ha guardado en "output.html"')
            webbrowser.open('output.html')

        else:
            print('No se encontró la etiqueta "article" en la página.')
    else:
        print(f'La solicitud a {url} falló con el código de estado {response.status_code}')

except requests.exceptions.RequestException as e:
    print(f'Error al hacer la solicitud: {e}')
