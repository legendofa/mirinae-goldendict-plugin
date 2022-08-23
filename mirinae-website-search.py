import argparse
import random
import time
import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class wait_for_non_empty_text(object):
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        try:
            element_text = EC._find_element(driver, self.locator).text.strip()
            return element_text != ""
        except StaleElementReferenceException:
            return False


def document_initialised(driver):
    return driver.execute_script("return initialised")


parser = argparse.ArgumentParser()
parser.add_argument("--url", action="store", help="Korean sentence input.")
args = parser.parse_args()

firefox_options = webdriver.FirefoxOptions()
firefox_options.set_headless()

driver = webdriver.Firefox(options=firefox_options)
driver.get("https://mirinae.io")

text_input = WebDriverWait(driver, timeout=10).until(
    lambda d: d.find_element(By.ID, "editable-source")
)

time.sleep(0.2)
text_input.send_keys(args.url)
time.sleep(0.2)
text_input.send_keys(Keys.ENTER)

exploration_page = driver.find_element(By.ID, "exploration-page")

WebDriverWait(driver, timeout=10).until(wait_for_non_empty_text((By.ID, "translation")))

random_file_name = str(random.getrandbits(64))
image_url = "/tmp/" + random_file_name + ".png"

driver.save_screenshot(image_url)

with open(image_url, "rb") as image_file:
    b64_string = base64.b64encode(image_file.read())

    print(
        '<html><body><img src="data:image/jpeg;base64,'
        + str(b64_string, "utf-8")
        + '"></body></html>'
    )

driver.close()
driver.quit()

# style="width: 100%; height: auto"