from playwright.sync_api import Page

EMAIL='user@test.com'
PASSWORD='password'

def login(page):
    page.goto('http://localhost:8000/login')
    page.fill('#email',EMAIL)
    page.fill('#password',PASSWORD)
    page.locator('button').nth(1).click()

def test_login(page:Page):
    login(page)
    page.wait_for_timeout(1000)
    assert page.locator('.welcome').text_content()=='Welcome User'
    assert page.locator('#flash').text_content()=='Your purchase was completed successfully.'

def test_login_with_invalid_credentials_stays_on_login(page: Page):
    login = LoginPage(page)
    login.open()
    login.submit("wrong@test.com", "bad-password")
 
    expect(page).to_have_url(f"{BASE_URL}/login")
    expect(page.get_by_role("button", name="Login")).to_be_visible

    expect(page.locator(".welcome")).to_have_count(0)

