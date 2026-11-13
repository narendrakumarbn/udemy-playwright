from playwright.sync_api import Page, Playwright, expect
import time
from utils.apiBase import APIUtils


def interceptRequest(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6af69bd092a4341c4c155f1b")

# api call from the browser -> api call contact server return back response to browser -> browser use response to generate the html


def test_network1(page: Page):
    #login
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", interceptRequest)
    page.get_by_placeholder("email@example.com").fill("naru05@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Narendra@123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    time.sleep(5)
    message = page.locator(".blink_me").text_content()
    print(message)


def test_session_storage(playwright:Playwright):
    api_utils = APIUtils()
    getToken = api_utils.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page =context.new_page()
    # script to inject token in session local storage
    page.add_init_script(f"""localStorage.setItem('token','{getToken}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text('Your Orders')).to_be_visible()
    