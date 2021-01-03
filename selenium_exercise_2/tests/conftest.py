from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):

    wd = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    wd.get("http://automationpractice.com")

    def close_driver():
        wd.quit()

    request.addfinalizer(close_driver)
    return wd