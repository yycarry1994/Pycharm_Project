import requests
import json



url = "http://172.25.16.7:8088/jrjc/api/send/data"
data = {
    "pttyah":"GFDGBA940A5RGDRGD5353B8965",
    "ywxtbs": "spxt",
    "fsdwbh": "123456789",
    "jsdwbh": "637",
    "ywjdbh": "1601A",
    "sjbs": "88CBBA940A5445353B89695B5test032",
    "ajmc": "xx案件",
    "xyrmcs": [
         {
    "xyrmc": "张三"
    },
    {
    "xyrmc": "李四"
    }
    ],
    "cflj": "/gajr/123456789_210400_0201A_0201_a3cda4384305773a66380250c63bcd0f_A24D4299E273CB3EC984D1AF4826BE40.zip",
    "fssj": "2019-04-20 17:30:00"
}
header = {
    "Content-Type": "application/json"
}

res = requests.post(url=url, data=data, headers=header).text
print(res)