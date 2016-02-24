from bs4 import BeautifulSoup
from urllib2 import urlopen
import re
import pandas as pd
from stocktwits_run import get_stocktwits_sentiment
from pandas import DataFrame as df

stocktwits_url = "http://stocktwits.com/"

soup = BeautifulSoup(urlopen(stocktwits_url)).prettify()

# get trending stocks
list_of_stocks = re.compile('(?<=data-symbol=")(.\w+)').findall(soup)
#list_of_stocks = [u'VSLR', u'PEIX']



#stock_sentiment_db = df(columns=[list_of_stocks], index=range(18))


for stock in list_of_stocks:
    try:
        print stock
        print get_stocktwits_sentiment(stock)
    except:
        pass