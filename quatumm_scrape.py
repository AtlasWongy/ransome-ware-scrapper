def scrape_quatumm(driver, data_map):

    url = "http://quantum445bh3gzuyilxdzs5xdepf3b7lkcupswvkryf3n7hgzpxebid.onion"

    driver.get(url)

    entire_list = driver.find_elements_by_class_name("col-sm-4")

    for i in range(0, len(entire_list) - 1, 1):

        companies_in_the_column = driver.find_elements_by_class_name("blog-post")

        for companies in companies_in_the_column:
            
            # Get the company title 
            data_map.data['Company Title'].append(companies.find_element_by_class_name("blog-post-title").text)

            # Get the company link
            company_links = companies.find_element_by_tag_name("a").get_attribute('href')
            company_links = company_links.split("/")[1] + company_links.split("/")[2]
            data_map.data['Company Links'].append(company_links.removesuffix('http://quantum445bh3gzuyilxdzs5xdepf3b7lkcupswvkryf3n7hgzpxebid.onion'))

    return data_map

