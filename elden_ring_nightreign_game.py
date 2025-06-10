from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import Toggle
from Options import OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class NightreignArchipelagoOptions:
    nightreign_heroes_owned: NightreignHeroesOwned
    nightreign_night_aspect_unlocked: NightreignNightAspectUnlocked


class NightreignGame(Game):
    name = "ELDEN RING NIGHTREIGN"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.XSX,
    ]

    is_adult_only_or_unrated = False

    options_cls = NightreignArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()
    
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Defeat NIGHTLORD as the HERO",
                data={
                    "NIGHTLORD": (self.nightlords, 1),
                    "HERO": (self.heroes, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Find ITEM",
                data={
                    "ITEM": (self.items, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Claim the Shifting Earth's Favor",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Defeat the Nightlord without RARITY gear",
                data={
                    "RARITY": (self.rarity, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Don't die until Day DAY",
                data={
                    "DAY": (self.day_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Revive REVIVES Teammates",
                data={
                    "REVIVES": (self.revive_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Defeat the next Nightlord with RELICS relics equipped",
                data={
                    "RELICS": (self.relic_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Defeat the next Nightlord with a COLOR relic equipped",
                data={
                    "COLOR": (self.color, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Defeat the next Nightlord with only COLOR relics equipped",
                data={
                    "COLOR": (self.color, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Increase your Flask of Crimson Tears cap to FLASKS next run",
                data={
                    "FLASKS": (self.flask_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),  
        ]
    
    @property
    def heroes_owned(self) -> List[str]:
        return sorted(self.archipelago_options.nightreign_heroes_owned.value)
    
    @property
    def night_aspect_unlocked(self) -> bool:
        return bool(self.archipelago_options.nightreign_night_aspect_unlocked.value)
    
    @functools.cached_property
    def heroes_all(self) -> List[str]:
        return [
            "Wylder",
            "Guardian",
            "Ironeye",
            "Duchess",
            "Raider",
            "Revenant",
            "Recluse",
            "Executor",
        ]
    
    def heroes(self) -> List[str]:
        return self.heroes_owned
    
    @functools.cached_property
    def nightlords_base(self) -> List[str]:
        return [
            "Tricephalos",
            "Gaping Jaw",
            "Sentient Pest",
            "Augur",
            "Equilibrious Beast",
            "Darkdrift Knight",
            "Fissure in the Fog",
        ]
    
    def nightlords(self) -> List[str]:
        nightlords: List[str] = self.nightlords_base[:]

        if self.night_aspect_unlocked:
            nightlords.extend(["Night Aspect"])

        return sorted(nightlords)
    
    @staticmethod
    def items() -> List[str]:
        return [
            "Boluses",
            "Spraymist/Aromatic",
            "Gravity Stone",
            "Glintstone Scrap",
            "Stonesword Key",
            "Wending Grace",
            "Smithing Stone (2)",
            "a legendary weapon",
            "an epic weapon"
            "Kukri"
        ]    
    
    @staticmethod
    def rarity() -> List[str]:
        return [
            "EPIC",
            "LEGENDARY",
        ]   
    
    @staticmethod
    def day_range() -> range:
        return range(2, 3)
        
    @staticmethod
    def revive_range() -> range:
        return range(1, 4)    
    
    @staticmethod
    def relic_range() -> range:
        return range(0, 2)
    
    @staticmethod
    def color() -> List[str]:
        return [
            "Blue",
            "Green",
            "Red",
            "Yellow",
        ]   
    
    @staticmethod
    def flask_range() -> range:
        return range(4, 7)
    
    

# Archipelago Options
class NightreignHeroesOwned(OptionSet):
    """
    Indicates which Heroes the player owns and wants to possibly play as.
    """

    display_name = "Nightreign Heroes Owned"
    valid_keys = NightreignGame().heroes_all

    default = valid_keys

class NightreignNightAspectUnlocked(Toggle):
    """
    Indicates whether to include the Night Aspect Boss when generating objectives.
    """

    display_name = "Nightreign Night Aspect Unlocked"