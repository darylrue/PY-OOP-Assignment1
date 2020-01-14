import unittest

from calculator import BusinessCalculator, Calculator, GraphingCalculator, ScientificCalculator

class BasicCalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def _test_repeat_last_answer(self, last_answer):
        self.assertEqual(self.calculator.repeat_last_answer(), last_answer)

    def test_add(self):
        self.assertEqual(self.calculator.add(1, 2.2), 3.2)
        self._test_repeat_last_answer(3.2)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10.5, 2), 5.25)
        self._test_repeat_last_answer(5.25)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(1.5, 10), 15)
        self._test_repeat_last_answer(15)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(5.5, 10), 4.5)
        self._test_repeat_last_answer(4.5)

class BusinessCalculatorTest(BasicCalculatorTest):
    def setUp(self):
        self.calculator = BusinessCalculator()

    def test_minus_percent(self):
        self.assertEqual(self.calculator.minus_percent(100, 5), 95)
        self.assertEqual(self.calculator.minus_percent(25, 20), 20)
        self._test_repeat_last_answer(20)

    def test_plus_tax(self):
        self.assertEqual(self.calculator.plus_tax(100), 107)
        self.assertEqual(self.calculator.plus_tax(10), 10.7)
        self._test_repeat_last_answer(10.7)

class ScientificCalculatorTest(BasicCalculatorTest):
    def setUp(self):
        self.calculator = ScientificCalculator()
    
    def test_square_root(self):
        self.assertEqual(self.calculator.sqrt(1), 1)
        self._test_repeat_last_answer(1)

    def test_squared(self):
        self.assertEqual(self.calculator.squared(1), 1)
        self.assertEqual(self.calculator.squared(4), 16)
        self._test_repeat_last_answer(16)

    def test_exponent(self):
        self.assertEqual(self.calculator.exp(0, 1), 0)
        self.assertEqual(self.calculator.exp(1, 4), 1)
        self.assertEqual(self.calculator.exp(2, 3), 8)
        self._test_repeat_last_answer(8)

class GraphingCalculatorTest(ScientificCalculatorTest, BusinessCalculatorTest):
    def setUp(self):
        self.calculator = GraphingCalculator()

    def _test_repeat_last_answer(self, last_answer):
        self.assertIsInstance(self.calculator.repeat_last_answer(), str)
        self.assertTrue(str(last_answer) in self.calculator.repeat_last_answer())

    def test_graph(self):
        self.assertIsInstance(self.calculator.graph('3x + 2'), str)

if __name__ == '__main__':
    unittest.main()
