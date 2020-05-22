from dataclasses import dataclass
from enum import Enum
from typing import List


class TraitType(Enum):
    PERSONALITY = "personality"


@dataclass
class Answer:
    text: str
    trait_value: str  # TODO: change to enum?


@dataclass
class QuestionType:
    text: str
    trait_type: TraitType
    score: int
    answers: List[Answer]
