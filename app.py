from scraper_tools import *
from plotting_tools import *

concentration_urls_list = main_page_scrape()

concentration_list = []

for i in range(len(concentration_urls_list)):
    concentration_list.append(Concentration(concentration_urls_list[i]))


plot_multiple(concentration_list[8], concentration_list[9], concentration_list[18])

#for item in concentration_list:
 #   print(item.enrollment_data)
