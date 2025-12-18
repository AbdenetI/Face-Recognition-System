import cv2
import os

def load_label_map(label_file):
	label_map = {}
	if not os.path.exists(label_file):
		return label_map
	with open(label_file, 'r') as f:
		for line in f:
			if ':' in line:
				label, name = line.strip().split(':', 1)
				label_map[int(label)] = name
	return label_map

def main():
	model_path = os.path.join(os.path.dirname(__file__), '..', 'trainer.yml')
	label_file = os.path.join(os.path.dirname(__file__), '..', 'labels.txt')
	label_map = load_label_map(label_file)
	if not os.path.exists(model_path):
		print('Trained model not found. Please run train.py first.')
		return
	recognizer = cv2.face.LBPHFaceRecognizer_create()
	recognizer.read(model_path)
	face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

	cap = cv2.VideoCapture(0)
	print('Starting face recognition. Press q to quit.')
	while True:
		ret, frame = cap.read()
		if not ret:
			print('Failed to grab frame from webcam.')
			break
		# Resize frame for faster processing
		small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
		gray = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
		# Debug: print shape
		# print(f'Frame shape: {gray.shape}')
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		for (x, y, w, h) in faces:
			face_img = gray[y:y+h, x:x+w]
			label, confidence = recognizer.predict(face_img)
			name = label_map.get(label, 'Unknown')
			# Scale coordinates back to original frame size
			x2, y2, w2, h2 = [int(v * 2) for v in (x, y, w, h)]
			cv2.rectangle(frame, (x2, y2), (x2+w2, y2+h2), (0, 255, 0), 2)
			cv2.putText(frame, f'{name} ({confidence:.0f})', (x2, y2-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
		cv2.imshow('Face Recognition', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()