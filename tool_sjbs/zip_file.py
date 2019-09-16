import zipfile
import random
import string
import os
import os.path
import xml.etree.ElementTree

# z = zipfile.ZipFile("zipfile.zip", "r")
#
# # 打印zip文件中的文件列表
# for filename in z.namelist():
#     print
#     'File:', filename
#
# # 读取zip文件中的第一个文件
# first_file_name = z.namelist()[0]
# content = z.read(first_file_name)
# print
# first_file_name

def get_file(file_dir):
    files = []
    for file in os.walk(file_dir):
        files.append(file)
        return files

def rename(old, sjbs):
    newname = r'C:\Users\86181\Desktop\新建文件夹\数据包\公安\逮捕3\\' + f'401_301_0101A_0101_38EF426C013A92AD88E596217A2C0EA5_{sjbs}.zip'
    old_name = r'C:\Users\86181\Desktop\新建文件夹\数据包\公安\逮捕3\\' + old
    os.renames(old_name, newname)

def set_sjbs():
    sjbs = ''.join(random.sample(string.ascii_letters + string.digits, 32))
    return sjbs



def change_sjbs(path, sjbs_data):
    tree = xml.etree.ElementTree.parse(path)
    root = tree.getroot()
    xtxx = root.find('XTXX')
    sjbs = xtxx.find('SJBS')
    sjbs.text = sjbs_data
    tree.write(r'H:\ywxx.xml', encoding="utf-8", xml_declaration=True)



def open_zip(file, sjbs):
    z = zipfile.ZipFile(r'C:\Users\86181\Desktop\新建文件夹\数据包\公安\逮捕3\\' + file, "r")
    ywxx = z.namelist()[0]
    ywxx2 = z.open(ywxx)
    change_sjbs(ywxx2, sjbs)
    ywxx2.close()


all_files = get_file(r'C:\Users\86181\Desktop\新建文件夹\数据包\公安\逮捕3')
for file in all_files[0][2]:
    print('开始执行')
    sjbs = set_sjbs()
    ywxx = open_zip(file, sjbs)
    new_xtxx = r'H:\ywxx.xml'
    azip = zipfile.ZipFile(r'C:\Users\86181\Desktop\新建文件夹\数据包\公安\逮捕3\\' + file, 'a')
    azip.write(new_xtxx)
    azip.close()

    rename(file, sjbs)
    print('完成一个\n')


print("-----------------done--------------------")