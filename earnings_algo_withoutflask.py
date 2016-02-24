import EarningsAlgorithm
import StringIO
from pandas import DataFrame as df
from TechnicalIndicators import get_and_proess_data
from stocktwits_run import get_stocktwits_sentiment

# input parameteres
urldata = {}

urldata['q'] = ticker = 'SPY'
urldata['x'] = 'NYSEARCA'
#urldata['x'] = 'NASDAQ'
urldata['i'] = 900
urldata['p'] = '15d' # number of past trading days
urldata['f'] = 'd,o,h,l,c,v' # requested data d is time, o is open, c is closing,



intradata = get_and_proess_data(urldata)

run_algo = EarningsAlgorithm.Algorithm()

train_file = df.from_csv("data/intradata_frompython_train.csv", index_col=False, header=0)

train_file_output = 'data/intradata_frompython_train_results.csv'

#  # get an instance of the class
run_algo.train_algo(train_file, train_file_output)

test_file = df.from_csv("data/intradata_frompython_test.csv", index_col=False, header=0)

test_file_output = 'data/intradata_frompython_test_results.csv'


agg_signals, past_5_signals, past_5_values, past_5_bayes = run_algo.test_algo(test_file, test_file_output)


print agg_signals

print str(past_5_values).strip('[]')
print "past 5 prices" + "\n"


print str(past_5_bayes).strip('[]')
print "past 5 bayesian scores" + "\n"


print str(past_5_signals).strip('[]')
print "past 5 buy sell signals" + "\n"



#twitter
urlticker = urldata['q']

print "stocktwits sentiments" + "\n"
print get_stocktwits_sentiment(urlticker)
