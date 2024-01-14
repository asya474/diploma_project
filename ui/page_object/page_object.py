from selene import browser, have, by


class TinkoffPage:

    def credit_cart_button(self):
        browser.element('[href = "/cards/credit-cards/?internal_source=home_icon"]').press_enter()

    def deposits_button(self):
        browser.element('[href = "/savings/deposit/?internal_source=home_icon"]').press_enter()

    def investition_button(self):
        browser.element('[href = "/invest/?internal_source=home_icon"]').press_enter()

    def insurance_button(self):
        browser.element('[href = "/insurance/?internal_source=home_icon"]').press_enter()

    def travel_button(self):
        browser.element('[href = "/travel/?internal_source=home_icon"]').press_enter()

    def go_to_credit_cart_button_page(self):
        browser.should(have.url_containing(
            f'https://www.tinkoff.ru/cards/credit-cards/?internal_source=home_icon'
        ))

    def go_to_deposits_button_page(self):
        browser.should(have.url_containing(
            f'https://www.tinkoff.ru/savings/deposit/?internal_source=home_icon'
        ))

    def go_to_investition_button_page(self):
        browser.should(have.url_containing(
            f'https://www.tinkoff.ru/invest/?internal_source=home_icon'
        ))

    def go_to_insurance_button_page(self):
        browser.should(have.url_containing(
            f'https://www.tinkoff.ru/insurance/?internal_source=home_icon'
        ))

    def go_to_travel_button_page(self):
        browser.should(have.url_containing(
            f'https://www.tinkoff.ru/travel/?internal_source=home_icon'
        ))

from selene import browser, be, have, command
from data import image


class PracticeFormRegistrationFactCheck:
    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def registration(self, guest):
        browser.element('#firstName').type(guest.first_name)
        browser.element('#lastName').type(guest.last_name)
        browser.element('#userEmail').type(guest.email)
        browser.element('#userNumber').type(guest.phone_number)
        browser.element('label[for="gender-radio-3').click()
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(guest.month_of_birth)
        browser.element('.react-datepicker__year-select').type(guest.year_of_birth)
        browser.element(
            f'.react-datepicker__day--0{guest.day_of_birth}:not(.react-datepicker__day--outside-month)'
        ).click()
        browser.element('#subjectsInput').type(guest.subject).press_enter()
        #browser.element('#uploadPicture').should(be.visible).type(os.path.abspath("tests/hedgehog.jpg"))
        browser.element('#uploadPicture').send_keys(image.path(guest.image))
        browser.element('#currentAddress').type(guest.address)
        browser.element('//*[@id="hobbiesWrapper"]/div[2]/div[2]/label').should(be.visible).with_(timeout=20).click()
        browser.element('#react-select-3-input').type(guest.state).press_enter()
        browser.element('#react-select-4-input').type(guest.city).press_enter()
        browser.element('#submit').click()

    def student_should_be_registred(self, guest):
        browser.all(".table-dark>tbody>tr>td:nth-child(2)").should(have.texts(
            f'{guest.first_name} {guest.last_name}',
            guest.email,
            guest.gender,
            guest.phone_number,
            f'{guest.day_of_birth} {guest.month_of_birth},{guest.year_of_birth}',
            guest.subject,
            guest.hobby,
            guest.image,
            guest.address,
            f'{guest.state} {guest.city}'
        ))