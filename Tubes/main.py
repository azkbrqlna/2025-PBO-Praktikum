"""
Quiz Duel Game - Tugas Besar Object-Oriented Programming
========================================================
Author: Azka Bariqlana
"""

import tkinter as tk
from tkinter import messagebox
import sys
import os

# untuk import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from ui.quiz_game import QuizDuelGame
except ImportError as e:
    print(f"Error importing modules: {e}")
    sys.exit(1)

class QuizDuelApp:
    def __init__(self):
        self.root = None
        self.game = None
        self.setup_application()
    
    def setup_application(self):
        try:
            self.root = tk.Tk()
            self.configure_window()
            self.game = QuizDuelGame(self.root)
            self.game.load_settings()
        except Exception as e:
            self.show_error(f"Error initializing application: {str(e)}")
            sys.exit(1)
    
    def configure_window(self):
        self.root.title("Quiz Duel Game - Tugas Besar OOP")
        self.root.geometry("900x700")
        self.root.minsize(800, 600)
        
        self.center_window(900, 700)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.configure(bg="#ecf0f1")
    
    def center_window(self, width=900, height=700):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def on_closing(self):
        if messagebox.askokcancel("Keluar", "Yakin ingin keluar dari Quiz Duel Game?"):
            self.cleanup()
            self.root.destroy()

    def cleanup(self):
        try:
            if self.game:
                self.game.timer_running = False
        except Exception as e:
            print(f"Error during cleanup: {e}")
    
    def show_error(self, message):
        if self.root:
            messagebox.showerror("Error", message)
        else:
            print(f"ERROR: {message}")
    
    def run(self):
        try:
            print("🎮 Starting Quiz Duel Game...")
            print("📚 Tugas Besar Object-Oriented Programming")
            print("=" * 50)
            self.check_directories()
            self.root.mainloop()
        except KeyboardInterrupt:
            print("\n⏹️  Quiz Duel Game dihentikan oleh user")
            self.cleanup()
        except Exception as e:
            self.show_error(f"Unexpected error: {str(e)}")
            print(f"💥 Fatal error: {e}")
            sys.exit(1)
        finally:
            print("👋 Quiz Duel Game ditutup")
    
    def check_directories(self):
        required_dirs = ["data", "models", "ui"]
        for directory in required_dirs:
            if not os.path.exists(directory):
                try:
                    os.makedirs(directory)
                    print(f"📁 Created directory: {directory}")
                except OSError as e:
                    print(f"❌ Failed to create directory {directory}: {e}")
        
        required_files = {
            "models/__init__.py": "",
            "ui/__init__.py": "",
        }

        for file_path, content in required_files.items():
            if not os.path.exists(file_path):
                try:
                    with open(file_path, "w") as f:
                        f.write(content)
                    print(f"📄 Created file: {file_path}")
                except IOError as e:
                    print(f"❌ Failed to create file {file_path}: {e}")

def main():
    print("🚀 Initializing Quiz Duel Game...")
   
    try:
        app = QuizDuelApp()
        app.run()
    except Exception as e:
        print(f"💥 Fatal error starting application: {e}")
        input("Press Enter to exit...")
        sys.exit(1)

if __name__ == "__main__":
    main()
