#Supreme Bot that can automate putting the item to cart and checking
#out in 8 seconds or less using Selenium and Chrome WebDriver

#TO DO
#Fix bug that crashes bot whenever it searches for color and the first color happens
#to be sold out.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

#checkout variables
name = "name"
email = "email"
tel = "tele number"
address = ""
zip = "zip"
city = "city"
ccnum = " "
ccexpmonth = " "
ccexpyear = " "

#site variables
#all, jackets, shirts, tops/sweaters, sweatshirts, pants, shorts
#t-shirts, hats, bags, accessories, shoes, skate
site = "shirts"
item = "Washed Corduroy"
size = "Large"
color = "Green"

col_string = 'button[data-style-name="{}"]'.format(color)

#Path to Chrome WebDriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#Supreme link to webpage:
driver.get("https://www.supremenewyork.com/shop/all/" + site)


#refresh site until item becomes available. Find the item
while True:
    try:
        driver.find_element_by_partial_link_text(item).click()
    except NoSuchElementException:
        time.sleep(2.5)
        driver.get(driver.current_url)
        driver.refresh()
    else:
        driver.find_element_by_partial_link_text(item).click()
        break

#find item 
#driver.find_element_by_partial_link_text(item).click()

#select color

time.sleep(1)
WebDriverWait(driver,10).until(EC.visibility_of_any_elements_located((By.ID,'s')))


driver.find_element_by_css_selector(col_string).click()
driver.find_element_by_css_selector(col_string).click()

#select size
WebDriverWait(driver,10).until(EC.visibility_of_any_elements_located((By.ID,'s')))

time.sleep(1)

select = Select(driver.find_element_by_id('s'))
select.select_by_visible_text(size)

time.sleep(1)
#hit "add to cart"
driver.find_element_by_name("commit").click()

#load checkout
#WebDriverWait(driver,10).until(EC.visibility_of_any_elements_located((By.NAME,'button checkout')))
time.sleep(1)

driver.get("https://www.supremenewyork.com/checkout")

#checkout
driver.find_element_by_id("order_billing_name").send_keys(name)
driver.find_element_by_id("order_email").send_keys(email)
driver.find_element_by_id("order_tel").send_keys(tel)
driver.find_element_by_id("bo").send_keys(address)
driver.find_element_by_id("order_billing_zip").send_keys(zip)
driver.find_element_by_id("order_billing_city").send_keys(city)
driver.find_element_by_id("rnsnckrn").send_keys(ccnum)

WebDriverWait(driver,10).until(EC.visibility_of_any_elements_located((By.ID,'credit_card_month')))

select2 = Select(driver.find_element_by_name('credit_card_month'))
select2.select_by_visible_text(ccexpmonth)

WebDriverWait(driver,10).until(EC.visibility_of_any_elements_located((By.ID,'credit_card_year')))

select3 = Select(driver.find_element_by_id('credit_card_year'))
select3.select_by_visible_text(ccexpyear)




