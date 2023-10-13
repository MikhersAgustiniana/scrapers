import requests

url = "https://full-text-rss.p.rapidapi.com/extract.php"

payload = {
	"url": "chomsky.info/articles/20131105.htm",
	"inputhtml": "<html><head><title>Example</title><body><article itemprop=\"articleBody\"><p>Test</p></article></body></html>",
	"xss": "1",
	"lang": "2",
	"links": "remove",
	"content": "1"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "c93a0b3d01msh9f9392b19ef14c6p12c1ecjsn0e32843eae6f",
	"X-RapidAPI-Host": "full-text-rss.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())