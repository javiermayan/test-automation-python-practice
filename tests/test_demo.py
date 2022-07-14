"""
Run these tests after completing the setup steps to verify that the framework works.
"""

def test_the_tests():
  print("Corriendo test de prueba...")
  assert True

  assert 2==3


"""
This script will open the Qxf2 website and verify its title
"""
from selenium import webdriver

site_url = 'https://qxf2.com/'


def test_site_title():
  "Checks Qxf2's website title"
  driver = webdriver.Chrome()
  driver.get(site_url)
  assert driver.title == 'Qxf2 Services: Outsourced Software QA for startups'


