import json
from pathlib import Path

from typing import Self
from playwright.sync_api import Browser, Playwright, Response, expect
import pytest

from framework.utils.apiBaseFramework import APIUtils
from framework.pageObjecs.dashboard import DashboardPage
from framework.pageObjecs.orderDetails import OrderDetailsPage
from framework.pageObjecs.Login import LoginPage
#json file -> util -> access into test
with open('data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data['user_credentials']
        

    

@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_ene_webapi(playwright:Playwright, user_credentials, browserInstance):
    username = user_credentials['userEmail']
    password = user_credentials['userPassword']

    #create order -> orderid
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright,user_credentials)
    

    #login
    loginpage = LoginPage(browserInstance)
    loginpage.navigate(browserInstance)
    dashboardPage = loginpage.login(username,password)

    #dashboard page
    orderHistoryPage = dashboardPage.selectOrdersNavLink()
    orderHistoryPage = orderHistoryPage.selectOrder(orderId)
    orderHistoryPage.verifyOrderMessage()
    #orders History page -> orser is present

