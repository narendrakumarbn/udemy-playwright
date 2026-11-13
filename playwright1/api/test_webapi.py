from multiprocessing import context
from tkinter import Button
from playwright.sync_api import Browser, Playwright, Response, expect
from utils.apiBase import APIUtils



def test_ene_webapi(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    

    #create order -> orderid
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright)
    

    #login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("naru05@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Narendra@123")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("button", name="ORDERS").click()


    #orders History page -> orser is present
    row = page.locator("tr").filter(has_text=orderId)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping")
    context.close()
