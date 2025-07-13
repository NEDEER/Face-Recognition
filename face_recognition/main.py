import cv2 
import face_recognition
import os 
import cvzone 
# !photo of reference 
images_path = 'C:/Users/neder/Desktop/FormationCV/Session 5/peoples'
images = []
dataset_encodings = []
names = []
tests=[]
for i in os.listdir(images_path):
    img = cv2.imread(images_path+'/'+i)
    images.append(img)
    name = i.split('.')[0]
    names.append(name)
# print(names)
for photo in images : 
    rgb = cv2.cvtColor(photo , cv2.COLOR_BGR2RGB)
    enc = face_recognition.face_encodings(rgb)[0]
    dataset_encodings.append(enc)
# print(len(dataset_encodings))
# !test photo
test_path='C:/Users/neder/Desktop/FormationCV/Session 5/test'
for i in os.listdir(test_path):
    testpic = cv2.imread(test_path+'/'+i)
    tests.append(testpic)
for ph in tests : 
    rgb = cv2.cvtColor(photo , cv2.COLOR_BGR2RGB)
    enc = face_recognition.face_encodings(rgb)[0]
    dataset_encodings.append(enc)
    test_rgb = cv2.cvtColor(testpic, cv2.COLOR_BGR2RGB)
    test_encodings = face_recognition.face_encodings(test_rgb)[0]
    y1 , x2 , y2 , x1 = face_recognition.face_locations(test_rgb)[0]


for counter ,  enc in enumerate(dataset_encodings) :
    results = face_recognition.compare_faces( [enc]   ,   test_encodings)[0]
    conf = 1-face_recognition.face_distance([enc] , test_encodings)[0]
    if results == True : 
        print(names[counter] , conf)
        cvzone.putTextRect(testpic ,names[counter]+' '+str(round(conf,2)) , (x1 , y1-20) , colorR=(0,0,255) )
        w = x2 - x1
        h = y2 - y1
        bbox = (x1, y1, w, h)
        cvzone.cornerRect(testpic,bbox,colorR=(0,0,255),colorC=(0,0,255),l=20,t=4)

        #cv2.rectangle(test_pic , (x1 , y1) , (x2 ,y2),(0,0,255) , 4)
        # if names[counter] == 'jack_Ma':
        #     file = open('C:/Users/neder/Desktop/FormationCV/Session 5/face_recognition/jack.txt')
        # elif names[counter] == 'kais_saied':
        #     file = open('C:/Users/neder/Desktop/FormationCV/Session 5/face_recognition/kaies.txt')
        # elif names[counter] == 'Elon_Musk':
        #     file = open('C:/Users/neder/Desktop/FormationCV/Session 5/face_recognition/Elon.txt')
        # else:
        #     file=None
        # text = file.readlines()
        # counter = 1
        # for line in text :
        #     cv2.putText(test_pic , line , (40,40*counter) , cv2.FONT_ITALIC , 0.5 , (0,0,0) , 1)
        #     counter = counter + 1 
    else :
        pass
    # print(results)


cv2.imshow('image' , testpic)
cv2.waitKey(0)



