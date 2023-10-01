nome = input('Digite seu nome: ')
idade = float(input('Digite sua idade: '))

if (nome.strip() != '' and idade is not None):
    nome_invertido = nome[::-1]
    possui_espacos = ' ' in nome
    num_letras = len(nome)
    primeira_letra = nome[0]
    ultima_letra = nome[-1]

    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome_invertido}')
    print(f'Seu nome contém ou não espaços: {"Sim" if possui_espacos else "Não"}')
    print(f'Seu nome tem {num_letras} letras!')
    print(f'A primeira letra do seu nome é: {primeira_letra}')
    print(f'A última letra do seu nome é: {ultima_letra}')
else:
    print('Desculpe, você deixou campos vazios!')
