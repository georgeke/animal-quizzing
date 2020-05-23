from typing import List, Optional, TypedDict


class Answer(TypedDict):
    text: str
    url: str
    villagerTrait: str  # TODO: change to enum?


class Question(TypedDict):
    questionId: str
    questionText: str
    questionFormat: str
    villagerTrait: str
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
    color: List[str]
    style: List[str]
