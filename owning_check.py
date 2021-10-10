import json
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options  # for suppressing the browser

def nft_checker(address, collection_file):

    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(executable_path = r'../chromedriver',options=option)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(f'https://singular.rmrk.app/space/{address}')
    
    nft_collection = []
    try:
        pages = driver.find_element_by_class_name('css-1bsyzis')
        pagination = int(pages.text.split('/')[-1])
        for page in range(pagination):
            print(page)
            sleep(2)
            nfts_to_check = driver.find_elements_by_class_name('css-riqgpc')
            for nft in nfts_to_check:
                ref = nft.get_attribute('href').split('/')[-1]
                nft_collection += [ref]
            driver.find_element_by_xpath('//*[@id="collection-paginated-list"]/div[3]/div/button[2]').click()
            print('skipping page...')
    except:
        nfts_to_check = driver.find_elements_by_class_name('css-riqgpc')
        for nft in nfts_to_check:
            sleep(3)
            ref = nft.get_attribute('href').split('/')[-1]
            nft_collection += [ref]

    
    f = open(collection_file)
    data = json.load(f)
    dict_keys = data.keys()

    final_val = ''
    for k in dict_keys:
        if any(check in nft_collection for check in data[k]):
            final_val = 'True'
            break
        else:
            final_val = 'False'

    validation_dict = {'address': address, 
                        'presence': final_val
                        }
    
    return validation_dict
    


if __name__ == '__main__':
    data = nft_checker('D8DyKaVB6pJc86wGj6WkBckiE1waeFt4nx6NrcYsDCEuysQ', 'collection-scraper.json')
    print(data)