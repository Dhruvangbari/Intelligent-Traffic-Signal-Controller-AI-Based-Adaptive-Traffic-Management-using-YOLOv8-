# Intelligent Traffic Signal Controller
# 🚦 Intelligent Traffic Signal Controller

An AI-based adaptive traffic signal control system built using Python, OpenCV, and YOLOv8.

This project detects vehicles in real-time and dynamically adjusts traffic signal timing based on traffic density. It simulates a smart traffic management system designed for intelligent transportation and smart city applications.

---

## 🚀 Features

- Real-time vehicle detection
- Detects: car, bus, truck, motorcycle
- Traffic density estimation
- Dynamic green signal timing simulation
- Live vehicle count display
- Webcam or video file support
- Lightweight YOLOv8 nano model

---

## 🧠 Tech Stack

- Python 3.10+
- OpenCV
- Ultralytics YOLOv8
- NumPy

---

## 📂 Project Structure

Intelligent_Traffic_Signal_Controller/
│
├── main.py
├── detector.py
├── config.py
├── requirements.txt
└── README.md

---

## ⚙️ Installation

1. Install Python 3.10 or later.
2. Clone the repository:

   git clone <your-repository-link>

3. Navigate to the project directory:

   cd Intelligent_Traffic_Signal_Controller

4. Install dependencies:

   pip install -r requirements.txt

5. Run the system:

   python main.py

The YOLOv8 model will automatically download on first execution.

---

## 📊 How It Works

1. Video input is captured from webcam or file.
2. YOLOv8 detects vehicles in each frame.
3. Vehicle count is calculated.
4. Traffic density level is classified:
   - Low
   - Medium
   - High
5. Green signal time is dynamically assigned based on density.

---

## 🚥 Signal Timing Logic

| Traffic Level | Vehicle Count | Green Time |
|--------------|--------------|------------|
| Low          | < 5          | 5 seconds  |
| Medium       | 5 – 14       | 10 seconds |
| High         | 15+          | 20 seconds |

---

## 🖥 System Requirements

Minimum:
- Windows 11
- 8GB RAM
- Webcam or video input

Recommended:
- NVIDIA GPU for faster inference

---

## ⚠️ Current Limitation

This version uses frame-based vehicle counting.
If vehicles remain in frame, duplicate counting may occur.

Future improvements:
- Object tracking (DeepSORT)
- Lane-wise signal control
- Multi-intersection simulation
- Traffic analytics dashboard
- Real-world hardware integration (Arduino/ESP32)

---

## 🔒 Ethical & Research Notice

This project is intended for educational and research purposes only.  
Not suitable for direct real-world deployment without validation and regulatory compliance.

---

## 👨‍💻 Author

Developed as an AI-based intelligent transportation system simulation project.

AI-based adaptive traffic signal system using YOLOv8 and OpenCV.

## Features
- Real-time vehicle detection
- Traffic density estimation
- Dynamic green signal timing simulation
- Webcam or video input support

## Setup

1. Install Python 3.10+
2. Install dependencies:
   pip install -r requirements.txt
3. Run:
   python main.py

YOLO model will auto-download on first run.
