import requests
from bs4 import BeautifulSoup
from db import PostgreSql


class Parser:
    def __init__(self):
        self.URL = 'https://www.wildberries.ru/catalog/elektronika/noutbuki-pereferiya/noutbuki-ultrabuki'
        self.HOST = 'https://www.wildberries.ru'
        self.HEADERS = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/89.0.4389.114 Safari/537.36 '
        }

    def get_html(self, url):
        response = requests.get(url, headers=self.HEADERS)
        try:
            response.raise_for_status()
            return response.text
        except requests.HTTPError:
            print(f'Ошибка {response.status_code}')

    def get_content(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        main_block = soup.find('div', class_='catalog_main_table')
        product_block = main_block.find_all('div', class_='dtList-inner')

        content = []
        for product in product_block:
            brand_name = product.find('strong', class_='brand-name').get_text(strip=True).replace('/', '')
            product_image = 'https:' + product.find('noscript').find('img')['src']
            product_price = product.find("span", class_="price").find(class_="lower-price").get_text(strip=True)
            product_configurations = product.find("span", class_="goods-name").get_text()
            product_url = self.HOST + product.find("a", class_="ref_goods_n_p")["href"]

            content.append({
                "brand_name": brand_name,
                "product_url": product_url,
                "product_image": product_image,
                "product_price": product_price,
                "configurations": product_configurations
            })
        return content

    def run(self):
        html = self.get_html(self.URL)
        content = self.get_content(html)

        data_base = PostgreSql()
        data_base.create_table("laptops")
        for product in content:
            data_base.insert_data("laptops", *product.values())


Parser().run()
