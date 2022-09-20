from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import pandas as pd
from data_object_map import DataMap
from ransomExx_scrape import scrape_ransomEXX
from quatumm_scrape import scrape_quatumm

binary = FirefoxBinary(r"C:\Users\atlas\Desktop\Tor Browser\Browser\firefox.exe")

driver = webdriver.Firefox(firefox_binary = binary, executable_path='C:\\Users\\atlas\Documents\\WebDriver\\geckodriver')

# Create the data dict object
map_for_data_frame = DataMap()

# # scrap from ransomEXX first
# map_for_data_frame = scrape_ransomEXX(driver, map_for_data_frame)

# scrape from quatumm next
map_for_data_frame = scrape_quatumm(driver, map_for_data_frame)

print(map_for_data_frame.data["Company Links"])

# Change dict into pandas
# pd.DataFrame(map_for_data_frame.data).to_csv('ransom_list.csv', index=False)

driver.quit()