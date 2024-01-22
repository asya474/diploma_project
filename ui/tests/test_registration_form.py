import allure
from allure_commons.types import Severity
from ui.data.users import User
from ui.page_object.registration_page import PracticeFormRegistrationFactCheck

import allure

practice_form = PracticeFormRegistrationFactCheck()


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "as.shemetova")
@allure.description("Registration")
@allure.feature("Registration")
def test_student_registration_form(setup_browser):
    with allure.step("Открыть страницу регистрации пользователей"):
        practice_form.open()
    with allure.step("Заполнить форму регистрации тестовыми данными"):
        user = User(first_name='Имя',
                    last_name='Фамилия',
                    email='testmail@mail.gg',
                    gender='Other',
                     month_of_birth='January',
                    phone_number='2589632147',
                    year_of_birth='2024',
                    day_of_birth='22',
                    subject='Physics',
                    hobby='Reading',
                    image='hedgehog.jpg',
                    address='221b, Baker Street, London, NW1 6XE, UK',
                    state='NCR',
                    city='Delhi')
        practice_form.registration(user)
    with allure.step("Проверка, что пользователь зарегистрирован"):
        practice_form.student_should_be_registred(user)
