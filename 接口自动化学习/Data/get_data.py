from Data.with_config import *
from api_gj.with_excel import with_excel
from api_gj.with_json import open_json
class GetData:

    def __init__(self):
        self.read_excel = with_excel()

    #获取数据量（行数）
    def get_case_lines(self):
        return self.read_excel.get_lines()

    #获取是否运行
    def get_if_run(self, row):
        col = int(if_run())
        run_model = self.get_case_cell(row, col)
        if run_model == 'Y':
            return run_model
        else:
            return None

    #获取是否携带header
    def get_if_header(self, row):
        col = int(get_data())
        header = self.get_case_cell(row, col)
        if header != 'None':
            return header
        else:
            return None

    #判断请求方式
    def get_request_methed(self, row):
        col = int(run_way())
        methed = self.get_case_cell(row, col)
        return methed

    #获取url
    def get_request_url(self, row):
        col = int(get_url())
        url = self.get_case_cell(row, col)
        return url

    #获取请求数据
    def get_request_data(self, row):
        col = int(get_data())
        data = self.get_case_cell(row, col)
        return data

    #通过关键字拿到json数据
    def get_json_data(self, row):
        opera_json = open_json('aaaa.json')
        data = self.get_request_data(row)
        if data == 'None':
            request_data = None
        else:
            request_data = opera_json.get_data(data)
        return request_data

    #获取预期结果
    def get_expcet_reult(self, row):
        col = int(get_expect())
        request_reult = self.get_case_cell(row, col)
        if request_reult == 'None':
            return None
        else:
            return request_reult

    #获取某一单元格的内容
    def get_case_cell(self, row, col):
        return self.read_excel.get_cell_data(row, col)

    #获取数据字典
    def get_data_dict(self):
        return self.read_excel.to_dict()

