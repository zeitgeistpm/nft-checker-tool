import json
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options  # for suppressing the browser

def nft_checker(collections, json_name):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(executable_path = r'./chromedriver',options=option)
    driver.maximize_window()
    driver.implicitly_wait(10)

    nft_dict = {}
    for collection in collections:
        driver.get(f'https://singular.rmrk.app/collections/{collection}')

        nft_collection = []
        try:    
            pages = driver.find_element_by_class_name('css-1bsyzis')
            pagination = int(pages.text.split('/')[-1])
            print(f'This collection has a total of {pagination} pages')
            for page in range(pagination):
                actual_page = page+1
                print(f'Scraping page number {actual_page}')
                driver.get(f'https://singular.rmrk.app/collections/{collection}?page={actual_page}')
                sleep(1)
                nfts_to_check = driver.find_elements_by_class_name('css-riqgpc')
                for nft in nfts_to_check:
                    ref = nft.get_attribute('href').split('/')[-1]
                    nft_collection += [ref]
        except:
            nfts_to_check = driver.find_elements_by_class_name('css-riqgpc')
            for nft in nfts_to_check:
                sleep(1)
                ref = nft.get_attribute('href').split('/')[-1]
                nft_collection += [ref]
        
        nft_dict[collection] = nft_collection

    final_name = json_name.replace(' ', '-') + '.json'
    with open(final_name, 'w') as outfile:
        json.dump(nft_dict, outfile)
        
    # return nft_dict
    


if __name__ == '__main__':
    addresses = ['06ea5e9291a7e86837-CLOWN', 'a24dc6c55d4881fe4c-NB1GX', '1862b745080ba19a21-HENCHMEN']
    output = nft_checker(addresses, 'collection scraper')
    # print(output)
