import unittest
from main import Fibonacci

class TestFibonacci(unittest.TestCase):
    
    def test_fibonacci_iteracao_0(self):
        fibo = Fibonacci(0)
        self.assertEqual(list(fibo), [])

    def test_fibonacci_iteracao_1(self):
        fibo = Fibonacci(1)
        self.assertEqual(list(fibo), [1])

    def test_fibonacci_iteracao_5(self):
        fibo = Fibonacci(5)
        self.assertEqual(list(fibo), [1, 1, 2, 3, 5])

    def test_fibonacci_dict_comprehension_iteracao_0(self):
        fibo = Fibonacci(0)
        d = {i+1: num for i, num in enumerate(fibo)}
        self.assertEqual(d, {})

    def test_fibonacci_dict_comprehension_iteracao_1(self):
        fibo = Fibonacci(1)
        d = {i+1: num for i, num in enumerate(fibo)}
        self.assertEqual(d, {1: 1})

    def test_fibonacci_dict_comprehension_iteracao_5(self):
        fibo = Fibonacci(5)
        d = {i+1: num for i, num in enumerate(fibo)}
        self.assertEqual(d, {1: 1, 2: 1, 3: 2, 4: 3, 5: 5})

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)