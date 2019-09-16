import os
import zipfile
import xml.dom.minidom
from zipfile import ZipFile


def open_zip(file):
    z = zipfile.ZipFile(r'C:\Users\86181\Desktop\新建文件夹\数据包\公安\逮捕2' + '\\' + file, "r")
    ywxx = z.namelist()[0]
    ywxx2 = z.open(ywxx)
    return ywxx2


def get_file(file_dir):
    files = []
    for file in os.walk(file_dir):
        files.append(file)
        return files

files = get_file(r'C:\Users\86181\Desktop\新建文件夹\数据包\公安\逮捕3')
ywxx = open_zip(files[0][2][1])
tree =xml.dom.minidom.parse(ywxx)
root = tree.documentElement
rootdata = tree.documentElement
# xtxx = root.getElementsByTagName("XTXX")
sjbs = rootdata.getElementsByTagName('SJBS')
sjbs_text=tree.createTextNode('计算机程序设计语言')
sjbs.text = 'sjbs'
print(tree.getroot().tag)


print(ywxx)
print(files[0][2][1])