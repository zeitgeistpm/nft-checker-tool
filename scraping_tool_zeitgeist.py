import pandas as pd
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options  # for suppressing the browser

def nft_checker(address, option):
    if option == 'user':
        driver.get(f'https://singular.rmrk.app/space/{address}')
    elif option == 'collection':
        driver.get(f'https://singular.rmrk.app/collections/{address}')

    nft_collection = []
    try:
        pages = driver.find_element_by_class_name('css-1bsyzis')
        pagination = int(pages.text.split('/')[-1])
        for page in range(pagination):
            print(page)
            sleep(2)
            nfts_to_check = driver.find_elements_by_class_name('css-riqgpc')
            for nft in nfts_to_check:
                ref = nft.get_attribute('href')
                nft_collection += [ref]
            driver.find_element_by_xpath('//*[@id="collection-paginated-list"]/div[3]/div/button[2]').click()
            print('skipping page...')
    except:
        nfts_to_check = driver.find_elements_by_class_name('css-riqgpc')
        for nft in nfts_to_check:
            sleep(3)
            ref = nft.get_attribute('href')
            nft_collection += [ref]
    
    return nft_collection
    


if __name__ == '__main__':
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(executable_path = r'./chromedriver',options=option)
    driver.maximize_window()
    driver.implicitly_wait(10)
    
    collection_list = list(pd.read_csv('collections.csv'))
    nft_collection_list = []
    for collection in collection_list:
        lista = nft_checker(collection, 'collection')


    owners_list = list(pd.read_csv('users.csv'))
    is_proper_owner = []
    not_proper_owner = []
    for owner in owners_list:
        temp = nft_checker(owner, 'user')

        out = any(check in temp for check in nft_collection_list)
        if out:
            is_proper_owner += [owner] 
        else :
            not_proper_owner += [owner]
    
    print('List of users that accomplish the condition: \n')
    print(is_proper_owner)
    print('----------------')
    print("List of users that DON'T accomplish the condition: \n")
    print(not_proper_owner)
