import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys



# print(browser.current_url)
# browser.quit()
def sendCode():
    browser = webdriver.Chrome()
    browser.get('http://localhost:7000/login/signup')
    for num in range(1, 20):
        mailEle = browser.find_element_by_xpath('/html/body/div[1]/main/div/form/div[1]/div[1]/input')
        mailEle.clear()
        mailEle.send_keys(str(num) + "rmvind75490@chacuo.net")
        mailEle.send_keys(Keys.RETURN)

        # sendCodeEle = browser.find_element_by_xpath('/html/body/div[1]/main/div/form/div[4]/div[1]/div[2]/input')

        browser.find_element_by_id("send_code").click()
        time.sleep(1)
    time.sleep(120)
    browser.quit()

sendCode()