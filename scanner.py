import socket

alvo = input("Digite o site ou IP: ")

for porta in range(1, 1025):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.5)
    
    if cliente.connect_ex((alvo, porta)) == 0:
        print(f"Porta {porta} está aberta")
    
    cliente.close()
