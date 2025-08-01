   Face Detection System with GUI (Python + OpenCV + Tkinter)
This project is a real-time face detection system built using Python, OpenCV, and Tkinter. It leverages the power of Haar Cascade Classifiers to detect faces in live video streams and displays the result in an interactive graphical user interface (GUI). The system is lightweight, responsive, and ideal for basic face detection use-cases, educational purposes, and demos.

  # Features
🎥 Live video stream from webcam

🧠 Real-time face detection using Haar cascades

🟩 Bounding boxes around detected faces

🔢 Face count display on screen

🖼️ Mirror effect applied for user-friendly view

🟢 Start/🔴 Stop webcam controls

🖥️ Simple and clean GUI using Tkinter

  
  # How It Works:

 1.Camera Initialization

When the "Start Camera" button is clicked, the system activates the webcam and begins capturing frames.

 2.Face Detection
Each frame is:Flipped horizontally for a mirror view

Converted to grayscale

Passed through Haar Cascade Classifier (haarcascade_frontalface_default.xml) to detect faces

 3.Drawing and Display

Green rectangles are drawn around detected faces

Text showing the number of detected faces is overlaid

The frame is converted to RGB and displayed in the Tkinter window using Pillow

Camera Stop

On clicking "Stop Camera" or closing the window, the video stream is released safely.

 # Requirements

Python 3.x

OpenCV

Pillow (for image handling in Tkinter)

# Output Preview

When the camera is started, the application shows a live feed with green rectangles around faces and a count like:

  fece detected : 1
  <img width="299" height="271" alt="Screenshot 2025-08-02 183553" src="https://github.com/user-attachments/assets/0f1ed614-bdb8-41b9-9653-5833ed914cf9" /> 
  <img width="814" height="748" alt="Screenshot 2025-08-02 183614" src="https://github.com/user-attachments/assets/0f6e356f-c3bb-4c72-9145-6b72ec3cfdb4" />



