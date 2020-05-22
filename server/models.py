from enum import Enum
from typing import List, TypedDict


class TraitType(Enum):
    PERSONALITY = "personality"


class Answer(TypedDict):
    text: str
    url: str
    trait_value: str  # TODO: change to enum?


class QuestionType(TypedDict):
    text: str
    trait_type: TraitType
    answers: List[Answer]
