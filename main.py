from ofxparse import OfxParser

# Abrir o arquivo OFX
with open("extrato.ofx", "rb") as arquivo:
    ofx = OfxParser.parse(arquivo)

# Pegar todas as movimentacoes
transacoes = ofx.account.statement.transactions

# Iniciar os totais
entradas = 0.0
saidas = 0.0

print("========== EXTRATO BANCARIO ==========")

# Mostrar cada movimentacao
for t in transacoes:
    data = t.date.strftime("%d/%m/%Y")
    valor = float(t.amount)
    descricao = t.memo or "Sem descricao"

    print(f"Data      : {data}")
    print(f"Valor     : R$ {valor:.2f}")
    print(f"Descricao : {descricao}")
    print("--------------------------------------")

    if valor > 0:
        entradas += valor
    elif valor < 0:
        saidas += abs(valor)

# Calcular o resumo
quantidade = len(transacoes)
saldo = entradas - saidas

print("\n========== RESUMO ==========")
print(f"Quantidade de movimentacoes: {quantidade}")
print(f"Total de entradas: R$ {entradas:.2f}")
print(f"Total de saidas: R$ {saidas:.2f}")
print(f"Saldo calculado: R$ {saldo:.2f}")