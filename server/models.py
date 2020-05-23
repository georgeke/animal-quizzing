from enum import Enum
from typing import List, Optional, TypedDict


class VillagerTrait(Enum):
    CATCHPHRASE = "catchphrase"
    COLOR = "color"
    FURNITURE = "furniture"
    HOBBY = "hobby"
    PERSONALITY = "personality"
    SONG = "song"
    STYLE = "style"


class Answer(TypedDict):
    text: str
    url: str
    villagerTrait: str  # TODO: change to enum?


class Question(TypedDict):
    questionId: str
    questionText: str
    questionFormat: str
    villagerTrait: VillagerTrait
    answers: List[Answer]
    generateSource: Optional[str]
    generateSourceCategory: Optional[str]


class Villager(TypedDict):
    name: str
    profileImageUrl: str
    houseImageUrl: str
    species: str
    gender: str
    personality: str
    hobby: str
    birthday: str
    catchphrase: str
    song: str
    song: str
    color: List[str]
    style: List[str]
