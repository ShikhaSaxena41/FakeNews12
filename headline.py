from bs4 import BeautifulSoup as bs
import requests
import numpy as np
import os
import pandas as pd
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

def news_list_request(news_list, news_table_tr, tag):
    for news in news_table_tr:
        news_tag={}
        news_tag['ticker'] = tag.lower()
        temp = news.find('td').text.split()
        if len(temp) == 1:
            news_tag['time'] = temp[0]
            news_tag['date'] = temp2
        else:
            news_tag['date'] = temp[0]
            temp2 = temp[0]
            news_tag['time'] = temp[1]
        news_tag['description']=news.find('a').text
        news_list.append(news_tag)
    return news_list

def news_headline(tag_list, news_list):
    for tag in tag_list:
        url = 'https://finviz.com/quote.ashx?t='+tag
        news_request = requests.get(url, headers=headers).content
        news_content = bs(news_request, 'html.parser')
        news_table = news_content.find_all('table', attrs={'id':'news-table'})
        news_table_tr = news_table[0].find_all('tr')
        news_list = news_list_request(news_list,news_table_tr, tag)
    return news_list

def main():
    news_list=[]
    news_all_list = news_headline(['FB', 'TSLA'], news_list)
    news_df = pd.DataFrame(news_all_list)
    news_df.to_csv('news.csv')
    news_headlines=news_df[['description','time']]
    news_headlines.set_index('time', inplace=True)


    return news_headlines
