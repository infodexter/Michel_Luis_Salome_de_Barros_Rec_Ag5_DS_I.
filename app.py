# Programa de cáculo de consumo
# Autor: Michel Luís Salomé de Barros

nome_aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts: "))
horasDias = float(input("Digite o tempo médio de uso diário em horas:  "))

# Processamento
consumoMensal = (potencia * horasDias * 30)/1000

# Saída
print(f"\nAparelho: {nome_aparelho}")
print(f"Consumo estimando: {consumoMensal:.2f}")