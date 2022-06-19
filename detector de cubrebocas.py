
import cv2
import os
import matplotlib.pyplot
import imutils
from mtcnn.mtcnn import MTCNN
direccion = 'C:\Users\FORGE527\proyecto ali reconocimiento'
dire_img = os.listdir(direccion)
print("nombre;", dire_img)

reconocimiento = cv2.face.LBFHFaceRecognizer_create()

reconocimiento.read('modeloLBF.xml')
while (cap.isOpened()):
    
    ret, frame = cap.read()
    gris= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('frame',gris)
    copia = frame.copy()
    
    caras=detector.detect_faces(copia)
    
    for i in range(len(caras)):
        x1, y1, ancho, alto = caras[i]['box']
        x2,y2= x1 + ancho, y1 + alto
        cara_reg= frame[y1:y2, x1:x2]
        cara_reg=cv2.resize(cara_reg, (150,200), interpolation = cv2.INTER_CUBIC)
        resultado = reconocimiento.predict(cara_reg)
        
        if resultado[0] == 0:
            cv2.putText(frame, '()'.format(dire_img[0]), (x1,y1-5),1,1,3,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x1,y1),(x1+ancho, y1+alto),(0,0,255),2)
        if resultado[0] == 1:
            cv2.putText(frame, '()'.format(dire_img[0]), (x1,y1-5),1,1,3,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x1,y1),(x1+ancho, y1+alto),(0,0,255),2)
    cv2.imshow('reconocimiento',frame)
    
    t=cv2.waikey(1)
    if t == 27:
        break
cap.release()
cv2.destroyAllWindows()