def image_analyze():
	import io
	import os
	import time

	# Imports the Google Cloud client library
	from google.cloud import vision

	# Instantiates a client
	client = vision.ImageAnnotatorClient()
	
	# The name of the image file to annotate
	file_name = os.path.join(os.path.dirname(__file__), 'captured.jpg')
	
	# Loads the image into memory in form of binary data
	with io.open(file_name, 'rb') as image_file:
	    content = image_file.read()
	
	start = time.time()
	image = vision.types.Image(content=content)
	
	response = client.face_detection(image=image)
	faces = response.face_annotations
	end = time.time()
	
	print('faces[0]:')
	print(str(faces[0]))
	print('how_long: ' + str(end - start) + 'sec.')

if __name__ == '__main__':
	image_analyze()
