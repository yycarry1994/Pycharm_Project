# -*- encoding=utf8 -*-
__author__ = "86181"
from airtest.core.api import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
driver = WebChrome()
driver.implicitly_wait(20)

driver.airtest_touch(Template(r"tpl1572937029483.png", record_pos=(3.335, 0.84), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1572937052577.png", record_pos=(3.37, 0.82), resolution=(100, 100)), "请填写测试点")


driver.switch_to_new_tab()


driver.switch_to_previous_tab()


driver.back()


driver.forward()

def find_element(driver, method, value):
    #封装元素定位方法
    if method == 'id':
        driver.find_element_by_id(value)
    elif method == 'name':
        driver.find_element_by_name(value)
    elif method == 'classname':
        driver.find_element_by_class_name(value)
    elif method == 'tagname':
        driver.find_element_by_tag_name(value)
    elif method == 'linktext':
        driver.find_element_by_link_text(value)
    elif method == 'partial_link':
        driver.find_element_by_partial_link_text(value)
    elif method == 'xpath':
        driver.find_element_by_xpath(value)
    else:
        driver.find_elements_by_css_selector(value)


page1 = {'anniu1': 'id:id1', 'anniu2': 'xpath://*[@id="cb_post_title_url"]'}
find_element(driver, page1['anniu2'].split(':')[0], page1['anniu2'].split(':')[2])





