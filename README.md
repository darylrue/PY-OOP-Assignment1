## PY-OOP-Assignment1
#### Object Oriented Programming in Python - Assignment 1

1. Clone this repository (or copy the starter code into your IDE of choice).
2. Implement the Calculator class. The starter code is in calculator.py.
3. Write a ScientificCalculator class that is a subclass of Calculator.

    ScientificCalculator has all of the methods of Calculator, plus (at a minimum) these additional methods:

      - sqrt(a) -> returns the square root of a
      - squared(a) -> returns the value of a squared
      - exp(a, b) -> returns the value of a to the power of b

4. Write a BusinessCalculator class that is a subclass of Calculator. 

    BusinessCalculator has all of the methods of Calculator, plus (at a minimum) these additional methods:

      - minus_percent(a, p) -> returns the value of a minus p percent of a
      - plus_tax(a) -> returns the value of a plus 7% tax

5. Write a GraphingCalculator class that is a subclass of both ScientificCalculator and BusinessCalculator.

    GraphingCalculator has all of the methods of ScientificCalculator and BusinessCalculator, plus the following methods:
    
    - graph(eq) -> returns a string of your choice (we're just pretending it's a graph)
    - repeat_last_answer()  Override this method from the Calculator class and change it so that it returns a string instead of a float. Make sure the answer is contained within the string.
     
        ex. 'The last answer was 4'

        NOTE: The graph() method should not affect the value of the attribute self.last_answer

6. Run the test functions for each of your classes and make sure that all tests pass.

    Full test suite is located in `calulator_tests.py`.

    ## All Tests
    - `python3 -m unittest calculator_tests`

    ## Test a Specific Calculator
    - `python -m unittest calculator_tests.BasicCalculatorTest`
    - `python -m unittest calculator_tests.BusinessCalculatorTest`
    - `python -m unittest calculator_tests.GraphingCalculatorTest`
    - `python -m unittest calculator_tests.ScientificCalculator`


    ## Test a Specific Calculator Function
    - `python -m unittest calculator_tests.BasicCalculatorTest.test_add`
