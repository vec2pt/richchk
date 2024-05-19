import dataclasses

from ...mrgn.rich_location import RichLocation
from ...unis.unit_id import UnitId
from ..player_id import PlayerId
from ..rich_trigger_condition import RichTriggerCondition
from ..trigger_condition_id import TriggerConditionId
from .comparators.numeric_comparator import NumericComparator


@dataclasses.dataclass(frozen=True)
class BringCondition(RichTriggerCondition):

    _group: PlayerId
    _comparator: NumericComparator
    _quantity: int
    _unit: UnitId
    _location: RichLocation

    @classmethod
    def condition_id(cls) -> TriggerConditionId:
        return TriggerConditionId.BRING

    @property
    def group(self) -> PlayerId:
        return self._group

    @property
    def comparator(self) -> NumericComparator:
        return self._comparator

    @property
    def quantity(self) -> int:
        return self._quantity

    @property
    def unit(self) -> UnitId:
        return self._unit

    @property
    def location(self) -> RichLocation:
        return self._location
