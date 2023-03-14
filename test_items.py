from selenium.webdriver.common.by import By



"""
    Hi, dear review! 
    Test-case must work with different browsers (chrome or firefox) and differen languages! 
    The assert must work too.

    You can enter:
    pytest --browser_name=[chrome | firefox] --language=[ru | en | fr | and so on] test_items.py

    Thank you for attention and your time!
    Have a good day!
"""


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_busket_show(browser):
    browser.get(link)
    button = browser.find_elements(By.CSS_SELECTOR, "button:nth-child(3)")
    assert button != [], '[!] Button is absent.'

