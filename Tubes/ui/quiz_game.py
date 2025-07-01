
import tkinter as tk
from tkinter import messagebox, ttk
import json
import random

from models.question import Question
from models.player import Player

class QuizDuelGame:
    def __init__(self, root):
        self.root = root
  
        self.players = []
        self.questions = []
        self.filtered_questions = []
        self.current_index = 0
        self.turn = 0
        self.time_left = 10
        self.timer_job = None
        self.timer_label = None

        self.game_mode = "Normal"
        self.settings = {
            "time_limit": 10,
            "questions_per_game": 5,
            "show_explanation": True
        }

        self.load_settings()
        self.load_questions()
        self.setup_start_screen()

    def clear_window(self):
        """Clear all widgets from the window."""
        for widget in self.root.winfo_children():
            widget.destroy()
        self.timer_label = None
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None

    def load_settings(self):
        """Load game settings from settings.json."""
        try:
            with open("data/settings.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                self.settings.update(data)
                print("✅ Pengaturan berhasil dimuat.")
        except FileNotFoundError:
            print("⚠️ File settings.json tidak ditemukan. Menggunakan pengaturan default.")
        except Exception as e:
            print(f"❌ Gagal memuat settings: {e}")

    def load_questions(self):
        """Load questions from questions.json or create sample questions if not found."""
        try:
            with open("data/questions.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            self.questions = [Question(**q) for q in data]
            if not self.questions:
                print("⚠️ Tidak ada soal ditemukan.")
        except FileNotFoundError:
            print("⚠️ File questions.json tidak ditemukan.")
        except Exception as e:
            messagebox.showerror("Error", f"Error loading questions: {str(e)}")

    def setup_start_screen(self):
        """Set up the start screen with player input and game settings."""
        self.clear_window()

        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        title_label = tk.Label(main_frame, text="Quiz Duel Game",
                               font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#2c3e50")
        title_label.pack(pady=20)

        input_frame = tk.LabelFrame(main_frame, text="Setup Pemain",
                                    font=("Arial", 14, "bold"), bg="#f0f0f0")
        input_frame.pack(pady=20, padx=50, fill="x")

        tk.Label(input_frame, text="Nama Pemain 1:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        self.player1_entry = tk.Entry(input_frame, font=("Arial", 12), width=30)
        self.player1_entry.pack(pady=5)

        tk.Label(input_frame, text="Nama Pemain 2:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        self.player2_entry = tk.Entry(input_frame, font=("Arial", 12), width=30)
        self.player2_entry.pack(pady=5)

        settings_frame = tk.LabelFrame(main_frame, text="Pengaturan Permainan",
                                       font=("Arial", 14, "bold"), bg="#f0f0f0")
        settings_frame.pack(pady=20, padx=50, fill="x")

        tk.Label(settings_frame, text="Pilih Kategori:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        self.category_combobox = ttk.Combobox(settings_frame, values=self.get_categories(),
                                              font=("Arial", 12), width=28, state="readonly")
        self.category_combobox.pack(pady=5)

        tk.Label(settings_frame, text="Mode Permainan:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        self.mode_var = tk.StringVar(value="Normal")
        mode_frame = tk.Frame(settings_frame, bg="#f0f0f0")
        mode_frame.pack(pady=5)

        modes = [("Normal", "Normal"), ("Timed Challenge", "Timed")]
        for text, value in modes:
            tk.Radiobutton(mode_frame, text=text, variable=self.mode_var, value=value,
                           font=("Arial", 10), bg="#f0f0f0").pack(side="left", padx=10)

        start_button = tk.Button(main_frame, text="Start", command=self.start_game,
                                 font=("Arial", 14, "bold"), bg="#27ae60", fg="white", width=15, height=2, borderwidth=0)
        start_button.pack(pady=20)

    def get_categories(self):
        """Get a list of available question categories."""
        if not self.questions:
            return ["Umum"]
        categories = sorted(set(q.category for q in self.questions))
        categories.insert(0, "Semua Kategori")
        return categories

    def start_game(self):
        """Start a new game with selected players and settings."""
        name1 = self.player1_entry.get().strip()
        name2 = self.player2_entry.get().strip()

        if not name1 or not name2:
            messagebox.showwarning("Peringatan", "Nama kedua pemain harus diisi!")
            return

        self.players = [Player(name1), Player(name2)]
        for player in self.players:
            player.reset_stats()  
        self.game_mode = self.mode_var.get()
        selected_category = self.category_combobox.get()

        if selected_category != "Semua Kategori":
            self.filtered_questions = [q for q in self.questions if q.category == selected_category]
        else:
            self.filtered_questions = self.questions.copy()

        if len(self.filtered_questions) < self.settings["questions_per_game"]:
            messagebox.showerror("Error", "Jumlah soal di kategori ini tidak cukup.")
            return

        random.shuffle(self.filtered_questions)
        self.current_index = 0
        self.turn = 0
        self.show_question_screen()

    def show_question_screen(self):
        """Display the question screen for the current player."""
        self.clear_window()

        if self.current_index >= self.settings["questions_per_game"]:
            self.show_result_screen()
            return

        current_player = self.players[self.turn % 2]
        current_question = self.filtered_questions[self.current_index]

        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Judul pertanyaan
        tk.Label(frame, text=f"Pertanyaan {self.current_index + 1}",
                font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

        # Nama pemain saat ini
        tk.Label(frame, text=f"Giliran: {current_player.name}",
                font=("Arial", 14), fg="#2980b9", bg="#f0f0f0").pack(pady=5)

        difficulty_colors = {
                "Easy": "#2ecc71",     
                "Medium": "#f1c40f",   
                "Hard": "#e74c3c"      
            }
        difficulty_color = difficulty_colors.get(current_question.difficulty)

        tk.Label(frame, text=f"Tingkat Kesulitan: {current_question.difficulty}",
                font=("Arial", 12, "bold"), fg=difficulty_color, bg="#f0f0f0").pack(pady=2)
        
        question_label = tk.Label(frame, text=current_question.question,
                                font=("Arial", 14), wraplength=600,
                                justify="center", bg="#f0f0f0")
        question_label.pack(pady=15)
        question_label.pack_configure(anchor="center")

        # Variabel untuk jawaban yang dipilih
        self.answer_var = tk.StringVar()

        # Opsi jawaban
        options_frame = tk.Frame(frame, bg="#f0f0f0")
        options_frame.pack(pady=10)

        for option in current_question.options:
            tk.Radiobutton(options_frame, text=option, variable=self.answer_var, value=option,
                        font=("Arial", 12), bg="#f0f0f0", anchor="w").pack(anchor="w", padx=40, pady=2)

        # Tombol submit
        submit_btn = tk.Button(frame, text="Submit", bg="#27ae60", fg="white",  borderwidth=0, width=10,
                            font=("Arial", 12, "bold"), command=self.check_answer)
        submit_btn.pack(pady=20)

        # Timer (jika mode timed)
        if self.game_mode == "Timed":
            self.time_left = self.settings["time_limit"]
            self.timer_label = tk.Label(frame, text=f"Sisa Waktu: {self.time_left} detik",
                                        font=("Arial", 12), fg="red", bg="#f0f0f0")
            self.timer_label.pack(pady=5)
            self.countdown_timer()

    def countdown_timer(self):
        """Run the countdown timer for Timed mode."""
        if self.time_left > 0:
            self.timer_label.config(text=f"Sisa Waktu: {self.time_left} detik")
            self.time_left -= 1
            self.timer_job = self.root.after(1000, self.countdown_timer)
        else:
            self.timer_label.config(text="Waktu Habis!")
            self.check_answer(time_up=True)

    def check_answer(self, time_up=False):
        """Periksa jawaban yang dipilih dan perbarui skor."""
        # Cegah timer jalan terus setelah jawaban masuk
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None

        current_question = self.filtered_questions[self.current_index]
        current_player = self.players[self.turn % 2]
        selected = "" if time_up else self.answer_var.get()

        # Kalau tidak pilih jawaban (dan bukan karena waktu habis), beri peringatan
        if not selected and not time_up:
            messagebox.showwarning("Peringatan", "Pilih salah satu jawaban terlebih dahulu!")
            return

        current_player.add_attempt()

        is_correct = current_question.is_correct(selected)
        explanation = f"\nPenjelasan: {current_question.explanation}" if self.settings["show_explanation"] else ""

        if is_correct:
            points = current_question.get_difficulty_points() * 100
            current_player.add_score(points)
            messagebox.showinfo("Benar!", f"✅ Jawaban benar!\nSkor: {current_player.score}{explanation}")
        else:
            if time_up:
                message = f"❌ Waktu habis!\nJawaban benar: {current_question.answer}{explanation}"
            else:
                message = f"❌ Jawaban salah.\nJawaban benar: {current_question.answer}{explanation}"
            messagebox.showinfo("Salah!", message)

        # Tambahkan giliran (ganti pemain)
        self.turn += 1

        # Kalau dua pemain sudah menjawab soal ini, lanjut ke soal berikutnya
        if self.turn % 2 == 0:
            self.current_index += 1

        self.show_question_screen()

    def show_result_screen(self):
        """Display the game result screen."""
        self.clear_window()

        winner = max(self.players, key=lambda p: p.score)
        draw = self.players[0].score == self.players[1].score

        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(frame, text="Permainan Selesai!", font=("Arial", 20, "bold"),
                 bg="#f0f0f0").pack(pady=20)

        if draw:
            tk.Label(frame, text="Hasil: Seri!", font=("Arial", 16), bg="#f0f0f0").pack(pady=10)
        else:
            tk.Label(frame, text=f"Pemenang: {winner.name}", font=("Arial", 16),
                     bg="#f0f0f0").pack(pady=10)

        for player in self.players:
            tk.Label(frame, text=f"{player.name}: {player.score} poin (Akurasi: {player.get_accuracy():.1f}%)",
                     font=("Arial", 14), bg="#f0f0f0").pack(pady=5)

        tk.Button(frame, text="Main Lagi", font=("Arial", 12), bg="#27ae60", fg="white", borderwidth=0,
                  command=self.setup_start_screen).pack(pady=20)
