class SumCalculator:
    
    @staticmethod
    def static_sum(v1, v2):
        return v1 + v2
    
    def sum(self, v1, v2):
        return v1 + v2
    
    def sumAll(self, *numbers):
        total = 0
        for n in numbers:
            total += n
        return total
    
if __name__ == "__main__":
    print(f"static sum: {SumCalculator.static_sum(100, 10)}")
    s = SumCalculator()
    print(f"sum: {s.sum(10, 10)}")
    print(f"sumAll: {s.sumAll(1, 2, 3, 4)}")