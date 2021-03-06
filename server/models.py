from typing import List, Optional, TypedDict


class Answer(TypedDict):
    text: Optional[str]
    imageUrl: Optional[str]
    audioUrl: Optional[str]
    traitValue: str


class QuestionBase(TypedDict):
    questionId: str
    questionText: str
    questionFormat: str
    villagerTrait: str


class QuestionBlueprint(QuestionBase):
    """ Used to generate a Question instance"""

    answers: List[Answer]
    generateSource: Optional[str]
    generateSourceCategory: Optional[str]


class Question(QuestionBase):
    """ A question that is returned to the client """

    answers: List[Answer]


class AnsweredQuestion(QuestionBase):
    """ An answered question passed back from the client """

    answer: Answer


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
    colors: List[str]
    styles: List[str]


class ItemVariant(TypedDict):
    imageUrl: str
    colors: List[str]


class Item(TypedDict):
    category: str
    name: str
    style: Optional[str]
    variants: List[ItemVariant]
