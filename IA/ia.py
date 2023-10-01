import pandas as pd
from sklearn.preprocessing import LabelEncoder as le
from sklearn.model_selection import train_test_split as tts
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

print('Rodando...')
print('Importando o banco de dados...')
#Importando o banco de dados e lendo
tabela = pd.read_csv("C:/Users/victo/OneDrive/Área de Trabalho/Python/Estudos-Python/IA/clientes.csv")
#print(tabela)

#Conferindo se a tabela possui algum campo vazio
#print(tabela.info())

#LabelEncoder
codificador = le()

tabela["profissao"] = codificador.fit_transform(tabela["profissao"])
tabela["mix_credito"] = codificador.fit_transform(tabela["mix_credito"])
tabela["comportamento_pagamento"] = codificador.fit_transform(tabela["comportamento_pagamento"])

print('Calculando x e y...')

#dados de x e y
y = tabela["score_credito"]
colunas = ["score_credito", "id_cliente"]

x = tabela.drop(columns=colunas)

#treino e teste
x_treino, x_teste, y_treino, y_teste = tts(x,y, test_size=0.3)

print('Gerando IA...')

#Criando IA
modelo_arvoredecisão = RandomForestClassifier()
modelo_knn = KNeighborsClassifier()

modelo_arvoredecisão.fit(x_treino, y_treino)
modelo_knn.fit(x_treino, y_treino)

#Teste previsões
previsao_arvoredecicao = modelo_arvoredecisão.predict(x_teste)
previsao_knnprevisao = modelo_knn.predict(x_teste.to_numpy())

print(accuracy_score(y_teste, previsao_arvoredecicao))
print(accuracy_score(y_teste, previsao_knnprevisao))

print('Calculando Accuracy...')

#Fazer novas previsões
novos_clientes = pd.read_csv("C:/Users/victo/OneDrive/Área de Trabalho/Python/Estudos-Python/IA/novos_clientes.csv")
novos_clientes["profissao"] = codificador.fit_transform(novos_clientes["profissao"])
novos_clientes["mix_credito"] = codificador.fit_transform(novos_clientes["mix_credito"])
novos_clientes["comportamento_pagamento"] = codificador.fit_transform(novos_clientes["comportamento_pagamento"])

print('Realizando Previsão...')

previsoes = modelo_arvoredecisão.predict(novos_clientes)
print(novos_clientes)
print(previsoes)
