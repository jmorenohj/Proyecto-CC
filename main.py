from typing import Dict, Any

import matplotlib.pyplot as plt
import numpy
import matplotlib.image as mpimg
import sys
import os
import operator

class nodo:
   def __init__(self,clave,valor,izquierdo=None,derecho=None,
                                       padre=None):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre


   def esHijoIzquierdo(self):
       return self.padre and self.padre.hijoIzquierdo == self

   def esHijoDerecho(self):
       return self.padre and self.padre.hijoDerecho == self

   def esRaiz(self):
       return not self.padre

class Arbol:
    def __init__(self,cant1,val1,cant2,val2):
        self.raiz = nodo(cant1+cant2,"x", None)
        self.raiz.hijoIzquierdo= nodo(cant2, val2,padre= self.raiz)
        self.raiz.hijoDerecho = nodo(cant1,val1,padre=self.raiz)


    def join(self,arbol2):
        nuevoNodo=nodo(self.raiz.clave+arbol2.raiz.clave,"x",None)
        self.raiz.padre=nuevoNodo
        nuevoNodo.hijoIzquierdo=arbol2.raiz
        nuevoNodo.hijoDerecho=self.raiz
        self.raiz=nuevoNodo

    def joinCant(self,cant1,val1):
        nuevoNodo=nodo(self.raiz.clave+cant1,"x",None)
        self.raiz.padre=nuevoNodo
        nuevoNodo.hijoIzquierdo=nodo(cant1,val1,padre=nuevoNodo)
        nuevoNodo.hijoDerecho= self.raiz
        self.raiz=nuevoNodo

def cortar(matrizImagen):
    copy = []
    for i in range(0, len(matrizImagen), 2):
        minicopy = []
        for j in range(0, len(matrizImagen), 2):
            minicopy.append(" ".join(list(map(str,matrizImagen[i][j]))))

        copy.append(" ".join(minicopy))

    return copy

def cortarn(matrizImagen):
    copy = []
    for i in range(0, len(matrizImagen), 2):
        minicopy = []
        for j in range(0, len(matrizImagen), 2):
            minicopy.append( matrizImagen[i][j])
        copy.append(minicopy)
        minicopy = []
    return copy

def descortar(matrizImagen):
    matrizNueva=[]
    for i in range(len(matrizImagen)):
        miniNueva=[]
        linea=matrizImagen[i]
        for j in range(len(linea) - 1, 0, -1):
            miniNueva.insert(0,linea[j])
            prom = promedio(linea[j],linea[j - 1])
            miniNueva.insert(0,prom)
        matrizNueva.append(miniNueva)
    matrizNuevaNueva=[]
    for i in range(len(matrizNueva)-1,0,-1):
        matrizNuevaNueva.insert(0,matrizNueva[i])
        matrizNuevaNueva.insert(0,promediolineas(matrizNueva[i],matrizNueva[i-1]))
    return matrizNuevaNueva

def promediolineas(linea1,linea2):
    lineaNueva=[]
    for i in range(len(linea1)):
        lineaNueva.append(promedio(linea1[i],linea2[i]))
    return lineaNueva

def promedio(arreglo1,arreglo2):
    arregloNuevo=[]
    arregloNuevo.append(int(int((arreglo1[0]) + int(arreglo2[0])) / 2))
    arregloNuevo.append(int(int((arreglo1[1]) + int(arreglo2[1])) / 2))
    arregloNuevo.append(int(int((arreglo1[2]) + int(arreglo2[2])) / 2))
    return arregloNuevo
dic = {}
dicre = {}
def recorrerHuffman(Nodo,bits):
    global dic
    global dicre
    if(Nodo.hijoDerecho==None and Nodo.hijoIzquierdo==None):
        dic[Nodo.cargaUtil]=bits
        dicre[bits]=Nodo.cargaUtil
    else:
        if(Nodo.hijoDerecho!=None):
            recorrerHuffman(Nodo.hijoDerecho,bits+"1")
        if (Nodo.hijoIzquierdo!= None):
            recorrerHuffman(Nodo.hijoIzquierdo, bits + "0")
    return dic,dicre

