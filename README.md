# # Demo test automation project (UI, Mobile, API) 
## :page_with_curl:    Content
> :heavy_check_mark: [Technology stack](#classical_building-technology-stack)
>
> :heavy_check_mark: [Running tests from the terminal](#running-tests-from-the-terminal)
>
> :heavy_check_mark: [Running Tests in Jenkins](#robot-remote-test-running)
>
> :heavy_check_mark: [Test results report in Allure Report](#skier-main-page-of-allure-report)
>
> :heavy_check_mark: [Telegram notifications using a bot](#-telegram-notifications-using-a-bot)
>
> :heavy_check_mark: [An example of running a test in Selenoid](#-an-example-of-running-a-test-in-selenoid)

## :technologist: Technology stack

<p align="center"
<a href="https://www.python.org/"><img src="files/readme_images/python.svg" width="50" height="50"  alt="PYTHON"/></a>
<a href="https://www.selenium.dev/"><img src="files/readme_images/selenium.svg" width="50" height="50"  alt="SELENIUM"/></a>
<a href="https://docs.pytest.org/en/"><img src="files/readme_images/pytest.svg" width="50" height="50"  alt="SELENIUM"/></a>
<a href="https://www.jetbrains.com/ru-ru/pycharm/"><img src="files/readme_images/pycharm.svg" width="50" height="50"  alt="PYCHARM"/></a>
<a href="https://docs.pydantic.dev/latest/"><img src="files/readme_images/pydantic.svg" width="50" height="50"  alt="PYDANTIC"/></a>
<a href="https://pypi.org/project/python-dotenv/"><img src="files/readme_images/dotenv.svg" width="50" height="50"  alt=".ENV"/></a>
<a href="https://www.jenkins.io/"><img src="files/readme_images/jenkins.svg" width="50" height="50"  alt="JENKINS"/></a>
<a href="https://python-poetry.org/"><img src="files/readme_images/poetry.svg" width="50" height="50"  alt="POETRY"/></a>
</p>

In this project, autotests are written in <code> Python </code> using:
<code> pytest </code>,
<code> selenium </code>,
<code> selene </code>,
<code> requests </code>,
<code> appium </code>.
>
> <code>Selenoid</code> launches browsers in <code>Docker</code> containers.
>
> <code>Allure Report</code> and <code>Allure TestOps</code> generates a test run report.
>
> <code>Jenkins</code> runs the tests.
>
> After the run is completed, notifications are sent using the bot to <code>Telegram</code>.

## Running tests from the terminal

### :robot: Remote test running

#### UI-тесты:
```
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install --no-root
pytest --browser=${BROWSER} --browser_version=${BROWSER_VERSION} tests/web
```

#### API-тесты:
```
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install --no-root
pytest tests/api
```

#### Мобильные тесты:
```
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install --no-root
pytest --env=${ENV} tests/mobile
```

### :robot: Running Tests Locally
Для локального запуска с значениями по умолчанию необходимо выполнить команду:
```
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install --no-root
pytest tests
```

#### Запуск мобильных тестов

Мобильные тесты могут быть запущены как в <code>BrowserStack</code>, так и локально. 
Для запуска в BrowserStack:
```
pytest --env=browserstack tests/mobile/
```
Для запуска локально:
```
pytest --env=local tests/mobile/
```
Для локального запуска мобильных тестов необходимо соблюдение некоторых условий:
 - <code>Appium Server</code> запущен;
 - включен эмулятор в AndroidStudio;

### :robot: Build Options
> <code>REMOTE_URL</code> – the address of the remote server where the tests will run.
>
> <code>BROWSER</code> – the browser the tests will be run (_default - <code>chrome</code>_).
>
> <code>BROWSER_VERSION</code> – version of the browser the tests will be run (_default - <code>91.0</code>_).
>
> <code>BROWSER_SIZE</code> – the size of the browser window the tests will be run (_default - <code>1920x1080</code>_).

Отчеты с видео, скриншотом, логами браузера
Сборка проекта в Jenkins
Отчеты Allure Report
Интеграция с Allure TestOps
Автоматизация отчетности о тестовых прогонах в Jira
Запуск автотестов в Selenoid