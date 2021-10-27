from selenium import webdriver

chrome_driver_path = "/Users/brianmendes/Projects/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

python = "https://www.python.org"

# ---------------------My Solution----------------------------
driver.get(python)

# events_dict = {}
# for i in range(0,5):
#     temp_dict = {}
#     date = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{i+1}]/time')
#     event_name = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{i+1}]/a')
#     temp_dict['time'] = date.text
#     temp_dict['name'] = event_name.text
#     events_dict[i] = temp_dict
#
# print(events_dict)

# ---------------------Course Solution----------------------------

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)

driver.quit()