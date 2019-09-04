#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding:UTF-8 -*-
# Author by : Mervin Yan
# WebSite   : http://blog.csdn.net/zhumingyan

from suds.client import Client

#要访问的Webservice地址
url = "http://www.webxml.com.cn/webservices/qqOnlineWebService.asmx?wsdl"
#创建Webservice Client对象
client = Client(url)
print(client)#可以打印出Client对象所有的方法
#print(client)
#client.service.qqCheckOnline方法
result = client.service.qqCheckOnline("0")

print("QQ在线结果为："+result)

