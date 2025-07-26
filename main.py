import cv2
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Load Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

class FaceDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time Face Detection")

        # Create a canvas to display video frames
        self.video_label = tk.Label(root)
        self.video_label.pack()

        # Start and Stop buttons
        self.start_button = tk.Button(root, text="Start Camera", command=self.start_camera, bg="green", fg="white")
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop Camera", command=self.stop_camera, bg="red", fg="white")
        self.stop_button.pack(pady=5)

        # Initialize video capture and loop ID
        self.cap = None
        self.update_id = None

    def start_camera(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            messagebox.showerror("Error", "fail to open camera.")
            return
        self.update_frame()

    def stop_camera(self):
        if self.cap:
            self.cap.release()
            self.cap = None
        if self.update_id:
            self.root.after_cancel(self.update_id)
            self.update_id = None
        self.video_label.config(image='')

    def update_frame(self):
        if self.cap:
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.flip(frame, 1) # Flip the frame horizontally for a mirror effect
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Detect faces
                faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

                # Draw bounding boxes around detected faces
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

                # Display number of faces detected
                text = f"Faces Detected: {len(faces)}"
                cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 255, 50), 2)

                # Convert frame to RGB and display in Tkinter GUI
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(rgb_frame)
                imgtk = ImageTk.PhotoImage(image=img)
                self.video_label.imgtk = imgtk
                self.video_label.config(image=imgtk)

            # Repeat every 15ms
            self.update_id = self.root.after(15, self.update_frame)

    def on_closing(self):
        self.stop_camera()
        self.root.destroy()

# Main fucntion to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = FaceDetectionApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
