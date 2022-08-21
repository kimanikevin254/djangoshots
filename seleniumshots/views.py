from django.http import FileResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def selenium(req):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get('https://www.geeksforgeeks.org/why-reading-code-is-more-important-than-writing/')
    driver.save_screenshot('seleniumshots/media/headless.png')
    driver.quit()

    return FileResponse(open('seleniumshots/media/headless.png', 'rb'))
