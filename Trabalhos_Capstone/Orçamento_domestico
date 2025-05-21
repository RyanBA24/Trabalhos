from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class Orçamento_domestico:

    def __init__(self):
        self.receitas = []
        self.despesas = []
        self.recorrentes = []

    def adicionar_receita(self, valor, data, descricao):
        self.receitas.append({'valor': valor, 'data': data, 'descricao': descricao})
    
    def adicionar_despesas(self, valor, data, descricao):
        self.despesas.append({'valor': valor, 'data': data, 'descricao': descricao})

    def adicionar_recorrente(self, valor, tipo, data_inicio, data_fim, descricao):
        self.recorrentes.append({
            'valor': valor,
            'tipo': tipo,  # "receita" ou "despesa"
            'inicio': data_inicio,
            'fim': data_fim,
            'descricao': descricao
        })

    def calcular_fluxo(self, data_inicio, data_fim):
        total_receitas = 0
        total_despesas = 0

        for r in self.receitas:
            if data_inicio <= r['data'] <= data_fim:
                total_receitas += r['valor']
        
        for d in self.despesas:
            if data_inicio <= d['data'] <= data_fim:
                total_despesas += d['valor']

        for item in self.recorrentes:
            data_atual = item['inicio']
            while data_atual <= item['fim'] and data_atual <= data_fim:
                if data_atual >= data_inicio:
                    if item['tipo'] == 'receita'