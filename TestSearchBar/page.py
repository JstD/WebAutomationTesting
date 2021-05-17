from locator import *
from element import BasePageElement
from element import BasePageElementAfter


class SearchTextElement(BasePageElement):
    locator = "keyword"

class SearchTextElementAfter(BasePageElementAfter):
    locator = "main-search-bar"

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

class MainPage(BasePage):

    search_text_element = SearchTextElement()

    search_text_element_after = SearchTextElementAfter()

    def is_title_matches(self):
        return "VietnamWorks" in self.driver.title

    def click_go_button(self):
        element =  self.driver.find_element(*MainPageLocaters.FIND_BUTTON)
        element.click()

    def click_go_button_after(self):
        element =  self.driver.find_element(*MainPageLocaters.FIND_BUTTON_AFTER)
        element.click()

    def click_check_box_urgent(self):
        element =  self.driver.find_element(*MainPageLocaters.CHECK_BOX)
        self.driver.execute_script("arguments[0].click();", element)

    def click_part_time(self):
        element =  self.driver.find_element(*MainPageLocaters.WELFARE_SELECTION)
        element.click()
        element =  self.driver.find_element(*MainPageLocaters.STYLE)
        element.click()
        element =  self.driver.find_element(*MainPageLocaters.PART_TIME)
        element.click()

    def click_position_NV(self):
        element =  self.driver.find_element(*MainPageLocaters.POSITION_ACTIVE)
        element.click()
        element =  self.driver.find_element(*MainPageLocaters.PNV)
        element.click()

    def click_career_doctor(self):
        element =  self.driver.find_element(*MainPageLocaters.CAREER_ACTIVE)
        element.click()
        element =  self.driver.find_element(*MainPageLocaters.CAREER_DOC)
        element.click()

    def click_location_selection(self):
        element =  self.driver.find_element(*MainPageLocaters.LOCATION_SELECTION)
        element.click()
        element =  self.driver.find_element(*MainPageLocaters.LOCATION_HCM)
        element.click()

    def click_welfare_selection(self):
        element =  self.driver.find_element(*MainPageLocaters.WELFARE_SELECTION)
        element.click()
        element =  self.driver.find_element(*MainPageLocaters.KHAM_SUC_KHOE)
        element.click()
    
    def log_in_1(self):
        element =  self.driver.find_element(*MainPageLocaters.LOG_IN_BUTTON)
        element.click()
        element =  self.driver.find_element(*MainPageLocaters.LOG_IN)
        element.click()

    def log_in_2(self):
        self.driver.find_element_by_name("username").send_keys("xuanmai.k18@gmail.com")
        self.driver.find_element_by_name("password").send_keys("XM123456")
        self.driver.find_element_by_id("button-login").submit()

    def click_sal_select(self):
        element =  self.driver.find_element(*MainPageLocaters.SALARY_SELECT)
        element.click()
        element =  self.driver.find_element(*MainPageLocaters.SAL_500_1000)
        element.click()

    def click_job_title(self):
        element =  self.driver.find_element(*MainPageLocaters.JOB_TITLE)
        element.click()


class SearchResultPage(BasePage):

    def is_results_found(self):
        return "Hiện chưa có công việc nào theo tiêu chí bạn tìm" not in self.driver.page_source

    def is_non_found(self):
        return "Hiện chưa có công việc nào theo tiêu chí bạn tìm" in self.driver.page_source

    # def is_type_part_time(self):
    #     elements = self.driver.find_elements(*MainPageLocaters.JOB_INFO_WRAPPER)
    #     check = False
    #     for ele in elements:
    #         job = ele.find_element(*MainPageLocaters.JOB_TITLE)
    #         for word in value.split(","):
    #             if word in job.text:
    #                 check = True
    #                 break
    #     return check

    def is_location_found(self,value):
        elements = self.driver.find_elements(*MainPageLocaters.JOB_INFO_WRAPPER)
        check = True
        for ele in elements:
            location = ""
            locations = ele.find_elements(*MainPageLocaters.LOCATION)
            for loca in locations:
                location += loca.text
            #print(location)
            if value not in location:
                check = False
                break
        return check
    
    def is_job_found(self,value):
        elements = self.driver.find_elements(*MainPageLocaters.JOB_INFO_WRAPPER)
        check = False
        for ele in elements:
            check = False
            # job = ele.find_element(*MainPageLocaters.JOB_TITLE)
            # print(job.text)
            for word in value.split(","):
                if word in ele.get_attribute('innerHTML'):
                    check = True
                    break
            if check == False:
                return check
        return check

    def is_welfare_found(self,value):
        elements = self.driver.find_elements(*MainPageLocaters.JOB_INFO_WRAPPER)
        check = True
        for ele in elements:
            welfares = ele.find_element(*MainPageLocaters.WELFARE_LIST)
            if value not in welfares.get_attribute('innerHTML'):
                check = False
                break
        return check

    def is_company_found(self,value):
        elements = self.driver.find_elements(*MainPageLocaters.JOB_INFO_WRAPPER)
        check = False
        for ele in elements:
            comp = ele.find_element(*MainPageLocaters.COMPANY_NAME)
            for word in value.split(","):
                if word in comp.text:
                    check = True
                    break
        return check

    def is_urgent_found(self):
        urgents = self.driver.find_elements(*MainPageLocaters.URGENT)
        numjob = self.driver.find_element(*MainPageLocaters.NO_OF_JOB)
        if int(numjob.text) == len(urgents):
            check = True
        else:
            check = False
        return check

    def is_job_position(self,value):
        position = self.driver.find_element(*MainPageLocaters.POSITION_ACTIVE)
        print(position.text)
        if position.text == value:
            return True
        else:
            return False

    def is_career(self,value):
        career = self.driver.find_element(*MainPageLocaters.CAREER_ACTIVE)
        if career.text == value:
            return True
        else:
            return False

    def is_salary(self,value):
        page = self.driver.page_source
        if value in page or "Thương lượng" in page:
            return True
        else:
            return False