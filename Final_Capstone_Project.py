import requests 
from bs4 import BeautifulSoup 
from requests.adapters import HTTPAdapter 
from urllib3.util.retry import Retry
import time
import pandas as pd

url = "https://www.citymall.com.mm/citymall/my/c/id05011"
current_url = url

base_domain = 'https://www.citymall.com.mm'


headers = { 
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " 
            "AppleWebKit/537.36 (KHTML, like Gecko) " 
            "Chrome/120.0.0.0 Safari/537.36", 
            "Accept-Encoding": "identity" 
            }

name_list = []
sale_price_list = []

def extract_name(i):
    name = i.find('a', class_='name')
    name = name.text
    name = ' '.join(name.split())
    return name

def extract_sale_price(i):
    
    old_sale_price = i.find('span', 'product-original-price')
    cur_sale_price = i.find('p', 'product-price mt-1')
    
    if old_sale_price:
        sale_price = old_sale_price.text
        sale_price = sale_price.replace('Ks', '')
        sale_price = sale_price.replace(',', '')
        sale_price = ' '.join(sale_price.split())
        sale_price = float(sale_price)
        #sale_price_list.append(sale_price)
    else :
        sale_price = cur_sale_price.text
        sale_price = sale_price.replace('Ks', '')
        sale_price = sale_price.replace(',', '')
        sale_price = ' '.join(sale_price.split())
        sale_price = float(sale_price)
        #sale_price_list.append(sale_price)
    
    return sale_price

session = requests.Session() 
retry = Retry( 
            total=5, 
            backoff_factor=1, 
            status_forcelist=[429, 500, 502, 503, 504] 
            )

session.mount("https://", HTTPAdapter(max_retries=retry))

count = 0

while True :
    count = count + 1
    response = session.get(current_url, headers=headers, timeout=30)

    print('Status ',response.status_code, count)

    soup = BeautifulSoup(response.text, "html5lib")

    main_tags = soup.find_all('div', class_= 'card-body')
    #print(main_tags)


    for i in main_tags:
        name = extract_name(i)
        name_list.append(name)
        #print(org_name)
        
        sale_price = extract_sale_price(i)
        sale_price_list.append(sale_price)
            
    time.sleep(2)
    
    next_page = soup.find('a', class_= 'page-link next')
    if next_page:
        next_link = next_page.get('href')
        if next_link == '#':
            break 
        current_url = base_domain + next_link
        #print(current_url)
    else:
        break
"""clean_name_list = []
clean_sale_price_list = []
    
for i in name_list:
    clean_name = ' '.join(i.split())
    clean_name_list.append(clean_name)
        
for i in sale_price_list:
    clean_sale_price = i.replace('Ks', '')
    clean_sale_price = clean_sale_price.replace(',', '')
    clean_sale_price = ' '.join(clean_sale_price.split())
    clean_sale_price = float(clean_sale_price)
    clean_sale_price_list.append(clean_sale_price)

print(clean_name_list)
print(clean_sale_price_list)"""
#print(sale_price_list)
#print(name_list)

dic = {'Product Name': name_list,
       'Product Prices': sale_price_list}

df = pd.DataFrame(dic)
df.to_excel("CityMall Products List.xlsx",index=False )
print("Completed")



