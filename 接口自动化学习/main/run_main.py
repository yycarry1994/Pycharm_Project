from base.run_method import RunMethod
from Data.get_data import GetData
class RunTest:
    def __init__(self):
         self.run_method = RunMethod()
         self.data = GetData()

    #程序执行
    def go_on_run(self):
        row_count = self.data.get_case_lines() #拿到数据行数
        for i in range(0, row_count):
            url = self.data.get_request_url(i) #获取请求url
            method = self.data.get_request_methed(i)  #获取请求方法
            is_run = self.data.get_if_run(i) #获取是否运行
            data = self.data.get_json_data(i) #获取请求数据
            header = self.data.get_if_header(i) #获取请求头
            if is_run:
                res = self.run_method.run_main(method, url=url, data=data, header=header)
            return res

if __name__ == '__main__':
    test = RunTest()
    res = test.go_on_run()
    print(res)
