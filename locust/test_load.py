from locust import HttpLocust, TaskSet, task

class AdminLoadTest(TaskSet):
    '''
    创建后台管理站点压测类，需要继承TaskSet
    可以添加多个任务
    '''
    def login(self):
        '''
        登录实例方法
        :return:
        '''
        self.client.post("http://www.baidu.com")

    def logout(self):
        '''
        退出实例方法
        :return:
        '''
        self.client.get("http://www.baidu.com")

    def on_start(self):
        '''
        当任何一个task调度执行前，on_start实例方法会被调用
        先登录
        :return：
        '''
        self.login()

    def on_stop(self):
        '''
        当任何一个task调度执行之后，on_stop实例方法会被调用
        :return:
        '''
        self.logout()

    @task
    def admin_index(self):
        '''
        对后台主页进行压测
        :return:
        '''
        self.client.get("http://www.baidu.com")


class RunLoadTests(HttpLocust):
    '''
    创建运行类
    '''
    task_set = AdminLoadTest