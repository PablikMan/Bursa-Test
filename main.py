########################################## IMPORTS ############################################
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

################################################################################################

################################################ DRIVER SETUP #################################################
os.environ['PATH'] += r"C:/Users/פבליק/Desktop/SeleniumDrivers/ChromeDriver"
driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(10)
driver.set_page_load_timeout(12)
driver.get("https://www.tase.co.il/en")
#################################################################################################################

####################################################### ELEMENTS #######################################################
ta_125_link = driver.find_element(By.XPATH, "//*[@id=\"trades_panel1\"]/article/div[1]/top-indices/table/tbody/tr["
                                            "3]/td[1]/a")

more_about_ta_125_button = driver.find_element(By.XPATH, "//*[@id=\"mainContent\"]/index-lobby/section["
                                                         "1]/div/div/section[2]/button")

index_components = driver.find_element(By.XPATH, "//*[@id=\"more_madad_nav\"]/ul/li[1]/ul/li[4]/a")


############################################################################################################################

######################################################## FUNCTIONS ############################################################
def click_on_ta_125_link():
    ta_125_link.click()


def click_on_more_about_ta_125_button():
    more_about_ta_125_button.click()


def click_on_index_components():
    index_components.click()


############################################################################################################################333

if __name__ == '__main__':
    click_on_ta_125_link()
    click_on_more_about_ta_125_button()
    click_on_index_components()
