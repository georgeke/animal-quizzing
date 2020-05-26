from models import AnsweredQuestion, Villager
from typing import Dict, List, Mapping, Set, Sequence


def filter_villagers(
    villagers: Sequence[Villager], answered_questions: Sequence[AnsweredQuestion]
) -> List[Villager]:
    trait_to_trait_values: Dict[str, Set[str]] = {}
    for question in answered_questions:
        trait = question["villagerTrait"]
        if trait not in trait_to_trait_values:
            trait_to_trait_values[trait] = set()

        chosen_trait_value = question["answer"]["traitValue"]
        if type(chosen_trait_value) is list:
            trait_to_trait_values[trait].update(chosen_trait_value)
        else:
            trait_to_trait_values[trait].add(chosen_trait_value)

    return [
        villager
        for villager in villagers
        if _villager_traits_match_answers(villager, trait_to_trait_values)
    ]


def _villager_traits_match_answers(
    villager: Villager, trait_to_trait_values: Mapping[str, Set[str]]
) -> bool:
    for trait, chosen_trait_values in trait_to_trait_values.items():
        chosen_trait_values = {s.lower() for s in chosen_trait_values}
        villager_trait_value = villager[trait]  # type: ignore
        match_found = False

        if type(villager_trait_value) is list:
            villager_trait_value = {v.lower() for v in villager_trait_value}
            match_found = villager_trait_value & chosen_trait_values
        else:
            match_found = villager_trait_value.lower() in chosen_trait_values

        if match_found:
            return True
    return False
