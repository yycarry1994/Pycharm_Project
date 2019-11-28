from selenium.webdriver.common.by import By

class duluye(object):
    '''
    sso单点登录页面
    '''
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://172.25.17.17:8082/ssoserver/login?service=http%3A%2F%2F172.25.16.111%3A8080%2Fimp%2Frcdd%2Fhtml%2Findex.html&tgt=null'
        #登录页面元素定位信息
        self.element_user = (By.ID, 'username1') #用户名输入框
        self.element_passwd = (By.ID, 'password1') #密码输入框
        self.element_login = (By.XPATH, "//a[@href='javascript:formLogin();']") #登录按钮

    def login(self, name, passwd):
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.element_user).sendkeys(name)
        self.driver.find_element(*self.element_passwd).sendkeys(passwd)
        self.driver.find_element(*self.element_login).click()

