# RPS-with-CV
# AI-Powered Rock Paper Scissors Game

## Overview
This project is an interactive Rock Paper Scissors game that uses computer vision to detect hand gestures. Players can play against an AI opponent using their webcam, with real-time hand tracking and gesture recognition.

## Features
- Real-time hand tracking and gesture recognition
- Interactive GUI with multiple windows for game state, player choice, and AI choice
- AI opponent with randomized choices
- Visual feedback for game progress and results

## How It Works
1. **Hand Tracking**: Uses OpenCV and MediaPipe to capture and process webcam feed for hand detection.
2. **Gesture Recognition**: Analyzes hand landmarks to identify Rock, Paper, or Scissors gestures.
3. **Game Logic**: Implements classic Rock Paper Scissors rules to determine the winner.
4. **User Interface**: Utilizes Tkinter for creating multiple windows:
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
