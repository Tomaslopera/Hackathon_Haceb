from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

# brew install chromium-chromedriver
# which chromedriver (/opt/homebrew/bin/chromedriver)
# ChromeDriverManager().install()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get('https://www.haceb.com/repuestos-y-accesorios/accesorios')
wait = WebDriverWait(driver, 10)

# Espera a que carguen los resultados
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.vtex-search-result-3-x-galleryItem.vtex-search-result-3-x-galleryItem--normal.vtex-search-result-3-x-galleryItem--category.pa4')))

# Parsear con BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Selecciona todos los items
items = soup.select('div.vtex-search-result-3-x-galleryItem.vtex-search-result-3-x-galleryItem--normal.vtex-search-result-3-x-galleryItem--category.pa4')

for item in items:
    # Selecciona el enlace del título con clase poly-component__title
    link = item.select_one('span.vtex-product-summary-2-x-productBrand.vtex-product-summary-2-x-brandName.t-body')
    
    if link:
        titulo = link.text.strip()
        print(titulo)

driver.quit()