from typing import Type

from .models import BaseUnit, Centiliter, Gram, Kilogram, Liter, Milliliter, Tonne


def symbol_to_unit(symbol: str):
    symbol_to_unit = {
        Gram.symbol: Gram,
        Kilogram.symbol: Kilogram,
        Centiliter.symbol: Centiliter,
        Liter.symbol: Liter,
        Milliliter.symbol: Milliliter,
        Tonne.symbol: Tonne
    }
    return symbol_to_unit[symbol]


def value_to_unit(symbol: str, value=None) -> BaseUnit:
    return symbol_to_unit(symbol)(value)


def convert_unit(origin: BaseUnit, destiny: Type[BaseUnit]):
    return origin.convert_to(destiny)
    