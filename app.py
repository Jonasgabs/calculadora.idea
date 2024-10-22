class calculator:
    
    def __init__(self, nome):
        self.nome = nome
        while True:
            operador = self.menu()
            if operador == "v":
                print("fechando a calculadora")
                break     
            elif operador == "operador inválido":
                print(operador)   
            else:
                self.get__numbers()
                resultado = self.calculate(operador)
                if resultado:
                    print(resultado)


    def get__numbers(self):
        self.num1 = float(input("digite o primeiro valor:"))
        self.num2 = float(input("digite o segundo valor:"))
        return self.num1, self.num2


    def menu(self):
            valid_operator = ["i","ii","iii","iv","v"]
            operador = input(f"""
            Informe o Operador:
            (i) soma
            (ii)subtração
            (iii)multiplicação 
            (iv) divisão
            (v) Sair                                 
                                  
        :""")
            return operador if operador in valid_operator else "operador inválido"


    def calculate(self,operador):
        
        match operador:
            case "i":
                return self.num1 + self.num2
            case "ii":
                return self.num1 - self.num2
            case "iii":
                return self.num1 * self.num2
            case "iv":
                if self.num2 ==0:
                    return "Não é possível dividir por zero"
                return self.num1 / self.num2
            
                
                              
            




nome = calculator(nome =input("Digite seu nome: "))

