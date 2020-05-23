import json

from models import Answer, AnsweredQuestion, QuestionBlueprint, Villager
from typing import Any, Dict, Sequence


def load_answered_questions(
    data: Sequence[Dict[str, Any]]
) -> Sequence[AnsweredQuestion]:
    return [
        QuestionBlueprint(
            questionId=question_data["questionId"],
            questionText=question_data["questionText"],
            questionFormat=question_data["questionFormat"],
            villagerTrait=question_data["villagerTrait"],
            answer=Answer(
                text=question_data["answer"].get("text"),
                url=question_data["answer"].get("url"),
                traitValue=question_data["answer"]["traitValue"],
            ),
        )
        for question_data in data
    ]


def load_question_blueprints() -> Sequence[QuestionBlueprint]:
    with open("db/questions.json") as f:
        data = json.load(f)

    question_types = []
    for question_data in data:
        answers = []
        for answer_data in question_data.get("answers", []):
            answers.append(
                Answer(
                    text=answer_data.get("text"),
                    url=answer_data.get("url"),
                    traitValue=answer_data["traitValue"],
                )
            )
        question_types.append(
            QuestionBlueprint(
                questionId=question_data["questionId"],
                questionText=question_data["questionText"],
                questionFormat=question_data["questionFormat"],
                villagerTrait=question_data["villagerTrait"],
                answers=answers,
                generateSource=question_data.get("generateSource"),
                generateSourceCategory=question_data.get("generateSourceCategory"),
            )
        )
    return question_types


def load_villagers() -> Sequence[Villager]:
    with open("db/villagers.json") as f:
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
