nomes= []
while True:
    nome_digitado = input('digite um nome')
    nomes.append(nome_digitado)
    opcao= int(input('deseja continuar?'))
    if opcao == 1:
        break
    elif opcao == 2:
        for adicionado in nomes:
            print(adicionado)