from models import AnsweredQuestion, Villager
from typing import Sequence


def filter_villagers(
    villagers: Sequence[Villager], answered_questions: Sequence[AnsweredQuestion]
) -> Sequence[Villager]:
    filtered_villagers = villagers
    for question in answered_questions:
        filtered_villagers = [
            villager
            for villager in filtered_villagers
            if _filter_villager_with_single_question(villager, question)
        ]
    return list(filtered_villagers)


def _filter_villager_with_single_question(
    villager: Villager, question: AnsweredQuestion
) -> bool:
    villager_trait = question["villagerTrait"]
    if villager_trait in ("color", "styles"):
        return question["answer"]["traitValue"] in villager[villager_trait]
    return question["answer"]["traitValue"] == villager[villager_trait]
