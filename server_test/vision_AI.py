import io
import os
import time
from google.cloud import vision

def image_analyze(image_bytes: bytes) -> dict:
	# Instantiates a client
	client = vision.ImageAnnotatorClient()
	image = vision.types.Image(content=image_bytes)
	response = client.face_detection(image=image)
	faces = response.face_annotations
	face = faces[0]

	return _parse_faces(face)

def read_image(image_name: str) -> bytes:
	with io.open(image_name, 'rb') as image_file:
		content = image_file.read()

	return content

def _parse_faces(face) -> dict:
	face_data = {}

	face_data['roll_angle'] = face.roll_angle
	face_data['pan_angle'] = face.pan_angle
	face_data['tilt_angle'] = face.tilt_angle
	face_data['detection_confidence'] = face.detection_confidence
	face_data['landmarking_confidence'] = face.landmarking_confidence
	face_data['joy_likelihood'] = face.joy_likelihood
	face_data['sorrow_likelihood'] = face.sorrow_likelihood
	face_data['angerl_ikelihood'] = face.anger_likelihood
	face_data['surprise_likelihood'] = face.surprise_likelihood
	face_data['under_exposed_likelihood'] = face.under_exposed_likelihood
	face_data['blurred_likelihood'] = face.blurred_likelihood
	face_data['headwear_likelihood'] = face.headwear_likelihood

	return face_data
	