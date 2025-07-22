import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Container - //div[@class = "sc-cb78bbba-1 fYSNbR"]
# Title - //div[@class = 'sc-666b6d83-0 jSTfiy"]//h2
# Description - //div[@class = 'sc-666b6d83-0 jSTfiy']//p
# Date - //div[@class = 'sc-666b6d83-0 jSTfiy']//span[@class = 'sc-ac6bc755-1 gxJSVz']
# Category - //div[@class = 'sc-666b6d83-0 jSTfiy']//span[@class = 'sc-ac6bc755-2 ivCQgh']
def scrape_news():
    website = 'https://www.bbc.com/news'
    path = r'F:\Software\chromedriver-win64\chromedriver.exe'

    options = Options()
    options.add_argument('--headless=new')

    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service,options=options)
    driver.get(website)

    try:
        # Wait for iframe to appear and switch into it
        print("Waiting for iframe...")
        iframe = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[src*='piano.io']"))
        )
        driver.switch_to.frame(iframe)
        print("Switched to iframe")

        # Wait for the Continue button inside iframe
        accept_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Continue")]'))
        )
        time.sleep(1)
        accept_button.click()
        print("Clicked the 'Continue' button")

        # Switch back to the main content
        driver.switch_to.default_content()
    except Exception as e:
        print(f'Something went wrong while closing the button {e}')

    data = []
    containers = driver.find_elements(by='xpath',value='//div[contains(@class , "jSTfiy")]')

    for container in containers:
        try:
            title = container.find_element(by='xpath',value='.//h2').text
            description = container.find_element(by='xpath',value='.//p').text
            date = container.find_element(by='xpath',value='.//span[contains(@class, "iFYhEd")]').text
            category = container.find_element(by='xpath',value='.//span[contains(@class, "hNeWKH")]').text

            if all([title, description, date, category]):
                data.append({
                    'title':title,
                    'description' : description,
                    'date' : date,
                    'category':category
                })
        except Exception as e:
            print(e)

    driver.quit()
    return data