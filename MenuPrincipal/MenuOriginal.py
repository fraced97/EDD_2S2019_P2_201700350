from MenuPrincipal import ListaDE, LeerArchivo
import csv
import json
import hashlib



class MenuPractica:


    #def __init__(self):


    def menuPrincipal(self):

        '''print("")
        print("")
        print("")
        print("")
        print("-------------Practica 2 EDD-----------------")
        print(""" 
                        [1] INSERTAR BLOQUE
                        [2] SELECCIONAR BLOQUE
                        [3] REPORTES
                        [0] SALIR
                        """)
        condicion = -1
        condicion2 = True;
        while(condicion2):
            condicion = int(input("Escribe alguna opcion del menu: "))
            print(""" 
                                   [1] INSERTAR BLOQUE
                                   [2] SELECCIONAR BLOQUE
                                   [3] REPORTES
                                   [0] SALIR
                                   """)
            switcher = {

                1: "ENTRO EN INSERTAR BLOQUE",
                2: " ENTRO EN SELECCIONAR BLOQUE",
                3: "ENTRO EN REPORTES",
                0: self.salir(condicion2)

            }
            p = switcher.get(condicion, "Invalid month")
            print(p)'''

        condicion = -1
        while (condicion != 0):

            print(""" 
                [1] INSERTAR BLOQUE
                [2] SELECCIONAR BLOQUE
                [3] REPORTES
                [0] SALIR
                """)
            try:
                condicion = int(input("Escribe alguna opcion del menu: " ))
            except ValueError:
                print("--------------------------------")
                print("No has ingresado un numero Entero")
                print("--------------------------------")

            if condicion==1:
                archivo = input("INGRESA EL NOMBRE DEL ARCHIVO CSV: ")
                auxArchivo = LeerArchivo.leerArchivoCSV(archivo)
                jsonCorrecto(auxArchivo)
            elif condicion==2:
                print("entro en dos")
            elif condicion ==3:
                condicion2 = -1
                while (condicion2 != 0):

                    print(""" 
                                [1] Reporte BlockChain
                                [2] Reporte Arbol
                                [3] PreOrden
                                [4] Inorden
                                [5] PosOrden
                                [0] SALIR
                                """)
                    try:
                        condicion2 = int(input("Escribe alguna opcion del menu: "))
                    except ValueError:
                        print("--------------------------------")
                        print("No has ingresado un numero Entero")
                        print("--------------------------------")

                    if condicion2 == 1:
                        archivo = input("INGRESA EL NOMBRE DEL ARCHIVO CSV: ")
                        LeerArchivo.leerArchivoCSV(archivo)
                    elif condicion2 == 2:
                        print("entro en dos")
                    elif condicion2 == 3:

                    elif condicion2 == 4:

                    elif condicion2 == 5:

                    elif condicion2 == 6:

                    elif condicion2 == 0:
                        print("Entro en salir")
                    else:
                        print("--------------------------------")
                        print("Escriba un numero entre 1-3")
                        print("--------------------------------")
            elif condicion==0:
                print("Entro en salir")
            else:
                print("--------------------------------")
                print("Escriba un numero entre 1-3")
                print("--------------------------------")


def jsonCorrecto(cadenaJson):
    cadenaJson2 = str(cadenaJson).replace("\'", '"').replace("None", "null")
    listaAux = json.loads(str(cadenaJson2))

    hashAnterior = listaAux["PREVIUSHASH"]
    hashActual = listaAux["HASH"]
    clase = listaAux["CLASS"]
    indice = listaAux["INDEX"]
    fechaHora = listaAux["TIMESTAMP"]
    data = listaAux["DATA"]
    hashJson = encriptarHash(str(indice) + str(fechaHora) + str(clase) + str(data).replace("\'", '"').replace("None", "null").replace(" ","") + str(hashAnterior))
    if hashJson == hashActual:
        return "true"
    else:
        return "false"
def encriptarHash(hashCodigo):
    aux = \
        hashlib.sha256(hashCodigo.encode()).hexdigest()
    return aux

MenuPractica().menuPrincipal()
