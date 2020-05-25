import random

from models import Answer, AnsweredQuestion, Question, QuestionBlueprint, Villager
from loader import load_items, load_villagers
from typing import Optional, List, Sequence


def generate_filter_question(
    questions: Sequence[QuestionBlueprint], answers: Sequence[AnsweredQuestion]
) -> Question:
    filter_question_ids = ["6"]  # ["1", "2", "3", "4", "5"]
    # TODO: also add "10", "11", "12", "13", "14", "15", "16", "17"

    random.shuffle(filter_question_ids)
    question_id = _get_question_id_not_used(filter_question_ids, answers)

    question_blueprint = _get_question_blueprint_with_id(questions, question_id)

    if question_blueprint.get("generateSource"):
        question = _get_generated_question_from_question_blueprint(
            question_blueprint, load_villagers()
        )
        if question:
            return question

    random.shuffle(question_blueprint["answers"])
    return Question(
        questionId=question_blueprint["questionId"],
        questionText=question_blueprint["questionText"],
        questionFormat=question_blueprint["questionFormat"],
        villagerTrait=question_blueprint["villagerTrait"],
        answers=question_blueprint["answers"][:4],
    )


def generate_score_question(
    questions: Sequence[QuestionBlueprint], answers: Sequence[AnsweredQuestion],
) -> Question:
    # for now, just return song question
    question_blueprint = _get_question_blueprint_with_id(questions, "18")
    print(question_blueprint)

    if question_blueprint.get("generateSource"):
        question = _get_generated_question_from_question_blueprint(
            question_blueprint, load_villagers()
        )
        if question:
            return question

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

    answer_ids = {answer["questionId"] for answer in answers}

    for question_id in question_ids:
        if question_id not in answer_ids:
            return question_id
    raise Exception()


def _get_question_blueprint_with_id(
    questions: Sequence[QuestionBlueprint], question_id: str
) -> QuestionBlueprint:
    for question in questions:
        if question["questionId"] == question_id:
            return question
    raise Exception()


def _get_generated_question_from_question_blueprint(
    blueprint: QuestionBlueprint, villagers: List[Villager],
) -> Optional[Question]:
    source = blueprint["generateSource"]
    villager_trait = blueprint["villagerTrait"]
    answers: Optional[List[Answer]] = None
    random.shuffle(villagers)

    if source == "catchphrase":
        answers = [
            Answer(
                imageUrl=None,
                audioUrl=None,
                text=f"\"{villager['catchphrase']}\"",
                traitValue=villager["catchphrase"],
            )
            for villager in villagers[:4]
        ]
    elif source == "items" and villager_trait == "color":
        answers = _generate_answers_for_non_clothing_items(blueprint, villagers)

    if answers:
        return Question(
            questionId=blueprint["questionId"],
            questionText=blueprint["questionText"],
            questionFormat=blueprint["questionFormat"],
            villagerTrait=blueprint["villagerTrait"],
            answers=answers,
        )
    return None


def _generate_answers_for_non_clothing_items(
    blueprint: QuestionBlueprint, villagers: List[Villager],
) -> List[Answer]:
    item_category = blueprint["generateSourceCategory"]
    assert item_category
    items = load_items()[item_category]
    random.shuffle(items)

    for item in items:
        variants = item["variants"]
        if len(variants) < 4:
            continue
        colors_set = set(tuple(v.get("colors", [])) for v in variants)
        if len(colors_set) < 4:
            continue

        answers = []
        for variant in variants:
            colors = tuple(variant["colors"])
            if colors not in colors_set:
                continue
            answers.append(
                Answer(
                    imageUrl=variant["imageUrl"],
                    audioUrl=None,
                    text=None,
                    traitValue=list(colors),
                )
            )
            colors_set.remove(colors)

        return answers[:4]
    raise ValueError(
        f"Item category {item_category} has no items with 4 or more variants with different colors!"
    )
