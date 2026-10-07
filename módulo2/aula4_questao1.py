
# Lê o comprimento do terreno como um número inteiro
comprimento = int(input("Digite o comprimento: "))
# Lê a largura do terreno como um número inteiro
largura     = int(input("Digite a largura: "))
# Lê o preço do metro quadrado como um número de ponto flutuante
preco_m2    = float(input("Valor do m2: "))
# Calcula a área total do terreno em metros quadrados
area = comprimento * largura #m2
# Calcula o preço total do terreno multiplicando a área pelo preço do metro quadrado
preco_total = area * preco_m2
# Imprime o resultado formatado conforme o exemplo solicitado (com separador de milhar e duas casas decimais)
print(f"O terreno possui {area}m2 e custa R${preco_total:,.2f}")