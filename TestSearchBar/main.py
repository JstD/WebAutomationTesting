import unittest
from unittest.main import main
from selenium import webdriver
import page
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchBar(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.vietnamworks.com/")
        self.driver.delete_all_cookies()

    ########## Start test #########
    '''
    def test_job_NV_IT(self):
        #TC-002-001 OK
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "Nhân viên IT"
        mainPage.click_go_button()
        time.sleep(3)
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_job_found("Nhân viên IT,Lập Trình,IT,Phần Mềm,Công Nghệ")
    '''

    def test_job_with_location(self):
        #TC-002-002 OK
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "Nhân viên IT"
        mainPage.click_go_button()
        time.sleep(3)
        mainPage.click_location_selection()  # HCM
        mainPage.click_go_button_after()
        time.sleep(3)
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_job_found(
            "Nhân viên IT,Lập Trình,IT,Công Nghệ")
        assert search_result_page.is_location_found("Hồ Chí Minh")

    def test_career_doctor_1(self):
        #TC-002-003 OK
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.click_go_button()
        time.sleep(3)
        mainPage.search_text_element_after = "Bác Sĩ"
        mainPage.click_go_button_after()
        time.sleep(3)
        mainPage.click_career_doctor()
        time.sleep(3)
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_career("Bác sĩ")

    #Web bị fail test này
    def test_career_doctor_2(self):
        #TC-002-004 OK
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "Bác Sĩ"
        mainPage.click_go_button()
        time.sleep(3)
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_career(
            "Bác sĩ,Bác SĨ,Y Khoa,Dược Phẩm,Bác Sỹ,Dược,Lâm Sàng,Medical,Dinh Dưỡng,Sức Khỏe")

    def test_job_NV_IT_NMS(self):
        #TC-002-005 OK
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "Nhân viên IT NMS"
        mainPage.click_go_button()
        time.sleep(3)
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_job_found("Nhân viên IT,Lập Trình,IT")
        assert search_result_page.is_company_found("NMS")

    def test_salary_1(self):
        #TC-002-006 OK
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.log_in_1()
        mainPage.log_in_2()
        time.sleep(3)
        mainPage.search_text_element = "Nhân viên IT"
        mainPage.click_go_button()
        time.sleep(3)
        mainPage.click_sal_select()  # 500-1000
        time.sleep(3)
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_job_found(
            "Nhân viên IT,Lập Trình,IT,Phần Mềm,Công Nghệ")
        mainPage.click_job_title()
        assert search_result_page.is_salary("$500 - $1000")

    def test_salary_2(self):
        #TC-002-007 OK
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.log_in_1()
        mainPage.log_in_2()
        time.sleep(3)
        mainPage.search_text_element = "Nhân viên IT 600"
        mainPage.click_go_button()
        time.sleep(3)
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_non_found()

    def test_job_position_NV(self):
        #TC-002-008 OK
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.click_go_button()
        time.sleep(3)
        mainPage.search_text_element_after = "Nhân viên IT"
        time.sleep(3)
        mainPage.click_go_button_after()
        time.sleep(3)
        mainPage.click_position_NV()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_job_position("Nhân viên")

    def test_job_welfare(self):
        #TC-002-009 OK
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "Nhân viên IT"
        mainPage.click_go_button()
        time.sleep(3)
        mainPage.click_welfare_selection()
        time.sleep(5)
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_welfare_found("Khám sức khỏe")

    def test_job_urgent(self):
        #TC-002-010 OK
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.click_go_button()
        time.sleep(3)
        mainPage.search_text_element_after = "Nhân viên IT"
        mainPage.click_check_box_urgent()
        mainPage.click_go_button_after()
        time.sleep(3)
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_urgent_found()

    #error
    def test_job_type_part_time(self):
        #TC-002-0011 OK
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "Nhân viên IT"
        time.sleep(0.3)
        mainPage.click_go_button()
        time.sleep(3)
        mainPage.click_part_time()
        time.sleep(1)
        mainPage.click_go_button_after()
        time.sleep(3)
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_non_found()
    '''
    #Web bị fail test này
    def test_without_job(self):
        #TC-002-0012 OK
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.click_go_button()
        time.sleep(3)
        mainPage.click_career_doctor()
        time.sleep(5)
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_job_found("Bác sĩ,Bác SĨ,Y Khoa,Dược Phẩm,Bác Sỹ,Dược,Lâm Sàng,Medical,Dinh Dưỡng,Sức Khỏe")

    def test_illegal_job(self):
        #TC-002-0013 OK
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "Bán Ma Túy"
        mainPage.click_go_button()
        time.sleep(3)
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_non_found()
    
    def test_nonsence(self):
        #TC-002-014 OK
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "đasadasdsad"
        mainPage.click_go_button()
        time.sleep(3)
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_non_found()
    
    def test_empty_search(self):
        #TC-002-015 OK
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.click_go_button()
        time.sleep(3)
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()
    '''
    ########## End test #########

    def tearDown(self):
        #pass
        #self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
