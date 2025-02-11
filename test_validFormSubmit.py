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

class TestValidFormSubmit():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_validFormSubmit(self):
    self.driver.get("https://demoqa.com/automation-practice-form")
    self.driver.set_window_size(1366, 768)
    self.driver.execute_script("window.scrollTo(0,488)")
    self.driver.find_element(By.ID, "firstName").click()
    self.driver.find_element(By.ID, "firstName").send_keys("Dilshani")
    self.driver.find_element(By.ID, "lastName").click()
    self.driver.find_element(By.ID, "lastName").send_keys("Chamodika")
    self.driver.find_element(By.ID, "userEmail").click()
    self.driver.find_element(By.ID, "userEmail").send_keys("k.d.chamodika@gmail.com")
    self.driver.find_element(By.CSS_SELECTOR, ".custom-radio:nth-child(2) > .custom-control-label").click()
    self.driver.find_element(By.ID, "userNumber").click()
    self.driver.find_element(By.ID, "userNumber").send_keys("0715289816")
    self.driver.find_element(By.ID, "userForm").click()
    self.driver.find_element(By.ID, "dateOfBirthInput").click()
    self.driver.find_element(By.CSS_SELECTOR, ".react-datepicker__year-select").click()
    dropdown = self.driver.find_element(By.CSS_SELECTOR, ".react-datepicker__year-select")
    dropdown.find_element(By.XPATH, "//option[. = '2001']").click()
    self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(102)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".react-datepicker__month-select").click()
    dropdown = self.driver.find_element(By.CSS_SELECTOR, ".react-datepicker__month-select")
    dropdown.find_element(By.XPATH, "//option[. = 'May']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".react-datepicker__month-select > option:nth-child(5)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".react-datepicker__day--019").click()
    self.driver.find_element(By.CSS_SELECTOR, ".custom-checkbox:nth-child(2) > .custom-control-label").click()
    self.driver.find_element(By.CSS_SELECTOR, ".custom-checkbox:nth-child(3) > .custom-control-label").click()
    self.driver.execute_script("window.scrollTo(0,674)")
    self.driver.find_element(By.ID, "currentAddress").click()
    self.driver.find_element(By.ID, "currentAddress").send_keys("Isuru, Mahagedarawaththa, Makandura")
    self.driver.execute_script("window.scrollTo(0,891)")
    self.driver.find_element(By.ID, "submit").click()

    time.sleep(1)

    assert self.driver.find_element(By.ID, "example-modal-sizes-title-lg").text == "Thanks for submitting the form"
    student_name = self.driver.find_element(By.XPATH, "//td[text()='Student Name']/following-sibling::td").text
    assert student_name == "Dilshani Chamodika", f"Expected 'Dilshani Chamodika', but got '{student_name}'"
    student_email = self.driver.find_element(By.XPATH, "//td[text()='Student Email']/following-sibling::td").text
    assert student_email == "k.d.chamodika@gmail.com", f"Expected 'k.d.chamodika@gmail.com', but got '{student_email}'"
    gender = self.driver.find_element(By.XPATH, "//td[text()='Gender']/following-sibling::td").text
    assert gender == "Female", f"Expected 'Female', but got '{gender}'"
    mobile = self.driver.find_element(By.XPATH, "//td[text()='Mobile']/following-sibling::td").text
    assert mobile == "0715289816", f"Expected '1234567890', but got '{mobile}'"