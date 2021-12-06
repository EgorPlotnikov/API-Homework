import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
news = []

for elem in root.findall(r'./channel/item'):
    dic = {}
    for item in elem:
        dic[item.tag] = item.text
    news.append(dic)

with open('xml_item.json', 'w', encoding='utf-8') as end_file:
    json.dump(news, fp=end_file, ensure_ascii=False, indent=4, sort_keys=True)
