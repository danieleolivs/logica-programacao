#Escreva um programa em Python que solicite ao usuário um número e verifique se o número é positivo, negativo ou zero. O programa deve imprimir uma mensagem correspondente ao resultado obtido.

numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
