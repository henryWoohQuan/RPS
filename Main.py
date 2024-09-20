# main.py
import tkinter as tk
from CameraWindow import CameraWindow
from RobotWindow import RobotWindow
from ChoiceWindow import ChoiceWindow
from GameStateWindow import GameStateWindow
from RPSManager import RPSManager

class MainApplication:
    def __init__(self):
        self.root = tk.Tk()
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.withdraw()  # Hide the main window

        self.camera_window = CameraWindow(self)
        self.robot_window = None
        self.user_choice_window = None
        self.robot_choice_window = None
        self.game_state_window = None
        self.game_manager = RPSManager()

    def start_game(self):
        self.camera_window.set_game_active(True)
        self.camera_window.move_left()
        
        if not self.robot_window:
            self.robot_window = RobotWindow(self)
        self.robot_window.show()
        
        choice_window_width = self.screen_width // 6
        choice_window_height = self.screen_height // 6

        if not self.user_choice_window:
            self.user_choice_window = ChoiceWindow(self, "Your Choice", choice_window_width, choice_window_height)
        
        if not self.robot_choice_window:
            self.robot_choice_window = ChoiceWindow(self, "Robot's Choice", choice_window_width, choice_window_height)
        
        # Position user choice window
        user_x = self.camera_window.width - choice_window_width
        user_y = self.screen_height - choice_window_height
        self.user_choice_window.position_window(user_x, user_y)
        self.user_choice_window.show()

        # Position robot choice window
        robot_x = self.screen_width - self.robot_window.width
        robot_y = self.screen_height - choice_window_height
        self.robot_choice_window.position_window(robot_x, robot_y)
        self.robot_choice_window.show()
        
        if not self.game_state_window:
            self.game_state_window = GameStateWindow(self)
        self.game_state_window.show()
        
        self.game_manager.start_game()
        self.run_game_sequence()

    def run_game_sequence(self):
        self.update_game_state()
        if self.game_manager.game_phase != "waiting":
            self.root.after(50, self.run_game_sequence)
        else:
            self.root.after(2000, self.end_game)

    def update_game_state(self):
        self.game_manager.update(self.camera_window.detector, self.camera_window.get_current_frame())
        result_text = self.game_manager.get_result_text()
        self.game_state_window.update_text(result_text)
        
        if self.game_manager.game_phase in ["shoot", "result"]:
            self.robot_choice_window.update_choice(self.game_manager.choice)
            self.user_choice_window.update_choice(self.game_manager.player_choice)

    def end_game(self):
        if self.robot_window:
            self.robot_window.hide()
        if self.user_choice_window:
            self.user_choice_window.hide()
        if self.robot_choice_window:
            self.robot_choice_window.hide()
        if self.game_state_window:
            self.game_state_window.hide()
        self.camera_window.center()
        self.camera_window.set_game_active(False)
        
    def end_program(self):
        if self.robot_window:
            self.robot_window.window.destroy()
        if self.user_choice_window:
            self.user_choice_window.window.destroy()
        if self.robot_choice_window:
            self.robot_choice_window.window.destroy()
        if self.game_state_window:
            self.game_state_window.window.destroy()
        self.camera_window.window.destroy()
        self.root.quit()
        self.root.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MainApplication()
    app.run()