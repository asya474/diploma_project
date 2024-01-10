Проект по тестированию сайта "Tinkoff"
Особенности проекта
Оповещения о тестовых прогонах в Telegram
Отчеты с видео, скриншотом, логами браузера
Сборка проекта в Jenkins
Отчеты Allure Report
Интеграция с Allure TestOps
Автоматизация отчетности о тестовых прогонах в Jira
Запуск автотестов в Selenoid
Список проверок, реализованных в автотестах
 Перейти на страницу Кредиты возможно
 Перейти на страницу Вклады возможно
 Перейти на страницу Инвестиции возможно
 Перейти на страницу Страховка возможно
 Перейти на страницу Путешествия возможно
Используемый стэк
Python	Pytest	Selene	Selenium	Selenoid	Jenkins	Allure Reports	Allure TestOps	Jira
          

Запуск автотестов выполняется на сервере Jenkins
Ссылка на проект в Jenkins

Параметры сборки
environment - параметр определяет окружение для запуска тестов
comment - комментарий
Для запуска автотестов в Jenkins
Открыть проект
Выбрать пункт Build with Parameters
Выбрать окружение в выпадающем списке
Указать комментарий
Нажать кнопку Build
Результат запуска сборки можно посмотреть в отчёте Allure
This is an image

Allure отчет
Общие результаты
This is an image

Список тест кейсов
This is an image

Пример отчета о прохождении теста
This is an image

Полная статистика по прохождению тестпланов, отчёты и приложения к ним хранятся в Allure TestOps
Ссылка на проект в AllureTestOps (запрос доступа admin@qa.guru)

Общий список всех кейсов, имеющихся в системе (без разделения по тест-планам и виду выполнения тестирования)
This is an image

Пример отчёта выполнения одного из автотестов
This is an image

Пример dashboard с общими результатами тестирования
This is an image

Интеграция с Jira
Ссылка на проект в Jira

This is an image

Оповещение о результатах прогона тестов в Telegram
This is an image

Пример видео прохождения автотеста

### Что проверяем
* Проверка авторизации с невалидными данными
* Проверка поиска отсутствующей книги
* Поиск существующей книги
* Поиск по серии
* Добавление книги в корзину неавторизованным пользователем
* Ввод неверного промокода в корзине


### <img width="5%" title="Jenkins" src="images/logo/jenkins.png"> Запуск проекта в Jenkins

### [Job](https://jenkins.autotests.cloud/job/Students/job/Book_House/)

##### При нажатии на "Собрать сейчас" начнется сборка тестов и их прохождение, через виртуальную машину в Selenide.
![This is an image](images/screenshot/jenkins.png)

<!-- Allure report -->

### <img width="5%" title="Allure Report" src="images/logo/allure_report.png"> Allure report
### [Report](https://jenkins.autotests.cloud/job/Students/job/Book_House/allure/)
##### После прохождения тестов, результаты можно посмотреть в Allure отчете, где так же содержится ссылка на Jenkins
![This is an image](images/screenshot/allure_dashboard.png)

##### Во вкладке Graphs можно посмотреть графики о прохождении тестов, по их приоритезации, по времени прохождения и др.
![This is an image](images/screenshot/allure_graphs.png)

##### Во вкладке Suites находятся собранные тест кейсы, у которых описаны шаги и приложены логи, скриншот и видео о прохождении теста
![This is an image](images/screenshot/allure_suites.png)

##### Видео прохождение теста
![This is an image](images/screenshot/tests_ui.gif)

<!-- Allure TestOps -->

### <img width="5%" title="Allure TestOps" src="images/logo/allure_testops.png"> Интеграция с Allure TestOps

### [Dashboard](https://allure.autotests.cloud/project/2291/dashboards)

##### Так же вся отчетность сохраняется в Allure TestOps, где строятся аналогичные графики.
![This is an image](images/screenshot/allure_testops_dashboard.png)

#### Во вкладке со сьютами, мы можем:
- Управлять всеми тест-кейсами или с каждым отдельно
- Перезапускать каждый тест отдельно от всех тестов
- Настроить интеграцию с Jira
- Добавлять ручные тесты и т.д

![This is an image](images/screenshot/allure_testops_suites.png)


<!-- Jira -->

### <img width="5%" title="Jira" src="images/logo/jira.png"> Интеграция с Jira
##### Настроив через Allure TestOps интеграцию с Jira, в тикет можно пробросить результат прохождение тестов и список тест-кейсов из Allure

![This is an image](images/screenshot/jira.png)


<!-- Telegram -->

### <img width="5%" title="Telegram" src="images/logo/tg.png"> Интеграция с Telegram
##### После прохождения тестов, в Telegram bot приходит сообщение с графиком и небольшой информацией о тестах.

![This is an image](images/screenshot/tg_bot.png