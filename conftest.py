from datetime import datetime
from pathlib import Path

import pytest
import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select


BaseUrl = "https://www.saucedemo.com/v1/"
Username = "standard_user"
Password = "secret_sauce"



driver = None
@pytest.fixture(scope='class', autouse=True )
def browser_setup(request):
        chr_option = Options()
        chr_option.add_experimental_option("detach", True)
        request.cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chr_option)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today = datetime.now()
    report_dir = Path('hrmreports', today.strftime("%Y%m%d"))
    report_dir.mkdir(parents=True, exist_ok=True)
    pytest_html = report_dir / f"report_{today.strftime('%Y%m%d%H%M')}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True


def pytest_html_report_title(report):
    report.title = "HRM Test Report"


