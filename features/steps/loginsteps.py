from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()
    # executable_path="C:\Drivers\chrome-win64\chrome.exe"


@when('open orange hrm homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter username "{user}" and password "{pwd}"')
def enterUserPswd(context):
    context.driver.find_element(By.ID, "txtUsername").send_keys(user)
    context.driver.find_element(By.ID, "txtPassword").send_keys(pwd)


@when('Click on Login button')
def clickLogin(context):
    context.driver.find_element(By.ID, "btnLogin").click()


@then('User must successfully login to the Dashboard page')
def successLogin(context):
    try:
        text = context.driver.find_element(By.XPATH, "//*[@id='content']/div/div[1]/h1").text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Dashboard":
        context.driver.close()
        assert True, "Test Passed"
