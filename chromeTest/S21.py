import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('http://localhost:8001/login/auth')

account = browser.find_element_by_id('account')
account.clear()
account.send_keys("admin")
account.send_keys(Keys.RETURN)

pwd = browser.find_element_by_id('password')
pwd.clear()
pwd.send_keys("123456")
pwd.send_keys(Keys.RETURN)

# sendCodeEle = browser.find_element_by_xpath('/html/body/div[1]/main/div/form/div[4]/div[1]/div[2]/input')
time.sleep(2)
# browser.find_element_by_id("send_code").click()
browser.switch_to.frame(browser.find_element_by_tag_name("iframe"))
recaptcha =browser.find_element_by_class_name('recaptcha-checkbox-border')


recaptcha.click();
time.sleep(2)


browser.switch_to.default_content()
# submit =browser.find_element_by_xpath('/html/body/div[1]/div[2]/form/button')
# submit.click()
time.sleep(120)
browser.quit()

# print(browser.current_url)
# browser.quit()