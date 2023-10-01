num_str = input('Digite um número: ')
int_num = float(num_str)

try:
    print(num_str.isdigit())
    print(f'{int_num} * 2 é: {(int_num * 2):.5f}')

except:
    print('Isso não é um número')