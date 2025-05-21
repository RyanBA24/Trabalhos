from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class OrcamentoDomestico:
    def __init__(self):
        self.receitas = []
        self.despesas = []
        self.recorrentes = []

    def adicionar_receita(self, valor, data, descricao):
        self.receitas.append({'valor': valor, 'data': data, 'descricao': descricao})

    
    def adicionar_despesa(self, valor, data, descricao):
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
            while data_atual <= item['fim'] <= data_fim:
                if data_atual >= data_inicio:
                    if item['tipo'] == 'receita':
                        total_receitas += item['valor']
                    elif item['tipo'] == 'despesa':
                        total_despesas += item['valor']
                data_atual += relativedelta(months=1)

        return total_receitas - total_despesas
    


    def exportar_para_google_sheets(self):
        # Define escopos
        scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
        ]

        creds = ServiceAccountCredentials.from_json_keyfile_name("caramel-era-460501-t3-140b194f4673.json", scope)
        client = gspread.authorize(creds)
        planilha = client.create("Orçamento Doméstico")
        planilha.share('ryan2ba4@gmail.com', perm_type='user', role='writer')
        # Adiciona abas e dados
        aba_receitas = planilha.add_worksheet(title="Receitas", rows="100", cols="20")
        aba_receitas.append_row(["Valor", "Data", "Descrição"])
        for r in self.receitas:
            aba_receitas.append_row([r["valor"], r["data"].strftime("%d-%m-%Y"), r["descricao"]])

        aba_despesas = planilha.add_worksheet(title="Despesas", rows="100", cols="20")
        aba_despesas.append_row(["Valor", "Data", "Descrição"])
        for d in self.despesas:
            aba_despesas.append_row([d["valor"], d["data"].strftime("%d-%m-%Y"), d["descricao"]])

        aba_recorrentes = planilha.add_worksheet(title="Recorrentes", rows="100", cols="20")
        aba_recorrentes.append_row(["Valor", "Tipo", "Início", "Fim", "Descrição"])
        for r in self.recorrentes:
            aba_recorrentes.append_row([
                r["valor"], r["tipo"],
                r["inicio"].strftime("%d-%m-%Y"),
                r["fim"].strftime("%d-%m-%Y"),
                r["descricao"]
            ])

        print("✅ Dados exportados com sucesso para o Google Sheets!")



    def menu(self):
        while True:
            print("1 - Adicionar Receita")
            print("2 - Adicionar Despesa")
            print("3 - Adicionar Custo Recorrente")
            print("4 - Calcular Fluxo entre duas datas")
            print("5 - Sair")
            print("6 - Exportar para Google Sheets")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                valor = float(input("Qual o valor da receita?"))
                data = datetime.strptime(input("Data (DD-MM-AAAA): "), "%d-%m-%Y")
                desc = input("Descrição: ")
                self.adicionar_receita(valor, data, desc)

            elif opcao == '2':
                valor = float(input("Valor da despesa: "))
                data = datetime.strptime(input("Data (DD-MM-AAAA): "), "%d-%m-%Y")
                desc = input("Descrição: ")
                self.adicionar_despesa(valor, data, desc)

            elif opcao == '3':
                valor = float(input("Valor: "))
                tipo = input("Tipo (receita/despesa): ").lower()
                inicio = datetime.strptime(input("Data início (DD-MM-AAAA): "), "%d-%m-%Y")
                fim = datetime.strptime(input("Data fim (DD-MM-AAAA): "), "%d-%m-%Y")
                desc = input("Descrição: ")
                self.adicionar_recorrente(valor, tipo, inicio, fim, desc)

            elif opcao == '4':
                inicio = datetime.strptime(input("Data início (DD-MM-AAAA): "), "%d-%m-%Y")
                fim = datetime.strptime(input("Data fim (DD-MM-AAAA): "), "%d-%m-%Y")
                fluxo = self.calcular_fluxo(inicio, fim)
                print(f"Fluxo líquido no período: R$ {fluxo:.2f}")
            
            elif opcao == '5':
                print("Encerrando")
                break

            elif opcao == '6':
                self.exportar_para_google_sheets()

            else:
                print("Opção inválida, tente novamente")
                continue





# Execução principal
if __name__ == "__main__":
    app = OrcamentoDomestico()
    app.menu()