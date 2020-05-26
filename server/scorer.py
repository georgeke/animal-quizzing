from models import AnsweredQuestion, Villager
from typing import Dict, List, Mapping, Set, Sequence


FILTERING_TRAIT_BLACKLIST = ["song"]


def filter_villagers(
    villagers: Sequence[Villager], answered_questions: Sequence[AnsweredQuestion]
) -> List[Villager]:
    filtered_villagers = _filter_villagers(villagers, answered_questions[:5])
    print(len(filtered_villagers))
    for question in answered_questions[5:]:
        next_filtered_villagers = _filter_villagers(filtered_villagers, [question])

        # if we filter down to 0, that means the user chose a filler question so don't want to consider it
        if len(next_filtered_villagers) > 0:
            filtered_villagers = next_filtered_villagers

        print(len(filtered_villagers))
    return filtered_villagers


def _filter_villagers(
    villagers: Sequence[Villager], answered_questions: Sequence[AnsweredQuestion]
) -> List[Villager]:
    trait_to_trait_values: Dict[str, Set[str]] = {}
    for question in answered_questions:
        trait = question["villagerTrait"]
        if trait in FILTERING_TRAIT_BLACKLIST:
            continue

        if trait not in trait_to_trait_values:
            trait_to_trait_values[trait] = set()

        chosen_trait_value = question["answer"]["traitValue"]
        trait_to_trait_values[trait].add(chosen_trait_value)

    return [
        villager
        for villager in villagers
        if _villager_traits_match_answers(villager, trait_to_trait_values)
    ]


def _villager_traits_match_answers(
    villager: Villager, trait_to_trait_values: Mapping[str, Set[str]]
) -> bool:
    if not trait_to_trait_values:
        return True

    for trait, chosen_trait_values in trait_to_trait_values.items():
        chosen_trait_values = {s.lower() for s in chosen_trait_values}
        villager_trait_value = villager[trait]  # type: ignore
        if type(villager_trait_value) is list:
            villager_trait_value = villager_trait_value[0]

        if villager_trait_value.lower() in chosen_trait_values:
            return True
    return False
