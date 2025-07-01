"""Question model for Quiz Duel Game."""
import random
from typing import List, Dict


class Question:
    """Represents a quiz question with answers and metadata."""
    
    DIFFICULTY_POINTS = {
        "Easy": 1,
        "Medium": 2,
        "Hard": 3
    }

    def __init__(self, category: str, question: str, options: List[str], 
                 answer: str, difficulty: str = "Medium", explanation: str = ""):
        """Initialize a new question.
        
        Args:
            category: Question category
            question: The question text
            options: List of answer options
            answer: Correct answer
            difficulty: Difficulty level (Easy/Medium/Hard)
            explanation: Explanation of the answer
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
        """Check if the chosen answer is correct.
        
        Args:
            choice: The selected answer
            
        Returns:
            True if correct, False otherwise
        """
        self.times_asked += 1
        is_correct = choice == self.answer
        if is_correct:
            self.times_correct += 1
        return is_correct

    def get_difficulty_points(self) -> int:
        """Get points based on question difficulty.
        
        Returns:
            Points value for this question
        """
        return self.DIFFICULTY_POINTS.get(self.difficulty, 1)
