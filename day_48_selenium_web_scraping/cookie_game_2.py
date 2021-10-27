from selenium import webdriver
import time

chrome_driver_path = "/Users/brianmendes/Projects/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

cookie_game = "http://orteil.dashnet.org/experiments/cookie/"

# ---------------------Time----------------------------
timeout = time.time() + 5
five_min = time.time() + 60*5

# ---------------------Game Buttons----------------------------
driver.get(cookie_game)

cookie = driver.find_element_by_id("cookie")

items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]



cursor = driver.find_element_by_id("buyCursor")
grandma = driver.find_element_by_id("buyGrandma")
factory = driver.find_element_by_id("buyFactory")
mine = driver.find_element_by_id("buyMine")
shipment = driver.find_element_by_id("buyShipment")
lab = driver.find_element_by_id("buyAlchemy lab")
portal = driver.find_element_by_id("buyPortal")
machine = driver.find_element_by_id("buyTime machine")
elder = driver.find_element_by_id("buyElder Pledge")
money = driver.find_element_by_id("money")


# ---------------------Game Loop----------------------------
while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        cursor.click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 2

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break