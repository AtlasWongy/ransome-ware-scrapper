from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

timeout = 10

def scrape_quatumm(driver, data_map):

    

#    for i in range(1000, 5000):
#     driver.get('http://quantum445bh3gzuyilxdzs5xdepf3b7lkcupswvkryf3n7hgzpxebid.onion/' + str(i))
    url = "http://quantum445bh3gzuyilxdzs5xdepf3b7lkcupswvkryf3n7hgzpxebid.onion"

    driver.get(url)

    list_of_company_links = []

    # element = driver.find_element_by_css_selector("div[class='blog-post-content]>a")
    # cur_link = element.get_attribute("href")

    list_of_companies = driver.find_elements_by_class_name("blog-post")

    for i in range(0, len(list_of_companies) - 1, 1):

        list_of_company_links.append(list_of_companies[i].find_element_by_tag_name("a").get_attribute("href"))

    # print(list_of_company_links)
    # print(len(list_of_company_links))

    for link in list_of_company_links:

        driver.get(link)

        column_of_information = driver.find_elements_by_class_name("col-sm-9")

        # Get company name 
        data_map.data['Company Title'].append(column_of_information[0].text)

        # Company official link
        data_map.data['Company Links'].append(column_of_information[1].get_attribute("href"))

        # Get Company description
        data_map.data['Company Description'].append(driver.find_elements_by_class_name("col-md-4")[-1].text)

        # Published date
        data_map.data['Leak Published Date'].append(column_of_information[3].text)

        # Number of visits
        parent_div_for_visits = driver.find_element_by_class_name("blog-post-meta")
        number_of_visits = parent_div_for_visits.find_element_by_css_selector(".btn.btn-success").text.removesuffix(' visibility')
        data_map.data['Number of visits'].append(number_of_visits)

        # Leak Size
        data_map.data['Leak Size'].append(parent_div_for_visits.find_element_by_css_selector(".label.label-light.label-warning").text)

    return data_map