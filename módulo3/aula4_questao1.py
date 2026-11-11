
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2
if soma % 2 == 0:
    print(f"A soma é {soma}. O número é **par**.")
else:
    print(f"A soma é {soma}. O número é **ímpar**.")