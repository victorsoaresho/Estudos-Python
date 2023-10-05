import requests
import pandas as pd
from io import StringIO

acao = input('Digite o simbolo da ação: ')
br = input('S - Sim\nN - Não\nEsta ação é brasileira?: ')

if (br == 'S'):
    chave_api = 'OWYAGTIWRHSLWD99'
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={acao}.SAO&apikey={chave_api}&datatype=csv'
    r = requests.get(url)
    #data = r.csv()
    tabela = pd.read_csv(StringIO(r.text))
    print(tabela)

else:
    chave_api = 'OWYAGTIWRHSLWD99'
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={acao}&apikey={chave_api}&datatype=csv'
    r = requests.get(url)
    #data = r.csv()
    tabela = pd.read_csv(StringIO(r.text))
    print(tabela)
            

