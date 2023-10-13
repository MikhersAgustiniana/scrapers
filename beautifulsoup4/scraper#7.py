import requests
from bs4 import BeautifulSoup

def get_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        ignored_tags = ['iframe', 'img', 'ul', 'li', 'footer', 'nav', 'comment', 'header']

        main_tag = soup.find('main')

        if main_tag:
            relevant_text = []
            for tag in main_tag.find_all(string=True, recursive=False):
                if tag.parent.name not in ignored_tags:
                    if len(tag.strip()) > 50:
                        relevant_text.append(tag.strip())

            # Une el texto relevante en un solo bloque de texto
            result_text = '\n'.join(relevant_text)
            return result_text
        else:
            return "No se encontró la etiqueta 'main' en la página."

    except requests.exceptions.RequestException as e:
        return f"Error al realizar la solicitud: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"

# Prueba la función con una URL
url = "https://www.ibiza-spotlight.es/magazine/2023/01/ibiza-virgins-guide-melodic-techno"
result = get_text_from_url(url)
print(result)
