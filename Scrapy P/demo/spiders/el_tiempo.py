import scrapy
from demo.items import DemoItem

class TiempoSpider(scrapy.Spider):
    name = 'tiempo'
    start_urls = [
        'https://txtify.it/https://www.eltiempo.com/justicia/paz-y-derechos-humanos/falsos-positivos-de-soacha-ministro-de-defensa-ivan-velasquez-pidio-perdon-812315']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, headers={'User-Agent': 'Mozilla/5.0'})

    def parse(self, response):
        # Puedes implementar aquí la lógica para manejar cookies y desafíos de Cloudflare si es necesario
        mis_items = DemoItem()
        mis_items['titulo'] = response.xpath('//html/body/pre/text()').get()
        yield mis_items
