import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

class Ayuda(unittest.TestCase):

    def setUp(self):
        global driver
        s = Service("../Drivers/chromedriver")
        driver = webdriver.Chrome(service=s)
        driver.maximize_window()
        driver.get("https://www.google.com")

    def test_site_title(self):
        time.sleep(5)  # Let the user actually see something!
        assert driver.title == 'Google'

        '''
        service.start()

        driver = webdriver.Remote(service.service_url)
        '''



    def test_the_tests(self):
        print("Corriendo test de prueba...")
        assert True

        assert 2 == 3

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    unittest.main()

#driver.get("https://www.userapp.dev.mfs-merchants.io")

