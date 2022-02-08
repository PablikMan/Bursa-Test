import datetime

class Index:

    def create_file_and_append(self, text, link):
        date = datetime.datetime.now()
        title = "shares_detail " + date.strftime("%d") + " " + date.strftime("%b") + " " + date.strftime("%Y") + ".txt"
        file = open(title, "a")
        file.write(text + str(link) + " \n")
        file.close()

    def __init__(self, list_of_details, href):
        href_link = ""
        list_of_data = []
        # count = 0
        for thing in list_of_details:
            list_of_data.append(thing)
            # count += 1
        # if count == 9:
        href_link = href
        string_list_of_details = ""
        for thing in list_of_data:
            string_list_of_details += thing + " "

        self.create_file_and_append(string_list_of_details, href)
        # print(string_list_of_details)
        # print(href_link)

