
"""
Quiz Duel Game - Tugas Besar Object-Oriented Programming
========================================================

Program Quiz Duel adalah aplikasi permainan kuis untuk dua pemain yang dibuat
menggunakan konsep Object-Oriented Programming (OOP) dengan Python dan Tkinter.

Fitur Utama:
- Permainan kuis untuk 2 pemain
- Multiple choice questions dengan berbagai kategori
- 3 mode permainan: Normal, Timed Challenge
- Timer system
- Antarmuka pengguna yang user-friendly

Struktur Proyek:
- main.py: File utama untuk menjalankan aplikasi
- models/: Package berisi class model (Player, Question)
- ui/: Package berisi class UI (QuizDuelGame)
- data/: Direktori untuk menyimpan data (questions.json, settings.json)

Author: Azka Bariqlana
NIM: 4.33.24.1.04
Mata Kuliah: Pemrograman Berorientasi Objek
"""

import tkinter as tk
from tkinter import messagebox
import sys
import os

# Tambahkan path untuk import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from ui.quiz_game import QuizDuelGame
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Pastikan struktur folder sudah benar:")
    print("- models/player.py")
    print("- models/question.py") 
    print("- ui/quiz_game.py")
    sys.exit(1)

class QuizDuelApp:
    """
    Main application class untuk Quiz Duel Game.
    
    Class ini bertanggung jawab untuk:
    - Inisialisasi aplikasi utama
    - Setup window properties
    - Error handling untuk aplikasi
    - Lifecycle management
    """
    
    def __init__(self):
        """
        Inisialisasi aplikasi Quiz Duel.
        """
        self.root = None
        self.game = None
        self.setup_application()
    
    def setup_application(self):
        """
        Setup konfigurasi aplikasi utama.
        """
        try:
            # Create main window
            self.root = tk.Tk()
            
            # Configure window
            self.configure_window()
            
            # Initialize game
            self.game = QuizDuelGame(self.root)
            
            # Load user settings
            self.game.load_settings()
            
        except Exception as e:
            self.show_error(f"Error initializing application: {str(e)}")
            sys.exit(1)
    
    def configure_window(self):
        """
        Konfigurasi properti window utama.
        """
        # Window properties
        self.root.title("Quiz Duel Game - Tugas Besar OOP")
        self.root.geometry("900x700")
        self.root.minsize(800, 600)
        
        # Center window on screen
        self.center_window()
        
        # Configure window behavior
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Set window icon (if available)
        try:
            if os.path.exists("assets/icon.ico"):
                self.root.iconbitmap("assets/icon.ico")
        except:
            pass  # Icon not found, continue without it
        
        # Configure style
        self.root.configure(bg="#ecf0f1")
    
    def center_window(self):
        """
        Posisikan window di tengah layar.
        """
        self.root.update_idletasks()
        
        # Get window dimensions
        window_width = self.root.winfo_reqwidth()
        window_height = self.root.winfo_reqheight()
        
        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Calculate position
        pos_x = (screen_width // 2) - (window_width // 2)
        pos_y = (screen_height // 2) - (window_height // 2)
        
        # Set window position
        self.root.geometry(f"+{pos_x}+{pos_y}")
    
    def on_closing(self):
        """
        Handle window closing event.
        """
        if messagebox.askokcancel("Keluar", "Yakin ingin keluar dari Quiz Duel Game?"):
            self.cleanup()
            self.root.destroy()
    
    def cleanup(self):
        """
        Cleanup resources sebelum aplikasi ditutup.
        """
        try:
            # Stop any running timers
            if self.game:
                self.game.timer_running = False
            
        except Exception as e:
            print(f"Error during cleanup: {e}")
    
    def show_error(self, message):
        """
        Menampilkan error message.
        
        Args:
            message (str): Pesan error
        """
        if self.root:
            messagebox.showerror("Error", message)
        else:
            print(f"ERROR: {message}")
    
    def run(self):
        """
        Menjalankan aplikasi.
        """
        try:
            print("🎮 Starting Quiz Duel Game...")
            print("📚 Tugas Besar Object-Oriented Programming")
            print("=" * 50)
            
            # Check required directories
            self.check_directories()
            
            # Start main loop
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
        """
        Periksa dan buat direktori yang diperlukan.
        """
        required_dirs = ["data", "models", "ui"]
        
        for directory in required_dirs:
            if not os.path.exists(directory):
                try:
                    os.makedirs(directory)
                    print(f"📁 Created directory: {directory}")
                except OSError as e:
                    print(f"❌ Failed to create directory {directory}: {e}")
        
        # Check required files
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
    """
    Fungsi main untuk menjalankan aplikasi Quiz Duel.
    """
    print("🚀 Initializing Quiz Duel Game...")
    
    # Check Python version
    if sys.version_info < (3, 6):
        print("❌ Python 3.6 atau lebih baru diperlukan!")
        sys.exit(1)
    
    # Check if running in proper environment
    try:
        import tkinter
    except ImportError:
        print("❌ Tkinter tidak tersedia! Install Python dengan tkinter support.")
        sys.exit(1)
    
    # Create and run application
    try:
        app = QuizDuelApp()
        app.run()
    except Exception as e:
        print(f"💥 Fatal error starting application: {e}")
        input("Press Enter to exit...")
        sys.exit(1)

if __name__ == "__main__":
    main()