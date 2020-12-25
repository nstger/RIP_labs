# Абстрактный класс «Геометрическая фигура» содержит абстрактный метод для вычисления площади фигуры.

from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def square(self):
        pass
