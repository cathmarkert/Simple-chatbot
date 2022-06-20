import socket
import _thread
from _thread import start_new_thread
import sys

porta = 1234

try:
    #criando um socket do cliente do tipo tcp 
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error:
    print("Falha na criação do socket. Tente novamente!")
    sys.exit(1)

#buscando conectar o socket cliente
try:
    socket_cliente.connect(('localhost' , porta))
    print("Seja bem vindo!")

except socket.error:
    print("Erro ao se conectar com o servidor. Tente novamente!")
    sys.exit(1)

except socket.gaierror:
    print("Erro ao buscar conectar-se a esse endereço. Tente novamente!")
    sys.exit(1)

#armazenando o nome de usuário do cliente
username = input("Insira seu nome de usuário: \n")
print("Chat iniciado: ")

#enviando mensagem, em loop infinito
def enviar_mensagem(conexao):
    while True:
        mnsg = input()
        try:
            conexao.send((f'{username} enviou: {mnsg}').encode('utf-8'))

        except socket.error:
            print("Erro ao mandar a mensagem. Tente novamente!")

#recebendo a mensagem de outro cliente, em loop infinito
def receber_mensagem(conexao):
    while True:
        try:
            rec_mnsg = conexao.recv(2048)
            rec_mnsg = rec_mnsg.decode('utf-8')

            print(rec_mnsg)
        except socket.error:
            print("Erro ao receber a mensagem. Tente novamente!")

start_new_thread(enviar_mensagem, (socket_cliente, ))
start_new_thread(receber_mensagem, (socket_cliente, ))

while True:
    pass

socket_cliente.close()
print("Conexão fechada")