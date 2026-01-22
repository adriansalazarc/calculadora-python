class RestaDosNumeros:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def restar(self):
        return self.num1 - self.num2
    
    def mostrar_resultado(self):
        print(f"La resta de {self.num1} - {self.num2} ={self.restar()}")