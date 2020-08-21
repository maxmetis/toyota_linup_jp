# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 14:22:45 2020

@author: Johnny Tsai
"""

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

url_car = 'https://toyota.jp/carlineup/?padid=tjptop_car-search_car-list'
url_biz = 'https://toyota.jp/carlineup/business/'

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.implicitly_wait(20)
driver.get(url=url_car)
html_source_car = driver.page_source
driver.quit()

soup_car = BeautifulSoup(html_source_car, 'lxml')
data_car = soup_car.select('div .cars_area__table')

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.implicitly_wait(20)
driver.get(url=url_biz)
html_source_biz = driver.page_source
driver.quit()

soup_biz = BeautifulSoup(html_source_biz, 'lxml')
data_biz = soup_biz.select('div .cars_area__table')

name =[]
price = []
engine = []
JC08 = []
WLTC = []
passengers = []
displacement = []
length = []
width = []
height = []
driving_method = []
capacity = []


for i in range(len(data_car)):
    name_ = data_car[i].find(class_='cars_area__table__cell type-name').text
    price_ = data_car[i].find(class_='cars_area__table__cell type-price').text
    engine_ = data_car[i].find(class_='cars_area__table__cell type-engine_type').text
    JC08_ = data_car[i].find(class_='cars_area__table__cell type-fuel').text
    WLTC_ = data_car[i].find(class_='cars_area__table__cell type-fuel02').text
    passengers_ = data_car[i].find(class_='cars_area__table__cell type-passengers').text
    displacement_ = data_car[i].find(class_='cars_area__table__cell type-displacement').text
    length_ = data_car[i].find(class_='cars_area__table__cell__inner type-body_size_length').text
    width_ = data_car[i].find(class_='cars_area__table__cell__inner type-body_size_width').text
    height_ = data_car[i].find(class_='cars_area__table__cell__inner type-body_size_height').text
    driving_method_ = data_car[i].find(class_='cars_area__table__cell type-driving_method').text
    
    name.append(name_)
    price.append(price_)
    engine.append(engine_)
    JC08.append(JC08_.replace('燃費*：',''))
    WLTC.append(WLTC_.replace('燃費*：',''))
    passengers.append(passengers_.replace('乗車人数：','').replace('名',''))
    displacement.append(displacement_.replace('排気量：',''))
    length.append(length_.replace('全長：','').replace('mm',''))
    width.append(width_.replace('全幅：','').replace('mm',''))
    height.append(height_.replace('全高：','').replace('mm',''))
    driving_method.append(driving_method_.replace('駆動方法：',''))
    capacity.append('none')

for i in range(len(data_biz)):
    name_ = data_biz[i].find(class_='cars_area__table__cell type-name').text
    price_ = data_biz[i].find(class_='cars_area__table__cell type-price').text
    engine_ = data_biz[i].find(class_='cars_area__table__cell type-engine_type').text
    JC08_ = data_biz[i].find(class_='cars_area__table__cell type-fuel').text
    WLTC_ = data_biz[i].find(class_='cars_area__table__cell type-fuel02').text
    passengers_ = data_biz[i].find(class_='cars_area__table__cell type-passengers').text
    displacement_ = data_biz[i].find(class_='cars_area__table__cell type-displacement').text
    length_ = data_biz[i].find(class_='cars_area__table__cell__inner type-body_size_length').text
    width_ = data_biz[i].find(class_='cars_area__table__cell__inner type-body_size_width').text
    height_ = data_biz[i].find(class_='cars_area__table__cell__inner type-body_size_height').text
    capacity_ = data_biz[i].find(class_='cars_area__table__cell type-capacity').text
        
    name.append(name_)
    price.append(price_)
    engine.append(engine_)
    JC08.append(JC08_.replace('燃費*：',''))
    WLTC.append(WLTC_.replace('燃費*：',''))
    passengers.append(passengers_.replace('乗車人数：','').replace('名',''))
    displacement.append(displacement_.replace('排気量：',''))
    length.append(length_.replace('全長：','').replace('mm',''))
    width.append(width_.replace('全幅：','').replace('mm',''))
    height.append(height_.replace('全高：','').replace('mm',''))
    capacity.append(capacity_)

linup = {
    'name':name,
    'price':price,
    'engine':engine,
    'fuel_consumption_JC08':JC08,
    'fuel_consumption_WLTC':WLTC,
    'passengers':passengers,
    'displacement':displacement,
    'length':length,
    'width':width,
    'height':height,
    'driving_method':driving_method,
    'capacity':capacity
}

df = pd.DataFrame(linup)
df.to_excel('/Users/ultsai/Desktop/temp/toyota_lineup.xlsx', 
    sheet_name='sheet1', index=None, header=True)


