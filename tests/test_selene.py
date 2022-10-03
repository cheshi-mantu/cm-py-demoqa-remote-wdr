from selene.support import by
from selene.support.conditions import be
from selene.support.shared.jquery_style import s


def test_github(setup_browser):
    browser = setup_browser
    browser.open("https://github.com/")

    s('.header-search-input').click()
    s('.header-search-input').send_keys('Bodan1992/Bodan1992-JS')
    s('.header-search-input').submit()

    s(by.link_text("Bodan1992/Bodan1992-JS")).click()

    s("#issues-tab").click()

    s(by.partial_text("#1")).should(be.visible)


def test_github_new(setup_browser):
    browser = setup_browser
    browser.open("https://github.com/")

    s('.header-search-input').click()
    s('.header-search-input').send_keys('Bodan1992/Bodan1992-JS')
    s('.header-search-input').submit()

    s(by.link_text("Bodan1992/Bodan1992-JS")).click()

    s("#issues-tab").click()

    s(by.partial_text("#1")).should(be.visible)