def capture():
	import cv2
	import os
	CAMERA = 0 
	cap = cv2.VideoCapture(CAMERA)
	
	width = cap.get(3)
	height = cap.get(4)
	
	while(True):
		# ret: <boolean> frame capture result
		# frame: Captured frame
		ret, frame = cap.read()
		if (ret):
			cv2.imshow('frame', frame)
	
			pressed = cv2.waitKey(1000//24)
			if pressed & 0xFF == ord('q'):
				break
			elif pressed & 0xFF == ord(' '):
				cv2.imwrite(os.path.join(os.path.dirname(__file__),
							   'captured.jpg') , frame)
				print('The image is captured')
				break
	
	cap.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	capture()