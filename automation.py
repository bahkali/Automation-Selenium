from selenium import webdriver

chrome_browser = webdriver.Chrome('./drivers/chromedriver')

# Maximize the window
chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
# check the title content
assert 'Selenium Easy Demo - Simple Form to Automate using Selenium' in chrome_browser.title

button = chrome_browser.find_element_by_class_name("btn-default")
print(button.get_attribute('innerHTML'))