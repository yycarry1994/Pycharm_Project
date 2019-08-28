from suds.client import Client
url = 'http://www.webxml.com.cn/webservices/qqOnlineWebService.asmx?wsdl'
con = Client(url)
print(con)
