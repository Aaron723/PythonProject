import requests
from lxml import etree
import numpy as np
headers = {
    'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}



def getEveryUrl(url):
    offsets = ['0', '10', '20', '30', '40', '50', '60', '70', '80', '90']
    urls = []
    for offset in offsets:
        iurl = url + 'offset=' + offset
        urls.append(iurl)
    return urls

def getData(urls, headers):
    super_items = []
    for url in urls:
        response = requests.get(url, headers = headers)
        e = etree.HTML(response.text)
        ranking = e.xpath('//div[@class="main"]//dd/i/text()')
        items = e.xpath('//div[@class="main"]//dd/a/@title')
        stars = e.xpath('//div[@class="main"]//dd//p[@class="star"]/text()')
        time = e.xpath('//div[@class="main"]//dd//p[@class="releasetime"]/text()')
        scores_integer = e.xpath('//div[@class="main"]//dd//p[@class="score"]/i[@class="integer"]/text()')
        scores_fraction = e.xpath('//div[@class="main"]//dd//p[@class="score"]/i[@class="fraction"]/text()')
        moives = []
        datafile = 'moives_ranking.txt'
        for i in range(len(scores_integer)):
            scores_integer[i] = scores_integer[i] + scores_fraction[i]
            stars[i] = stars[i].strip()
            with open(datafile,'a') as df:
                df.write(ranking[i] + '\r' + items[i] + '\r' + stars[i] + '\r' + time[i] + '\r' + scores_integer[i] + '\n')
                # df.write(items[i])
                # df.write(stars[i])
                # df.write(time[i])
                df.write('\n')
            # print(ranking[i])
            # print(items[i])
            # print(time[i])
            # print(scores_integer[i])
            # print('\n')
            # moive = ranking[i] + "\r" + items[i] + "\r" + time[i] + "\r" +scores_integer
            # moives.append(moive)

        super_items.append(items)
    return super_items
url = 'https://maoyan.com/board/4?'
urls = getEveryUrl(url)
items_1 = getData(urls, headers)
print(items_1)