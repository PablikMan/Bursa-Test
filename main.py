########################################## IMPORTS ############################################
import datetime
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from index import Index

################################################################################################

######################################################## FUNCTIONS ############################################################
def setup():
    path = str(input("Please provide me with a path to your chrome driver:\n"))
    global driver
    os.environ['PATH'] += path
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(12)
    driver.get("https://www.tase.co.il/en")


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


def write_table_to_a_file():
    print("Inside 'write_table_to_a_file' function...\n")
    count = 0
    list_of_table_webelements = driver.find_elements(By.XPATH, "//*[@id=\"mainContent\"]/index-lobby/index-composition/index"
                                                     "-market-data/gridview-lib/div/div[2]/div/div/div["
                                                     "2]/table/tbody/tr")

    next_button = WebDriverWait(driver, 8).until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@id=\"pageS\"]/pagination-template/ul/li[8]/a")))

    text_from_web_element_sorted(list_of_table_webelements)

    # while count < 4:
        # time.sleep(3)
        # text_from_web_element_sorted(list_of_table_webelements)
        # next_button.click()
        # count += 1
    print("Outside 'write_table_to_a_file' function...\n")


def text_from_web_element_sorted(list_of_table_webelements):
    list_of_classes = []
    for element in list_of_table_webelements:
        href = element.find_element(By.CLASS_NAME, "item-name").get_attribute("href")
        split_table_rows = element.text.split(
            " \n ")  # Give back a list like: ['LEUMI\nLUMI IL0006046119 3,355 0.96% 143,922.44 EoD 3,323 3,366\nלינקים לפעולות שונות']
        remove_slash_n = []
        for thing in split_table_rows:
            remove_slash_n.append(thing.replace("\n", " "))  # Gives back a list like: ['LEUMI LUMI IL0006046119 3,355 0.96% 143,922.44 EoD 3,323 3,366 לינקים לפעולות שונות']
        some_what_sorted_list = []
        for thing in remove_slash_n:
            some_what_sorted_list.append(thing.split(" "))  # Gives back a list like: [['LEUMI', 'LUMI', 'IL0006046119', '3,355', '0.96%', '143,922.44', 'EoD', '3,323', '3,366', 'לינקים', 'לפעולות', 'שונות']]
        almost_sorted = []
        for thing1 in some_what_sorted_list:
            for thing2 in thing1:
                almost_sorted.append(thing2)  # Gives back a list like: ['LEUMI', 'LUMI', 'IL0006046119', '3,355', '0.96%', '143,922.44', 'EoD', '3,323', '3,366']
        sorted_list = almost_sorted[:-3]
        if 'DL' in sorted_list:
            sorted_list.remove('DL')  # In case there is a 'DL' inside the list, it removes it
        if 'MM' in sorted_list:
            sorted_list.remove('MM')  # In case there is a 'MM' inside the list, it removes it
        if 'C' in sorted_list:
            sorted_list.remove('C')
        list_of_classes.append(Index(sorted_list, href))


def get_into_share_link_and_take_screenshot():
    print("Inside 'get_into_share_link' function...\n")
    user_selection = int(input(
        "Please select from the following:\n(1) Enter the symbol for the company you would like to see.\n(2) Exit\n"))
    if user_selection == 1:
        while True:
            user_share = str(input("Please enter the symbol for your company share. For example: LEUMI --> LUMI\n")).upper()
            href_link = ""
            string_from_text = ""
            date = datetime.datetime.now()
            today_date = date.strftime("%d") + " " + date.strftime("%b") + " " + date.strftime("%Y")  # Gives back a date like: 07 Dec 2022
            file = open("shares_detail " + today_date + ".txt", "r")
            share_found = False
            for line in file:
                if user_share in line:
                    string_from_text = line.split(" ")
                    href_link = string_from_text[-2]  # Takes the link from the line
                    share_found = True
                    break
            if share_found:
                driver.execute_script("window.open('');")  # Opens a new tab in driver
                driver.switch_to.window(driver.window_handles[1])  # Switches to the new tab
                driver.get(str(href_link))
                driver.save_screenshot("share_image " + today_date + ".png")
            if not share_found:
                print("The symbol you have entered is wrong..")
                print("Please enter again.")
                continue
            to_continue = str(input("Would you like to enter another company symbol? (y/n):\n"))
            if to_continue == "n":
                break
            elif to_continue == "y":
                continue
            else:
                print("Not a valid input..")
                break
    elif user_selection != 2:
        print("Not a valid input..")
    print("Outside 'get_into_share_link' function...\n")

############################################################################################################################


if __name__ == '__main__':
    setup()
    click_on_ta_125_link()
    click_on_more_about_ta_125_button()
    click_on_index_components()
    click_on_market_data()
    click_on_turn_over_down()
    write_table_to_a_file()
    get_into_share_link_and_take_screenshot()
