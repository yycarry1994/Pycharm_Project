
import os
import shutil

def fileRemove(rootdir):
    filelist=[]
    filelist=os.listdir(rootdir)                #列传入目录下的所有文件名
    for f in filelist:
        filepath = os.path.join(rootdir, f)   #将文件名映射成绝对路劲
        if os.path.isfile(filepath):            #判断该文件是否为文件或者文件夹
            os.remove(filepath)                 #若为文件，则直接删除
            print(str(filepath)+"removed!")
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath, True)        #若为文件夹，则删除该文件夹及文件夹内所有文件
            print("dir " + str(filepath) + "removed!")
    #shutil.rmtree(rootdir, True)                 #最后删除img总文件夹
    print("删除成功")
