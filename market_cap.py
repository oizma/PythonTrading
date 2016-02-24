import ystockquote
import stocktwits_stockfinder

#list = [' AMBA',
#' AEO',
#' CBK',
#' COO',
#' FNSR',
#' FIVE',
#' RALY',
#' SD',
#' SWHC',
#' ULTA',
#' ZUMZ']


list = stocktwits_stockfinder.list_of_stocks

for i in list:
    print i
    print ystockquote.get_market_cap(i)

