#Dado o tamanho da base e da altura de um retângulo, crie um programa que calcula a sua área e o seu perímetro.

base = float(input("Digite o tamanho da base do retângulo: "))
altura = float(input("Digite o tamanho da altura do retângulo: "))

area = base * altura

perimetro = 2 * (base + altura)

print("A área do retângulo é:", area)
print("O perímetro do retângulo é:", perimetro)
