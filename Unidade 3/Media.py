#Suponha que uma escola deseja automatizar o processo de avaliação dos alunos com base nas notas obtidas em três testes. Escreva um programa em Python que solicite ao usuário as notas dos três testes e calcule a média dessas notas. Em seguida, o programa deve determinar se o aluno foi aprovado, reprovado ou precisa de recuperação, baseando-se nas seguintes condições:

#Se a média for igual ou superior a 7, o aluno é considerado aprovado.
#Se a média for menor que 5, o aluno é considerado reprovado.
#Se a média estiver entre 5 e 7, o aluno precisa de recuperação.

#O programa deve imprimir uma mensagem correspondente ao resultado obtido.


nota_teste1 = float(input("Digite a nota do primeiro teste: "))
nota_teste2 = float(input("Digite a nota do segundo teste: "))
nota_teste3 = float(input("Digite a nota do terceiro teste: "))

media = (nota_teste1 + nota_teste2 + nota_teste3) / 3

if media >= 7:
    status = "Aprovado"
elif media < 5:
    status = "Reprovado"
else:
    status = "Recuperação"

print("Média:", media)
print("Status do aluno:", status)
