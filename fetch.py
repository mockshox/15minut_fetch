from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
import logging

logging.basicConfig(level=logging.INFO)


from selenium.webdriver.chrome.options import Options

options = Options()
# options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

for i in range(300):
    page = f"https://kwadransnaangielski.pl/lekcja/{i+1}"
    driver.get(page)
    logging.info(f'page={page}')
    try:
        download_button = driver.find_element(By.CSS_SELECTOR, ".button-download")
    except:
        continue
    download_url = download_button.get_attribute('href')
    logging.info(f'download_url={download_url}')
    response = urllib.request.urlopen(download_url)

    with open(f'Lekcja {i+1}.mp3', 'wb') as file:
        file.write(response.read())

driver.close()
