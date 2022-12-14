import socket
import threading
host = "0.0.0.0"
port = 9990

#Creating functions for sending and receiving data
def Receive(client):
    while True :
        request = client_socket.recv(400)      #also work with request = client.recv(400)
        print('Received {}'.format(request.decode('utf-8')))
        if not request : #if client sending is empty
            print('Closing connection')
            break

def Sending(client):
    while True:
        msg = input("->")
        client_socket.send(msg.encode('utf-8'))


#Socket creation
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)
print(f'Listening on {host}:{port}')
client_socket, address = server.accept()
print(f'Connection {address[0]}:{address[1]}')


receiveTh = threading.Thread(target=Receive,args=(client_socket,))
sendTh = threading.Thread(target=Sending,args=(client_socket,))
receiveTh.start()
sendTh.start()

receiveTh.join()    #do not execute following instructions if receiveTh not done, here if
                    #did not break 
    
   

client_socket.close()
server.close()

