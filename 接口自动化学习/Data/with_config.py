#coding:utf-8

class global_var:
    #case_id
    Id = '0'
    name = '1'
    url = '2'
    run = '3'
    request_way = '4'
    header = '5'
    case_depend = '6'
    data_depend = '7'
    field_depend = '8'
    data ='9'
    expect = '10'
    result = '11'

#获取case_id
def get_id():
    return global_var.Id

#获取url
def get_url():
    return global_var.url

#获取是否运行
def if_run():
    return global_var.run

#获取request_way(运行方式)
def run_way():
    return global_var.request_way

#获取header
def get_header():
    return global_var.header

#获取case_depend
def case_depend():
    return global_var.case_depend

#获取data_depend
def data_depend():
    return global_var.data_depend

#获取field_depend
def field_depend():
    return global_var.field_depend

#获取data
def get_data():
    return global_var.data

#获取expect(预期结果)
def get_expect():
    return global_var.expect

#获取result（返回结果）
def get_result():
    return global_var.result