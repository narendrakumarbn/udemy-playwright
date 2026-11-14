from sys import api_version
import token
from playwright.sync_api import Playwright

ordersPayload = {"orders": [{"country": "India", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}

class APIUtils:

    def getToken(self, playwright:Playwright,user_credentials):
        user_email = user_credentials['userEmail']
        user_password = user_credentials['userPassword']
        api_request_context =playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
        response = api_request_context.post("/api/ecom/auth/login",
                                            data={"userEmail": user_email, "userPassword": user_password})
        assert response.ok
        return response.json()["token"]
        
        

    def createOrder(self, playwright:Playwright,user_credentials):
        token = self.getToken(playwright, user_credentials)
        api_request_context =playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
        response = api_request_context.post("/api/ecom/order/create-order",
                                data=ordersPayload,
                                headers={
                                    "Authorization": token,
                                    "Content-Type": "application/json"
                                })
        responsebody = response.json()
        print(responsebody)
        return responsebody["orders"][0]


