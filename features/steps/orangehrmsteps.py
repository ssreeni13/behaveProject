# from behave import *
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# @given('launch chrome browser')
# def launchBrowser(context):
#     context.driver = webdriver.Chrome()
#     # executable_path="C:\Drivers\chrome-win64\chrome.exe"
#
#
# @when('open orange hrm homepage')
# def openHomePage(context):
#     context.driver.get("https://opensource-demo.orangehrmlive.com/")
#
#
# @then('verify that the logo present on page')
# def verifyLogo(context):
#     status = context.driver.find_element(By.XPATH, "//div[@id='divLogo']//img").is_displayed()
#     assert status is True
#
#
# @then('close browser')
# def closeBrowser(context):
#     context.driver.close()
