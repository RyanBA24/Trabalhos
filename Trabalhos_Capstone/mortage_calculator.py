# Entrada de dados

Valor_Imovel = float(input("Qual o valor do imóvel a ser financiado? "))
Taxas_Juros = float(input("Qual a taxa de juros anual? "))
Prazo_anos = int(input("Qual o prazo em anos para quita-lo? "))

Taxas_juros_mensal = (Taxas_Juros / 100) / 12
Total_parcelas = Prazo_anos * 12

Parcelas = Valor_Imovel * (Taxas_juros_mensal * (1 + Taxas_juros_mensal)** Total_parcelas)  / ((1 + Taxas_juros_mensal) ** Total_parcelas -1)

# Visualização 

print("Parcela mensal estimada: R$", round(Parcelas, 2))
print("Total pago ao final do financiamento: R$", round(Parcelas * Total_parcelas, 2))
print("Total de juros pagos: R$", round(Parcelas * Total_parcelas - Valor_Imovel, 2))