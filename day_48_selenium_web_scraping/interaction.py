from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/brianmendes/Projects/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

wiki = "https://en.wikipedia.org/wiki/Main_Page"

# ---------------------My Solution----------------------------
driver.get(wiki)

article_total = driver.find_element_by_css_selector("#articlecount a")
# print(article_total.text)
# article_total.click()

all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# driver.quit()