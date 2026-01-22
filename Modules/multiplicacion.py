class MultiplicacionNumeros:
    def __init__(self, num1, num2, num3 = None):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    
    def multiplicar(self):
        if(self.num3):
            return self.num1 * self.num2 * self.num3
        else:
            return self.num1 * self.num2

    def mostrar_resultado(self):
        print(f"La multiplicacion tiene por resultado: {self.multiplicar()}")