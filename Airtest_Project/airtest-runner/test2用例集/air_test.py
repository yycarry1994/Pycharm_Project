# -*- encoding=utf8 -*-
__author__ = "86181"

from airtest.core.api import *


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
driver = WebChrome()
driver.implicitly_wait(20)

#浏览器打开需要访问的起始页，点击“start_web”
#1、打开百度首页
driver.get("https://www.baidu.com/")
#2、输入北京华宇信息有心公司
driver.find_element_by_id("kw").send_keys("北京华宇信息有限公司")
#3、点击百度一下
driver.find_element_by_xpath("//input[@type='submit']").click()
#4、点击其百度百科
driver.airtest_touch(Template(r"tpl1572352408518.png", record_pos=(2.19, 5.515), resolution=(100, 100)))
driver.switch_to_new_tab()
#5、获取百度百科词条(citiaoxinxi = driver.find_element_by_xpath("//div[@label-module='para']").text)
driver.assert_exist("//div[@label-module='para']", "xpath", "通过词条信息断言")
driver.assert_template(Template(r"tpl1572348184708.png", record_pos=(24.415, 4.215), resolution=(100, 100)), "通过词条页面的图片断言")
#6、退出浏览器
driver.quit()


































auto_setup(__file__)

