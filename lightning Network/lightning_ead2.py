'''
Created on 24.09.2018

@author: rpickhardt

https://www.rene-pickhardt.de

License APCHE2

'''
import time

from lightning.lightning import LightningRpc
from matplotlib import pyplot as plt

# Define os caminhos para os nós lightning
rpc_path_node1 = "PATH_TO_FIRST/lightning-rpc"
rpc_path_node2 = "PATH_TO_SECOND/lightning-rpc"

if __name__ == '__main__':
    # Conecta aos nós lightning usando a Lightning API
    ln1 = LightningRpc(rpc_path_node1)
    ln2 = LightningRpc(rpc_path_node2)
    
    # Define o número de rodadas de pagamento
    rounds = 1000
    start = time.time()  # Marca o tempo inicial
    
    # Lista para armazenar os tempos de cada rodada de pagamento
    times = []
    
    # Loop sobre o número de rodadas de pagamento
    for i in range(rounds):
        s = time.time()  # Marca o tempo de início da rodada de pagamento
        
        # Cria uma fatura no nó 1 e paga no nó 2
        invoice = ln1.invoice(500000000, str(time.time()), "description")
        bolt11 = invoice["bolt11"]
        ln2.pay(bolt11)
        
        # Cria uma fatura no nó 2 e paga no nó 1
        invoice = ln2.invoice(500000000, str(time.time()), "description")
        bolt11 = invoice["bolt11"]
        ln1.pay(bolt11)
        
        e = time.time()  # Marca o tempo de término da rodada de pagamento
        times.append(e-s)  # Adiciona o tempo da rodada à lista de tempos
        print("\n\n\n\ncompleted pay round", i+1,
               "transfered BTC: {:4.2f}".format((i+1)*2*500000/100000000.),
               "tx per second: {:4.2f}".format((i+1)*2/(e-start)))
    
    end = time.time()  # Marca o tempo final
    diff = end-start  # Calcula a diferença de tempo total
    
    # Cria um histograma dos tempos de pagamento
    label = ["       pay API","sendpay API"]
    fig, ax = plt.subplots()
    plt.title("Times for complete round trip payments on the lightning network using two local c-lightning clients")
    plt.hist(times,40, label=label[0]+" - {:4.2f} payments per second".format(2*len(times)/sum(times)))
    ax.legend()
    plt.xlabel("seconds")
    plt.ylabel("frequency")
    ax.grid()
    fig.text(0.90, 0.75, 'by Rene Pickhardt https://www.rene-pickhardt.de',
         fontsize=15, color='gray',
         ha='right', va='bottom', alpha=0.5)
    plt.show()
    plt.close() 
    
    # Obtém os IDs dos nós
    node1_id = res = ln1.getinfo()["id"]
    node2_id = res = ln2.getinfo()["id"]
    
    # Obtém as rotas para os nós
    route_to_ln1 = ln2.getroute(node1_id, "500000000", 1, 10)["route"]
    route_to_ln2 = ln1.getroute(node2_id, "500000000", 1, 10)["route"]
    start = time.time()  # Marca o tempo inicial
    
    # Lista para armazenar os tempos de cada rodada de pagamento usando sendpay
    times2= []
    
    # Loop sobre o número de rodadas de pagamento usando sendpay
    for i in range(rounds):
        s = time.time()  # Marca o tempo de início da rodada de pagamento
        
        # Cria uma fatura no nó 1 e paga no nó 2 usando sendpay
        invoice = ln1.invoice(500000000, str(time.time()), "description")
        payment_hash = invoice["payment_hash"]        
        ln2.sendpay(route_to_ln1, payment_hash)
        
        # Cria uma fatura no nó 2 e paga no nó 1 usando sendpay
        invoice = ln2.invoice(500000000, str(time.time()), "description")
        payment_hash = invoice["payment_hash"]        
        ln1.sendpay(route_to_ln2, payment_hash)
        
        e = time.time()  # Marca o tempo de término da rodada de pagamento
        times2.append(e-s)  # Adiciona o tempo da rodada à lista de tempos
        print("\n\n\n\ncompleted sendpay round", i+1,
               "transfered BTC: {:4.2f}".format((i+1)*2*500000/100000000.),
               "tx per second: {:4.2f}".format((i+1)*2/(e-start)))
    
    end = time.time()  # Marca o tempo final
    print("pay api:",diff, 1000 // diff)
    print("sendpay api:", end-start, 1000// (end-start))
    
    # Cria um histograma dos tempos de pagamento usando pay e sendpay
    label = ["       pay API","sendpay API"]
    fig, ax = plt.subplots()
    plt.title("Times for complete round trip payments on the lightning network using two local c-lightning clients")
    plt.hist(times,40, label=label[0]+" - {:4.2f} payments per second".format(2*len(times)/sum(times)))
    plt.hist(times2,40, label=label[1]+" - {:4.2f} payments per second".format(2*len(times2)/sum(times2)))
    ax.legend()
    plt.xlabel("seconds")
    plt.ylabel("frequency")
    ax.grid()
    fig.text(0.90, 0.7, 'by Rene Pickhardt https://www.rene-pickhardt.de',
         fontsize=15, color='gray',
         ha='right', va='bottom', alpha=0.5)
    plt.show()
    plt.close() 
    
    # Cria um histograma dos 90-percentile dos tempos de pagamento usando pay e sendpay
    label = ["       pay API","sendpay API"]
    fig, ax = plt.subplots()
    plt.title("90-percentile of times for complete round trip payments on the lightning network using two local c-lightning clients")
    values = sorted(times)
    values = values[:int(rounds*0.9)]
    plt.hist(values,40, label=label[0]+" - {:4.2f} payments per second".format(2*len(values)/sum(values)))
    values = sorted(times2)
    values = values[:int(rounds*0.9)]
    plt.hist(values,40, label=label[1]+" - {:4.2f} payments per second".format(2*len(values)/sum(values)))
    ax.legend()
    plt.xlabel("seconds")
    plt.ylabel("frequency")
    ax.grid()
    fig.text(0.90, 0.7, 'by Rene Pickhardt https://www.rene-pickhardt.de',
         fontsize=15, color='gray',
         ha='right', va='bottom', alpha=0.5)
    plt.show()
    plt.close()
    
    # Imprime os tempos de pagamento
    print(times)
    print(times2)
