from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/brianmendes/Projects/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

app_brew = "http://secure-retreat-92358.herokuapp.com"

# ---------------------My Solution----------------------------
driver.get(app_brew)

first = driver.find_element_by_name("fName")
last = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")

first.click()
first.send_keys("Homer")

last.click()
last.send_keys("Simpson")

email.click()
email.send_keys("homer.simpson@google.com")
email.send_keys(Keys.ENTER)

# driver.quit()