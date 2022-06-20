import socket
import _thread
from _thread import start_new_thread
import sys

#definindo o número da porta que será utilizada
porta = 1234

#Criando o socket do tipo TCP
try:
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error:
    #Printando caso haja falha na criação do socket
    print("Falha na criação do socket")
    sys.exit(1)


#tentando realizar a conexão entre o servidor e a porta especificada.
try:
    socket_server.bind(('localhost', porta))
    print("Servidor conectado! Seja bem vindo! \n")

except socket.error:
    print("Falha na ligação entre o socket e a porta selecionada. Tente novamente." )
    sys.exit(1)

#criando um array para armazenar todos os clientes que entrarão no servidor
clientes = []

#começando a buscar conexões de clientes no servidor.
socket_server.listen()

#função para enviar mensagens no servidor, em loop infinito.
def cliente(conexao):
    while True:
        try:
            #armazenando a variável mensagem
            mnsg = conexao.recv(2048)

        except socket.error:
            print("Não foi possível receber a mensagem, tente novamente!")
            break

        if not mnsg:
            break
        
        #enviando mensagem para outros clientes
        for cliente in clientes:
            if cliente != conexao:
                try:
                    cliente.send(mnsg)

                except socket.error:
                    print("Não foi possível receber a mensagem, tente novamente!")

    #fechando a conexão após o cliente enviar a mensagem
    conexao.close()

#rodando o servidor, loop infinito
while True:
    try:
        conex_socket, end = socket_server.accept()
        print("Conexão iniciada com: " + end[0] + ':' + str(end[1]))

        start_new_thread(cliente, (conex_socket, ))

        clientes.append(conex_socket)
    except socket.error:
        print("Erro ao estabelecer conexão, tente novamente!")

conex_socket.close()