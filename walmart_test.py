from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.walmart.com/browse/electronics/3944'

url1 = 'https://www.walmart.com/cp/clothing/5438'

hdr = {'User-Agent': 'Mozilla/5.0', "content-type": "text"}
response = requests.get(url, headers=hdr)
soup = BeautifulSoup(response.text, 'html.parser')

def search_key(prep, desired):
    queue = [prep]

    while queue:
        node = queue.pop(0)
        keys = node.keys()
        for key in keys:
            if key == desired:
                return True
            if type(node[key]) == dict:
                queue.append(node)
            if type(node[key]) == list:
                for item in node[key]:
                    


itemBody = soup.find('script', {'id': 'searchContent','type': 'application/json'})

itemDict = json.loads(itemBody.contents[0])
print(search_key(itemDict, 'items'))
#items = itemDict['category']['presoData']['modules']['center'][0]['configs']['items']
items = itemDict['searchContent']['preso']['items']

# for item in items:
#     print(item['title'])

#pressdata modules top[2] center configs
