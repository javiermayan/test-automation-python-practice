import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.chrome.service import Service as ChromiumService
#from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.core.utils import ChromeType
import pyscreenrec

#driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

'''
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
'''
recorder = pyscreenrec.ScreenRecorder()

s = Service("../Drivers/chromedriver")
driver = webdriver.Chrome(service=s)
driver.maximize_window()

# to start recording
recorder.start_recording("recording.mp4", 10)
# 'recording.mp4' is the name of the output video file, may also contain full path like 'C:/Users/<user>/Videos/video.mp4'
# the second parameter(10) is the FPS. You can specify the FPS for the screen recording using the second parameter. It must not be greater than 60.

driver.get('https://www.google.com')
print(driver.title)

# to pause recording
#recorder.pause_recording()

# to resume recording
#recorder.resume_recording()

# to stop recording
recorder.stop_recording()
driver.quit()