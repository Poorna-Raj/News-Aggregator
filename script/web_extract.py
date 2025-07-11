from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Container - //div[@class = "sc-cb78bbba-1 fYSNbR"]
# Title - //div[@class = 'sc-666b6d83-0 jSTfiy"]//h2
# Description - //div[@class = 'sc-666b6d83-0 jSTfiy']//p
# Date - //div[@class = 'sc-666b6d83-0 jSTfiy']//span[@class = 'sc-ac6bc755-1 gxJSVz']
# Category - //div[@class = 'sc-666b6d83-0 jSTfiy']//span[@class = 'sc-ac6bc755-2 ivCQgh']
def scrape_news():
    website = 'https://www.bbc.com/news'
    path = r'F:\Software\chromedriver-win64\chromedriver.exe'

    options = Options()

    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service)
    driver.get(website)

    titles = []
    descriptions = []
    dates = []
    categories = []

    containers = driver.find_elements(by='xpath',value='//div[@class = "sc-cb78bbba-1 fYSNbR"]')

    for container in containers:
        try:
            title = container.find_element(by='xpath',value='.//h2').text
            description = container.find_element(by='xpath',value='.//p').text
            date = container.find_element(by='xpath',value='.//span[@class = "sc-ac6bc755-1 gxJSVz"]').text
            category = container.find_element(by='xpath',value='.//span[@class = "sc-ac6bc755-2 ivCQgh"]').text

            titles.append(title)
            descriptions.append(description)
            dates.append(date)
            categories.append(category)
        except Exception as e:
            print(e)

    driver.quit()


    data = []
    for i in range(len(titles)):
        data.append({
            'title':titles[i],
            'description':descriptions[i],
            'date':dates[i],
            'category':categories[i]
        })
    return data