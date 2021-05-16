from selenium.webdriver.common.by import By

class MainPageLocaters(object):
    FIND_BUTTON = (By.XPATH,"//*[@id=\"centered-search-bar\"]/div[2]/div/div/div/div/div/div/div/form/a")

    FIND_BUTTON_AFTER = (By.CLASS_NAME,"btn-search")

    CHECK_BOX = (By.CLASS_NAME,"check-box")

    LOG_IN_BUTTON = (By.XPATH,"//*[@id=\"__next\"]/div[1]/div[2]/div[4]/div[1]/div")

    LOG_IN = (By.XPATH,"//*[@id=\"__next\"]/div[1]/div[2]/div[4]/div[2]/div[2]/a")

    JOB_INFO_WRAPPER = (By.CLASS_NAME,"job-info-wrapper")

    LOCATION = (By.CLASS_NAME,"location")

    JOB_TITLE = (By.CLASS_NAME,"job-title")

    NO_OF_JOB = (By.XPATH,"//*[@id=\"__next\"]/div[7]/div[2]/main/div/div/div[1]/div[2]/div/div/div[1]/span/h1/div[1]/span/strong")

    URGENT = (By.CLASS_NAME,"badge-icon")

    STYLE = (By.XPATH,"//*[@id=\"__next\"]/div[7]/div[2]/div[2]/div/div/div[1]/div[1]/span/div[2]/div[1]/div/div[2]/div[1]")
    
    PART_TIME = (By.XPATH,"//*[@id=\"__next\"]/div[7]/div[2]/div[2]/div/div/div[1]/div[1]/span/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[3]/div")

    PNV = (By.XPATH,"//*[@id=\"__next\"]/div[7]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/div[3]/div")

    POSITION_ACTIVE = (By.XPATH,"//*[@id=\"__next\"]/div[7]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/span[1]")

    CAREER_ACTIVE = (By.XPATH,"//*[@id=\"__next\"]/div[7]/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[1]/span[1]")

    CAREER_DOC = (By.XPATH,"//*[@id=\"__next\"]/div[7]/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div[2]/div[3]/div")

    LOCATION_SELECTION = (By.XPATH,"//*[@id=\"__next\"]/div[4]/div[2]/div/div[2]/div/div/div/div[1]/span[1]")

    LOCATION_HCM = (By.XPATH,"//*[@id=\"__next\"]/div[4]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div")

    COMPANY_NAME = (By.CLASS_NAME,"company-name")

    WELFARE_SELECTION = (By.XPATH,"//*[@id=\"__next\"]/div[7]/div[2]/div[2]/div/div/div[1]/div[1]/span/div[1]")

    KHAM_SUC_KHOE = (By.XPATH,"//*[@id=\"__next\"]/div[7]/div[2]/div[2]/div/div/div[1]/div[1]/span/div[2]/div[2]/div[2]/div[2]")

    WELFARE_LIST = (By.CLASS_NAME,"skill-tags")

    SALARY_SELECT = (By.XPATH,"//*[@id=\"__next\"]/div[7]/div[2]/div[2]/div/div/div[1]/div[1]/div[3]/div/div")

    SAL_500_1000 = (By.XPATH,"//*[@id=\"__next\"]/div[7]/div[2]/div[2]/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div[2]/div[3]/div")

class SearchResultsPageLocators(object):
    pass

