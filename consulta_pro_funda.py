from bitcoinlib.wallets import Wallet

def listar_transacoes(nome_carteira):
    # Carrega a carteira existente pelo nome
    carteira = Wallet(name=nome_carteira)

    # Obtém o histórico de transações da carteira
    historico_transacoes = carteira.transactions()

    # Exibe as transações
    for transacao in historico_transacoes:
        print("ID da transação:", transacao['txid'])
        print("Tamanho:", transacao['size'])
        print("Taxa:", transacao['fee'])
        print("Versão:", transacao['version'])
        print("Locktime:", transacao['locktime'])
        print("Data e hora:", transacao['time'])
        print("Confirmações:", transacao['confirmations'])
        print("Hash do bloco:", transacao['blockhash'])
        print("Altura do bloco:", transacao['blockheight'])
        print("Inputs:")
        for entrada in transacao['inputs']:
            print("   Endereço:", entrada['address'])
            print("   Valor:", entrada['value'])
            print("   Script:", entrada['script'])
            print("   Índice:", entrada['index'])
            print("   TxID da transação anterior:", entrada['prev_txid'])
            print()
        print("Outputs:")
        for saida in transacao['outputs']:
            print("   Endereço:", saida['address'])
            print("   Valor:", saida['value'])
            print("   Script:", saida['script'])
            print("   Índice:", saida['index'])
            print()

if __name__ == "__main__":
    # Nome da carteira a ser consultada
    nome_carteira = 'sua_carteira'

    # Chama a função para listar as transações da carteira
    listar_transacoes(nome_carteira)
