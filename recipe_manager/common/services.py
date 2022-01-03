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


# TODO: Remove tests from here!

# print('Using convert_unit service method:')
# kilos = Kilogram(100.5)
# converted = convert_unit(kilos, Gram)
# print(kilos)
# print(converted)

# print('\n---\n')

# litrao = value_to_unit('L', 1.2)
# print(litrao)

# print('\n---\n')

# gramas = Gram(1200)
# toneladas = Tonne(1.9)

# print(f'GRAMAS: {gramas}')
# print(f'to Kg: {gramas.convert_to(Kilogram)}')
# print(f'to t:  {gramas.convert_to(Tonne)}')

# print('\n---\n')

# print(f'TONELADAS: {toneladas}')
# print(f'to Kg: {toneladas.convert_to(Kilogram)}')
# print(f'to g:  {toneladas.convert_to(Gram)}')

# print('\n---\n')

# litros = Liter(2)
# mililitros = Milliliter(500)

# print(f'LITROS: {litros}')
# print(f'to cL: {litros.convert_to(Centiliter)}')
# print(f'to mL: {litros.convert_to(Milliliter)}')

# print('\n---\n')

# print(f'MILILITROS: {mililitros}')
# print(f'to L: {mililitros.convert_to(Liter)}')

# print('\n---\n')
