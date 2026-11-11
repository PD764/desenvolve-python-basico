try:
    ano = int(input("Digite um ano: "))
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("Bissexto")
    else:
        print("Não Bissexto")        
except ValueError:
    print("Por favor, digite apenas números inteiros válidos para o ano.")