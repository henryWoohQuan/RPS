# rps_manager.py
import time
import random

class RPSManager:
    def __init__(self):
        self.choice = None
        self.time = 0
        self.rpsResult = None
        self.player_choice = None
        self.game_phase = "waiting"

    def start_game(self):
        self.time = time.time()
        self.choice = random.randint(0, 2)
        self.rpsResult = None
        self.player_choice = None
        self.game_phase = "countdown"

    def update(self, detector, frame):
        if self.game_phase == "waiting":
            return

        current_time = time.time()
        elapsed_time = current_time - self.time

        if elapsed_time < 3:
            self.game_phase = "countdown"
        elif elapsed_time < 4:
            self.game_phase = "shoot"
            lm_list = detector.findPosition(frame, draw=False)
            if lm_list:
                self.player_choice = detector.rockPaperOrScissors()
        elif elapsed_time < 6:
            if self.game_phase == "shoot":
                self.rpsResult = self.decide_winner()
            self.game_phase = "result"
        else:
            self.game_phase = "waiting"

    def decide_winner(self):
        if self.player_choice is None:
            return "No hand detected"
        elif self.player_choice == self.choice:
            return "Tie"
        elif (self.player_choice == 0 and self.choice == 2) or \
             (self.player_choice == 1 and self.choice == 0) or \
             (self.player_choice == 2 and self.choice == 1):
            return "Win"
        else:
            return "Loss"

    def get_result_text(self):
        if self.game_phase == "waiting":
            return ""
        elif self.game_phase == "countdown":
            elapsed_time = time.time() - self.time
            if elapsed_time < 1:
                return "Rock"
            elif elapsed_time < 2:
                return "Paper"
            else:
                return "Scissors"
        elif self.game_phase == "shoot":
            return "SHOOT"
        elif self.game_phase == "result":
            return self.rpsResult if self.rpsResult else "Waiting for result..."
        else:
            return ""