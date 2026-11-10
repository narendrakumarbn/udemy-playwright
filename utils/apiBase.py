from sys import api_version
from playwright.sync_api import Playwright

ordersPayload = {"orders": [{"country": "India", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}

class APIUtils:

    def getToken(self, playwright:Playwright):
        api_request_context =playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
        response = api_request_context.post("/api/ecom/order/create-order",
                                            data={"userEmail": "naru05@gmail.com", "userPassword": "Narendra@123"})
        assert response.ok
        print(response.json())
        
        

    def createOrder(self, playwright:Playwright):
        api_request_context =playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
        response = api_request_context.post("/api/ecom/order/create-order",
                                data=ordersPayload,
                                headers={
                                    "Authorization0": token,
                                    "Content-Type": "application/json"
                                })
        print(response)


