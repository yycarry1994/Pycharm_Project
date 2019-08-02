import pandas as pd

path = 'test.xlsx'
sheet_name = 'test_data'
'''
pd.read_excel(io, sheet_name=0, header=0, names=None, index_col=None, usecols=None)
io:很明显, 是excel文件的路径+名字字符串
sheet_name:返回指定的sheet
如果将sheet_name指定为None，则返回全表
如果需要返回多个表, 可以将sheet_name指定为一个列表, 例如['sheet1', 'sheet2']
name:如果没有表头, 可用此参数传入列表做表头
header:指定数据表的表头,默认值为0, 即将第一行作为表头
index_col:用作行索引的列编号或者列名，如果给定一个序列则有多个行索引。一般可以设定index_col=False指的是pandas不适用第一列作为行索引。
usecols：读取指定的列, 也可以通过名字或索引值
'''



class with_excel:

    #构造函数，调用类时就运行
    def __init__(self, path=None, sheet_name=None):
        if path and sheet_name:
            self.path = path
            self.sheet_name = sheet_name
        else:
            self.path = 'test.xlsx'
            self.sheet_name = 'test_data'
        self.data = self.open_excel()

    #获取表格数据
    def open_excel(self):
        df = pd.read_excel(self.path, self.sheet_name)
        return df

    #获取表中单元格行数
    def get_lines(self):
        lines = self.data.shape[0]#获取了最后一行的行数
        return lines

    #获取一个单元格的内容(获取多行的内容)
    def get_cell_data(self, row, col):
        return self.data.iloc[row, col]

    #将表格数据转字典
    def to_dict(self):
        test_data = []
        for i in self.data.index.values:  # 获取与表头对应的字典数据
            row_data = self.data.loc[i].to_dict()
            test_data.append(row_data)
        return test_data

'''
if __name__ == '__main__':
    aa = with_excel(path, sheet_name)
    print(str(aa.get_cell_data(0, 0)))
'''









