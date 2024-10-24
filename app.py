class Calculator:
    historico = []

    def __init__(self,nome):
        self.nome = nome

        while True:
            operador = self.menu()
            if operador == "operador inválido":
                print("operador inválido, por favor insira o código correto: ")
                continue
            else:
                num1,num2 = self.get_data()
                result = self.calc(num1,num2)
                print(result)
                self.historico.append(result)
                reset = input("Deseja continuar ? S ou N:  ").upper()

                if reset == "S":
                    continue
                else:
                    print(*self.historico)
                    break




    def menu(self):
        valid_op = ["i","ii", "iii","iv"]
        self.operador = input(f'''Defina a operação:  (i) soma (ii)subtração (iii)multiplicação (iv) divisão:  ''')
        return self.operador if self.operador in valid_op else  "operador inválido"

    def get_data(self):
        self.num1 = float(input("digite o numero 1:  "))
        self.num2 = float(input("digite o numero 2:  "))
        return self.num1, self.num2

    def calc(self, num1, num2):

        match self.operador:
            case "i":
                return f"{num1} + {num2} = {num1 + num2}\n"
            case "ii":
                return f"{num1} - {num2} = {num1 - num2}\n"
            case "iii":
                return f"{num1} x {num2} = {num1 *  num2}\n"
            case "iv":
                if num2 != 0:
                    return f"{num1} / {num2} = {num1 / num2}\n"
                else:
                    return f"{num1} / {num2} = Não é possível dividir por zero\n"
            




user = Calculator(input("digite o seu nome: "))