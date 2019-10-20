import csv
import datetime
from MenuPrincipal import ListaDE
import hashlib
import json
from MenuPrincipal import ArbolAVL

indiceJson = ListaDE.ListaDE()


#x  listaSimple = ListaDE.ListaDE()
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

def guardarJson(cadenaJson):
    cadenaJson2 = json.loads(str(cadenaJson))
    indiceJson.insertar_final(cadenaJson, cadenaJson2["HASH"])
'''
def leerArchivoCSV(rutaArchivo):
    with open(rutaArchivo, 'r') as abrir:
        leer= csv.reader(abrir)
        archivo = list(leer)
    #abrir2 = open(rutaArchivo)
    #leer2= abrir2.read(abrir2)
    #archivo2= list(leer2)
    #print(archivo[0])
    #print(archivo[0][1])
    return generarData(archivo)'''


def encriptarHash(hashCodigo):
    aux = \
        hashlib.sha256(hashCodigo.encode()).hexdigest()
    return aux

def generarData(rutaArchivo):

    with open(rutaArchivo, 'r') as abrir:
        leer= csv.reader(abrir)
        archivo = list(leer)

    clase=archivo[0][1]
    data = archivo[1][1]
    fechaHora = datetime.datetime.now()
    #fechaHora.strftime('%m-%d-%y %H:%M:%S')
    #auxfechaHora="02-10-19-::14:30:25"
    #auxhashAnterior ="fd5f6d5fdfdf232Y232312QW12196255"
    indiceBloque = indiceJson.contarNodos()
    if indiceJson.listaEsNula():
        hashAnterior = '0000'
    else:
        hashAnterior= "\""+indiceJson.retornarUltimoNodo().valor2+"\""

    print(data.replace(" ","").replace("\n",""))
    objetoJson = json.dumps(str(data).replace(" ","").replace("\n",""))
    auxobj=str(objetoJson).replace("\\","")

    objetoJson2 = json.loads(str(data).replace(" ","").replace("\n",""))
    hashActual=  encriptarHash(str(indiceBloque) + str(fechaHora.strftime('%m-%d-%y-::%H:%M:%S')) + str(clase) + str(objetoJson2).replace("None", "null").replace(" ", "").replace("\'", '"') + str(hashAnterior))

    textoJson = "{\n" + '"INDEX": ' + "\""+str(indiceBloque)+"\"" + ",\n" + '"TIMESTAMP": ' + "\""+ str(fechaHora.strftime('%m-%d-%y-::%H:%M:%S'))+"\""+ ",\n"+'"CLASS": '+"\""+ str(clase)+"\""+",\n"+'"DATA": '+ str(data)+ ",\n"+'"PREVIUSHASH": '+"\""+ str(hashAnterior)+"\""+",\n"
    textoJson = textoJson + '"HASH": '+ "\""+str(hashActual)+"\"" + "\n}"
    #print(textoJson)
    #print(objetoJson)
    #print(auxobj)
    #print(str(objetoJson2).replace("None", "null").replace(" ", "").replace("\'", '"'))
    #print(str(2) + str(fechaHora) + str(clase) + str(objetoJson2).replace("\'", '"').replace("None", "null").replace(" ", "") + str(hashAnterior))
    return textoJson

def encontrarCarnets(cadenJson):
    #print("HOLAAAAAAA"+cadenJson)
    carnets = []
    json.loads(cadenJson, object_hook=encontrarNombre)
    #print(carnets)
    return carnets

def crearArbol(cadenaJson):
    jsonCadena = str(cadenaJson).replace("None", "null").replace("\'", '"')
    temp = encontrarCarnets(str(jsonCadena))
    print(temp)
    auxArbol = ArbolAVL.ArbolAVLOriginal()
    for i in temp:
        aux = str(i).split("-")
        auxArbol.insertar(aux[0], aux[1])
    auxArbol.graficarArbol()

def graficarInorden(cadenaJson):
    jsonCadena = str(cadenaJson).replace("None", "null").replace("\'", '"')
    temp = encontrarCarnets('value', str(jsonCadena))
    auxArbol = ArbolAVL.ArbolAVLOriginal()
    for iteracion in temp:
        aux = str(iteracion).split("-")
        auxArbol.insertar(aux[0], aux[1])
    auxArbol.graficarInorden()

def graficarPostOrden(cadenaJson):
    jsonCadena = str(cadenaJson).replace("\'", '"').replace("None", "null")
    temp = encontrarCarnets('value', str(jsonCadena))
    auxArbol = ArbolAVL.ArbolAVLOriginal()
    for iteracion in temp:
        aux = str(iteracion).split("-")
        auxArbol.insertar(aux[0], aux[1])
    auxArbol.graficarPostOrden()

def graficarPreOrden(cadenaJson):
    jsonCadena = str(cadenaJson).replace("\'", '"').replace("None", "null")
    temp = encontrarCarnets('value', str(jsonCadena))
    auxArbol = ArbolAVL.ArbolAVLOriginal()
    for iteracion in temp:
        aux = str(iteracion).split("-")
        auxArbol.insertar(aux[0], aux[1])
    auxArbol.graficarPreOrden()


def obtenerLista():
    return indiceJson
