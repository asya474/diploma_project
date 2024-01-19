

import allure
from allure_commons.types import Severity
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from ui.data.users import User
from ui.page_object.registration_page import RegistrationPage


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "as.shemetova")
@allure.description("Registration")
@allure.feature("Registration")
def test_registration_form(browser_setup):
    user = User('Test',
                'Test',
                'test@test.com',
                'Male',
                '1234567890',
                '2001',
                'May',
                '15',
                'Computer Science',
                'Reading',
                'character.png',
                'Sugar Palace, a candy store in Ponyville',
                'NCR',
                'Delhi')
    registration_page = RegistrationPage()
    with allure.step("Открыть страницу регистрации пользователей"):
        registration_page.open()
    with allure.step("Заполнить форму регистрации тестовыми данными"):
        registration_page.register(user=user)
    with allure.step("Проверка, что пользователь зарегистрирован"):
        registration_page.should_have_registered(user)