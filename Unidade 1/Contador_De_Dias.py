#Você tem a missão de construir um contador de dias, em que o usuário informa o total de meses desejado e o programa irá retornar a quantidade de dias totais que existem nesses meses, considere que um mês tem 30 dias.

meses = float(input("Digite o total de meses desejado: "))
dias_totais = meses * 30
print(f"O total de dias em {meses} meses é: {dias_totais} dias")