from operations.sum_calculator import SumCalculator

class Calculator:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
        self.__sc = SumCalculator() # private field -> name convention with double underscore
        
    def sum(self):
        return self.value1 + self.value2
    
    def subtract(self):
        return self.value1 - self.value2
    
    def multiple(self):
        return self.value1 * self.value2
    
    def divide(self):
        return self.value1 / self.value2
    
    def sumValues(self, v1, v2):
        return self.__sc.sum(v1, v2)
    
    def sumAll(self, *numbers):
        return self.__sc.sumAll(*numbers)
   
if __name__ == "__main__":
    c = Calculator(50, 10)
    print(f"sum: {c.sum()}")
    print(f"subtract: {c.subtract()}")
    print(f"multiple: {c.multiple()}")
    print(f"divide: {c.divide()}")
    print(f"sumValues: {c.sumValues(50, 50)}")
    print(f"sumAll: {c.sumAll(10, 10, 10)}")
    print(f"static sum: {SumCalculator.static_sum(60.5, 60.5)}")