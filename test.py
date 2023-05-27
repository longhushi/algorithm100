import pandas_datareader as web

start_date = '2020-01-01'
end_date = '2020-03-18'

data = web.data.DataReader('601318.ss','yahoo',start_date,end_date)
data.head()