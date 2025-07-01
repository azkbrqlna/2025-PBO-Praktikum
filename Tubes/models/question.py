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

    def shuffle_options(self) -> List[str]:
        """Return a shuffled copy of the answer options.
        
        Returns:
            Shuffled list of options
        """
        return random.sample(self.options, len(self.options))

    def validate(self) -> bool:
        """Validate the question data.
        
        Returns:
            True if valid, False otherwise
        """
        return (self.question and len(self.options) >= 2 and 
                self.answer in self.options)

    def __str__(self) -> str:
        """String representation of the question."""
        return f"[{self.category}] {self.question[:50]}..."

    def to_dict(self) -> Dict:
        """Convert question to dictionary for serialization.
        
        Returns:
            Dictionary representation of the question
        """
        return {
            "category": self.category,
            "question": self.question,
            "options": self.options,
            "answer": self.answer,
            "difficulty": self.difficulty,
            "explanation": self.explanation
        }