from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class CostumeConfig:
    path: str
    size: Tuple[int, int]


@dataclass
class ShipConfig:
    name: str
    costume: CostumeConfig
    top_speed: float = 10
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


@dataclass
class PlayerConfig:
    ships: List[ShipConfig]
    keys: PlayerKeysConfig
