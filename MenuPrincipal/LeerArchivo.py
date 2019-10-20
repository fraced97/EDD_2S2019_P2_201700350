import csv
import datetime
from MenuPrincipal import ListaDE
import hashlib
import json
from MenuPrincipal import ArbolAVL

indiceJson = ListaDE.ListaDE()
#x  listaSimple = ListaDE.ListaDE()
def guardarJson(cadenaJson):
    cadenaJson2 = json.loads(str(cadenaJson))
    if len(cadenaJson) > 1:
        indiceJson.insertar_final(cadenaJson, cadenaJson2["HASH"])

def leerArchivoCSV(rutaArchivo):
    with open(rutaArchivo, 'r') as abrir:
        leer= csv.reader(abrir)
        archivo = list(leer)
    #print(archivo[0])
    #print(archivo[0][1])
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
    print(data.replace(" ","").replace("\n",""))
    objetoJson = json.dumps(str(data).replace(" ","").replace("\n",""))
    auxobj=str(objetoJson).replace("\\","")

    objetoJson2 = json.loads(str(data).replace(" ","").replace("\n",""))
    hashActual=  encriptarHash(str(indiceBloque) + str(fechaHora.strftime('%m-%d-%y-::%H:%M:%S')) + str(clase) + str(objetoJson2).replace("None", "null").replace(" ", "").replace("\'", '"') + str(hashAnterior))

    textoJson = "{\n" + '"INDEX": ' + "\""+str(indiceBloque)+"\"" + ",\n" + '"TIMESTAMP": ' + "\""+ str(fechaHora.strftime('%m-%d-%y-::%H:%M:%S'))+"\""+ ",\n"+'"CLASS": '+"\""+ str(clase)+"\""+",\n"+'"DATA": '+ str(data)+ ",\n"+'"PREVIUSHASH": '+"\""+ str(hashAnterior)+"\""+",\n"
    textoJson = textoJson + '"HASH": '+ "\""+str(hashActual)+"\"" + "\n}"
    print(textoJson)
    print(objetoJson)
    print(auxobj)
    print(str(objetoJson2).replace("None", "null").replace(" ", "").replace("\'", '"'))
    print(str(2) + str(fechaHora) + str(clase) + str(objetoJson2).replace("\'", '"').replace("None", "null").replace(" ", "") + str(hashAnterior))
    return textoJson

def encontrarCarnets(palabra, cadenJson):
    carnets = []
    def encontrarNombre(valor):
        try:
            carnets.append(valor[palabra])
        except KeyError:
            pass
        return valor
    json.loads(cadenJson, object_hook=encontrarNombre)  # Return value ignored.
    return carnets


