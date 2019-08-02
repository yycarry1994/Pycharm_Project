import requests
import time
from bs4 import BeautifulSoup
import pymysql
import lxml

class IpProxy():
    conn = pymysql.connect(host="127.0.0.1", user="root",password="123",database="testdb",charset="utf8")
    mysql = conn.cursor()
    url = f'https://www.xicidaili.com/nn/{page}'

    def __int__(self):

    def save_data(self, ip, port, address, proxy_typle):
        sql = "insert into proxy_ip(ip, port, address, proxy_type)VALUES('{0}', '{1}', '{2}', '{3}');"
        self.mysql.execute(sql.format(ip, port, address, proxy_typle))
        self.conn.commit()

    def prase_ip(self, url)
        '''
        爬取西刺免费代理ip池
        :return:无返回
        '''
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-CN;q=0.6",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": "_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTZjNDNmNjgzZWY5OWQ4ZWRmNTA5MzU3YWJiOGJlYWMwBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMVBsU3h6aU0xa25KWlZXZE5qZ0tGd21xYkJtc3J0K2w0YlEwdUhlNjFBN009BjsARg%3D%3D--abe7f4154a205b8515bfb204e3fe924006ae1d68",
            "Host": "www.xicidaili.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
        }
        r_html = None
        for i in range(2):
            try:
                r_html = requests.get(url, headers=headers, timeout=10)
            except requests.exceptions.Timeout:
                print("请求超时，第%d次重新请求" % (i + 1))
                r_html = requests.get(url, headers=headers, timeout=10)
            if r_html.status_code == 200:
                break
        soup = BeautifulSoup(r_html.text, 'lxml')
        h1 = soup.find_all('tr', class_='odd')
        for item in h1:
            item_list = item.find_all('td')
            yield {
                'ip': item_list[1].text,
                'port': item_list[2].text,
                'address': item_list[3].text,
                'proxy_typle': item_list[5].text
            }

    def get_ip(self):
        '''
        从数据库里获取ip
        :return:(ip,port,speed,typle)
        无数据时返回None
        '''
        sql = '''select ip, port, proxy_typle from proxy_ip order by rand() limit 1;'''
        self.sql.execute(sql)







