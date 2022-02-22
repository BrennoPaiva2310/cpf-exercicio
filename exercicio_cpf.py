cpf = "168.995.350-09"
cpf2 = cpf.split('.')
cpf3 = ''.join(cpf2)
cpf4 = cpf3.split('-')
cpf5 = ''.join(cpf4)
cpf6 = cpf5[0:9]


interador = 10
acumulador1 = []
mult_acumulador = 0


for item in cpf6:
    conta = int(item) * interador
    print(f'{item} x {interador} = {conta}')

    acumulador1 += item
    mult_acumulador += conta
    interador -= 1


conta1 = 11 - (mult_acumulador % 11)
digito1 = ' '

if conta1 > 9:
    print('Maior que Zero\n')
    digito1 = 0
else:
    print('Menor que zero')
    print('Conta errada')


cpf6 = cpf5[0:10]
interador = 11
acumulador2 = []
mult_acumulador = 0

for item in cpf6:
    conta = int(item) * interador
    print(f'{item} x {interador} = {conta}')
    mult_acumulador += conta
    acumulador2 += item
    interador -= 1

conta2 = 11 - (mult_acumulador % 11)

digito2 = 9

conversao = ''.join(acumulador1)

novo_cpf = conversao + str(digito1) + str(digito2)


if novo_cpf == cpf5:
    print('\nCpf Valido')
else:
    print('\nCpf Invalido')


