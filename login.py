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
def check_exception(driver):
    driver.find_element_by_id("button-login").submit()
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
        print(self.driver.title)
        print("Username " + user.text)
        assert False
    time.sleep(0.3)

class LoginTesting(unittest.TestCase):
    def setUp(self):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('./chromedriver.exe')
        self.driver.get('https://www.vietnamworks.com/')
        self.driver.find_element_by_css_selector("div.wrapper-user-btn").click()
        self.driver.find_element_by_css_selector("div.dropdownSection.login").click()

    def test_login_successfull(self):
        self.driver.find_element_by_name("username").send_keys(self.username)
        self.driver.find_element_by_name("password").send_keys(self.password)
        time.sleep(0.3)
        btnLogin = self.driver.find_element_by_id("button-login").submit()
        time.sleep(0.3)
        try:
            if self.driver.title == "VietnamWorks Account":
                raise Exception()
            self.driver.find_element_by_css_selector("div.wrapper-user-btn").click()
            user = self.driver.find_element_by_class_name("username")
        except:
            print(self.driver.title)
            feedback = self.driver.find_elements_by_class_name(
                "invalid-feedback")
            print(list(reduce(lambda x, y: x+[y.text], feedback, [])))
            assert False
        else:
            print(self.driver.title)
            print("Username " + user.text)
            assert True
        time.sleep(0.3)

    def test_login_wrong_pass(self):
        self.driver.find_element_by_name("username").send_keys(self.username)
        self.driver.find_element_by_name("password").send_keys(self.password + "abc")
        time.sleep(0.3)
        check_exception(self.driver)     

    def test_login_wrong_username(self):
        self.driver.find_element_by_name("username").send_keys(self.username + ".vn")
        self.driver.find_element_by_name("password").send_keys(self.password)
        time.sleep(0.3)
        check_exception(self.driver)

    def test_login_empty_password(self):
        self.driver.find_element_by_name(
            "username").send_keys(self.username)
        self.driver.find_element_by_name("password").send_keys("")
        time.sleep(0.3)
        check_exception(self.driver)

    def test_login_empty_email(self):
        self.driver.find_element_by_name(
            "username").send_keys("")
        self.driver.find_element_by_name("password").send_keys(self.password)
        time.sleep(0.3)
        check_exception(self.driver)

    def test_login_empty_both_2fields(self):
        self.driver.find_element_by_name(
            "username").send_keys("")
        self.driver.find_element_by_name("password").send_keys("")
        time.sleep(0.3)
        check_exception(self.driver)
    

    def tearDown(self):
        self.driver.close()

class TestLoginWithSocial(unittest.TestCase):
    def setUp(self):
        self.username = mydata.username
        self.password = mydata.password
        self.driver = webdriver.Chrome('./chromedriver.exe')
        self.driver.get('https://www.vietnamworks.com/')
        self.driver.find_element_by_css_selector(
            "div.wrapper-user-btn").click()

    def test_login_fb(self):
        self.driver.find_element_by_css_selector("a.social-login-facebook").click()
        self.driver.find_element_by_name("email").send_keys(fbname)
        self.driver.find_element_by_name("pass").send_keys(fbpass)
        time.sleep(0.3)
        btnLogin = self.driver.find_element_by_id("loginbutton").submit()
        time.sleep(0.3)
        if "VietnamWorks"in self.driver.title:
            assert True
        assert False
        time.sleep(0.3)

        
    
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
        
    
