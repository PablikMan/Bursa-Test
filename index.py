class Index:
    list_of_details = []
    href = ""

    def __init__(self, list_of_details, href):
        count = 0
        for thing in list_of_details:
            if thing == 'DL' or thing == 'MM':
                continue
            else:
                self.list_of_details.append(thing)
                count += 1
        if count == 8:
            self.href = href

    def __repr__(self):
        count = 0
        string_list_of_details = ""
        for thing in self.list_of_details:
            string_list_of_details += thing + " "
            count += 1

        return string_list_of_details
