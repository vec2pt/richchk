"""AI script.

Use KnownAiScript#value when possible.  Otherwise construct the AI script with a 4-byte
string.

U32: AI script (4-byte string)
"""

import dataclasses
from enum import Enum


@dataclasses.dataclass(frozen=True)
class AiScript:
    _name: str
    _description: str

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description


class UnknownAiScript(AiScript):
    pass


class KnownAiScript(Enum):
    JUNKYARD_DOG = AiScript("JYDg", "Junkyard Dog")
    ENTER_CLOSEST_BUNKER = AiScript(
        "EnBk",
        "Enter closest bunker",
    )
    ENTER_CLOSEST_TRANSPORT = AiScript(
        "EnTr",
        "Enter closest transport",
    )
    EXIT_CLOSEST_TRANSPORT = AiScript(
        "ExTr",
        "Exit closest transport",
    )
    CAST_DISRUPTION_WEB = AiScript(
        "DWHe",
        "Cast disruption web",
    )
    TURN_ON_SHARED_VISION_WITH_PLAYER_1 = AiScript(
        "+Vi0",
        "Turn on shared vision of Player 1 with current player",
    )
