import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
import pyscreenrec
import allure
from allure_commons.types import AttachmentType
import os

#driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

#------- config browser actions
chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--headless",
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
#---------------

filename = os.path.basename(__file__)
recorder = pyscreenrec.ScreenRecorder()

'''
s = Service("../Drivers/chromedriver")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
'''

def test_site_title():

    # to start recording
    #@allure.step("start_recording")
    recorder.start_recording("recording_prueba_07-09-22.mp4", 10)
    #recorder.start_recording(str(filename + "mp4"), 10)

    # 'recording.mp4' is the name of the output video file, may also contain full path like 'C:/Users/<user>/Videos/video.mp4'
    # the second parameter(10) is the FPS. You can specify the FPS for the screen recording using the second parameter. It must not be greater than 60.

    driver.get('https://www.google.com')
    assert driver.title == 'Google'
    #driver.get("http://www.python.org")
    #assert "Python" in driver.title
    print(driver.title)

    # to pause recording
    #recorder.pause_recording()

    # to resume recording
    #recorder.resume_recording()

    # to stop recording
    recorder.stop_recording()
    allure.attach(filename, name="Video", attachment_type=AttachmentType.MP4)
    driver.quit()