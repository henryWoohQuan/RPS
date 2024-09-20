# camera_window.py
from Window import Window
import tkinter as tk
import cv2
from PIL import Image, ImageTk
from RPSDetector import RPSDetector
from Button import Button

class CameraWindow(Window):
    def __init__(self, main_app):
        width = main_app.screen_width // 3
        height = int(width * 0.75)  # 4:3 aspect ratio
        super().__init__(main_app, "Camera Feed", width, height)

        self.video_source = 1  # Use 0 for default camera
        self.vid = cv2.VideoCapture(self.video_source)
        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height)
        self.canvas.pack()

        # Create the Button instance
        self.start_button = Button(3, (0, 0), "Start Game", 2, (0, 255, 0))
        button_width = self.start_button.width
        button_height = self.start_button.height
        button_x = (self.width - button_width) // 2
        button_y = (self.height // 2) - button_height
        self.start_button.setPos((button_x, button_y))

        self.detector = RPSDetector(detectionCon=0.7, trackCon=0.9)
        self.game_active = False

        # Start the update loop
        self.update()

    def update(self):
        ret, frame = self.vid.read()
        if ret:
            frame = cv2.flip(frame, 1)
            frame = cv2.resize(frame, (self.width, self.height))
            self.detector.findHands(frame)
            lm_list = self.detector.findPosition(frame, draw=False)

            if not self.game_active:
                if self.start_button.drawButton(frame, lm_list, True):
                    self.main_app.start_game()
            else:
                # Just draw the button without checking for activation
                self.start_button.drawButton(frame, lm_list, False)

            # Convert the image from OpenCV BGR format to RGB
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(rgb_image))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.window.after(15, self.update)

    def set_game_active(self, active):
        self.game_active = active
        if not active:
            self.start_button.reset()  # Reset the button when the game ends

    def move_left(self):
        x = 0
        y = (self.main_app.screen_height - self.height) // 2
        self.window.geometry(f'{self.width}x{self.height}+{x}+{y}')

    def center(self):
        super().position()  # Use the default centering from the base class
    
    # In CameraWindow class
    def get_current_frame(self):    
        ret, frame = self.vid.read()
        if ret:
            frame = cv2.flip(frame, 1)
            frame = cv2.resize(frame, (self.width, self.height))
        return frame