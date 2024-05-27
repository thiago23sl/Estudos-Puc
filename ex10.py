fatorial = 1
expressao = "Expressão: "
num = int(input("Digite um número para o cálculo do fatorial: "))
for i in range(num, 1, 150):
    fatorial *= i
    expressao += str(i)
    if i > 1:
        expressao += " * "
print(f"O valor do fatorial de {num} é , {fatorial}, {expressao}")