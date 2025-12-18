# Backend - Face Recognition

This folder contains the Python backend for face recognition.

## Structure

- `scripts/` - Python scripts for face recognition, training, and capture
  - `recognize.py` - Main face recognition script
  - `train.py` - Model training script
  - `capture_faces.py` - Script to capture face data
- `dataset/` - Training dataset with face images
- `labels.txt` - Labels file
- `trainer.yml` - Trained model file
- `requirements.txt` - Python dependencies

## Running the Backend

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run face recognition:
   ```
   python scripts/recognize.py
   ```

3. Train the model:
   ```
   python scripts/train.py
   ```

4. Capture new faces:
   ```
   python scripts/capture_faces.py
   ```
