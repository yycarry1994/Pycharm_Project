import requests
import json
'''
封装requests请求类
'''

class runMain:

    def __init__(self, url, method, data=None):
        self.res = self.run_main(url, method, data)

    #模拟post请求
    def send_post(self, url, data):
        res = requests.post(url=url, data=data).json()
        return json.dumps(res, indent=1, sort_keys=True)#将返回的json格式化输出

    #模拟get请求
    def sen_get(self, url, data):
        res = requests.get(url=url, data=data).json()
        return json.dumps(res, indent=1, sort_keys=True)#将返回的json格式化输出

    def run_main(self, url, method, data=None):
        if method == 'POST':
            res = self.send_post(url=url, data=data)
        else:
            res = self.sen_get(url=url, data=data)
        return res

