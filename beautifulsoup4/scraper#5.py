import webbrowser
import requests
from bs4 import BeautifulSoup

url = 'https://www.ibiza-spotlight.es/magazine/2023/01/ibiza-virgins-guide-melodic-techno'

def limpieza(text):
    cleaned_text = '\n'.join(line.strip() for line in text.splitlines() if line.strip())
    return cleaned_text

def encontrar_titulo(html: BeautifulSoup) -> BeautifulSoup:
    for i in range(1, 8):
        header = html.find(f'h{i}')
        if header:
            return header.get_text()
    return ''

def contenido(html: BeautifulSoup) -> str:

    return

def encontrar_main(html: BeautifulSoup) -> BeautifulSoup:
    main = html.find("main")
    import pdb;pdb.set_trace()
    if main:
        return main
    article = html.find("article")
    if article:
        return article
    return None



try:
    response = requests.get(url)

    if response.status_code == 200:
        content = response.text

        soup = BeautifulSoup(content, 'html.parser')

        articulo_completo = encontrar_titulo(soup)
        articulo_completo += f"{encontrar_main(soup)}"

#        if articulo_completo:
#            article_text = ''

#            for element in articulo_completo.stripped_strings:
#                if str(element) == ".":
#                    del element
#                else:
#                    article_text += element + '\n'

#            with open('output.html', 'w', encoding='utf-8') as file:
#                file.write('<!DOCTYPE html>\n<html>')
#                file.write('\n<head>\n<title>Contenido del Artículo</title>\n</head>')
#                file.write('\n<meta name="color-scheme" content="light dark">')
#                file.write('\n<body>\n')
#                file.write(f"<pre>\n{article_text.strip()}\n</pre>")
#                file.write('\n</body>\n</html>')

#            print('El contenido del artículo se ha guardado en "output.html"')
#            webbrowser.open('output.html')
#        else:
#            print('No se encontró la etiqueta "article" en la página.')
#    else:
#        print(f'La solicitud a {url} falló con el código de estado {response.status_code}')

except requests.exceptions.RequestException as e:
    print(f'Error al hacer la solicitud: {e}')
