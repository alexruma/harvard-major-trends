import requests
from bs4 import BeautifulSoup

def main_page_scrape():
    """Scrapes Fields of Concentrations page and returns list of links to each concentration."""

    url = "https://handbook.fas.harvard.edu/book/fields-concentration"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # List that will hold url for all concentration pages.
    url_list = []

    # Select Sidebar UL element containing concentration page links.
    sidebar = soup.select("#boxes-box-os_booktoc > div > ul > li > ul > li.expanded.active-trail.active-trail.menu-depth-2.menu-item-97026 > ul")[0]
    sidebar_li_elements = sidebar.find_all("a")

    # Loop through list of <a> elements to extract urls.
    for elem in sidebar_li_elements:
        link = elem['href']
        url_list.append(link)

    return url_list

class Concentration:
    """Class creating objects representing individual concentrations.
    Initiated with url for concentration page."""

    def __init__(self, url):
        self.page = requests.get(url)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        self.year_list = []
        self.enrollment_list = []
        self.enrollment_data = self.get_enrollment_data()
        self.name = self.get_name()


    def get_name(self):
        """Scrapes page to return name of concentration."""
        title_element = self.soup.find(id = "page-title")
        return title_element.text.strip()

    def get_enrollment_data(self):
        """Scrape enrollment data and stores in dict."""
        data_table = self.soup.find_all("table")[-1]
        row_list = data_table.find_all("tr")

        # List containing <strong> elements containing years from first table row.
        year_list = row_list[0].find_all("strong")

        # List containing <div> elements containing enrollment numbers from second table row.
        enrollment_list = row_list[1].find_all("td")
        try:
            year_list.pop(0)
            enrollment_list.pop(0)
        except IndexError:
            print("empty list")

        # Transform list to just contain text elements
        for i in range(len(year_list)):
            year_list[i] = year_list[i].text.strip()

        # Transform list to just contain integers derived from text elements.
        for i in range(len(enrollment_list)):
            enrollment_list[i] = int(enrollment_list[i].text.strip())

        self.enrollment_list = enrollment_list
        self.year_list = year_list

        data_dict = {}
        for i in range(len(year_list)):
            data_dict[year_list[i]] = enrollment_list[i]

        return data_dict


#main_page_scrape()

test = Concentration("https://handbook.fas.harvard.edu/book/english")
test.get_enrollment_data()