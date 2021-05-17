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

def check_exception_forgot(driver):
    time.sleep(0.3)
    driver.find_element_by_id("button-reset").submit()
    time.sleep(0.3)
    try:
        feedback = driver.find_elements_by_class_name(
            "invalid-feedback")
        txt = list(reduce(lambda x, y: x+[y.text], feedback, []))
        if txt:
            raise Exception()
    except:
        print(txt)
        assert True
    else:
        assert False
    time.sleep(0.3)
    

class LoginTesting(unittest.TestCase):
    def setUp(self):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://www.vietnamworks.com/')
        self.driver.find_element_by_css_selector("div.wrapper-user-btn").click()
        self.driver.find_element_by_css_selector("div.dropdownSection.login").click()
    
    def test_login_successfull(self):
        self.driver.find_element_by_name("username").send_keys(self.username)
        self.driver.find_element_by_name("password").send_keys(self.password)
        
        btnLogin = self.driver.find_element_by_id("button-login").submit()
        
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
        

    def test_login_wrong_pass(self):
        self.driver.find_element_by_name("username").send_keys(self.username)
        self.driver.find_element_by_name("password").send_keys(self.password + "abc")
        
        check_exception(self.driver)     

    def test_login_wrong_username(self):
        self.driver.find_element_by_name("username").send_keys(self.username + ".vn")
        self.driver.find_element_by_name("password").send_keys(self.password)
        
        check_exception(self.driver)

    def test_login_empty_password(self):
        self.driver.find_element_by_name(
            "username").send_keys(self.username)
        self.driver.find_element_by_name("password").send_keys("")
        
        check_exception(self.driver)

    def test_login_empty_email(self):
        self.driver.find_element_by_name(
            "username").send_keys("")
        self.driver.find_element_by_name("password").send_keys(self.password)
        
        check_exception(self.driver)

    def test_login_empty_both_2fields(self):
        self.driver.find_element_by_name(
            "username").send_keys("")
        self.driver.find_element_by_name("password").send_keys("")
        
        check_exception(self.driver)
    
    def test_forgot_password_with_valid_email(self):
        forgot = self.driver.find_element_by_css_selector("a.inline.m-t-sm.forgot-password__text.clickable").click()
        time.sleep(0.3)
        self.driver.find_element_by_id("username").send_keys(username)  #email real
        time.sleep(0.3)
        self.driver.find_element_by_id("button-reset").submit()
        time.sleep(0.3)
        try:
            feedback = self.driver.find_elements_by_class_name("invalid-feedback")
            txt = list(reduce(lambda x, y: x+[y.text], feedback, []))
            if txt:
                raise Exception()
        except:
            print(txt)
            assert False
        else:
            print(self.driver.find_element_by_css_selector("div.alert.alert-success").text)
            assert True

    def test_forgot_password_with_random_valid_email(self):
        forgot = self.driver.find_element_by_css_selector(
            "a.inline.m-t-sm.forgot-password__text.clickable").click()
        time.sleep(0.3)
        self.driver.find_element_by_id(
            "username").send_keys(valid_email)  # random valid email
        check_exception_forgot(self.driver)
    
    def test_forgot_password_with_invalid_email(self):
        fforgot = self.driver.find_element_by_css_selector(
            "a.inline.m-t-sm.forgot-password__text.clickable").click()
        time.sleep(0.3)
        self.driver.find_element_by_id(
            "username").send_keys(invalid_email)  # invalid_email
        check_exception_forgot(self.driver)
       
    def tearDown(self):
        self.driver.close()

class TestLoginWithSocial(unittest.TestCase):
    def setUp(self):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('./chromedriver.exe')
        self.driver.get('https://www.vietnamworks.com/')
        self.driver.find_element_by_css_selector(
            "div.wrapper-user-btn").click()

    def test_login_fb(self):
        self.driver.find_element_by_css_selector("a.social-login-facebook").click()
        self.driver.find_element_by_name("email").send_keys(fbname)
        self.driver.find_element_by_name("pass").send_keys(fbpass)
        
        btnLogin = self.driver.find_element_by_id("loginbutton").submit()
        
        if "VietnamWorks"in self.driver.title:
            assert True
        assert False
        
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
        
    
