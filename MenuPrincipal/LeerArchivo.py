import csv
import datetime
from MenuPrincipal import ListaDE
import hashlib
import json
from MenuPrincipal import ArbolAVL



class leerArchivo():
#x  listaSimple = ListaDE.ListaDE()
    indiceJson = ListaDE.ListaDE()

    def jsonCorrecto(self,cadenaJson):
        cadenaJson2 = str(cadenaJson).replace("\'", '"').replace("None", "null")
        listaAux = json.loads(str(cadenaJson2))
        hashAnterior = listaAux["PREVIUSHASH"]
        hashActual = listaAux["HASH"]
        clase = listaAux["CLASS"]
        indice = listaAux["INDEX"]
        fechaHora = listaAux["TIMESTAMP"]
        data = listaAux["DATA"]
        hashJson = self.encriptarHash(str(indice) + str(fechaHora) + str(clase) + str(data).replace("\'", '"').replace("None", "null").replace(" ","") + str(hashAnterior))
        if hashJson == hashActual:
            return "true"
        else:
            return "false"

    def guardarJson(self,cadenaJson):
        cadenaJson2 = json.loads(str(cadenaJson))
        self.indiceJson.insertar_final(cadenaJson, cadenaJson2["HASH"])



    def encriptarHash(self,hashCodigo):
        aux = hashlib.sha256(hashCodigo.encode()).hexdigest()
        return aux

    def generarData(self,rutaArchivo):

        with open(rutaArchivo, 'r') as abrir:
            leer= csv.reader(abrir)
            archivo = list(leer)

        clase=archivo[0][1]
        data = archivo[1][1]
        fechaHora = datetime.datetime.now()
        #fechaHora.strftime('%m-%d-%y %H:%M:%S')
        #auxfechaHora="02-10-19-::14:30:25"
        #auxhashAnterior ="fd5f6d5fdfdf232Y232312QW12196255"
        indiceBloque = self.indiceJson.contarNodos()
        if self.indiceJson.listaEsNula():
            hashAnterior = '0000'
        else:
            hashAnterior= "\""+self.indiceJson.retornarUltimoNodo().valor2+"\""

        print(data.replace(" ","").replace("\n",""))
        objetoJson = json.dumps(str(data).replace(" ","").replace("\n",""))
        auxobj=str(objetoJson).replace("\\","")

        objetoJson2 = json.loads(str(data).replace(" ","").replace("\n",""))
        hashActual=  self.encriptarHash(str(indiceBloque) + str(fechaHora.strftime('%m-%d-%y-::%H:%M:%S')) + str(clase) + str(objetoJson2).replace("None", "null").replace(" ", "").replace("\'", '"') + str(hashAnterior))

        textoJson = "{\n" + '"INDEX": ' + "\""+str(indiceBloque)+"\"" + ",\n" + '"TIMESTAMP": ' + "\""+ str(fechaHora.strftime('%m-%d-%y-::%H:%M:%S'))+"\""+ ",\n"+'"CLASS": '+"\""+ str(clase)+"\""+",\n"+'"DATA": '+ str(data)+ ",\n"+'"PREVIUSHASH": '+"\""+ str(hashAnterior)+"\""+",\n"
        textoJson = textoJson + '"HASH": '+ "\""+str(hashActual)+"\"" + "\n}"
        #print(textoJson)
        #print(objetoJson)
        #print(auxobj)
        #print(str(objetoJson2).replace("None", "null").replace(" ", "").replace("\'", '"'))
        #print(str(2) + str(fechaHora) + str(clase) + str(objetoJson2).replace("\'", '"').replace("None", "null").replace(" ", "") + str(hashAnterior))
        return textoJson
    def graficarLista(self):
        self.indiceJson.graficarLista()

    def encontrarCarnets(self,cadenJson):

        carnets = []
        def encontrarNombre(carnetNombre):
            try:
                carnets.append(carnetNombre['value'])
            except KeyError:
                pass
            return carnetNombre
        json.loads(cadenJson, object_hook=encontrarNombre)

        return carnets

    def crearArbol(self,cadenaJson):
        auxArbol = ArbolAVL.ArbolAVLOriginal()
        jsonCadena = str(cadenaJson).replace("None", "null").replace("\'", '"')
        temp = self.encontrarCarnets(str(jsonCadena))
        #print(temp)

        for i in temp:
            aux = str(i).split("-")
            auxArbol.insertar(aux[0], aux[1])
        auxArbol.graficarArbol()

    def graficarInorden(self,cadenaJson):
        auxArbol = ArbolAVL.ArbolAVLOriginal()
        jsonCadena = str(cadenaJson).replace("None", "null").replace("\'", '"')
        temp = self.encontrarCarnets(str(jsonCadena))

        for iteracion in temp:
            aux = str(iteracion).split("-")
            auxArbol.insertar(aux[0], aux[1])
        auxArbol.graficarInorden()

    def graficarPostOrden(self,cadenaJson):
        auxArbol = ArbolAVL.ArbolAVLOriginal()
        jsonCadena = str(cadenaJson).replace("\'", '"').replace("None", "null")
        temp = self.encontrarCarnets(str(jsonCadena))

        for iteracion in temp:
            aux = str(iteracion).split("-")
            auxArbol.insertar(aux[0], aux[1])
        auxArbol.graficarPostOrden()

    def graficarPreOrden(self,cadenaJson):
        auxArbol = ArbolAVL.ArbolAVLOriginal()
        jsonCadena = str(cadenaJson).replace("\'", '"').replace("None", "null")
        temp = self.encontrarCarnets(str(jsonCadena))

        for iteracion in temp:
            aux = str(iteracion).split("-")
            auxArbol.insertar(aux[0], aux[1])
        auxArbol.graficarPreOrden()


    def obtenerLista(self):
        return self.indiceJson

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