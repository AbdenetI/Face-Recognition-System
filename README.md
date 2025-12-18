# Real‑Time Face Recognition (OpenCV + Python)

This project is split into two main directories:
- **backend/** - Python face recognition system
- **frontend/** - Web interface (coming soon)

## Quick Start (Backend)

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python scripts/capture_faces.py --user YOUR_NAME --max 100
python scripts/train.py
python scripts/recognize.py
```

## Project Structure

```
Face-recog/
├── backend/           # Python ML backend
│   ├── scripts/       # Python scripts
│   ├── dataset/       # Training data
│   ├── requirements.txt
│   └── README.md
├── frontend/          # Web interface
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── README.md
└── README.md
```
