import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

import time
import random

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

        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://www.vietnamworks.com/')
        self.driver.set_window_size(1600,1000)
        self.driver.delete_all_cookies()

    def test_apply_job_without_login(self):
        inp = self.driver.find_element_by_id('search-bar-input')
        inp.send_keys('IT')
        self.driver.find_element_by_class_name('searchBar__button').click()
        link = self.driver.find_element_by_class_name('job-item').find_element_by_tag_name('a').get_attribute('href')
        self.driver.get(link)
        lstBtn = self.driver.find_elements_by_class_name('btn-apply')
        for x in lstBtn:
            try:
                x.click()
                break
            except:
                pass
        assert self.driver.title == 'VietnamWorks Account' #Login requirement!!!
    
    def test_apply_job_without_login_random_item(self):
        inp = self.driver.find_element_by_id('search-bar-input')
        inp.send_keys('Luật')
        self.driver.find_element_by_class_name('searchBar__button').click()
        link = self.driver.find_elements_by_class_name('job-item')[random.randint(0,10)].find_element_by_tag_name('a').get_attribute('href')
        self.driver.get(link)
        lstBtn = self.driver.find_elements_by_class_name('btn-apply')
        for x in lstBtn:
            try:
                x.click()
                break
            except:
                pass
        assert self.driver.title == 'VietnamWorks Account' #Login requirement!!!
        
    def test_apply_job_with_new_account(self):
        '''
        Login with VNworks account
        '''
        login = self.driver.find_element_by_class_name('login')
        self.driver.get(login.find_element_by_tag_name('a').get_attribute('href'))
        self.driver.find_element_by_id('email').send_keys(self.username)
        self.driver.find_element_by_id('login__password').send_keys(self.password)
        self.driver.find_element_by_id('button-login').click()


        inp = self.driver.find_element_by_id('search-bar-input')
        inp.send_keys('IT')
        self.driver.find_element_by_class_name('searchBar__button').click()
        job_item = self.driver.find_element_by_class_name('job-item')
        
        self.driver.get(job_item.find_element_by_tag_name('a').get_attribute('href'))
        self.driver.switch_to.window(self.driver.window_handles[-1]) # switch to newest tab
        btn_apply = self.driver.find_elements_by_class_name('btn-apply')
        for x in btn_apply:
            try:
                x.click()
                break
            except:
                pass
        try:
            self.driver.find_element_by_id('applySendProcessBtn').click()
            assert False
        except:
            assert True
    def test_wrong_cvs(self):
        '''
        Login with VNworks account
        '''
        login = self.driver.find_element_by_class_name('login')
        self.driver.get(login.find_element_by_tag_name('a').get_attribute('href'))
        self.driver.find_element_by_id('email').send_keys(self.username)
        self.driver.find_element_by_id('login__password').send_keys(self.password)
        self.driver.find_element_by_id('button-login').click()
        time.sleep(1)
        self.driver.get(self.driver.find_elements_by_class_name('dropdownItem')[0].get_attribute('href'))
        time.sleep(1)
        self.driver.find_element_by_class_name('update-btn').click()
        time.sleep(1.5)
        self.driver.find_elements_by_class_name('ActionButton_button__J0r81')[1].click()
        time.sleep(1)
        self.driver.find_elements_by_class_name('class-input-recommend')[1].send_keys('00000000')
        self.driver.find_elements_by_class_name('class-input-recommend')[2].send_keys('10/04/2021')
        self.driver.find_elements_by_class_name('class-input-recommend')[3].send_keys('Thủ Đức')
        try:
            self.driver.find_elements_by_class_name('btn-md')[2].click()
            assert False
        except:
            assert True
    def test_cancel_cvs(self):
        '''
        Login with VNworks account
        '''
        login = self.driver.find_element_by_class_name('login')
        self.driver.get(login.find_element_by_tag_name('a').get_attribute('href'))
        self.driver.find_element_by_id('email').send_keys(self.username)
        self.driver.find_element_by_id('login__password').send_keys(self.password)
        self.driver.find_element_by_id('button-login').click()
        time.sleep(1)
        self.driver.get(self.driver.find_elements_by_class_name('dropdownItem')[0].get_attribute('href'))
        time.sleep(1)
        self.driver.find_element_by_class_name('update-btn').click()
        time.sleep(1.5)
        self.driver.find_elements_by_class_name('ActionButton_button__J0r81')[1].click()
        time.sleep(1)
        self.driver.find_elements_by_class_name('class-input-recommend')[1].send_keys('00000000')
        self.driver.find_elements_by_class_name('class-input-recommend')[2].send_keys('10/04/2021')
        self.driver.find_elements_by_class_name('class-input-recommend')[3].send_keys('Thủ Đức')
        try:
            self.driver.find_elements_by_class_name('btn-md')[1].click()
            assert True
        except:
            assert False
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
