import unittest
'''
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService, Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.chrome.service import Service

'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
'''
import time


class Ayuda(unittest.TestCase):

    def setUp(self):
        global driver
        #s = Service("../Drivers/chromedriver")
        #driver = webdriver.Chrome(service=s)
        #driver = webdriver.Chrome(ChromeDriverManager().install())
        '''
        driver_path = ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
        driver = webdriver.Chrome(driver_path)
        driver.maximize_window()
        
        driver = webdriver.Chrome(
            service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
        '''
        chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

        chrome_options = Options()
        options = [
            #"--headless",
            "--disable-gpu",
            "--window-size=1920,1200",
            "--ignore-certificate-errors",
            "--disable-extensions",
            "--no-sandbox",
            "--disable-dev-shm-usage"
        ]
        for option in options:
            chrome_options.add_argument(option)

        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

        driver.get("https://www.google.com")
        print(driver.title)

    def test_site_title(self):
        time.sleep(5)  # Let the user actually see something!
        assert driver.title == 'Google'


    def test_the_tests(self):
        print("Corriendo test de prueba...")
        assert True

        assert 2 == 3

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()



