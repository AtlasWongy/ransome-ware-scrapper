from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import pandas as pd
import requests

# Data Information
data = {
    'Company Title': [], 
    'Company Links': [], 
    'Company Description': [], 
    'Leak Published Date': [], 
    'Number of visits': [], 
    'Leak Size': [], 
}

binary = FirefoxBinary(r"C:\Users\atlas\Desktop\Tor Browser\Browser\firefox.exe")

driver = webdriver.Firefox(firefox_binary = binary, executable_path='C:\\Users\\atlas\Documents\\WebDriver\\geckodriver')

# Need to chain 3 times for 3 pages

for i in range(1, 4, 1):

    url = f"http://rnsm777cdsjrsdlbs4v5qoeppu3px6sb2igmh53jzrx7ipcrbjz5b2ad.onion/?page={i}"

    driver.get(url)

    entire_list_page_1 = driver.find_element_by_xpath("//div[@class='container py-4']")

    list_of_companies = entire_list_page_1.find_elements_by_class_name("col-md-10")

    for i in range(0, len(list_of_companies) - 1, 1):

        # Grab the company name
        data['Company Title'].append(list_of_companies[i].find_element_by_class_name("card-title").text)

        # Grab the description of the ransom
        data['Company Description'].append(list_of_companies[i].find_elements_by_class_name("card-text")[1].text)

        # Grab the company URL
        data['Company Links'].append(list_of_companies[i].find_elements_by_class_name("card-text")[0].text)

        # Process to grab the last information: Published Date, Number of Visits and Leak size
        string_of_information = list_of_companies[i].find_elements_by_class_name("card-text")[2].text.split(", ")

        # The published date
        data['Leak Published Date'].append(string_of_information[0])

        # Number of visits
        data['Number of visits'].append(string_of_information[1])

        # Leak Size
        data['Leak Size'].append(string_of_information[2])

# Change dict into pandas
pd.DataFrame(data).to_csv('ransom_list.csv', index=False)

driver.quit()
