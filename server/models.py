from typing import List, Optional, TypedDict


class Answer(TypedDict):
    text: Optional[str]
    url: Optional[str]
    villagerTrait: str  # TODO: change to enum?


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
    color: List[str]
    style: List[str]
