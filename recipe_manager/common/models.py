from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Type


class UnitType(Enum):
    ONE_UNIT = auto()
    MASS = auto()
    VOLUME = auto()


class BaseUnit(ABC):
    _unit_type = UnitType.ONE_UNIT
    _symbol = 'N/A'

    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return f'{self.value} {self.symbol} ({self.unit_type})'

    @abstractmethod
    def _from_base(self, value) -> 'BaseUnit':
        pass

    @abstractmethod
    def _to_base(self) -> 'BaseUnit':
        pass

    @classmethod
    @property
    def symbol(cls) -> str:
        return cls._symbol
    
    @classmethod
    @property
    def unit_type(cls) -> UnitType:
        return cls._unit_type

    def convert_to(self, target: Type['BaseUnit']):
        if self.unit_type != target.unit_type:
            raise TypeError(
                f'Impossible to convert from {self.unit_type} to {target.unit_type}: Different unit types')
        return target(self.value)._from_base(self._to_base().value)


class MassUnit(BaseUnit):
    _unit_type = UnitType.MASS

class VolumeUnit(BaseUnit):
    _unit_type = UnitType.VOLUME


class Kilogram(MassUnit):
    _symbol = 'Kg'

    def _from_base(self, value) -> BaseUnit:
        return __class__(value)

    def _to_base(self) -> BaseUnit:
        return __class__(self.value)


class Gram(MassUnit):
    _symbol = 'g'

    def _from_base(self, value) -> BaseUnit:
        return __class__(value * 1000)

    def _to_base(self) -> BaseUnit:
        return Kilogram(self.value / 1000)


class Tonne(MassUnit):
    _symbol = 't'

    def _from_base(self, value) -> BaseUnit:
        return __class__(value / 1000)

    def _to_base(self) -> BaseUnit:
        return Kilogram(self.value * 1000)


class Liter(VolumeUnit):
    _symbol = 'L'

    def _from_base(self, value) -> BaseUnit:
        return __class__(value)

    def _to_base(self) -> BaseUnit:
        return __class__(self.value)


class Centiliter(VolumeUnit):
    _symbol = 'cL'

    def _from_base(self, value) -> BaseUnit:
        return __class__(value * 100)

    def _to_base(self) -> BaseUnit:
        return Liter(self.value / 100)


class Milliliter(VolumeUnit):
    _symbol = 'mL'

    def _from_base(self, value) -> BaseUnit:
        return __class__(value * 1000)

    def _to_base(self) -> BaseUnit:
        return Liter(self.value / 1000)
