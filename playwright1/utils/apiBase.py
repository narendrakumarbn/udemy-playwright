from sys import api_version
import token
from playwright.sync_api import Playwright

ordersPayload = {"orders": [{"country": "India", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}

class APIUtils:

    def getToken(self, playwright:Playwright):
        api_request_context =playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
        response = api_request_context.post("/api/ecom/auth/login",
                                            data={"userEmail": "naru05@gmail.com", "userPassword": "Narendra@123"})
        assert response.ok
        return response.json()["token"]
        
        

    def createOrder(self, playwright:Playwright):
        token = self.getToken(playwright)
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


