import pandas as pd

# Arquivo Leo
with pd.HDFStore('svi_word_by_word_from_leo.h5') as hdf:
    keys_leo = hdf.keys()
# Arquivo Servidor
with pd.HDFStore('svi_word_by_word_up_to_129.h5') as hdf:
    keys_servidor = hdf.keys()
# Arquivo Guilherme
with pd.HDFStore('svi_word_by_word_gui.h5') as hdf:
    keys_gui = hdf.keys()

# carregar um ticker
key = keys_leo.pop(0)
svi = pd.read_hdf('svi_word_by_word_from_leo.h5', key)
# criar um dataframe novo
data = pd.DataFrame(index=svi.index, data=svi[key[1:]], columns=[key[1:]])
# para cada key
for key in keys_leo:
    ticker = key[1:]
    # verifica se ja existe
    if ticker in data.columns:
        pass
    else:
        # senao abre o arquivo, adiciona coluna
        svi = pd.read_hdf('svi_word_by_word_from_leo.h5', ticker)
        data[ticker] = svi[ticker]
for key in keys_servidor:
    ticker = key[1:]
    if ticker in data.columns:
        pass
    else:
        svi = pd.read_hdf('svi_word_by_word_up_to_129.h5', ticker)
        data[ticker] = svi[ticker]
for key in keys_gui:
    ticker = key[1:]
    if ticker in data.columns:
        pass
    else:
        svi = pd.read_hdf('svi_word_by_word_gui.h5', ticker)
        data[ticker] = svi[ticker]
# salvar o dataframe num csv
data.to_csv('svi_data.csv')
# salvar o dataframe num csv substituindo NaN por 0
data.to_csv('svi_data.csv', na_rep='0')

# gerar lista com todos os tickers que foram adicionados
added_tickers = set(data.columns.values)
# calcular diferenca entre todos os tickers e os adicionados
tickers = pd.read_csv('sp500_ticker.txt', header=None)
tickers = set(tickers.values.ravel())
# salvar a lista num .txt
remaining = tickers.difference(added_tickers)
pd.DataFrame(data=list(remaining)).to_csv(
    'need_to_get_svi_for_these_tickers.csv',
    index=False, header=None)
