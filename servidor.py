#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Programa Servidor

import socket
import sys
import os

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('0.0.0.1', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

if len(sys.argv) != 2:
    print ("Agregar el puerto donde se va a ofrecer el servicio desarrollado.")
    sys.exit(0)

IP = get_ip()  
PUERTO = int(sys.argv[1])

print ("\nServicio se va a configurar en el puerto: ", PUERTO, "en el servidor ", IP, "\n")

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlace del socket con la IP y el puerto
socket_servidor.bind((IP, PUERTO))

# Escuchar conexiones entrantes con el metodo listen,
# El parametro indica el numero de conexiones entrantes que vamos a aceptar
socket_servidor.listen(2)

print ("Servicio configurado en puerto ", PUERTO, "en el servidor ", IP, "\n")

try:
    while True:
        print ("Esperando conexión de un cliente ...")
        # Instanciar objeto socket_cliente para recibir datos,
        # direccion_cliente recibe la tupla de conexion: IP y puerto
        socket_cliente, direccion_cliente = socket_servidor.accept()
        print ("Cliente conectado desde: ", direccion_cliente)
        
        while True:
            try:
                recibido = socket_cliente.recv(1024).decode('utf-8')
                print (direccion_cliente[0] + " >> ", recibido)
                if recibido == "finalizar()":
                    print ("Cliente finalizo la conexion.")
                    print ("Cerrando la conexion con el cliente ...")
                    socket_cliente.close()
                    print ("Conexion con el cliente cerrado.")
                    break
                
                if recibido == "c13":       
                    respuesta_servidor = direccion_cliente[0] + " envio: " + recibido
                    socket_cliente.send(respuesta_servidor.encode("utf-8"))
                    
                    recibido = socket_cliente.recv(2048).decode('utf-8')
                    if recibido == "lunes":
                        
                        with open("ProgramacionTv/c13/" + "Lunes.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))

                    elif recibido == "martes":
                        
                        with open("ProgramacionTv/c13/" + "Martes.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    elif recibido == "miercoles":
                        
                        with open("ProgramacionTv/c13/" + "Miercoles.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    elif recibido == "jueves":
                        
                        with open("ProgramacionTv/c13/" + "Jueves.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    elif recibido == "viernes":
                        
                        with open("ProgramacionTv/c13/" + "Viernes.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    elif recibido == "sabado":
                        
                        with open("ProgramacionTv/c13/" + "Sabado.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    elif recibido == "domingo":
                        
                        with open("ProgramacionTv/c13/" + "Domingo.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    else :
                        respuesta_servidor = direccion_cliente[0] + " envio: Coloca un dia valido... volviendo"
                        
                        socket_cliente.send(respuesta_servidor.encode("utf-8")) 

                elif recibido == "chilevision":
                    
                    respuesta_servidor = direccion_cliente[0] + " envio: " + recibido
                    socket_cliente.send(respuesta_servidor.encode("utf-8"))
                    
                    recibido = socket_cliente.recv(2048).decode('utf-8')
                    if recibido == "lunes":
                        
                        with open("ProgramacionTv/chilevision/" + "Lunes.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))

                    elif recibido == "martes":
                        
                        with open("ProgramacionTv/chilevision/" + "Martes.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    elif recibido == "miercoles":
                        
                        with open("ProgramacionTv/chilevision/" + "Miercoles.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    elif recibido == "jueves":
                        
                        with open("ProgramacionTv/chilevision/" + "Jueves.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    elif recibido == "viernes":
                        
                        with open("ProgramacionTv/chilevision/" + "Viernes.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    elif recibido == "sabado":
                        
                        with open("ProgramacionTv/chilevision/" + "Sabado.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    elif recibido == "domingo":
                        
                        with open("ProgramacionTv/chilevision/" + "Domingo.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    else :
                        respuesta_servidor = direccion_cliente[0] + " envio: Coloca un dia valido... volviendo"
                        
                        socket_cliente.send(respuesta_servidor.encode("utf-8")) 


                elif recibido == "la_red":
                    
                    respuesta_servidor = direccion_cliente[0] + " envio: " + recibido
                    socket_cliente.send(respuesta_servidor.encode("utf-8"))
                    
                    recibido = socket_cliente.recv(2048).decode('utf-8')
                    if recibido == "lunes":
                        
                        with open("ProgramacionTv/la_red/" + "Lunes.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))

                    elif recibido == "martes":
                        
                        with open("ProgramacionTv/la_red/" + "Martes.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    elif recibido == "miercoles":
                        
                        with open("ProgramacionTv/la_red/" + "Miercoles.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    elif recibido == "jueves":
                        
                        with open("ProgramacionTv/la_red/" + "Jueves.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    elif recibido == "viernes":
                        
                        with open("ProgramacionTv/la_red/" + "Viernes.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    elif recibido == "sabado":
                        
                        with open("ProgramacionTv/la_red/" + "Sabado.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    elif recibido == "domingo":
                        
                        with open("ProgramacionTv/la_red/" + "Domingo.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    else :
                        respuesta_servidor = direccion_cliente[0] + " envio: Coloca un dia valido... volviendo"
                        
                        socket_cliente.send(respuesta_servidor.encode("utf-8")) 


                elif recibido == "mega":

                    respuesta_servidor = direccion_cliente[0] + " envio: " + recibido
                    socket_cliente.send(respuesta_servidor.encode("utf-8"))
                    
                    recibido = socket_cliente.recv(2048).decode('utf-8')
                    if recibido == "lunes":
                        
                        with open("ProgramacionTv/mega/" + "Lunes.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))

                    elif recibido == "martes":
                        
                        with open("ProgramacionTv/mega/" + "Martes.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    elif recibido == "miercoles":
                        
                        with open("ProgramacionTv/mega/" + "Miercoles.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    elif recibido == "jueves":
                        
                        with open("ProgramacionTv/mega/" + "Jueves.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    elif recibido == "viernes":
                        
                        with open("ProgramacionTv/mega/" + "Viernes.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    elif recibido == "sabado":
                        
                        with open("ProgramacionTv/mega/" + "Sabado.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    elif recibido == "domingo":
                        
                        with open("ProgramacionTv/mega/" + "Domingo.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    else :
                        respuesta_servidor = direccion_cliente[0] + " envio: Coloca un dia valido... volviendo"
                        
                        socket_cliente.send(respuesta_servidor.encode("utf-8")) 


                elif recibido == "tvn":     

                    respuesta_servidor = direccion_cliente[0] + " envio: " + recibido
                    socket_cliente.send(respuesta_servidor.encode("utf-8"))
                    
                    recibido = socket_cliente.recv(2048).decode('utf-8')
                    if recibido == "lunes":
                        
                        with open("ProgramacionTv/tvn/" + "Lunes.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))

                    elif recibido == "martes":
                        
                        with open("ProgramacionTv/tvn/" + "Martes.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    elif recibido == "miercoles":
                        
                        with open("ProgramacionTv/tvn/" + "Miercoles.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    elif recibido == "jueves":
                        
                        with open("ProgramacionTv/tvn/" + "Jueves.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    elif recibido == "viernes":
                        
                        with open("ProgramacionTv/tvn/" + "Viernes.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    elif recibido == "sabado":
                        
                        with open("ProgramacionTv/tvn/" + "Sabado.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    elif recibido == "domingo":
                        
                        with open("ProgramacionTv/tvn/" + "Domingo.txt",'r') as file:
                            data = file.read()
                            print (direccion_cliente[0] + " >> ", recibido)
                            socket_cliente.send(data.encode("utf-8"))
                    else :
                        respuesta_servidor = direccion_cliente[0] + " envio: Coloca un dia valido... volviendo"
                        
                        socket_cliente.send(respuesta_servidor.encode("utf-8")) 

                else:
                    respuesta_servidor = direccion_cliente[0] + " envio: Escribe un canal valido" 
                    socket_cliente.send(respuesta_servidor.encode("utf-8"))
                    recibido= None
                    respuesta_servidor=None
                
            except socket.error:
                print ("Conexion terminada abruptamente por el cliente.")
                print ("Cerrando conexion con el cliente ...")
                socket_cliente.close()
                print ("Conexion con el cliente cerrado.")
                break
            except KeyboardInterrupt:
                print ("\n∫Se interrunpio el cliente con un Control_C.")
                print ("Cerrando conexion con el cliente ...")
                socket_cliente.close()
                print ("Conexion con el cliente cerrado.")
                break

except KeyboardInterrupt:
    print ("\nSe interrumpio el servidor con un Control_C.")
    #socket_cliente.close()
    print ("Cerrando el servicio ...")
    socket_servidor.close()
    print ("Servicio cerrado, Adios!")