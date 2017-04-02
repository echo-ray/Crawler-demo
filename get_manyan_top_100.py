import requests
import re
import json
from requests.exceptions import RequestException
from multiprocessing import Pool

def get_one_page(url):
    try:
        r= requests.get(url)
        if r.status_code==200:
            return r.text
        return None
    except RequestsException:
        print("获取页面失败",url)
        return "Faile to get page"

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)@160w_220h_1e_1c".*?name"><a'
                         '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?in'
                        'teger">(.*?)</i>.*?fraction">(.*?)</i>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2],
            'actors':item[3].strip()[3:],
            'date':item[4].strip()[5:],
            'score':item[5]+item[6]
        }
        
def write2file(content):
    with open("result.txt", 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')
        f.close()


def main(page):
    url = "http://maoyan.com/board/4?offset=" + str(page)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write2file(item)

if __name__ == '__main__':
    pool = Pool(10)
    pool.map(main, [i for i in range(0,100,10)])
    print('Done')

