#locoust学习
from locust import HttpLocust, TaskSet, task
import requests
#禁用安全警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class First_lesson(TaskSet):
    #访问某个地址
    @task
    def visit_url(self):
        #定义请求头
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
        }
        req = self.client.get("/imyalost", headers=header, verify=False)
        if req.status_code == 200:
            print("success")
        else:
            print("fails")


class websitUser(HttpLocust):
    task_set = First_lesson
    min_wait = 3000 #单位为毫秒
    max_wait = 6000 #单位为毫秒

if __name__ == "main":
    import os
    os.system("locust -f locusttest.py --host=https://www.cnblogs.com")