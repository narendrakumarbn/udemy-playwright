
import json
from playwright.sync_api import Browser, Playwright, Response, expect
from apiBase import APIUtils
import pytest

#json file -> util -> access into test
with open('data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data['user_credentials']
        

    

@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_ene_webapi(playwright:Playwright, user_credentials):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()


    #create order -> orderid
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright,user_credentials)
    

    #login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill(user_credentials['userEmail'])
    page.get_by_placeholder("enter your passsword").fill(user_credentials['userPassword'])
    page.get_by_role("button", name="Login").click()

    page.get_by_role("button", name="ORDERS").click()


    #orders History page -> orser is present
    row = page.locator("tr").filter(has_text=orderId)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping")
    context.close()
