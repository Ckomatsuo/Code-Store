import re
import requests
from bs4 import BeautifulSoup
from pyquery import PyQuery


def get_content():
    url = "https://www.cfmem.com/search/label/free"
    # proxies = {
    #     "http": "http://localhost:1080",
    #     "https": "http://localhost:1080",
    # }
    proxies = {}
    data = requests.get(url, proxies=proxies)
    text = data.text
    soup = BeautifulSoup(text, "lxml")
    div_list = soup.findAll(
        name="a",
        attrs={
            "href": re.compile(
                r"https?://www\.cfmem\.com/\d{4}/\d{2}/\S+v2rayclash-vpn.html"
            )
        },
    )
    a_list = []
    p = re.compile(r"\d{4}年\d+月\d{2}日更新")
    for val in div_list[:1]:
        print(val.text)
        if p.search(val.text):
            a_list.append(val.get("href"))

    new_v2ray_url = a_list[0]
    new_v2ray_data = requests.get(new_v2ray_url, proxies=proxies)
    new_v2ray_data_html = new_v2ray_data.text
    doc = PyQuery(new_v2ray_data_html)
    urls = re.findall(
        "https?://raw.githubusercontent\.com/changfengoss/pub/main/data/\S+\.yaml",
        doc.text(),
    )
    for url in urls:
        file = requests.get(url, proxies=proxies)
        with open("sub/cfmem.yaml", "wb") as f:
            f.write(file.content)


if __name__ == '__main__':
    get_content()
