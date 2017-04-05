import requests
import re
import json

def getHTML(url):
    kv = {'user-agent':'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=kv, timeout=10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("产生异常")
        return None

def have_comment(html):
    comment_list = html['data']['list']
    if comment_list == False:
        print('No comment in this page')
    else:
        return comment_list

def get_comment(list):
    for each in list[0:2]:
        user_id = each["uid"]
        user_name = each["user_name"]
        comment_id = each["comment_id"]
        comment = each["content"]
        time = each["pretty_time"]
        url = each["app_url"]
        
      



def main():
    url = 'http://www.luoo.net/comment/get/app/1/id/193/commid/0/sort/new?p=4'
    #url = 'http://www.luoo.net/comment/get/app/1/id/193/commid/0/sort/new?p=100'

    page = json.loads(getHTML(url))
    if have_comment(page):
        get_comment(have_comment(page))
        
        


main()
