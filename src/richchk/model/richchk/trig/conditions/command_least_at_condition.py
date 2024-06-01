import dataclasses

from ...mrgn.rich_location import RichLocation
from ...unis.unit_id import UnitId
from ..rich_trigger_condition import (
    RichTriggerCondition,
    _RichTriggerConditionDefaultsBase,
)
from ..trigger_condition_id import TriggerConditionId


@dataclasses.dataclass(frozen=True)
class _CommandLeastAtConditionBase(RichTriggerCondition):

    _unit: UnitId
    _location: RichLocation

    @classmethod
    def condition_id(cls) -> TriggerConditionId:
        return TriggerConditionId.COMMAND_THE_LEAST_AT

    @property
    def unit(self) -> UnitId:
        return self._unit

    @property
    def location(self) -> RichLocation:
        return self._location


@dataclasses.dataclass(frozen=True)
class CommandLeastAtCondition(
    _RichTriggerConditionDefaultsBase,
    _CommandLeastAtConditionBase,
):
    pass
