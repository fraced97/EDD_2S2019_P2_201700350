import socket
import threading
import LeerArchivo
import  time


class Client:
    condicion2=""
   # LeerArchivo.leerArchivo()
    def __init__(self):
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cadenaJson = ""

        ipLocal = "192.168.1.11"

        from urllib.request import localhost
        Puerto = 8080
        self.cliente.connect((ipLocal, Puerto))
        hilo = threading.Thread(target=self.enviarYRecibirDatos)
        #start_new_thread(self.enviarYRecibirDatos,(self.cliente)
        hilo.start()

    contador = 0
    def enviarYRecibirDatos(self):
            try:
                print("hola")
                #time.sleep(3)

                if(self.cliente is not None):
                    datoRecibiryEnviar = self.cliente.recv(2048)
                    x = datoRecibiryEnviar.decode('utf-8')
                    if x:
                        print(x +"   LA DATA QUE PASA ANTES DEL IF")
                        if str(x) == "false":
                            print("ENTRO EN EL FALSE DE CLIENTE")
                        elif str(x) == "true":
                            LeerArchivo.leerArchivo().guardarJson(self.cadenaJson)
                            print("ENTRO EN EL TRUE DE CLIENTE")
                        else:

                            if (self.contador!=0):
                                self.cadenaJson = str(x)
                                condicion = str(LeerArchivo.leerArchivo().jsonCorrecto(str(self.cadenaJson)))
                                self.condicion2 = condicion
                                self.cliente.sendall(condicion.encode('utf-8'))
                                # self.cliente.sendall(condicion.encode('utf-8'))
                                print(condicion + "   ESTA ES LA CONDICION QUE MANDAMOS AL SERVIDOR")
                            self.contador=self.contador-1
                            #self.cliente.sendall(condicion.encode('utf-8'))
                            # self.cliente.sendall(condicion.encode('utf-8'))
                        print(str(x)+" IMPRIME LA DATA")
                self.enviarYRecibirDatos() #RECURSIVIDAD
            except Exception as e:
                print(e)
                #self.cliente.sendall(self.condicion2.encode('utf-8'))
