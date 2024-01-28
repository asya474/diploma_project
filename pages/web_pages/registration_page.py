import os
from selene.support.shared import browser
from selene import be, have, command


class PracticeFormRegistrationFactCheck:
    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def registration(self, user):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        browser.element('#userNumber').type(user.phone_number)
        browser.element('label[for="gender-radio-3').click()
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(user.month_of_birth)
        browser.element('.react-datepicker__year-select').type(user.year_of_birth)
        browser.element(
            f'.react-datepicker__day--0{user.day_of_birth}:not(.react-datepicker__day--outside-month)'
        ).click()
        browser.element('#subjectsInput').type(user.subject).press_enter()
        browser.element('#uploadPicture').should(be.visible).type(os.path.abspath("hedgehog.jpg"))
        browser.element('#currentAddress').type(user.address)
        browser.element('//*[@id="hobbiesWrapper"]/div[2]/div[2]/label').should(be.visible).with_(timeout=20).click()
        browser.element('#react-select-3-input').type(user.state).press_enter()
        browser.element('#react-select-4-input').type(user.city).press_enter()
        browser.element('#submit').click()

    def student_should_be_registred(self, user):
        browser.all(".table-dark>tbody>tr>td:nth-child(2)").should(have.texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.phone_number,
            f'{user.day_of_birth} {user.month_of_birth},{user.year_of_birth}',
            user.subject,
            user.hobby,
            user.image,
            user.address,
            f'{user.state} {user.city}'
        ))
