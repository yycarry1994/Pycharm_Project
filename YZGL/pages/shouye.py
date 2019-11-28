from selenium.webdriver.common.by import By

class shouye(object):
    '''
    监狱一站式综合管理平台--首页
    '''
    def __init__(self, driver):
        self.driver = driver
        """元素定位"""
        self.element_xxgl = (By.XPATH, "//*[@id=‘yzglIndex’]/div/ul/li[2]/div")
