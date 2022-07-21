import pytest

class Calculator:
    def __init__(self, name):
        self.name = name
        
    def add(self, a, b):
        return a + b
    
    def subtraction(self, a, b):
        return a - b
        
    def multiply(self, a, b):
        return a * b
        
calc = Calculator("my calculator")

@pytest.fixture
def base_calculator():
    return Calculator("Base Calculator")

def test_lab4_test1(base_calculator):
    print("#1 This calculator's name is " + base_calculator.name)
    
    # Changing calculator's name
    base_calculator.name = "Changed Calculator"
    print("#1 This calculator's name is " + base_calculator.name)
    
    assert True

def test_lab4_test2(base_calculator):
    print("#2 This calculator's name is " + base_calculator.name)
    
    assert True
    

#SUBTRACTION   
def test_subtract_a():
   assert calc.subtraction(5, 2) == 3
    
def test_subtract_b():
   assert calc.subtraction(7, 1) == 6
    
def test_subtract_c():
    calc.subtraction(4, 4) == 0
    
    
#MULTIPLCATION    
def test_multiply_a():
    assert calc.multiply(1, 2) == 2
    
def test_multiply_b():
    assert calc.multiply(1, 2) == 2
    
def test_multiply_c():
    assert calc.multiply(-5, 4) == -20
    
def test_multiply_d():
    assert calc.multiply(3, 4) == 12
 





    

    

