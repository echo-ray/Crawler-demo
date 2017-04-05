import urllib.request
import urllib.parse
import re
import requests



def get_user_info(user_id):

    url ='http://www.luoo.net/user/vols/'+str(user_id)
    header = {'User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    
    req = urllib.request.Request(url)

    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
    response = urllib.request.urlopen(req)

    html = response.read().decode('utf-8')

    pattern = re.compile(r'<a href="http://www.luoo.net/music/(.*)" class="name">(.*)</a>')
    result = re.findall(pattern, html)
    username= re.findall(re.compile(r'<h1 class="uname">\s+(\S*)\s+</h1>'), html)

    #打印 用户名和收藏的期刊（列表）
    print()
    print('-'*10,user_id,username[0],'-'*10)
    print(result)
    for vol in result:
        print(vol[0],vol[1])
    if result==[]:
        print("该用户无收藏期刊")

def get_commit(url): #获取评论
    url = 'http://www.luoo.net/comment/get/app/1/id/193/commid/0/sort/new?p=2'
    


for id in range(11110,11120):
    get_user_info(id)

