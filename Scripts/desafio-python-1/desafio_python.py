#Lê o primeiro valor (salário) como float
valor_salario = float(input())

#Lê o segundo valor (benefícios) como float
valor_beneficios = float(input())

#Função útil para o calculo do imposto (baseado nas alíquotas).
def calcular_imposto(salario):
    if salario >= 0 and salario <= 1100:
        aliquota = 0.05
    elif salario >= 1100.01 and salario <= 2500.00:
        aliquota = 0.10
    else:
        aliquota = 0.15
    return aliquota * salario

#Cálculos:
valor_imposto = calcular_imposto(valor_salario)
saida = valor_salario - valor_imposto + valor_beneficios

#Imprime a saída formatada com 2 casas decimais usando f-string 
print(f"{saida:.2f}")
