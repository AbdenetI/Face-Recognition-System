# Real-Time Face Recognition System

A comprehensive face recognition application built with OpenCV and Python that detects and identifies faces in real-time using computer vision and machine learning. This system allows users to capture face data, train custom recognition models, and perform live identification through webcam feed with high accuracy.

## About The Project

This face recognition system implements computer vision algorithms to:
- Detect faces in real-time video streams using Haar Cascade classifiers
- Train custom face recognition models using LBPH (Local Binary Patterns Histogram) algorithm
- Identify individuals with confidence scoring
- Manage multiple user profiles with organized dataset structure

Perfect for learning computer vision fundamentals, building attendance systems, access control applications, or security monitoring solutions.

## Technologies & Skills

**Programming & Frameworks:**
- Python 3.x
- OpenCV (cv2) - Computer Vision
- NumPy - Numerical Computing
- Machine Learning (LBPH Face Recognition)

**Core Skills Demonstrated:**
- Computer Vision & Image Processing
- Real-time Video Processing
- Machine Learning Model Training
- File I/O & Data Management
- Algorithm Implementation
- Software Architecture (Frontend/Backend separation)

## Features

- **Real-time Face Detection** - Live webcam feed processing with Haar Cascade
- **Custom Model Training** - Train recognition models on personal datasets
- **Face Data Capture** - Automated face image collection tool
- **Multi-user Support** - Handle multiple individuals in database
- **Confidence Scoring** - Recognition results with accuracy metrics
- **Organized Architecture** - Clean separation of frontend and backend
- **Easy Setup** - Simple installation and usage instructions

## 📁 Project Structure

```
Face-Recognition-System/
├── backend/              # Python ML backend
│   ├── scripts/          # Core Python scripts
│   │   ├── recognize.py      # Real-time recognition
│   │   ├── train.py          # Model training
│   │   └── capture_faces.py  # Data collection
│   ├── dataset/          # Training images (not in repo)
│   ├── requirements.txt  # Python dependencies
│   └── README.md
├── frontend/             # Web interface (in development)
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── README.md
├── .gitignore
├── LICENSE (MIT)
└── README.md
```

## Quick Start

### Prerequisites
- Python 3.7 or higher
- Webcam/Camera
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AbdenetI/Face-Recognition-System.git
   cd Face-Recognition-System
   ```

2. **Navigate to backend and create virtual environment**
   ```bash
   cd backend
   python -m venv .venv
   
   # On Windows:
   .venv\Scripts\activate
   
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

**Step 1: Capture Face Data**
```bash
python scripts/capture_faces.py --user YOUR_NAME --max 100
```
This will capture 100 images of your face for training.

**Step 2: Train the Model**
```bash
python scripts/train.py
```
Trains the recognition model on your captured data.

**Step 3: Run Face Recognition**
```bash
python scripts/recognize.py
```
Starts real-time face recognition. Press 'q' to quit.

## What I Learned

Through this project, I gained hands-on experience with:
- Implementing computer vision algorithms using OpenCV
- Working with real-time video streams and image processing
- Training and deploying machine learning models
- Handling file systems and data organization
- Building modular, maintainable code architecture
- Version control with Git and GitHub best practices

## Future Enhancements

- [ ] Complete web-based frontend interface
- [ ] REST API for backend communication
- [ ] Deep learning models (CNN) for improved accuracy
- [ ] Face emotion detection
- [ ] Multiple face recognition in single frame
- [ ] Database integration for user management
- [ ] Deployment to cloud platform

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Abdenet Tadese**
- GitHub: [@AbdenetI](https://github.com/AbdenetI)
- Email: abdenet.tadese@mnsu.edu

## Acknowledgments

- OpenCV community for comprehensive documentation
- Computer vision tutorials and resources
- Open source contributors

---

**If you find this project useful, please consider giving it a star!**
