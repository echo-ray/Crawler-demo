# coding:utf-8

import requests
import re

'''
input the keyword of photo you wanna search & download,
then input howmany pages you need to download.

then just wait for a second...& it`s done
'''

def getPhotoURL(url):   # 返回下载链接
    header = {'uesr-Agent':'Mozilla/5.0'}
    try:
        r = requests.get(url, headers = header, timeout = 10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding   
    except:
        print("网页爬取异常")
    
    pattern = '"objURL":"(.*?)",'
    try:
        PhotoURL_list = re.findall(pattern, r.text)
        print(PhotoURL_list)
        return PhotoURL_list
    except:
        print("下载链接获取异常")


def downloadPhoto(pic_URL,pic_name):#根据链接，下载图片

    print('{:50}'.format(pic_URL),end='')
    try:
        pic = requests.get(pic_URL)
        print('爬取成功')
    except requests.exceptions.ConnectionError:
        print('【错误】当前图片无法下载')
        continue
        
    pic_type = pic_URL.split('.')[-1]
    if pic_type not in ['jpeg','JPEG','png','PNG','jpg','JPG','gif','GIF']:
        pic_type = 'jpg'
    pic_file = 'pictures\\'+ str(pic_name) + '.' + pic_type
    fp = open(pic_file, 'wb')
    fp.write(pic.content)
    fp.close()


def main():
    
    keyword = input("请输入要搜索图片的关键字： ")
    page = eval(input("请输入要下载的页数： "))
    base_url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + str(keyword) + '&pn='
    download_list = []
    for i in range(page):
        url = base_url + str(i*20)
        PhotoURL_list = getPhotoURL(url)[0:20]
        download_list.extend(PhotoURL_list)
        
    for url in download_list:
        downloadPhoto(url,(download_list.index(url)+1))

if __name__=='__main__':
    main()
