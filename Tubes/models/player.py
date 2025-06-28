class Player:
    """
    Class untuk merepresentasikan pemain dalam permainan Quiz Duel.
    
    Attributes:
        name (str): Nama pemain
        score (int): Skor pemain
        correct_answers (int): Jumlah jawaban benar
        total_answers (int): Total jawaban yang diberikan
    """
    
    def __init__(self, name):
        """
        Inisialisasi objek Player.
        
        Args:
            name (str): Nama pemain
        """
        self.name = name
        self.score = 0
        self.correct_answers = 0
        self.total_answers = 0
    
    def add_score(self, points=1):
        """
        Menambah skor pemain.
        
        Args:
            points (int): Jumlah poin yang ditambahkan (default: 1)
        """
        self.score += points
        self.correct_answers += 1
    
    def add_attempt(self):
        """
        Menambah jumlah total percobaan jawaban.
        """
        self.total_answers += 1
    
    def get_accuracy(self):
        """
        Menghitung akurasi pemain.
        
        Returns:
            float: Persentase akurasi (0-100)
        """
        if self.total_answers == 0:
            return 0.0
        return (self.correct_answers / self.total_answers) * 100
    
    def reset_stats(self):
        """
        Reset statistik pemain untuk permainan baru.
        """
        self.score = 0
        self.correct_answers = 0
        self.total_answers = 0
    
    def __str__(self):
        """
        String representation dari objek Player.
        
        Returns:
            str: Informasi pemain dalam format string
        """
        return f"Player: {self.name}, Score: {self.score}, Accuracy: {self.get_accuracy():.1f}%"
    
    def __repr__(self):
        """
        Developer representation dari objek Player.
        
        Returns:
            str: Representasi untuk debugging
        """
        return f"Player(name='{self.name}', score={self.score})"
    
    def to_dict(self):
        """
        Konversi objek Player ke dictionary untuk serialisasi.
        
        Returns:
            dict: Data pemain dalam format dictionary
        """
        return {
            "name": self.name,
            "score": self.score,
            "correct_answers": self.correct_answers,
            "total_answers": self.total_answers,
            "accuracy": self.get_accuracy()
        }