from urllib.request import Request
from urllib.request import urlopen


request_url = "http://m.11st.co.kr/MW/Shockingdeal/main.html"

def get_value_without_white_space(data_string):
    return data_string.replace(" ", "").replace("\n", "").replace("\t", "").replace("\r", "")

def get_value_without_white_space_with_line(data_string):
    return data_string.replace(" ", "").replace("\t", "").replace("\r", "")

class Collector:
    def get_basic_info(self):
        req = Request(request_url)
        data = urlopen(req).read()
        html_parser = HtmlParser()
        return html_parser.find_product_list(data)

    def __init__(self):
        pass


from bs4 import BeautifulSoup
class HtmlParser:
    def __init__(self):
        pass

    def find_product_list(self, web_source):
        product_list = []
        soup = BeautifulSoup(web_source, "html.parser")
        item_list_html = soup.find('ul', attrs={'class':'list_skdcard'}).find_all('li')
        for list_item in item_list_html:
            product_list.append(self.find_product_info(list_item))
        return product_list

    def find_product_info(self, product_info):
        product = {}
        product['link'] = product_info.find('a', {'href':True})['href']
        product['thumb_image'] = product_info.find('img')['src']
        product['name'] = product_info.find('span', attrs={'class':'name'}).text
        price_info = product_info.find('div', attrs={'class':'price'})
        product['price'] = price_info.find('span', attrs={'class':'prc'}).text.replace(',', '').replace('원','')
        product['delivery'] = get_value_without_white_space(product_info.find('span', attrs={'class':'bf'}).text)
        product['id'] = self.find_product_id(product['link'])
        print(product)
        return product

    def find_product_id(self, url_link):
        one_depth = url_link.split('prdNo=')
        two_depth = one_depth[1].split('&')
        return two_depth[0]