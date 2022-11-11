from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

for i in range(24):
    driver.get(f"https://kwadransnaangielski.pl/lekcja/page/{i+1}/")
    lesson_blocks = driver.find_elements(By.CSS_SELECTOR, '.lesson-block')
    for lesson_block in lesson_blocks:
        url = lesson_block.find_element(By.XPATH, "//h3/a[@href]")
        lesson_number = lesson_block.find_element(By.CSS_SELECTOR, '.lesson-block-data-number').text
        page_driver = webdriver.Chrome(options=options)
        page_driver.get(url.get_property('href'))
        download_button = page_driver.find_element(By.CSS_SELECTOR, ".button-download")
        download_url = download_button.get_attribute('href')
        response = urllib.request.urlopen(download_url)

        with open(f'{lesson_number}.mp3', 'wb') as file:
            file.write(response.read())

    page_driver.close()
driver.close()
