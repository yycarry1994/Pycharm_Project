import requests

class request_method:

    def get_main(self, url, headers=None, data=None):
        res = requests.get(url, headers, data)
        return res

    def post_main(self, url, headers=None, data=None):
        res = requests.post(url, headers, data)
        return res



