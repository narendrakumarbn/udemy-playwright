from playwright.sync_api import expect, Page
import time
def test_UIcheck(page):

    #hide/display and placeholder check
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #alert check    
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Confirm").click()
    time.sleep(1)

    #Mouse hover check
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()
    
    #frame checks
    pageframe = page.frame_locator("#courses-iframe")
    pageframe.get_by_role("link", name="All Access plan").click()
    expect(pageframe.locator("body")).to_contain_text("Happy Subscibers!")


    #check the price of the rice is equal to 
def test_UIcheck2(page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator("th").count()):
        pricecolvalue = index
        print(f"price column value is {pricecolvalue}")
        break

    ricerow = page.locator("tr").filter(has_text="Rice")
    expect(ricerow.locator("td").nth(pricecolvalue)).to_have_text("37")
    
  

