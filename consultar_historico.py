from bitcoinlib.wallets import Wallet

def listar_transacoes(nome_carteira):
    # Carrega a carteira existente pelo nome
    carteira = Wallet(name=nome_carteira)

    # Obtém o histórico de transações da carteira
    historico_transacoes = carteira.transactions()

    # Exibe as transações
    for transacao in historico_transacoes:
        print("ID da transação:", transacao['txid'])
        print("Data e hora:", transacao['time'])
        print("Valor:", transacao['amount'])
        print("Endereço de origem:", transacao['addresses'][0])
        print("Endereço de destino:", transacao['addresses'][1])
        print("Confirmações:", transacao['confirmations'])
        print()

if __name__ == "__main__":
    # Nome da carteira a ser consultada
    nome_carteira = 'sua_carteira'

    # Chama a função para listar as transações da carteira
    listar_transacoes(nome_carteira)
