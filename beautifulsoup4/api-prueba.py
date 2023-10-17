import requests

url = "https://txtify.it/go.php"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "es-ES,es;q=0.9",
    "Cache-Control": "max-age=0",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "cf_clearance=764OwO5xuDhzmiWvzPtkyhiV26FTRjJ9Y95Umz5OWj8-1697216355-0-1-34a0b652.d58591ea.63a1e9b2-160.0.0",
    "Origin": "https://txtify.it",
    "Referer": "https://txtify.it/",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

data = {
    "url": "https://www.eltiempo.com/bogota/capturaron-a-colombiano-que-violo-y-mato-a-su-hijastro-de-17-meses-por-llorar-815729"
}

response = requests.post(url, headers=headers, data=data)

import pdb; pdb.set_trace()
print(response.json())
