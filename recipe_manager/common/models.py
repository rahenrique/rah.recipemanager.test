from enum import Enum, auto
from typing import Type


class UnitType(Enum):
    MASS = auto()
    VOLUME = auto()


class BaseUnit:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return f'{self.value} {self.symbol} ({self.type})'

    def _from_base(self, value) -> 'BaseUnit':
        raise NotImplementedError

    def _to_base(self) -> 'BaseUnit':
        raise NotImplementedError

    def convert_to(self, target: Type['BaseUnit']):
        if self.type != target.type:
            raise TypeError(
                f'Impossible to convert from {self.type} to {target.type}: Different unit types')
        return target(self.value)._from_base(self._to_base().value)


class MassUnit(BaseUnit):
    type = UnitType.MASS

    def __init__(self, value) -> None:
        super().__init__(value)


class VolumeUnit(BaseUnit):
    type = UnitType.VOLUME

    def __init__(self, value) -> None:
        super().__init__(value)


class Kilogram(MassUnit):
    symbol = 'Kg'

    def __init__(self, value) -> None:
        super().__init__(value)

    def _from_base(self, value) -> BaseUnit:
        return __class__(value)

    def _to_base(self) -> BaseUnit:
        return __class__(self.value)


class Gram(MassUnit):
    symbol = 'g'

    def __init__(self, value) -> None:
        super().__init__(value)

    def _from_base(self, value) -> BaseUnit:
        return __class__(value * 1000)

    def _to_base(self) -> BaseUnit:
        return Kilogram(self.value / 1000)


class Tonne(MassUnit):
    symbol = 't'

    def __init__(self, value) -> None:
        super().__init__(value)

    def _from_base(self, value) -> BaseUnit:
        return __class__(value / 1000)

    def _to_base(self) -> BaseUnit:
        return Kilogram(self.value * 1000)


class Liter(VolumeUnit):
    symbol = 'L'

    def __init__(self, value) -> None:
        super().__init__(value)

    def _from_base(self, value) -> BaseUnit:
        return __class__(value)

    def _to_base(self) -> BaseUnit:
        return __class__(self.value)


class Centiliter(VolumeUnit):
    symbol = 'cL'

    def __init__(self, value) -> None:
        super().__init__(value)

    def _from_base(self, value) -> BaseUnit:
        return __class__(value * 100)

    def _to_base(self) -> BaseUnit:
        return Liter(self.value / 100)


class Milliliter(VolumeUnit):
    symbol = 'mL'

    def __init__(self, value) -> None:
        super().__init__(value)

    def _from_base(self, value) -> BaseUnit:
        return __class__(value * 1000)

    def _to_base(self) -> BaseUnit:
        return Liter(self.value / 1000)
