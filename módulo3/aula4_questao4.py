try:
    distancia = float(input("Digite a distância da entrega (em km): "))
    peso = float(input("Digite o peso do pacote (em kg): "))

    if distancia < 0 or peso < 0:
        print("A distância e o peso não podem ser negativos.")
    else:
        if distancia <= 100:
            preco_por_kg = 1.00
        elif distancia <= 300:
            preco_por_kg = 1.50
        else:
            preco_por_kg = 2.00
            frete = peso * preco_por_kg
        if peso > 10:
            frete += 10.00
        print(f"O valor total do frete é: R$ {frete:.2f}")

except ValueError:
    print("Por favor, digite apenas números válidos.")