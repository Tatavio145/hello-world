num = float(input("Digite um número: "))
num1 = float(input("Digite outro número: "))
operação = input("Digite qual operação você quer fazer: +, -, / ou *: ")
if operação == "+":
    soma = num + num1
    print(f"O resultado da operação é {soma}")
elif operação == "-":
    soma = num - num1
    print(f"O resultado da operação é {soma}")
elif operação == "/":
    soma = num / num1
    print(f"O resultado da operação é {soma}")
elif operação == "*":
    soma = num * num1
    print(f"O resultado da operação é {soma}")
else:
    print("A operação é inválida")