import cv2
import os
import numpy as np
direccion='C:/Users/FORGE527/proyecto ali reconocimiento'
lista = os.listdir(direccion)

etiquetas = []

rostro=[]
con=0

for nameDir in lista:
    nombre = direccion + '/'+ nameDir
    
    for fileName in os.listdir(nombre):
        etiquetas.append(con)
        rostro.append(cv2.imread(nombre + '/' + dileName,0))
        con = con + 1
        
reconomiciento = cv2.face.LBPHFaceRecognizet_create()
reconomiciento.train(rostro, np.array(etiquetas))
reconomiciento.write('modeloLBP.xml')