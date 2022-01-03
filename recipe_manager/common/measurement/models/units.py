from .base import BaseUnit, MassUnit, VolumeUnit


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
