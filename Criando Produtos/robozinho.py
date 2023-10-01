# Passo a passo do projeto
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time
import pandas 

#Entrar no Chrome

pyautogui.PAUSE = 0.4

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
pyautogui.moveTo(x=644, y=425)
pyautogui.click()
pyautogui.click()

#Acessar o site

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3.0)

pyautogui.moveTo(x=690, y=549)
pyautogui.click()

#Trabalhando com dados

tabela = pandas.read_csv("C:/Users/victo/OneDrive/Área de Trabalho/Python/Estudos-Python/Criando Produtos/produtos.csv")
print(tabela)

#Cadastrando Produtos


for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=653, y=294)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim

'''
Documentação: 
# Clicar                pyautogui.click 
# Escreve o texto       pyhttps://dlp.hashtagtreinamentos.com/python/intensivao/loginautogui.write
# Pressiona uma tecla   pyautogui.press
# Combinação de teclas  pyautogui.hotkey

Pegar a localização Mouse
time.sleep(5)
entrada = pyautogui.position()
print(entrada)

'''
