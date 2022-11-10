from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request


driver = webdriver.Chrome()

for i in range(24):
    driver.get(f"https://kwadransnaangielski.pl/lekcja/page/{i}/")
    urls_page = driver.find_elements(By.XPATH, "//h3/a[@href]")
    for url in urls_page:
        page_driver = webdriver.Chrome()
        page_driver.get(url.get_property('href'))
        download_button = page_driver.find_element(By.CSS_SELECTOR, ".button-download")
        download_url = download_button.get_attribute('href')
        response = urllib.request.urlopen(download_url)

        with open(url.text, 'wb') as file:
            file.write(response.read())

        page_driver.close()
    driver.close()
