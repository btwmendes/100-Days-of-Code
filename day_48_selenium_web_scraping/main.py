from selenium import webdriver

chrome_driver_path = "/Users/brianmendes/Projects/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

amazon = "https://www.amazon.com/gp/product/B079BG3M7D?pf_rd_r=38Y15QDZE6SNC1JTCKT5&pf_rd_p=1ab92b69-98d7-4842-a89b-ad387c54783f&pd_rd_r=622534f3-ee97-4cad-ad7a-671c92e24576&pd_rd_w=Q5PS6&pd_rd_wg=PWv0I&ref_=pd_gw_unk"
python = "https://www.python.org"

# ---------------------Find Element by ID----------------------------
driver.get(python)
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# ---------------------Find Element by Name----------------------------
# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# ---------------------Find Element by CSS Selector----------------------------
# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)
# # one way to drill down when something doesn't have a unique tag.
# # Uses my understanding of css style classes. Remember . and # from styles

# ---------------------Find Element by XPath----------------------------
bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)


# driver.close()
# closes the active tab

driver.quit()
# quits the entire browser