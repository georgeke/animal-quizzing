import random

from models import Answer, AnsweredQuestion, Question, QuestionBlueprint, Villager
from loader import load_items, load_villagers
from scorer import filter_villagers
from typing import Optional, List, Sequence


HARDCODED_TEXT_QUESTION_IDS = ["1", "2", "3", "4", "5"]
HARDCODED_AUDIO_QUESTION_IDS = ["6"]
GENERATED_COLOR_QUESTION_IDS = ["7", "8", "9"]
GENERATED_CLOTHING_QUESTION_IDS = ["10", "11", "12", "13", "14", "15", "16"]
GENERATED_MISC_QUESTION_IDS = ["18"]


def generate_filter_question(
    questions: Sequence[QuestionBlueprint], answers: Sequence[AnsweredQuestion]
) -> Question:
    filter_question_ids = list(
        HARDCODED_TEXT_QUESTION_IDS
        + GENERATED_COLOR_QUESTION_IDS
        + GENERATED_CLOTHING_QUESTION_IDS
    )

    random.shuffle(filter_question_ids)
    question_id = _get_question_id_not_used(filter_question_ids, answers)

    question_blueprint = _get_question_blueprint_with_id(questions, question_id)

    if question_blueprint.get("generateSource"):
        question = _get_generated_question_from_question_blueprint(
            question_blueprint, load_villagers()
        )
        if question:
            return question
        raise ValueError(
            f"No answers were generated for blueprint {question_blueprint}"
        )

    return _get_question_from_question_blueprint(question_blueprint)


def generate_score_question(
    questions: Sequence[QuestionBlueprint], answers: Sequence[AnsweredQuestion],
) -> Question:
    scoring_question_ids = list(
        HARDCODED_TEXT_QUESTION_IDS
        + HARDCODED_AUDIO_QUESTION_IDS
        + GENERATED_CLOTHING_QUESTION_IDS
        + GENERATED_MISC_QUESTION_IDS
    )

    random.shuffle(scoring_question_ids)
    question_id = _get_question_id_not_used(scoring_question_ids, answers)

    question_blueprint = _get_question_blueprint_with_id(questions, question_id)

    if question_blueprint.get("generateSource"):
        filtered_villagers = filter_villagers(load_villagers(), answers)
        print(len(filtered_villagers))
        question = _get_generated_question_from_question_blueprint(
            question_blueprint, filtered_villagers
        )
        if question:
            return question
        raise ValueError(
            f"No answers were generated for blueprint {question_blueprint}"
        )

    return _get_question_from_question_blueprint(question_blueprint)


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


def _get_question_from_question_blueprint(blueprint: QuestionBlueprint) -> Question:
    random.shuffle(blueprint["answers"])
    if blueprint["questionFormat"] == "audio":
        answers = blueprint["answers"][:2]
    else:
        answers = []
        trait_value_set = set()
        for answer in blueprint["answers"]:
            trait_value = answer["traitValue"]
            if trait_value not in trait_value_set:
                trait_value_set.add(trait_value)
                answers.append(answer)
            if len(trait_value_set) == 4:
                break
        assert len(answers) == 4

    return Question(
        questionId=blueprint["questionId"],
        questionText=blueprint["questionText"],
        questionFormat=blueprint["questionFormat"],
        villagerTrait=blueprint["villagerTrait"],
        answers=answers,
    )


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
    elif source == "items" and villager_trait == "colors":
        answers = _generate_answers_for_non_clothing_items(blueprint, villagers)
    elif source == "items" and villager_trait == "styles":
        answers = _generate_answers_for_clothing_items(blueprint, villagers)

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

        color_set = set()
        for v in variants:
            colors = v.get("colors")
            if colors:
                color_set.add(colors[0])

        if len(color_set) < 4:
            continue

        random.shuffle(variants)
        answers = []
        for variant in variants:
            primary_color = variant["colors"][0]
            if primary_color not in color_set:
                continue
            answers.append(
                Answer(
                    imageUrl=variant["imageUrl"],
                    audioUrl=None,
                    text=None,
                    traitValue=primary_color,
                )
            )
            color_set.remove(primary_color)

        assert len(answers) >= 4
        return answers[:4]
    raise ValueError(
        f"Item category {item_category} has no items with 4 or more variants with different colors!"
    )


def _generate_answers_for_clothing_items(
    blueprint: QuestionBlueprint, villagers: List[Villager],
) -> List[Answer]:
    item_category = blueprint["generateSourceCategory"]
    assert item_category
    items = load_items()[item_category]
    random.shuffle(items)

    answers = []
    styles = set()
    for item in items:
        style = item["style"]
        assert style

        variants = item["variants"]

        if style in styles:
            continue

        if len(variants) > 1:
            random.shuffle(variants)

        variant = variants[0]

        styles.add(style)
        answers.append(
            Answer(
                imageUrl=variant["imageUrl"], audioUrl=None, text=None, traitValue=style
            )
        )
    return answers[:4]