def HuffmanArbol(caracteres):
    arbolP=Arbol(caracteres[0][1],caracteres[0][0],caracteres[1][1],caracteres[1][0])
    cont=2

    while cont<len(caracteres):
        if caracteres[cont][1]>= arbolP.raiz.clave:
            arbolP.joinCant(caracteres[cont][1],caracteres[cont][0])
            cont+=1;
        else:
            if cont+2<=len(caracteres):
                newArbol=Arbol(caracteres[cont][1],caracteres[cont][0],caracteres[cont+1][1],caracteres[cont+1][0])
                arbolP.join(newArbol)
                cont+=2
            else:
                arbolP.joinCant(caracteres[cont][1],caracteres[cont][0])
                cont+=1
    return recorrerHuffman(arbolP.raiz,"")

def inttoBin(numero):
    numero=int(numero)
    binario=bin(numero)[2:]
    binario="0"*(8-len(binario)) +binario
    return binario

def binaryToLetter(binaryString):
    mod=len(binaryString)%8
    finalString=""
    for i in range(0,len(binaryString)-mod,8):
        miniString=binaryString[i:i+8]
        asciicode=int(miniString,2)
        char=chr(asciicode)
        finalString+=char
    finalString+=binaryString[-mod:]
    return (finalString,mod)

def Huffman(String):
    cantidades={}
    for i in String:
        if i not in cantidades:
            cantidades[i]=1
        else:
            cantidades[i]+=1
    cantidades=sorted(cantidades.items(), key=operator.itemgetter(1))
    BitsTable=HuffmanArbol(cantidades)
    numBits=BitsTable[0]
    Bitnum=BitsTable[1]
    HuffmanString=""
    for i in String:
        HuffmanString+=numBits[i]
    HuffmanString=binaryToLetter(HuffmanString)
    return HuffmanString,numBits,Bitnum

def toMatriz(numList):
    numList=list(map(int,numList.split()))
    matriz=[]
    filas=[]
    trio=[]
    cont3=0
    contFilas=0
    for i in numList:

        cont3+=1
        trio.append(i)
        if cont3==3:
            filas.append(trio)
            trio=[]
            contFilas+=1
            cont3=0
            if contFilas==256:
                matriz.append(filas)
                filas=[]
                contFilas=0
    return matriz

def desHuffman(HuffmanString,mod,bitDistribution):
    binarynoHuffmanString=""
    for i in range(len(HuffmanString)-mod):
        binarynoHuffmanString+=inttoBin(ord(HuffmanString[i]))
    binarynoHuffmanString+=HuffmanString[-mod:]
    noHuffmanString=""
    controler=""
    for i in binarynoHuffmanString:
        controler+=i
        if controler in bitDistribution:
            noHuffmanString+=bitDistribution[controler]
            controler=""
    matriz=toMatriz(noHuffmanString)
    return matriz






    
#fichero = open('C:/Users/JOSE LUIS/Downloads/pruebas_tamaño.txt','w')
img = mpimg.imread('C:/Users/JOSE LUIS/Downloads/lena_color.BMP')
img=" ".join(cortar(img))
s=Huffman(img)
nuevaMatriz=desHuffman(s[0][0],s[0][1],s[2])
nuevaMatriz=descortar(nuevaMatriz)
plt.imshow(nuevaMatriz)
plt.show()






#fichero.close()
#img=descortar(img)
#plt.imshow(img)
#plt.show()

#s=img.tolist()


#s=cortarn(img)
#s=descortar(descortar(s))
#s=" ".join(s)
#print("Longitud s: "+str(len(s)))
#print("Imagen en String: "+str(sys.getsizeof(s)))
#k=Huffman(s)
#print(k[0][0])
#desHuffman(k[0][0],k[0][1],k[2])
#m=desHuffman(k[0][0],k[0][1],k[2])
#m=descortar(m)
#plt.imshow(s)
#r=k.encode()
#print(k)
#print("Comprimido: "+str(sys.getsizeof(r)))
#fichero.write(r)


#print(sys.getsizeof(s))
#mpimg.imsave('C:/Users/JOSE LUIS/Downloads/prueba1.BMP',img)

#plt.imshow(s)

#plt.show()



#os.remove('C:/Users/JOSE LUIS/Downloads/pruebas_tamaño.txt')