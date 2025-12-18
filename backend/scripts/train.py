import cv2
import os
import numpy as np

def get_images_and_labels(dataset_dir):
	image_paths = []
	labels = []
	label_map = {}
	current_label = 0
	for user_name in os.listdir(dataset_dir):
		user_dir = os.path.join(dataset_dir, user_name)
		if not os.path.isdir(user_dir):
			continue
		if user_name not in label_map:
			label_map[user_name] = current_label
			current_label += 1
		for img_name in os.listdir(user_dir):
			img_path = os.path.join(user_dir, img_name)
			image_paths.append(img_path)
			labels.append(label_map[user_name])
	return image_paths, labels, label_map

def main():
	dataset_dir = os.path.join(os.path.dirname(__file__), '..', 'dataset')
	model_path = os.path.join(os.path.dirname(__file__), '..', 'trainer.yml')
	image_paths, labels, label_map = get_images_and_labels(dataset_dir)
	faces = []
	ids = []
	for idx, image_path in enumerate(image_paths):
		img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
		if img is None:
			continue
		faces.append(img)
		ids.append(labels[idx])
	if not faces:
		print('No faces found in dataset. Please run capture_faces.py first.')
		return
	recognizer = cv2.face.LBPHFaceRecognizer_create()
	recognizer.train(faces, np.array(ids))
	recognizer.save(model_path)
	# Save label map for later use
	with open(os.path.join(os.path.dirname(__file__), '..', 'labels.txt'), 'w') as f:
		for name, label in label_map.items():
			f.write(f'{label}:{name}\n')
	print(f'Training complete. Model saved to {model_path}.')

if __name__ == '__main__':
	main()