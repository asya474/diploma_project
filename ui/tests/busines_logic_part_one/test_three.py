import os
from selene import browser, have, be
from selene.support.shared import browser


def test_registration_form(browser_management):
    browser.open("/automation-practice-form")
    browser.element("[for='hobbies-checkbox-3']").click()
    browser.element("#firstName").type('Test')
    browser.element("#lastName").type('Test')
    browser.element("#userEmail").type('test@test.com')
    browser.element("[for='gender-radio-1']").click()
    browser.element("#userNumber").type("1234567890")
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").should(be.visible).click()
    browser.element(".react-datepicker__month-select > option:nth-child(5)").should(be.visible).click()
    browser.element(".react-datepicker__year-select").should(be.visible).click()
    browser.element(".react-datepicker__year-select > option:nth-child(20)").should(be.visible).click()
    browser.element(".react-datepicker__day.react-datepicker__day--012").should(be.visible).click()
    browser.element('#subjectsInput').type('computer science').press_enter()
    browser.element("#uploadPicture").should(be.visible).type(os.path.abspath("pictures/character.png"))
    browser.element("#currentAddress").type("Sugar Palace, a candy store in Ponyville.")
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element("#submit").click()
    browser.all('tbody td:nth-of-type(2)').should(have.exact_texts(
        'Test Test',
        'test@test.com',
        'Male',
        '1234567890',
        '12 May,1919',
        'Computer Science',
        'Music',
        'character.png',
        'Sugar Palace, a candy store in Ponyville.',
        'NCR Delhi'))