import random

class Question:
    """
    Class untuk merepresentasikan pertanyaan dalam permainan Quiz Duel.
    
    Attributes:
        category (str): Kategori pertanyaan
        question (str): Teks pertanyaan
        options (list): List pilihan jawaban
        answer (str): Jawaban yang benar
        difficulty (str): Tingkat kesulitan pertanyaan
        explanation (str): Penjelasan jawaban
    """
    
    def __init__(self, category, question, options, answer, difficulty="Medium", explanation=""):
        """
        Inisialisasi objek Question.
        
        Args:
            category (str): Kategori pertanyaan
            question (str): Teks pertanyaan
            options (list): List pilihan jawaban
            answer (str): Jawaban yang benar
            difficulty (str): Tingkat kesulitan (Easy, Medium, Hard)
            explanation (str): Penjelasan jawaban
        """
        self.category = category
        self.question = question
        self.options = options
        self.answer = answer
        self.difficulty = difficulty
        self.explanation = explanation
        self.times_asked = 0
        self.times_correct = 0
    
    def is_correct(self, choice):
        """
        Mengecek apakah pilihan jawaban benar.
        
        Args:
            choice (str): Pilihan jawaban yang dipilih
            
        Returns:
            bool: True jika benar, False jika salah
        """
        self.times_asked += 1
        is_right = choice == self.answer
        if is_right:
            self.times_correct += 1
        return is_right
    
    def get_difficulty_points(self):
        """
        Mendapatkan poin berdasarkan tingkat kesulitan.
        
        Returns:
            int: Jumlah poin yang diberikan
        """
        difficulty_points = {
            "Easy": 1,
            "Medium": 2,
            "Hard": 3
        }
        return difficulty_points.get(self.difficulty, 1)
    
    def get_success_rate(self):
        """
        Menghitung tingkat keberhasilan pertanyaan.
        
        Returns:
            float: Persentase keberhasilan (0-100)
        """
        if self.times_asked == 0:
            return 0.0
        return (self.times_correct / self.times_asked) * 100
    
    def shuffle_options(self):
        """
        Mengacak urutan pilihan jawaban.
        
        Returns:
            list: List pilihan jawaban yang sudah diacak
        """
        shuffled = self.options.copy()
        random.shuffle(shuffled)
        return shuffled
    
    def get_hint(self):
        """
        Memberikan hint untuk pertanyaan.
        
        Returns:
            str: Hint pertanyaan
        """
        if len(self.answer) > 1:
            return f"Hint: Jawaban dimulai dengan huruf '{self.answer[0]}'"
        return "Hint: Jawaban hanya satu huruf"
    
    def validate_question(self):
        """
        Memvalidasi kelengkapan data pertanyaan.
        
        Returns:
            bool: True jika valid, False jika tidak
        """
        if not self.question or not self.options or not self.answer:
            return False
        if len(self.options) < 2:
            return False
        if self.answer not in self.options:
            return False
        return True
    
    def __str__(self):
        """
        String representation dari objek Question.
        
        Returns:
            str: Informasi pertanyaan dalam format string
        """
        return f"[{self.category}] {self.question[:50]}..."
    
    def __repr__(self):
        """
        Developer representation dari objek Question.
        
        Returns:
            str: Representasi untuk debugging
        """
        return f"Question(category='{self.category}', difficulty='{self.difficulty}')"
    
    def to_dict(self):
        """
        Konversi objek Question ke dictionary untuk serialisasi.
        
        Returns:
            dict: Data pertanyaan dalam format dictionary
        """
        return {
            "category": self.category,
            "question": self.question,
            "options": self.options,
            "answer": self.answer,
            "difficulty": self.difficulty,
            "explanation": self.explanation,
            "times_asked": self.times_asked,
            "times_correct": self.times_correct,
            "success_rate": self.get_success_rate()
        }