class calculator:
    
    def __init__(self, nome):
        self.nome = nome
        while True:
            operador = self.menu()
            if operador != "v":
                self.get__numbers()
                resultado = self.calculate(operador)
                if resultado:
                    print(resultado)
            else:
                print("fechando a calculadora")
                break

        

    def get__numbers(self):
        self.num1 = float(input("digite o primeiro operador:"))
        self.num2 = float(input("digite o segundo operador:"))
        return self.num1, self.num2

    def menu(self):

            operador = input(f"""
Informe o Operador:
            (i) soma
            (ii)subtração
            (iii)multiplicação 
            (iv) divisão
            (v) Sair                                 
                                  
:""")
            return operador


    def calculate(self,operador):
        
        match operador:
            case "i":
                return self.num1 + self.num2
            case "ii":
                return self.num1 - self.num2
            case "iii":
                return self.num1 * self.num2
            case "iv":
                return self.num1 / self.num2
            case _:
                print("operador inválido")
                return False               
            




nome = calculator(nome =input("Digite seu nome: "))

