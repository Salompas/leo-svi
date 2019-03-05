from os import path

from dailydata import getDailyData
import pandas as pd

tickers_file = path.expanduser('./sp500_ticker.txt')
words = list(pd.read_csv(tickers_file, header=None).values.ravel())
words.reverse()

filename = 'svi_word_by_word'
folder = path.expanduser('./')
# Define results as a dictionary format
# In the loop, associate each ticker with its SVI with starting and end year
for word, i in zip(words[136:200], range(0, 813)[136:200]):
    print(f'Word number: {i}')
    svi_word = getDailyData(word, 2004, 2017, wait_time=2)
    svi_word.to_hdf(f'{folder}/{filename}.h5', word, mode='a')

# After going over all ticker, concatenate variables using only SVI scaled
# Then save as a .csv file in the same folder
results = pd.concat([pd.read_hdf(f'{folder}/{filename}.h5', word)[
                    word] for word in words], axis=1)
results.to_csv(f'{folder}/SVI.csv')
