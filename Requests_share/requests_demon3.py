import requests
import json

'''
1、post请求
以字典的方式传入参数
'''
parm = {'key': 'value'}
res_post = requests.post('http://172.25.8.167:1080/post', data=parm)
print(res_post.text)

'''
2、post请求
以元祖列表的方式传入参数,也可以直接以元祖方式传入
'''
parm = [('key1', 'value1'), ('key2', 'value3')]
res_post = requests.post('http://172.25.8.167:1080/post', data=parm)
print(res_post.text)

'''
3、post请求
以json方式传入参数
'''
url = 'http://172.25.8.167:1080/post'
payload = {'some': 'data'}
res_post = requests.post(url, data=json.dumps(payload))
print(res_post.text)

'''
4、post请求
将文件以参数的方式传入
'''
url = 'http://172.25.8.167:1080/post'
payload = {'file': open('report.xls', 'rb')}
res_post = requests.post(url, data=json.dumps(payload))
print(res_post.text)