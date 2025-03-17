"""Functional test to search for the package name on the page with xpath expression and verifying the value of the element."""

import time
from selenium import webdriver

# Create an instance of Chrome WebDriver
browser = webdriver.Chrome()

# Make a request to the PyPI website for the selenium package
browser.get("https://pypi.org/project/selenium/4.29.0/")

# Find the name field using xpath with id
package_name = browser.find_element("xpath", '//*[@id="content"]/div[1]/div/div[1]/h1')

# Check if the title of the page is proper
if(package_name.text):
    # Verify an element on the page
    assert "selenium 4.29.0" in package_name.text
    print("✅ Successed Test: selenium 4.29.0 version found")
else:
    print("❌ Failed Test: selenium 4.29.0 version is incorrect")

# Quit the browser window
browser.quit()
