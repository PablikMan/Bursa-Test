class Index:

    def create_file_and_append(self, text):
        file = open("shares_detail.txt", "a")
        file.write(text + "\n")
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

        self.create_file_and_append(string_list_of_details)
        print(string_list_of_details)
        print(href_link)
    # def __repr__(self):
    # count = 0
    # string_list_of_details = ""
    # for thing in self.list_of_details:
    # string_list_of_details += thing + " "
    # count += 1

    # return string_list_of_details
