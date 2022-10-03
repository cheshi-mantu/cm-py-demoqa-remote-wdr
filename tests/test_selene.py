from selene.support import by
from selene.support.conditions import be
from selene.support.shared.jquery_style import s


def test_github(setup_browser):
    browser = setup_browser
    browser.open("https://github.com/")

    s('.header-search-input').click()
    s('.header-search-input').send_keys('cheshi-mantu/')
    s('.header-search-input').submit()

    s(by.link_text("cheshi-mantu/qa-local-test-bed")).click()

    s("#issues-tab").click()

    s(by.partial_text("#1")).should(be.visible)
