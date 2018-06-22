from selenium import webdriver
#from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome('./chromedriver')
browser.get('https://sellers.kraftly.com/login')
element = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ng-scope"))
    )


email = browser.find_element_by_name('email')
email.send_keys("youremail@gmail.com")

password = browser.find_element_by_name('password')
password.send_keys('yourpassword')

submit = browser.find_element_by_class_name('btn-flat')
submit.click()

browser.get('https://sellers.kraftly.com/product/add')
element = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "wrapper"))
    )



pname = browser.find_element_by_name('productName')
pname.send_keys('The broken horse')

category = browser.find_element_by_name('country-object')
category.send_keys('paintings')

category.send_keys(Keys.ENTER)

browser.find_element_by_id("productImage").send_keys("/home/chindi/Desktop/automation/brokenHorse.jpg")

description = browser.find_element_by_class_name('ng-pristine')
description.send_keys('Painting of a broken horse')
browser.implicitly_wait(1)


merch = browser.find_element_by_class_name('ng-pristine')
merch.send_keys('100')
browser.implicitly_wait(1)


quantity = browser.find_element_by_class_name('ng-pristine')
quantity.send_keys('1')
browser.implicitly_wait(1)

mrp = browser.find_element_by_name('retail')
mrp.send_keys('3000')


browser.implicitly_wait(1)

#select = browser.find_element_by_name('weight')
#select.send_keys

browser.implicitly_wait(1)

select1 = Select(browser.find_element_by_name('duration'))
select1.select_by_index(1)


addP = browser.find_element_by_xpath("//button[@class='btn btn-primary btn-flat']")
addP.click();