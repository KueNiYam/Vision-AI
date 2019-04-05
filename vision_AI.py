def image_analyze():
	import io
	import os
	import time

	# Imports the Google Cloud client library
	from google.cloud import vision

	start = time.time()
	# Instantiates a client
	client = vision.ImageAnnotatorClient()
	
	# The name of the image file to annotate
	file_name = '.\captured.jpg'
	
	# Loads the image into memory in form of binary data
	with io.open(file_name, 'rb') as image_file:
	    content = image_file.read()
	
	image = vision.types.Image(content=content)
	
	response = client.face_detection(image=image)
	faces = response.face_annotations
	end = time.time()
	
	print('faces <json>:')
	print(str(faces))
	print('how_long: ' + str(end - start) + 'sec.')

if __name__ == '__main__':
	image_analyze()
