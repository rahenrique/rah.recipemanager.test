from typing import Type

from models.base import BaseUnit
from models.units import Centiliter, Gram, Kilogram, Liter, Milliliter, Tonne


def convert_unit(origin: BaseUnit, destiny: Type[BaseUnit]):
    return destiny(origin.convert_to(destiny))


# TODO: Remove tests from here!
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

print('Using convert_unit service method:')
print(convert_unit(Kilogram(100.5), Gram))

print('\n---\n')
