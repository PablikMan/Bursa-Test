########################################## IMPORTS ############################################
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from index import Index

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

######################################################## FUNCTIONS ############################################################
def click_on_ta_125_link():
    print("Inside 'click_on_ta_125_link' function...\n")
    ta_125_link = driver.find_element(By.XPATH, "//*[@id=\"trades_panel1\"]/article/div[1]/top-indices/table/tbody/tr["
                                                "3]/td[1]/a")
    ta_125_link.click()
    print("Outside 'click_on_ta_125_link' function...\n")


def click_on_more_about_ta_125_button():
    print("Inside 'click_on_more_about_ta_125_button' function...\n")
    more_about_ta_125_button = driver.find_element(By.XPATH, "//*[@id=\"mainContent\"]/index-lobby/section["
                                                             "1]/div/div/section[2]/button")
    more_about_ta_125_button.click()
    print("Outside 'click_on_more_about_ta_125_button' function...\n")


def click_on_index_components():
    print("Inside 'click_on_index_components' function...\n")
    index_components = driver.find_element(By.XPATH, "//*[@id=\"more_madad_nav\"]/ul/li[1]/ul/li[4]/a")
    index_components.click()
    print("Outside 'click_on_index_components' function...\n")


def click_on_market_data():
    print("Inside 'click_on_market_data' function...\n")
    market_data_button = driver.find_element(By.XPATH, "//*[@id=\"mainContent\"]/index-lobby/index-composition/index"
                                                       "-weight/gridview-lib/div/div[2]/div/filter-data/div[1]/div["
                                                       "2]/div/div[1]/div/label[2]")
    market_data_button.click()
    print("Outside 'click_on_market_data' function...\n")


def click_on_turn_over_down():
    print("Inside 'click_on_turn_over_down' function...\n")
    turn_over_down_button = driver.find_element(By.XPATH, "//*[@id=\"mainContent\"]/index-lobby/index-composition"
                                                          "/index-market-data/gridview-lib/div/div[2]/div/div/div["
                                                          "2]/table/thead/tr[2]/td[6]/ul/li[2]/button")
    turn_over_down_button.click()
    print("Outside 'click_on_turn_over_down' function...\n")


def return_table_as_list():
    print("Inside 'return_table_as_list' funtion...\n")
    list_of_table_webelements = driver.find_elements(By.XPATH,
                                                     "//*[@id=\"mainContent\"]/index-lobby/index-composition/index"
                                                     "-market-data/gridview-lib/div/div[2]/div/div/div["
                                                     "2]/table/tbody/tr")
    list_of_classes = []
    for element in list_of_table_webelements:
        href = driver.find_element(By.CLASS_NAME, "item-name").get_attribute("href") # Gives back the href
        split_table_rows = element.text.split(" \n ") # Give back a list like: ['LEUMI\nLUMI IL0006046119 3,355 0.96% 143,922.44 EoD 3,323 3,366\nלינקים לפעולות שונות']
        remove_slash_n = []
        for thing in split_table_rows:
            remove_slash_n.append(thing.replace("\n", " ")) # Gives back a list like: ['LEUMI LUMI IL0006046119 3,355 0.96% 143,922.44 EoD 3,323 3,366 לינקים לפעולות שונות']
        some_what_sorted_list = []
        for thing in remove_slash_n:
            some_what_sorted_list.append(thing.split(" ")) # Gives back a list like: [['LEUMI', 'LUMI', 'IL0006046119', '3,355', '0.96%', '143,922.44', 'EoD', '3,323', '3,366', 'לינקים', 'לפעולות', 'שונות']]
        almost_sorted = []
        for thing1 in some_what_sorted_list:
            for thing2 in thing1:
                almost_sorted.append(thing2) # Gives back a list like: ['LEUMI', 'LUMI', 'IL0006046119', '3,355', '0.96%', '143,922.44', 'EoD', '3,323', '3,366']
        sorted_list = almost_sorted[:-3]
        if 'DL' in sorted_list:
            sorted_list.remove('DL') # In case there is a 'DL' inside the list, it removes it
        if 'MM' in sorted_list:
            sorted_list.remove('MM') # In case there is a 'MM' inside the list, it removes it

        list_of_classes.append(Index(sorted_list, href))

    print("Outside 'return_table_as_list' function...\n")


############################################################################################################################


if __name__ == '__main__':
    click_on_ta_125_link()
    click_on_more_about_ta_125_button()
    click_on_index_components()
    click_on_market_data()
    click_on_turn_over_down()
    return_table_as_list()
