import requests         #导入requests模块
'''
号称最优雅的http请求库
'''
#创建一个http请求：
res_get = requests.get('http://172.25.8.167:1080/get') #请求获取由 Request-URI 所标识的资源  请求参数在 请求行中
res_post = requests.post('http://172.25.8.167:1080/post', data={'key': 'value'})  #请求服务器接收在请求中封装的实体，并将其作为由 Request-Line 中的 Request-URI 所标识的资源的一部分请求参数在请求体中
res_put = requests.put('http://172.25.8.167:1080/put', data={'key': 'value'})   #	请求服务器存储一个资源，并用 Request-URI 作为其标识符
res_delete = requests.delete('http://172.25.8.167:1080/delete')         #请求服务器删除由 Request-URI 所标识的资源
res_head = requests.head('http://172.25.8.167:1080/get')            #请求获取由 Request-URI 所标识的资源的响应消息报头
res_options = requests.options('http://172.25.8.167:1080/get')       #请求查询服务器的性能，或者查询与资源相关的选项和需求

res_list = [res_get, res_post, res_put, res_delete, res_head, res_options]

for i in range(len(res_list)):
   print(f'\n第{i + 1}个http请求的响应结果:', res_list[i].text)
