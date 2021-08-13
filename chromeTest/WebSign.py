import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys



# print(browser.current_url)
# browser.quit()
def sendCode():
    browser = webdriver.Chrome()
    browser.get('http://localhost:8000/login/signup')
    for num in range(1, 20):
        mailEle = browser.find_element_by_id('email')
        mailEle.clear()
        mailEle.send_keys(str(num) + "rmvind75490@chacuo.net")
        mailEle.send_keys(Keys.RETURN)

        # sendCodeEle = browser.find_element_by_xpath('/html/body/div[1]/main/div/form/div[4]/div[1]/div[2]/input')
        sendBtn = browser.find_element_by_id("send_code")
        removeAttribute(browser,sendBtn,'disabled')
        # sendBtn.click()
        sendBtn.send_keys(Keys.ENTER)

        time.sleep(1)
    time.sleep(120)
    browser.quit()

def removeAttribute(driver, elementobj, attributeName):
    '''
    封装删除页面属性的方法
    调用JS代码删除页面元素的指定的属性，arguments[0]~arguments[1]分别
    会用后面的element，attributeName参数进行替换
    '''
    driver.execute_script("arguments[0].removeAttribute(arguments[1])",
                          elementobj, attributeName)
sendCode()