# Demo test automation project (UI, Mobile, API)

##:page_with_curl:    Content

> heavy_check_mark: [Technology stack](#technology-stack)
>
> heavy_check_mark: [Running Tests in Jenkins](#running_tests_in_jenkins)
>
> heavy_check_mark: [Test results report in Allure Report](#allure-report)
>
> heavy_check_mark: [Telegram notifications using a bot](#telegram-notifications-using-a-bot)
>
> heavy_check_mark: [An example of running a test in Selenoid](#example-of-running-a-test-in-selenoid)

## Technology stack

<p align="center"></p>
<a href="https://www.python.org/"><img src="files/readme_images/python.png" width="50" height="50"  alt="PYTHON"/></a>
<a href="https://www.selenium.dev/"><img src="files/readme_images/selenium.png" width="50" height="50"  alt="SELENIUM"/></a>
<a href="https://docs.pytest.org/en/"><img src="files/readme_images/pytest.png" width="50" height="50"  alt="PYTEST"/></a>
<a href="https://www.jetbrains.com/ru-ru/pycharm/"><img src="files/readme_images/intellij_pycharm.png" width="50" height="50"  alt="PYCHARM"/></a>
<a href="https://www.jenkins.io/"><img src="files/readme_images/jenkins.png" width="50" height="50"  alt="JENKINS"/></a>
<a href="https://python-poetry.org/"><img src="files/readme_images/selene.png" width="50" height="50"  alt="SELENE"/></a>

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
> After completed run, notifications are sent in <code>Telegram</code>.

## Running Tests in Jenkins

#### UI-tests:

```
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install --no-root
pytest --browser=${BROWSER} --browser_version=${BROWSER_VERSION} tests/web
```

#### API-tests:

```
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install --no-root
pytest tests/api
```

#### Mobile tests:

```
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install --no-root
pytest --env=${ENV} tests/mobile
```

For running in BrowserStack:

```
pytest --env=browserstack tests/mobile/
```

For local running:

```
pytest --env=local tests/mobile/
```

There are some conditions for local mobile tests running:

- <code>Appium Server</code> is running;
- android emulator device is enabled in AndroidStudio;

### Build Options

> <code>REMOTE_URL</code> – the address of the remote server where the tests will run.
>
> <code>BROWSER</code> – the browser the tests will be run (_default - <code>chrome</code>_).
>
> <code>BROWSER_VERSION</code> – version of the browser the tests will be run (_default - <code>91.0</code>_).
>
> <code>BROWSER_SIZE</code> – the size of the browser window the tests will be run (_default - <code>1920x1080</code>_).

## Test results report in Allure Report

## Telegram notifications using a bot

## An example of running a test in Selenoid
