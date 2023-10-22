from selenium import webdriver
import time

options = webdriver.ChromeOptions()
driver = webdriver.Remote(
             command_executor = 'http://192.168.56.19:4444/wd/hub',
             options = options
             )

driver.implicitly_wait(10)

url = 'https://yahoo.co.jp/'
driver.get(url)

time.sleep(3)
print(driver.title)
driver.quit()
