from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class CostumeConfig:
    path: str
    size: Tuple[int, int]


@dataclass
class ShipConfig:
    name: str
    costumes: List[CostumeConfig]
    top_speed: float
    slow_speed: float
    acceleration: float
    turn_speed: float
    slowdown_percent: float


@dataclass
class PlayerKeysConfig:
    left: int
    right: int
    forward: int
    backward: int
    fire: int


@dataclass
class PlayerConfig:
    player_index: int
    keys: PlayerKeysConfig
