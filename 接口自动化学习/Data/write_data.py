from api_gj.with_excel2 import with_excel2

class write_data:

    def __init__(self):
        self.write_excel = with_excel2()

    def write(self,row, col, data1):
        self.write_excel.write_data(row, col, data1)