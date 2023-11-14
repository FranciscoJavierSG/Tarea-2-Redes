#!/usr/bin/python
# -*- coding: utf-8 -*-
# Programa Cliente

import socket
import sys

if len(sys.argv) != 3:
    print ("Agregar la IP del servidor y el puerto donde se ofrece el servicio.")
    sys.exit(0)

IP = sys.argv[1]
PUERTO = int(sys.argv[2])

print ("\nConectandose al servidor ", IP, " en el puerto ", PUERTO, " ...")

try:
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect((IP, PUERTO))
except:
    print ("No se puede conectar con el servidor.", IP, " en el puerto ", PUERTO)
    sys.exit(0)

print ("\nConectado!\n")
print("----------------------------------------------------")
print("      PROGRAMACION PARA CANALES NACIONALES")
print("----------------------------------------------------")
print("")
print(""" ESCRIBA EL CANAL QUE DESEA 

    1) c13                3) la_red         5) tvn
    2) chilevision        4) mega           6) finalizar(), para salir
    """)

try:
    while True:   
        mensaje = str(input(">> Yo:  "))
        socket_cliente.send(mensaje.encode("utf-8"))
        if mensaje == "finalizar()":
            break
        recibido = socket_cliente.recv(3000).decode('utf-8')
        print("")
        print ("Servidor >> \n" + recibido)
        
        
        if(recibido==IP+" envio: c13" or recibido==IP+" envio: mega" or recibido==IP+" envio: la_red" or 
        recibido==IP+" envio: tvn" or recibido==IP+" envio: chilevision"):
            
        
            print("")
            print(""" ESCRIBA EL DIA QUE DESEE

    1) lunes         3) miercoles        5) viernes         7) Domingo
    2) martes        4) jueves           6) sabado          8) finalizar(), para salir
    """)
        else:
            
            print("----------------------------------------------------")
            print("      PROGRAMACION PARA CANALES NACIONALES")
            print("----------------------------------------------------")
            print("")
            print(""" ESCRIBA EL CANAL QUE DESEA 

    1) c13                3) la_red         5) tvn
    2) chilevision        4) mega           6) finalizar(), para salir
    """)    

except socket.error:
    print ("Se perdio la conexion con el servidor.")
except KeyboardInterrupt:
    print ("\nSe interrunpio el cliente con un Control_C.")

finally:
    print ("Terminando conexion con el servidor ...")
    socket_cliente.close()
    print ("Conexion con el servidor terminado.")
