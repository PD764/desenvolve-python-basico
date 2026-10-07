
#4 - Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a menor quantidade possível de notas necessárias para pagar aquele valor. As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. A saída deve estar formatada exatamente como indicado.

#Entrada

#Saída

#576

#5 nota(s) de R$100,00

1# nota(s) de R$50,00

#1 nota(s) de R$20,00

#0 nota(s) de R$10,00

#1 nota(s) de R$5,00

#0 nota(s) de R$2,00

#1 nota(s) de R$1,00


valor = int(input("Digite o valor em reais: "))
print(valor)
notas = [100, 50, 20, 10, 5, 2, 1]
for nota in notas:
 quantidade = valor // nota
 valor = valor % nota
 print(f"{quantidade} nota(s) de R${nota},00")