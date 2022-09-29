
def scrape_cuba(driver, data_map):

    url = [
        "http://cuba4ikm4jakjgmkezytyawtdgr2xymvy6nvzgw5cglswg3si76icnqd.onion/ginspectionservices/",
        "http://cuba4ikm4jakjgmkezytyawtdgr2xymvy6nvzgw5cglswg3si76icnqd.onion/skupstina/",
        "http://cuba4ikm4jakjgmkezytyawtdgr2xymvy6nvzgw5cglswg3si76icnqd.onion/site-technology/",
        "http://cuba4ikm4jakjgmkezytyawtdgr2xymvy6nvzgw5cglswg3si76icnqd.onion/stm-com-tw/",
        "http://cuba4ikm4jakjgmkezytyawtdgr2xymvy6nvzgw5cglswg3si76icnqd.onion/r1group/"
    ]

    for link in url:

        driver.get(link)

        # Company Title
        company_name = driver.find_element_by_class_name("page-h1").text
        data_map.data['Company Title'].append(company_name)

        information_container = driver.find_element_by_class_name("page-list-ul")
        list_of_information = information_container.find_elements_by_tag_name("p")

        # Company Description
        data_map.data['Company Description'].append(list_of_information[2].text)

        # Company URL
        data_map.data['Company Links'].append(list_of_information[1].text)

        # Published data
        data_map.data['Leak Published Date'].append(list_of_information[0].text)

        # Number of visits
        data_map.data['Number of visits'].append("")

        # Leak Size
        data_map.data['Leak Size'].append("")

    return data_map
        




    