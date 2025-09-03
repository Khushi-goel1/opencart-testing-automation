import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import os
import base64

@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument("--headless")  
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("browser")
        if driver:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name
            screenshot_path = f"screenshots/{test_name}_{timestamp}.png"

            driver.save_screenshot(screenshot_path)
            print(f"\nScreenshot saved: {screenshot_path}")

            # Attach screenshot to pytest-html report
            pytest_html = item.config.pluginmanager.getplugin("html")
            if pytest_html is not None:
                with open(screenshot_path, "rb") as f:
                    img_base64 = base64.b64encode(f.read()).decode("utf-8")
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.image(img_base64, mime_type="image/png"))
                rep.extra = extra

def pytest_html_results_table_header(cells):
    cells.insert(2, '<th>Extras</th>')

def pytest_html_results_table_row(report, cells):
    extra = getattr(report, 'extra', [])
    if extra:
        html = ''
        for e in extra:
            if e.get('format_type') == 'image':
                html += f'<img src="data:image/png;base64,{e["content"]}" style="max-width:200px; max-height:100px;" />'
        cells.insert(2, html)
    else:
        cells.insert(2, '')
