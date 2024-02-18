#Escreva um programa em Python que calcule a energia cinética “Ec” de um objeto em movimento, dado sua massa m e sua velocidade v. Utilize a seguinte fórmula da física: 

#Ec = (m*v^2)/2 

#Onde: 

#m é a massa do objeto (em quilogramas) 
#v é a velocidade do objeto (em metros por segundo).

#O programa deve solicitar ao usuário a massa e a velocidade do objeto, calcular a energia cinética utilizando a fórmula dada e então imprimir o resultado.


massa = float(input("Digite a massa do objeto (em quilogramas): "))
velocidade = float(input("Digite a velocidade do objeto (em metros por segundo): "))
energia_cinetica = (massa * velocidade ** 2) / 2
print("A energia cinética do objeto é:", energia_cinetica, "joules")
