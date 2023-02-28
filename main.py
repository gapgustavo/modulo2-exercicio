class Fibonacci:
    def __init__(self, iteracao):
        self.iteracao = iteracao
        self.anterior = 0
        self.proximo = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.iteracao == 0:
            raise StopIteration
        else:
            resultado = self.proximo
            soma = self.anterior + self.proximo
            self.anterior = self.proximo
            self.proximo = soma
            self.iteracao -= 1
            return resultado
          
n = 10
fibo = Fibonacci(n)
d = {i+1: num for i, num in enumerate(fibo)}
print(d)