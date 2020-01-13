import math


class Calculator:

    def __init__(self):
        self.last_answer = None  # TODO - each time the calculator returns an answer, store it here

    def add(self, a: float, b: float) -> float:
        pass  # TODO - add a to b and return the sum

    def subtract(self, a, b) -> float:
        pass  # TODO - subtract a from b and return the difference

    def multiply(self, a, b) -> float:
        pass  # TODO - multiply a by b and return the product

    def divide(self, a, b) -> float:
        pass  # TODO - divide a by b and return the quotient

    def repeat_last_answer(self) -> float:
        pass  # TODO - implement this method


class ScientificCalculator:
    pass  # TODO


class BusinessCalculator:
    pass  # TODO


class GraphingCalculator:
    pass  # TODO


# TESTS

def test_calculator():
    calculator = Calculator()
    _test_base_calculator_methods(calculator=calculator)
    Util.print_green('All Calculator tests passed!')


def test_scientific_calculator():
    calculator = ScientificCalculator()
    _test_scientific_calculator_methods(calculator=calculator)
    Util.print_green('All ScientificCalculator tests passed!')


def test_business_calculator():
    calculator = BusinessCalculator()
    _test_business_calculator_methods(calculator=calculator)
    Util.print_green('All BusinessCalculator tests passed!')


def test_graphing_calculator():
    calculator = GraphingCalculator()
    _test_graphing_calculator_methods(calculator=calculator)
    Util.print_green('All GraphingCalculator tests passed!')


def test_all():
    test_calculator()
    test_scientific_calculator()
    test_business_calculator()
    test_graphing_calculator()


def _test_base_calculator_methods(calculator: Calculator, last_answer_is_float: bool = True):

    def last_answer_equals(value) -> bool:
        return _last_answer_equals(calculator=calculator, value=value, last_answer_is_float=last_answer_is_float)

    assert calculator.add(1, 2.2) == 3.2
    assert last_answer_equals(3.2)
    assert calculator.subtract(5.5, 10) == 4.5
    assert last_answer_equals(4.5)
    assert calculator.multiply(1.5, 10) == 15
    assert last_answer_equals(15)
    assert calculator.divide(10.5, 2) == 5.25
    assert last_answer_equals(5.25)


def _test_scientific_calculator_methods(calculator: ScientificCalculator, last_answer_is_float: bool = True):
    _test_base_calculator_methods(calculator=calculator, last_answer_is_float=last_answer_is_float)

    def last_answer_equals(value) -> bool:
        return _last_answer_equals(calculator=calculator, value=value, last_answer_is_float=last_answer_is_float)

    assert calculator.sqrt(1) == 1
    assert last_answer_equals(1)
    assert calculator.sqrt(4) == 2
    assert last_answer_equals(2)
    assert calculator.squared(1) == 1
    assert last_answer_equals(1)
    assert calculator.squared(4) == 16
    assert last_answer_equals(16)
    assert calculator.exp(0, 1) == 0
    assert last_answer_equals(0)
    assert calculator.exp(1, 4) == 1
    assert last_answer_equals(1)
    assert calculator.exp(2, 3) == 8
    assert last_answer_equals(8)


def _test_business_calculator_methods(calculator: BusinessCalculator, last_answer_is_float: bool = True):
    _test_base_calculator_methods(calculator=calculator, last_answer_is_float=last_answer_is_float)

    def last_answer_equals(value) -> bool:
        return _last_answer_equals(calculator=calculator, value=value, last_answer_is_float=last_answer_is_float)

    assert calculator.minus_percent(100, 5) == 95
    assert last_answer_equals(95)
    assert calculator.minus_percent(25, 20) == 20
    assert last_answer_equals(20)
    assert calculator.plus_tax(100) == 107
    assert last_answer_equals(107)
    assert calculator.plus_tax(10) == 10.7
    assert last_answer_equals(10.7)


def _test_graphing_calculator_methods(calculator: GraphingCalculator):
    _test_scientific_calculator_methods(calculator=calculator, last_answer_is_float=False)
    _test_business_calculator_methods(calculator=calculator, last_answer_is_float=False)
    assert isinstance(calculator.graph('3x + 2'), str)


def _last_answer_equals(calculator: Calculator, value: float, last_answer_is_float: bool) -> bool:
    last_answer = calculator.repeat_last_answer()
    if last_answer_is_float:
        return last_answer == value
    else:
        return isinstance(last_answer, str) and str(value) in last_answer


class Util:
    @staticmethod
    def print_green(message: str):
        print('\033[92m' + message + '\033[0m')
