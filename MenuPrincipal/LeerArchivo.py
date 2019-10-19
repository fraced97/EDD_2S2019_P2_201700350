import csv
import datetime
from MenuPrincipal import ListaDE
import hashlib
import json

indiceJson = ListaDE.ListaDE()

def leerArchivoCSV(rutaArchivo):
    with open(rutaArchivo, 'r') as abrir:
        leer= csv.reader(abrir)
        archivo = list(leer)
    print(archivo[0])
    print(archivo[0][1])
    generarData(archivo)

def encriptarHash(hashCodigo):
    aux = \
        hashlib.sha256(hashCodigo.encode()).hexdigest()
    return aux

def generarData(listaData:list):

    clase=listaData[0][1]
    data = listaData[1][1]
    fechaHora = datetime.datetime.now()
    #fechaHora.strftime('%m-%d-%y %H:%M:%S')
    #auxfechaHora="02-10-19-::14:30:25"
    #auxhashAnterior ="fd5f6d5fdfdf232Y232312QW12196255"
    indiceBloque = indiceJson.contarNodos()
    if indiceJson.listaEsNula():

        hashAnterior = '0000'
    else:
        hashAnterior= "\""+indiceJson.retornarUltimoNodo().valor2+"\""
    print(data)
    objetoJson = json.dumps(str(data).replace(" ","").replace("\n",""))
    auxobj=str(objetoJson).replace("\\","")

    objetoJson2 = json.loads(str(data))
    hashActual=  encriptarHash(str(indiceBloque) + str(fechaHora.strftime('%m-%d-%y-::%H:%M:%S')) + str(clase) + str(objetoJson2).replace("\'", '"').replace("None", "null").replace(" ", "") + str(hashAnterior))

    textoJson = "{\n" + '"INDEX": ' + "\""+str(indiceBloque)+"\"" + ",\n" + '"TIMESTAMP": ' + "\""+ str(fechaHora.strftime('%m-%d-%y-::%H:%M:%S'))+"\""+ ",\n"+'"CLASS": '+"\""+ str(clase)+"\""+",\n"+'"DATA": '+ str(data)+ ",\n"+'"PREVIUSHASH": '+"\""+ str(hashAnterior)+"\""+",\n"
    textoJson = textoJson + '"HASH": '+ "\""+str(hashActual)+"\"" + "\n}"
    print(textoJson)
    print(objetoJson)
    print(auxobj)
    print(str(objetoJson2).replace("\'", '"').replace("None", "null").replace(" ", ""))
    print(str(2) + str(auxfechaHora) + str(clase) + str(objetoJson2).replace("\'", '"').replace("None", "null").replace(" ", "") + str(auxhashAnterior))
    return textoJson