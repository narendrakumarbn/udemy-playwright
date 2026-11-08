from playwright.sync_api import Page, expect


# # def test_playwright_basics(playwright):
# #     browser = playwright.chromium.launch(headless=True)
# #     context = browser.new_context()
# #     page = context.new_page()
# #     page.goto("https://www.google.com")
# #     page.wait_for_load_state("networkidle")
# #     browser.close()


# # chromium headless mode and in single context
# def test_playwrightshortcut(page):
#     page.goto("https://www.hackculture.io")
    

def test_corelocators(page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("UserName").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teacher")
    # page.get_by_role("link", name="I Agree to the").click()
    page.get_by_label("I Agree to the terms and conditions").check()
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_timeout(2000)
    iphoneproduct = page.locator("app-card").filter(has_text="iphone X")
    iphoneproduct.locator("button").click()
    nokiaproduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaproduct.locator("button").click()
    checkout = page.locator("text=Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)


def test_childwindow(page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as newpage_info:
        page.locator(".blinkingText").first.click()

    childpage = newpage_info.value
    childpage.wait_for_load_state()

    text = childpage.locator(".red").text_content()
    words = text.split("at")
    email = words[1].strip().split(" ")[0]

    assert email == "mentor@rahulshettyacademy.com"
    print(email)