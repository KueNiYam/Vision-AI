import requests
import time
import threading

def request_test(URL, start_time):
	face_info = requests.get(URL + '/face/analysis/test')
	end_time = time.time()
	print(str(face_info.text))
	print('thread end time from program start: ' + str(end_time - start_time))
	return

if __name__ == '__main__':
	URL = 'http://127.0.0.1:5000'
	start_time = time.time()
	for i in range(0, 100):
		request_thread = threading.Thread(target=request_test, args=(URL,start_time,))
		request_thread.start()
