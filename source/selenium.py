from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def elan_datasi(product_id):
    url = f"https://tap.az/product/{product_id}"

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    try:
        wait = WebDriverWait(driver, 10)

        title = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))
        ).text

        price = driver.find_element(By.CSS_SELECTOR, ".product-price__i").text

        description = driver.find_element(By.CSS_SELECTOR, ".product-description__content").text

        data = {
            "id": product_id,
            "title": title,
            "price": price,
            "description": description,
            "url": url
        }

    except Exception as e:
        data = {"error": str(e)}

    driver.quit()
    return data