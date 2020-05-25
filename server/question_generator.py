import random

from models import Question, QuestionBlueprint, AnsweredQuestion
from typing import Sequence


def generate_filter_question(
    questions: Sequence[QuestionBlueprint], answers: Sequence[AnsweredQuestion]
) -> Question:
    filter_question_ids = ["1", "2", "3", "4", "5"]
    # TODO: also add "10", "11", "12", "13", "14", "15", "16", "17"

    random.shuffle(filter_question_ids)
    question_id = _get_question_id_not_used(filter_question_ids, answers)

    question_blueprint = _get_question_with_id(questions, question_id)

    # TODO: check here if question has generateSource
    random.shuffle(question_blueprint["answers"])
    return Question(
        questionId=question_blueprint["questionId"],
        questionText=question_blueprint["questionText"],
        questionFormat=question_blueprint["questionFormat"],
        villagerTrait=question_blueprint["villagerTrait"],
        answers=question_blueprint["answers"][:4],
    )


def generate_score_question(
    questions: Sequence[QuestionBlueprint],
    answers: Sequence[AnsweredQuestion],
) -> Question:
    # for now, just return song question
    question_blueprint = _get_question_with_id(questions, "6")

    # TODO: check here if question has generateSource
    random.shuffle(question_blueprint["answers"])
    return Question(
        questionId=question_blueprint["questionId"],
        questionText=question_blueprint["questionText"],
        questionFormat=question_blueprint["questionFormat"],
        villagerTrait=question_blueprint["villagerTrait"],
        answers=question_blueprint["answers"][:4],
    )


def _get_question_id_not_used(
    question_ids: Sequence[str], answers: Sequence[AnsweredQuestion]
) -> str:
    if len(answers) == 0:
        return question_ids[0]

    for question_id in question_ids:
        for answer in answers:
            if answer["questionId"] != question_id:
                return question_id


def _get_question_with_id(
    questions: Sequence[QuestionBlueprint], question_id: str
) -> QuestionBlueprint:
    for question in questions:
        if question["questionId"] == question_id:
            return question
    raise Exception()
