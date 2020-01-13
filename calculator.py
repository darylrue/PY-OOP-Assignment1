import math


class Calculator:

    def __init__(self):
        self.last_answer = None  # TODO - each time the calculator returns an answer, store it here

    def add(self, a: float, b: float) -> float:
        # TODO - add a to b and return the sum
        raise NotImplementedError

    def subtract(self, a, b) -> float:
        # TODO - subtract a from b and return the difference
        raise NotImplementedError

    def multiply(self, a, b) -> float:
        # TODO - multiply a by b and return the product
        raise NotImplementedError

    def divide(self, a, b) -> float:
        # TODO - divide a by b and return the quotient
        raise NotImplementedError

    def repeat_last_answer(self) -> float:
        # TODO - implement this method
        raise NotImplementedError


class ScientificCalculator:
    # TODO
    pass


class BusinessCalculator:
    # TODO
    pass


class GraphingCalculator:
    # TODO
    pass
