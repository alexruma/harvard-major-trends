from scraper_tools import *
from plotting_tools import *

concentration_urls_list = main_page_scrape()

concentration_list = []

for i in range(len(concentration_urls_list)):
    concentration_list.append(Concentration(concentration_urls_list[i]))

    print(i, concentration_list[i].name)


plot_multiple(concentration_list[7], concentration_list[11], concentration_list[23], concentration_list[14], concentration_list[17],  concentration_list[22], concentration_list[39], concentration_list[38], concentration_list[37])

#for item in concentration_list:
 #   print(item.enrollment_data)
