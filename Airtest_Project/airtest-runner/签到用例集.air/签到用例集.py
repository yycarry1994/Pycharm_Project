
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
driver = WebChrome()
driver.implicitly_wait(20)

driver.find_element_by_xpath("//a[@href='javascript:formLogin();']").click()
driver.find_element_by_id("username1").click()
driver.find_element_by_id("password1").click()
driver.find_element_by_xpath("//a[@href='javascript:formLogin();']").click()
driver.find_element_by_xpath("//*[@id=\"yzglIndex\"]/div/ul/li[2]/div").click()




driver.find_element_by_xpath("//*[@id=\"app\"]/div/ul/li[2]/div").click()
driver.find_element_by_xpath("//*[@id=\"app\"]/div/ul/li[2]/div/span").click()
driver.find_element_by_xpath("//*[@id=\"app\"]/div/ul/li").click()
driver.find_element_by_xpath("//*[@id=\"yzglIndex\"]/div/ul/li[3]/div/span").click()
driver.find_element_by_xpath("//*[@id=\"yzglIndex\"]/div/ul/li[3]/div[2]/ul/li[2]/span").click()
driver.find_element_by_xpath("//*[@id=\"rcddIndex\"]/div[2]/div[2]/div/div/div/div/ul/li/div/a").click()
driver.find_element_by_xpath("//*[@id=\"dlxxSplc\"]/div[2]/div[2]/div/div[2]/div/button/span").click()
driver.find_element_by_xpath("//*[@id=\"dlxxSplc\"]/div[3]/div[2]/div/div[2]/div/button").click()
driver.find_element_by_xpath("//*[@id=\"dlxxSplc\"]/div[3]/div[2]/div/div[2]/div/button").click()
driver.find_element_by_xpath("//*[@id=\"jsAppControllerDlxxTqxx\"]/div[2]/div[2]/div/div[3]/form/div[2]/button/span").click()
driver.find_element_by_xpath("").click()
driver.find_element_by_xpath("").click()
driver.find_element_by_xpath("").click()
driver.find_element_by_xpath("//input[@type='text']").click()
driver.find_element_by_xpath("").click()
driver.find_element_by_xpath("//input[@type='text']").click()
driver.find_element_by_xpath("//input[@spellcheck='false']").click()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/a/i").click()

