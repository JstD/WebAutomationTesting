import unittest
from selenium import webdriver

import time
from functools import reduce
'''The package below include VNworks account form:
    username = ...
    password = ...
'''
from mydata import *
# from selenium.webdriver.common.by import By

"""
This test use normal login case.
Please change self.driver path for the successful runtime.
"""

def fill_in_register(driver, fname, lname, email, pw):
    driver.find_element_by_id("firstname").send_keys(fname)
    driver.find_element_by_id("lastname").send_keys(lname)
    driver.find_element_by_id("username").send_keys(email)
    driver.find_element_by_id("password").send_keys(pw)

def check_exception(driver):
    btnLogin = driver.find_element_by_id("button-register").submit()
    time.sleep(0.3)
    try:
        if driver.title == "VietnamWorks Account":
            raise Exception()
        driver.find_element_by_css_selector(
            "div.wrapper-user-btn").click()
        user = driver.find_element_by_class_name("username")
    except:
        print(driver.title)
        feedback = driver.find_elements_by_class_name(
            "invalid-feedback")
        print(list(reduce(lambda x, y: x+[y.text], feedback, [])))
        assert True
    else:
        assert False
    time.sleep(0.3)

class SigninTesting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/home/jstd/Desktop/Source/software_testing/chromedriver')
        self.driver.get('https://www.vietnamworks.com/')
        self.driver.find_element_by_css_selector(
            "div.wrapper-user-btn").click()
        self.driver.find_element_by_css_selector(
            "div.dropdownSection.registration").click()
    
    def test_register_empty_fname(self):
        fill_in_register(self.driver, '', lname, valid_email, valid_pw)
        time.sleep(0.3)
        check_exception(self.driver)

    def test_register_empty_lname(self):
        fill_in_register(self.driver, fname, '', valid_email, valid_pw)
        time.sleep(0.3)
        check_exception(self.driver)

    def test_register_empty_email(self):
        fill_in_register(self.driver, fname, lname, '', valid_pw)
        time.sleep(0.3)
        check_exception(self.driver)

    def test_register_empty_password(self):
        fill_in_register(self.driver, fname, lname, valid_email, '')
        time.sleep(0.3)
        check_exception(self.driver)
    
    def test_register_invalid_name(self):
        fill_in_register(self.driver, fname+'@', lname+'2', valid_email, valid_pw)
        time.sleep(0.3)
        check_exception(self.driver)
    
    def test_register_invalid_email(self):
        fill_in_register(self.driver,fname, lname, invalid_email, valid_pw)
        time.sleep(0.3)
        check_exception(self.driver)

    def test_register_used_email(self):
        fill_in_register(self.driver, fname, lname, used_email, valid_pw)
        time.sleep(0.3)
        check_exception(self.driver)

    def test_register_nonUpper_password(self):
        fill_in_register(self.driver, fname, lname, valid_email, nonUpper_pw)
        time.sleep(0.3)
        check_exception(self.driver)

    def test_register_nonNumber_password(self):
        fill_in_register(self.driver, fname, lname, valid_email, nonNumber_pw)
        time.sleep(0.3)
        check_exception(self.driver)

    def test_register_lessMinLength_password(self):
        fill_in_register(self.driver, fname, lname,
                         valid_email, lessMinLength_pw)
        time.sleep(0.3)
        check_exception(self.driver)

    def test_register_moreMaxLength_password(self):
        fill_in_register(self.driver, fname, lname,
                         valid_email, moreMaxLength_pw)
        time.sleep(0.3)
        check_exception(self.driver)

    def test_register_moreMaxLength_password(self):
        fill_in_register(self.driver, fname, lname,
                         valid_email, moreMaxLength_pw)
        time.sleep(0.3)
        check_exception(self.driver)
    
    def test_register_successful(self):
        fill_in_register(self.driver, fname, lname, valid_email, valid_pw)
        time.sleep(0.3)
        btnLogin = self.driver.find_element_by_id("button-register").submit()
        time.sleep(0.3)
        try:
            feedback = self.driver.find_elements_by_class_name(
                "invalid-feedback")
            txt = list(reduce(lambda x, y: x+[y.text], feedback, []))
            if not txt:
                raise Exception()
        except:
            print("Email " + self.driver.find_element_by_css_selector('strong').text)
            assert True
        else:
            print(txt)
            assert False
        time.sleep(1)

    def tearDown(self):
        self.driver.close()



if __name__ == '__main__':
    unittest.main()
