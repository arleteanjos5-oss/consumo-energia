# Solicita os dados ao usuário
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potencia em watts (W):"))
horas_dia = float(input("Digite o tempo de uso diario (horas) :"))

# Cálculo do consumo mensal
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Valor da energia (R$ por kwh)
valor_kwh = 0.75

# Cálculo do custo
custo = consumo_mensal * valor_kwh

# Exibe os resultados
print("\n--- Resultado ---")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kwh/mês")
print(f"Custo estimado: R$ {custo:.2f}")
