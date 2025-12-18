import cv2
import os

def ensure_dir(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)

def main():
	face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
	dataset_dir = os.path.join(os.path.dirname(__file__), '..', 'dataset')
	ensure_dir(dataset_dir)

	user_id = input('Enter user ID or name: ')
	user_dir = os.path.join(dataset_dir, str(user_id))
	ensure_dir(user_dir)

	cap = cv2.VideoCapture(0)
	print('Capturing faces. Press q to quit.')
	count = 0
	while True:
		ret, frame = cap.read()
		if not ret:
			break
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
		for (x, y, w, h) in faces:
			count += 1
			face_img = gray[y:y+h, x:x+w]
			img_path = os.path.join(user_dir, f'{count}.jpg')
			cv2.imwrite(img_path, face_img)
			cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
		cv2.imshow('Face Capture', frame)
		if cv2.waitKey(1) & 0xFF == ord('q') or count >= 50:
			break
	cap.release()
	cv2.destroyAllWindows()
	print(f'Captured {count} face images for user {user_id}.')

if __name__ == '__main__':
	main()