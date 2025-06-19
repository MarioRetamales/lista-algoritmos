numeros = []
for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)
maior = max(numeros)
menor = min(numeros)
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
if numeros == int(input("Digite um número inteiro: ")):
    print(f"O número {numeros} é um inteiro.")
else:
    print(f"O número {numeros} não é um inteiro.")
    print("O número não é um inteiro.")
                                    
