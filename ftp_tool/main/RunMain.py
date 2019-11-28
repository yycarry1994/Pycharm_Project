from tools.ftp_tool import MyFTP
from tools.remove_files import fileRemove
import time



if __name__ == "__main__":
    i = 0
    while True:
        my_ftp = MyFTP("172.25.17.50")
        my_ftp.login("admin", "123456")
        my_ftp.upload_file_tree("C:\\Users\\86181\\Desktop\\新建文件夹\\ftp_up", "/JR")
        fileRemove("C:\\Users\\86181\\Desktop\\新建文件夹\\ftp_up")
        my_ftp.close()
        time.sleep(1800)
