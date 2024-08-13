from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver(browser="chrome"):
    """
    Get a WebDriver instance for the specified browser.

    :param browser: Name of the browser ("chrome" or "firefox")
    :return: WebDriver instance
    :raises ValueError: If an unsupported browser is specified
    """
    if browser == "chrome":
        options = Options()
        options.add_argument('--ignore-certificate-errors, --disable-search-engine-choice-screen')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.accept_insecure_certs = True
        driver = webdriver.Firefox(options=options)
    # Add other browsers if needed
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    driver.maximize_window()
    return driver
