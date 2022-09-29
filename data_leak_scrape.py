
def scrape_data_leak(driver, data_map):

    url = "http://7ukmkdtyxdkdivtjad57klqnd3kdsmq6tp45rrsxqnu76zzv3jvitlqd.onion/"

    driver.get(url)

    entire_page = driver.find_elements_by_xpath("//div[@class='border border-warning card-body shadow-lg ']")

    # attempt_get_company_title = entire_page[1].find_element_by_tag_name("h4").text

    # print(f"The company name is {attempt_get_company_title}")

    for i in range(0, len(entire_page) - 1, 1):

        # Grab the company name
        data_map.data['Company Title'].append(entire_page[i].find_element_by_tag_name("h4").text)

        # Grab the description of the ransom
        data_map.data['Company Description'].append(entire_page[i].find_elements_by_class_name("card-text")[1].text)

        # Grab the company URL
        data_map.data['Company Links'].append(entire_page[i].find_elements_by_class_name("card-subtitle")[0].text)

        # The published date
        data_map.data['Leak Published Date'].append("")

        # Number of visits
        data_map.data['Number of visits'].append("")

        # Leak Size
        data_map.data['Leak Size'].append("")

    return data_map