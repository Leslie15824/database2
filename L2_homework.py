#汽车数据采集，使用selenium自动抓取
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time
def get_html():
    driver = webdriver.Chrome(executable_path = './chromedriver.exe')
    request_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-1.shtml'
    driver.get(request_url)
    time.sleep(1)
    html = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
    return html

def parse_table(content):
    #通过content创建BeautifulSoup对象
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    tr = soup.find('tr')
    th_list = tr.find_all('th') #找到所有表头信息，添加到columns中
    columns = []
    for th in th_list:
        columns.append(th.text)
    #创建一个空表，只有表头
    df = pd.DataFrame(columns = columns)
    #解析数据，添加到df空表中
    tbody = soup.find('tbody')
    #创建数据列表，找到所有的行信息
    tr_list = tbody.find_all('tr')
    #遍历所有的行，添加到表df中
    for tr in tr_list:
        #遍历每行的列数据信息
        td_list = tr.find_all('td')
        temp = {}#创建字典
        column_index = 0
        for td in td_list:
            temp[columns[column_index]] = td.text #text代表td里的存储信息
            column_index += 1
        #得到数据到df
        df = df.append(temp, ignore_index=True)
    return df

#得到HTML代码
content = get_html()
#从代码中解析table
df = parse_table(content)
print(df)
df.to_excel('汽车质量投诉.xlsx', index = False)
