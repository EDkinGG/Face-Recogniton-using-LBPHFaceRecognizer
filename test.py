import cv2

model = cv2.face.LBPHFaceRecognizer_create()

functions = dir(cv2.face.__package__)
for f in functions:
    print (f)