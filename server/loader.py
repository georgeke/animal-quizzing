import json

from models import Answer, Question, Villager, VillagerTrait
from typing import Sequence


def load_questions() -> Sequence[Question]:
    with open("../db/questions.json") as f:
        data = json.load(f)

    question_types = []
    for question_data in data:
        answers = []
        for answer_data in question_data.get("answers", []):
            answers.append(
                Answer(
                    text=answer_data.get("text"),
                    url=answer_data.get("url"),
                    trait_value=answer_data["traitValue"],
                )
            )
        question_types.append(
            Question(
                questionId=question_data["questionId"],
                questionText=question_data["questionText"],
                questionFormat=question_data["questionFormat"],
                villagerTrait=VillagerTrait(question_data["villagerTrait"]),
                answers=answers,
                generateSource=question_data.get("generateSource"),
                generateSourceCategory=question_data.get("generateSourceCategory"),
            )
        )
    return question_types


def load_villagers() -> Sequence[Villager]:
    with open("../db/villagers.json") as f:
        data = json.load(f)

    return [
        Villager(
            name=villager_data["name"],
            profileImageUrl=villager_data["iconImage"],
            houseImageUrl=villager_data["houseImage"],
            species=villager_data["species"],
            gender=villager_data["gender"],
            personality=villager_data["personality"],
            hobby=villager_data["hobby"],
            birthday=villager_data["birthday"],
            catchphrase=villager_data["catchphrase"],
            song=villager_data["favoriteSong"],
            color=villager_data["colors"],
            style=villager_data["styles"],
        )
        for villager_data in data
    ]
