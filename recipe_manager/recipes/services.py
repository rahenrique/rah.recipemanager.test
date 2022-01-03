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


class Kilogram(MassUnit):
    symbol = 'Kg'

    def __init__(self, amount) -> None:
        super().__init__(amount)

    def _from_base(self, amount) -> BaseUnit:
        return __class__(amount)

    def _to_base(self) -> BaseUnit:
        return __class__(self.amount)


class Gram(MassUnit):
    symbol = 'g'

    def __init__(self, amount) -> None:
        super().__init__(amount)

    def _from_base(self, amount) -> BaseUnit:
        return __class__(amount * 1000)

    def _to_base(self) -> BaseUnit:
        return Kilogram(self.amount / 1000)


class Tonne(MassUnit):
    symbol = 't'

    def __init__(self, amount) -> None:
        super().__init__(amount)

    def _from_base(self, amount) -> BaseUnit:
        return __class__(amount / 1000)

    def _to_base(self) -> BaseUnit:
        return Kilogram(self.amount * 1000)


class Liter(VolumeUnit):
    symbol = 'L'

    def __init__(self, amount) -> None:
        super().__init__(amount)

    def _from_base(self, amount) -> BaseUnit:
        return __class__(amount)

    def _to_base(self) -> BaseUnit:
        return __class__(self.amount)


class Centiliter(VolumeUnit):
    symbol = 'cL'

    def __init__(self, amount) -> None:
        super().__init__(amount)

    def _from_base(self, amount) -> BaseUnit:
        return __class__(amount * 100)

    def _to_base(self) -> BaseUnit:
        return Liter(self.amount / 100)


class Milliliter(VolumeUnit):
    symbol = 'mL'

    def __init__(self, amount) -> None:
        super().__init__(amount)

    def _from_base(self, amount) -> BaseUnit:
        return __class__(amount * 1000)

    def _to_base(self) -> BaseUnit:
        return Liter(self.amount / 1000)


def convert_measurement(origin: BaseUnit, destiny: Type[BaseUnit]):
    return destiny(origin.convert_to(destiny))


print('\n---\n')

gramas = Gram(1200)
toneladas = Tonne(1.9)

print(f'GRAMAS: {gramas}')
print(f'to Kg: {gramas.convert_to(Kilogram)}')
print(f'to t:  {gramas.convert_to(Tonne)}')

print('\n---\n')

print(f'TONELADAS: {toneladas}')
print(f'to Kg: {toneladas.convert_to(Kilogram)}')
print(f'to g:  {toneladas.convert_to(Gram)}')

print('\n---\n')

litros = Liter(2)
mililitros = Milliliter(500)

print(f'LITROS: {litros}')
print(f'to cL: {litros.convert_to(Centiliter)}')
print(f'to mL: {litros.convert_to(Milliliter)}')

print('\n---\n')

print(f'MILILITROS: {mililitros}')
print(f'to L: {mililitros.convert_to(Liter)}')

print('\n---\n')

print('Using convert_measurement service method:')
print(convert_measurement(Kilogram(100.5), Gram))

print('\n---\n')
