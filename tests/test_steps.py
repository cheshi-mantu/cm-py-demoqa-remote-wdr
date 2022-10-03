import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared.jquery_style import s


def test_github(setup_browser):
    browser = setup_browser
    with allure.step('Open main page'):
        browser.open("https://github.com/")

    with allure.step('Searching for a repository'):
        s('.header-search-input').click()
        s('.header-search-input').send_keys('Bodan1992/Bodan1992-JS')
        s('.header-search-input').submit()

    with allure.step('Follow the repository link'):
        s(by.link_text("Bodan1992/Bodan1992-JS")).click()

    with allure.step('Switch to tab Issues'):
        s("#issues-tab").click()

    with allure.step('Checking the number Issue with number 1'):
        s(by.partial_text("#1")).should(be.visible)