from enum import Enum, auto
from typing import Type


class UnitTypes(Enum):
    MASS = auto()
    VOLUME = auto()


class BaseUnit:
    def __init__(self, amount) -> None:
        self.amount = amount

    def __str__(self) -> str:
        return f'{self.amount} {self.symbol} ({self.type})'

    def _from_base(self, amount) -> 'BaseUnit':
        raise NotImplementedError

    def _to_base(self) -> 'BaseUnit':
        raise NotImplementedError

    def convert_to(self, target: Type['BaseUnit']):
        if self.type != target.type:
            raise TypeError(
                f'Impossible to convert from {self.type} to {target.type}: Different unit types')
        return target(self.amount)._from_base(self._to_base().amount)


class MassUnit(BaseUnit):
    type = UnitTypes.MASS

    def __init__(self, amount) -> None:
        super().__init__(amount)


class VolumeUnit(BaseUnit):
    type = UnitTypes.VOLUME

    def __init__(self, amount) -> None:
        super().__init__(amount)
