import json

from models import Answer, Question, VillagerTrait


def load_questions():
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
