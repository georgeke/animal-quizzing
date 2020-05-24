from models import AnsweredQuestion, Villager
from typing import Dict, Mapping, Set, Sequence


def filter_villagers(
    villagers: Sequence[Villager], answered_questions: Sequence[AnsweredQuestion]
) -> Sequence[Villager]:
    trait_to_trait_values: Dict[str, Set[str]] = {}
    for question in answered_questions:
        trait = question["villagerTrait"]
        if trait not in trait_to_trait_values:
            trait_to_trait_values[trait] = set()

        trait_to_trait_values[trait].add(trait)

    return [
        villager
        for villager in villagers
        if _filter_villager_with_trait_map(villager, trait_to_trait_values)
    ]


def _filter_villager_with_trait_map(
    villager: Villager, trait_to_trait_values: Mapping[str, Set[str]]
) -> bool:
    for trait, trait_values in trait_to_trait_values.items():
        is_filtered = False
        if trait in ("color", "styles"):
            is_filtered = villager[trait] & trait_values  # type: ignore
        is_filtered = villager[trait] in trait_values  # type: ignore

        if is_filtered:
            return False
    return True
