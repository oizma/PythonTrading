from bs4 import BeautifulSoup
from urllib2 import urlopen
import re
import pandas as pd


def get_stocktwits_sentiment(url_ticker):

    url_start = 'http://stocktwits.com/symbol/'
    #url_finish = '?q=aa'
    url_ticker = url_ticker

    url = url_start + url_ticker

    soup = BeautifulSoup(urlopen(url)).prettify()

    p = re.compile('(?<=sentiment_data =)(.*)') # ?<= everything after sentiment_data
    parsed = p.findall(soup)
    parsed_string = ', '.join(parsed) # turns the list into a string

    #{"bullish":86.59,"bearish":13.41,"timestamp":"2015-02-12"}


    bearish_values = re.findall('(?<="bearish":)(.{5})(?=,)', parsed_string) # this will fail for all the values with only 4 chars
    bullish_values = re.findall('(?<="bullish":)(.{5})(?=,)', parsed_string)

    bearish_values = [float(i) for i in bearish_values]
    bullish_values = [float(i) for i in bullish_values]

    bearish_values = pd.Series(bearish_values, name = 'Bearish')
    bullish_values = pd.Series(bullish_values, name = 'bullish')


    return "bearish most recent", bearish_values[0], bearish_values.describe(), "bearish summary end", "bullish most recent", bullish_values[0], bullish_values.describe(), "bullish summary end"

