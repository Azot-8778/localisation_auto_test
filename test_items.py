import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_cart_button(browser):
    browser.get(link)
    buttons = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(buttons) > 0, 'add_to_basket button not found'
    time.sleep(30)