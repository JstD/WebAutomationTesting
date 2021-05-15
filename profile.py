import unittest
from selenium import webdriver
import time
# from selenium.webdriver.common.by import By

"""
This test use normal login case.
"""
class ApplyJobAndProfileTesting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/home/jstd/Desktop/Source/software_testing/chromedriver')
        self.driver.get('https://www.vietnamworks.com/')

    def test_apply_job_without_login(self):
        inp = self.driver.find_element_by_id('search-bar-input')
        inp.send_keys('IT')
        self.driver.find_element_by_class_name('searchBar__button').click()
        self.driver.find_element_by_class_name('job-item').click()
        self.driver.find_element_by_link_text('Nộp đơn').click()
        time.sleep(5)
        assert True
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
