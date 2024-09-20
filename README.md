# RPS-with-CV
# AI-Powered Rock Paper Scissors Game

## Overview
This project is an interactive Rock Paper Scissors game that uses computer vision to detect hand gestures. Players can play against an AI opponent using their webcam, with real-time hand tracking and gesture recognition, an interactive GUI with multiple windows for game state, player choice, and AI choice, an AI opponent with randomized choices, Visual feedback for game progress and results.

## How It Works
1. **Hand Tracking**: Uses OpenCV and MediaPipe to capture and process webcam feed for hand detection.
2. **Gesture Recognition**: Analyzes hand landmarks by applying trig property Law of Cosines to calculate the angle of middle finger joints to detect if fingers are bent: all fingers bent is identified as rock pose, two fingers bent is identified as paper pose, and no fingers bent is identified as paper pose.
3. **Button Logic**: Draws button's onto webCamera using openCV's draw function, buttons can be hovered over with hand for set time to activate or "push"
4. **Game Logic**: Implements classic Rock Paper Scissors rules to determine the winner, the AI choice is decided with Python's random module.
5. **User Interface**: Utilizes Tkinter for creating multiple windows:
   - Main game window with webcam feed
   - Player's choice display
   - AI's choice display
   - Game state window for instructions and results

## Technical Stack
- Python 3.x
- OpenCV for image processing
- MediaPipe for hand tracking
- Tkinter for GUI
- Pillow for image handling

## Setup and Installation
1. Clone the repository
2. Install required packages:
