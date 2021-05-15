import unittest
from selenium import webdriver

import time

'''The package below include VNworks account form:
    username = ...
    password = ...
'''
import mydata
# from selenium.webdriver.common.by import By



"""
This test use normal login case.
Please change self.driver path for the successful runtime.
"""
class ApplyJobAndProfileTesting(unittest.TestCase):
    def setUp(self):
        self.username = mydata.username
        self.password = mydata.password
        self.driver = webdriver.Chrome('/home/jstd/Desktop/Source/software_testing/chromedriver')
        self.driver.get('https://www.vietnamworks.com/')

    def test_apply_job_without_login(self):
        inp = self.driver.find_element_by_id('search-bar-input')
        inp.send_keys('IT')
        self.driver.find_element_by_class_name('searchBar__button').click()
        self.driver.find_element_by_class_name('job-item').click()
        self.driver.switch_to.window(self.driver.window_handles[-1]) # switch to newest tab
        lstBtn = self.driver.find_elements_by_class_name('btn-apply')
        for x in lstBtn:
            try:
                x.click()
                break
            except:
                pass
        assert self.driver.title == 'VietnamWorks Account'

    def test_apply_job_with_new_account(self):
        '''
        Login with VNworks account
        '''
        login = self.driver.find_element_by_class_name('login')
        self.driver.get(login.find_element_by_tag_name('a').get_attribute('href'))
        self.driver.find_element_by_id('email').send_keys(self.username)
        self.driver.find_element_by_id('login__password').send_keys(self.password)
        self.driver.find_element_by_id('button-login').click()
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
