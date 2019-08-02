import json

class open_json:

    def __init__(self, filename):
        self.data = self.read_data(filename)

    #打开json文件
    def read_data(self, filename):
        with open(filename) as fp:
            data = json.load(fp)
            return data
    #获取对应的json数据
    def get_data(self, data_id):
        return self.data[data_id]
