import requests

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
    'Accept': 'text/html, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': "gzip, deflate, br",
    'Referer': 'https://bh.sb/post/category/main/',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive=false'
}

def download_img(path, title, img_url):
    if img_url[-3:] == 'jpg':
        pic = requests.get(img_url, headers=header)
        with open(path + title + '.jpg', 'wb') as f:
            print('正在下载', title)
            f.write(pic.content)
            f.close()
    else:
        pic = requests.get(img_url, headers=header)
        with open(path + title + '.gif', 'wb') as f:
            print('正在下载', title)
            f.write(pic.content)
            f.close()

path = 'H:\渤海拾贝趣图\\'
title = '1234'
img_url = 'http://img.mp.itc.cn/upload/20170805/19ad9705aec44c81af1760d40622c9fb.jpg'
download_img(path, title, img_url)