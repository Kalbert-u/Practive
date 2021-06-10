import cv2
import os
import time

IMAGES_PATH = 'Tensorflow/workspace/images/collectedimages'

#labels= ['hello','thanks','yes','no','iloveyou']
labels= ['arm']
number_imgs = 100
nlb = 0

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) #cv2.VideoCapture(0,cv2.CAP_DSHOW)

for label in labels:
	os.makedirs('Tensorflow/workspace/images/collectedimages/'+label, exist_ok=True)
	#os.makedirs('Tcollectedimages/'+label, exist_ok=True)
	print('Collecting images for {} '.format(label))
	#time.sleep(5)

def show():
	print("chuyen sang chup hinh "+labels[nlb])
	while (1):
		ret, frame = cap.read()
		cv2.imshow('hien_thi_frame', frame)
		if cv2.waitKey(1) & 0xFF == ord('/'):
			break


def chup():
	for imgnum in range(number_imgs):
		ret, frame = cap.read()
		imgname = os.path.join(IMAGES_PATH, labels[nlb], labels[nlb]+'{}.jpg'.format(imgnum))
		cv2.imshow('hien_thi_frame', frame)
		cv2.imwrite(imgname, frame)
		time.sleep(1)
		print(imgnum)
		
		if cv2.waitKey(1) & 0xFF == ord('/'):
			break	


while (1):
	show()
	chup()
	nlb+=1
	if (nlb==5): break
print("hoan thanh")