"""Functional test to search for the HTML element 'title' and verifying the page title."""

from selenium import webdriver

# Create an instance of Chrome WebDriver
browser = webdriver.Chrome()

# Make a request to the PyPI website for the selenium package
browser.get("https://pypi.org/project/selenium/4.29.0/")

# Check if the title of the page is proper
if(browser.title=="selenium · PyPI"):
    print("✅ Successed Test: selenium · PyPI page launched successfully")
else:
    print("❌ Failed Test: selenium · PyPI page Title is incorrect")

# Quit the browser window
browser.quit()
