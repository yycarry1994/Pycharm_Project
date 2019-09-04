import requests

'''
1、post请求
以字典的方式传入参数
'''
# parm = {'key': 'value'}
# res_post = requests.post('http://172.25.8.167:1080/post', data=parm)
# print(res_post.text)

'''
2、post请求
以元祖列表的方式传入参数,也可以直接以元祖方式传入
'''
parm = [('key1', 'value1'), ('key1', 'value2')]
res_post = requests.post('http://172.25.8.167:1080/post', data=parm)
print(res_post.text)