# 👀 Stay Awake Detector

A real-time computer vision project built with Python and OpenCV that detects when eyes remain closed for too long and plays an audio alert.

---

## 🚀 Features

- Real-time webcam detection
- Face detection using Haar Cascades
- Eye detection inside face region
- Frame-based stability logic (ignores blinking)
- Audio alert when eyes stay closed
- Stops alert when eyes reopen

---

## 🧠 How It Works

Pipeline:

Webcam → Grayscale → Face Detection → Eye Detection →  
Closed-eye frame counter → Trigger audio alert

If eyes are not detected for multiple consecutive frames, the alert sound plays.

---

## 🛠 Technologies Used

- Python 3
- OpenCV
- Haar Cascade Classifiers
- Pygame (for non-blocking audio)

---

## 📂 Project Structure

- ├── main.py
- ├── haarcascade_frontalface_default.xml
- ├── haarcascade_eye.xml
- ├── sound.mp3
- └── README.md

---

## 📦 Installation

Install dependencies:

```bash
pip install opencv-python pygame
```

## ▶️ Run the Project
```bash
python main.py
```
