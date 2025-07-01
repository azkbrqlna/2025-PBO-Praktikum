"""Model Question untuk permainan Quiz Duel."""
import random
from typing import List


class Question:
    """Mewakili satu soal kuis dengan jawaban dan metadata tambahan."""
    
    DIFFICULTY_POINTS = {
        "Easy": 1,
        "Medium": 2,
        "Hard": 3
    }

    def __init__(self, category: str, question: str, options: List[str], 
                 answer: str, difficulty: str = "Medium", explanation: str = ""):
        """
        Inisialisasi soal baru.

        Parameter:
            category: Kategori soal
            question: Teks pertanyaan
            options: Pilihan jawaban
            answer: Jawaban yang benar
            difficulty: Tingkat kesulitan
            explanation: Penjelasan untuk jawaban benar
        """
        self.category = category
        self.question = question
        self.options = options
        self.answer = answer
        self.difficulty = difficulty
        self.explanation = explanation
        self.times_asked = 0
        self.times_correct = 0

    def is_correct(self, choice: str) -> bool:
        """
        Mengecek apakah jawaban yang dipilih benar dan mencatat statistik.

        Parameter:
            choice: Jawaban yang dipilih pemain

        Mengembalikan:
            True jika benar, False jika salah
        """
        self.times_asked += 1
        is_correct = choice == self.answer
        if is_correct:
            self.times_correct += 1
        return is_correct

    def get_difficulty_points(self) -> int:
        """
        Mengembalikan jumlah poin sesuai tingkat kesulitan soal.

        Mengembalikan:
            int: Jumlah poin (1, 2, atau 3)
        """
        return self.DIFFICULTY_POINTS.get(self.difficulty, 1)
