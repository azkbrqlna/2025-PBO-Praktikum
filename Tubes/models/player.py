"""Player model for Quiz Duel Game."""


class Player:
    """Represents a player in the game with score tracking."""
    
    def __init__(self, name: str):
        """Initialize a new player.
        
        Args:
            name: The player's name
        """
        self.name = name
        self.score = 0
        self.correct_answers = 0
        self.total_answers = 0

    def add_score(self, points: int = 100) -> None:
        """Add points to the player's score.
        
        Args:
            points: Points to add (default 100)
        """
        self.score += points
        self.correct_answers += 1

    def add_attempt(self) -> None:
        """Record an answer attempt."""
        self.total_answers += 1

    def get_accuracy(self) -> float:
        """Calculate the player's answer accuracy.
        
        Returns:
            Accuracy percentage (0-100)
        """
        if self.total_answers == 0:
            return 0.0
        return (self.correct_answers / self.total_answers) * 100

    def reset_stats(self) -> None:
        """Reset all player statistics."""
        self.score = 0
        self.correct_answers = 0
        self.total_answers = 0

    def __str__(self) -> str:
        """String representation of the player."""
        return f"{self.name} (Score: {self.score}, Accuracy: {self.get_accuracy():.1f}%)"