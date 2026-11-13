
from playwright.sync_api import Page


# api call from the browser -> api call contact server return back response to browser -> browser use response to generate the html

fakePayLoadOrderResponse = {"data":[], "message":"No Orders"}


def intercept_response(route):
    route.fulfill(
        json = fakePayLoadOrderResponse
    )

def test_network1(page: Page):
    #login
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("naru05@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Narendra@123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)