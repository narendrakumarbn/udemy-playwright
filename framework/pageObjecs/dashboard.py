

from .ordersHistory import OrdersHisoryPage


class DashboardPage():
    
    def __init__(self, page):
        self.page = page

    def selectOrdersNavLink(self):
        self.page.get_by_role("button", name="ORDERS").click()
        ordersHistorypage = OrdersHisoryPage(self.page)
        return ordersHistorypage