salario = int(input('vamos calcular seu abono salarial por favor nos informe seu salario mensal '))
if salario<=5000:
    abono= (10/100)*salario
    print(f'seu abono salario é igual a {abono}')
else:
    abono= (15/100)*salario
    print(f'seu abono salario é igual a {abono}')
