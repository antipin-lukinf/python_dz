# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}

from decimal import Decimal, getcontext
import decimal
import math

number = Decimal(math.pi)
print(number)
getcontext().prec = 5
print(number.quantize(Decimal('1.0000')))