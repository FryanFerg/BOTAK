import cv2
import numpy as np
from os import listdir
from os.path import isfile,join


data_path = 'dataset/'
only_files = [f for f in listdir(data_path) if isfile(join(data_path,f))]

Training_Data, Labels = [], [] 

for i, files in enumerate(only_files):
    image_path = data_path + only_files[i]
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    Training_Data.append(np.asarray(images, dtype=np.uint8))
    Labels.append(i)

Labels = np.asarray(Labels, dtype=np.int32)

model = cv2.face.LBPHFaceRecognizer_create()

model.train(np.asarray(Training_Data), np.asarray(Labels))

print('Model Training Completed')

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_detector(img, size = 0.5):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_classifier.detectMultiScale(gray,1.3,5)
	if faces is ():
		return img,[]
		
	for(x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w, y+h),(0,255,255),2)
		roi = img[y:y+h, x:x+w]
		roi = cv2.resize(roi,(200,200))
		
		return img,roi

