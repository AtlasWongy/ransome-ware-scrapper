from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import pandas as pd
from data_object_map import DataMap
from ransomExx_scrape import scrape_ransomEXX
from quatumm_scrape import scrape_quatumm

binary = FirefoxBinary(r"C:\Users\atlas\Desktop\Tor Browser\Browser\firefox.exe")

driver = webdriver.Firefox(firefox_binary = binary, executable_path='C:\\Users\\atlas\Documents\\WebDriver\\geckodriver')

# Create the data dict object
map_for_data_frame_ransom_exx = DataMap()
map_for_data_frame_quatumm = DataMap()

# scrap from ransomEXX first
map_for_data_frame_1 = scrape_ransomEXX(driver, map_for_data_frame_ransom_exx)

# scrape from quatumm next
map_for_data_frame_2 = scrape_quatumm(driver, map_for_data_frame_quatumm)

# Change dict into pandas
pd.DataFrame(map_for_data_frame_1.data).to_csv('ransomEXX.csv', index=False)
pd.DataFrame(map_for_data_frame_2.data).to_csv('quantum.csv', index=False)


driver.quit()