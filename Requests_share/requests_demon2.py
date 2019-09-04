import requests


'''
1、带参数的get请求
get请求使用字典的形式传参
'''
parm = {'key1': 'value1', 'key2': 'value2'}
res_get = requests.get('http://172.25.8.167:1080/get', params=parm)
print(res_get.text, '\n请求url为：', res_get.url)

'''
2、当传入字典的值为null时，也会将字典的键传入url中
'''
parm = {'key1': 'value1', 'key2': ''}
res_get = requests.get('http://172.25.8.167:1080/get', params=parm)
print(res_get.text, '\n请求url为：', res_get.url)

'''
3、传入字典的值可以是一个列表
'''
parm = {'key1': 'value1', 'key2': ['value2', 'value3']}
res_get = requests.get('http://172.25.8.167:1080/get', params=parm)
print(res_get.text, '\n请求url为：', res_get.url)