from selene import have, command
from selene.support.shared import browser


def resource(relative_path):
    import demoqa_test
    from pathlib import Path
    return (
        Path(demoqa_test.__file__)
        .parent
        .parent
        .joinpath('resources/')
        .joinpath(relative_path)
        .absolute()
        .__str__()
    )


def arrange_form_opened():
    browser.open('/automation-practice-form')
    browser.all(
        '[id^=google_ads][id$=container__]').with_(timeout=10).should(have.size(3)).perform(command.js.remove)
