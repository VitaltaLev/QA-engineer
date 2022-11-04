# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestPZN5():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_pZN5(self):
    self.driver.get("https://qa.neapro.site/login/")
    self.driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys("vitalya.lev@mail.ru")
    self.driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys("129535851")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".active .document-tile:nth-child(1)").click()
    self.driver.find_element(By.ID, "surname").send_keys("Шангин")
    self.driver.find_element(By.ID, "name").send_keys("Виталий")
    self.driver.find_element(By.ID, "patronymic").send_keys("Игоревич")
    self.driver.find_element(By.NAME, "date").click()
    self.driver.find_element(By.NAME, "date").send_keys("01.01.1981")
    self.driver.find_element(By.ID, "passportSeries").send_keys("1111")
    self.driver.find_element(By.ID, "passportNumber").send_keys("222222")
    self.driver.find_element(By.CSS_SELECTOR, "#dateOfIssue .mx-input").click()
    self.driver.find_element(By.CSS_SELECTOR, "#dateOfIssue .mx-input").send_keys("01.01.1990")
    self.driver.find_element(By.ID, "code").send_keys("333333")
    self.driver.find_element(By.ID, "cardId").send_keys("444444444444")
    self.driver.find_element(By.ID, "issued").send_keys("ОВД")
    self.driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".document-page").click()
    self.driver.find_element(By.CSS_SELECTOR, ".vue-dadata__input").send_keys("Кировская обл")
    self.driver.find_element(By.CSS_SELECTOR, ".vue-dadata__suggestions-item").click()
    self.driver.find_element(By.ID, "phone").send_keys("9992224455")
    self.driver.find_element(By.CSS_SELECTOR, ".outline").click()
    self.driver.find_element(By.CSS_SELECTOR, ".upload-widget> input").send_keys("C:\\Doc.pdf")
    self.driver.get("https://qa.neapro.site/logincss=.fill")
    time.sleep(3)
    self.driver.get("https://qa.neapro.site/login/")
  
