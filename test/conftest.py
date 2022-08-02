import logging
import os
import shutil

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def setup(browser, request):
    remove_screenshots()

    if browser == "firefox":
        logging.info("Tests will run in Firefox")
        ff_options = webdriver.FirefoxOptions()
        ff_options.add_argument('--disable-notifications')  # for windows
        ff_options.add_argument('--kiosk')  # for mac
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=ff_options)
    else:
        logging.info("Tests will run in Chrome")
        chr_options = webdriver.ChromeOptions()
        chr_options.add_experimental_option("detach", True)
        chr_options.add_argument('--disable-notifications')
        chr_options.add_argument('--start-maximized')  # for windows
        chr_options.add_argument('--kiosk')  # for mac
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chr_options)

    driver.implicitly_wait(30)
    request.cls.driver = driver
    logging.info("---- TESTS STARTED ----")

    yield  # tearDown

    method_name = request.node.name

    if request.node.rep_call.failed:
        logging.info('**************test {} failed :('.format(method_name))
        driver.save_screenshot("./screenshots/" + method_name + ".png")

    driver.close()
    logging.info("---- TESTS FINISHED ----")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


def pytest_addoption(parser):
    parser.addoption("--browser")


def remove_screenshots():
    folder = './screenshots'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            logging.warning("Could not delete screenshots : {}", e)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
