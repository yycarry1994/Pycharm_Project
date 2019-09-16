from base.run_method import RunMethod
from Data.get_data import GetData
from api_gj.with_excel2 import with_excel2
from api_gj.with_compare import compare


class RunTest:
    def __init__(self):
         self.run_method = RunMethod()
         self.data = GetData()
         self.write = with_excel2()
         self.compare = compare()
    #程序执行
    def go_on_run(self):
        row_count = self.data.get_case_lines() #拿到数据行数
        for i in range(0, row_count):
            url = self.data.get_request_url(i) #获取请求url
            method = self.data.get_request_methed(i)  #获取请求方法
            is_run = self.data.get_if_run(i) #获取是否运行
            data = self.data.get_json_data(i) #获取请求数据
            header = self.data.get_if_header(i) #获取请求头
            exc = self.data.get_expcet_reult() #获取预期结果
            if is_run:
                res = self.run_method.run_main(method, url=url, data=data, header=header)
                self.write.write_data(i+2, 12, res)
                res_flag = self.compare.is_contain(exc, res)
            return res

if __name__ == '__main__':
    test = RunTest()
    res = test.go_on_run()
    print(res)
