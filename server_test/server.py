from flask import request, Flask, jsonify
import vision_AI
import os

app = Flask(__name__)

@app.route('/face/analysis/test', methods=['GET'])
def analyze_test():
	image_bytes = vision_AI.read_image(os.path.join(os.path.dirname(__file__),'captured.jpg'))
	response = vision_AI.image_analyze(image_bytes)
	return jsonify(response), 200

if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 5000)