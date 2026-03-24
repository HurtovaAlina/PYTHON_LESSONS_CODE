"""
модуль для роботи з площею фігур

"""

import math


def triangle_area(a: float, b: float, c: float) -> float:
    """

    :param a: сторона трикутника а
    :param b: сторона трикутника в
    :param c: кут між ними в градусах
    :return: площа трикутника
    """
    """
    переведення кута в градусах в радіани
    """
    rad = math.radians(c)
    return 0.5 * a * b * math.sin(rad)
