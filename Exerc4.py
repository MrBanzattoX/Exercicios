#Cálculo de salário
print("Bemvindo !!")
print("Vamos calcular o seu salário ?")
valorhora = float(input("Entre com o valor do salário, por hora:"))
bruto = valorhora * 220
print("Calculando salário bruto...")
print("Calculando descontos...")
#imposto de renda de 11% ( 11% = 11/100 )
impostorenda = bruto * 0.11
# INSS de 8% ( 8% = 8/100 )
inss = bruto * 0.08
#Desconto do sindicato pelego 2,5% ( 2,5% = 2,5/100 )
sindicato = bruto * 0.025
print("Aplicando descontos...")
liquido = bruto - impostorenda - inss - sindicato
print("Seu salário bruto é                   : R$",round(bruto, 2))
print("Os descontos são:")
print("Imposto de renda retido na fonte, 11% : R$",round(impostorenda, 2))
print("INSS, 8%                              : R$",round(inss, 2))
print("Imposto sindical, 2,5%                : R$",round(sindicato, 2))
print("Liquido à receber                     : R$",round(liquido, 2))
#Comando round serve para arredeondar números, o primeiro é o número que se quer arrendondar,
# e o segundo a quantidade de casas decimais.
