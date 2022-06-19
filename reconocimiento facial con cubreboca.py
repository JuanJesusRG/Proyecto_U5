import cv2
import matplotlib.pyplot
import imutils
from mtcnn.mtcnn import MTCNN
import os
direccion="C:/Users/FORGE527/proyecto ali reconocimiento"
nombre="daniel cubreboca"
carpeta= direccion + '/' + nombre
if not os.path.exists(carpeta):
    os.makedirs(carpeta)
detector = MTCNN()
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
count = 0
while (cap.isOpened()):

    ret, frame = cap.read()
    gris= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gris)
    copia = frame.copy()
    
    caras=detector.detect_faces(copia)
    
    for i in range(len(caras)):
        x1, y1, ancho, alto = caras[i]['box']
        x2,y2= x1 + ancho, y1 + alto
        cara_reg= frame[y1:y2, x1:x2]
        cara_reg=cv2.resize(cara_reg, (150,200), interpolation = cv2.INTER_CUBIC)
        cv2.imwrite(carpeta + "/rostro {}.jpg".format(count), cara_reg)
        count = count + 1
    cv2.imshow("entrenamiento", frame)
    t= cv2.waitKey(1)
    if t == 27 or count >= 300:
        break
    cap.release()
    cv2.destroyAllWindows()
