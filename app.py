class Calculator:
    def __init__(self, nome):
        self.nome = nome
        self.historico = []

    def play(self):
        while True:
            operador = self.menu()
            if operador == "operador inválido":
                print("Operador inválido, por favor insira o código correto.")
                continue
            else:
                num1, num2 = self.get_data()
                result = self.calc(operador, num1, num2)
                print(result)
                self.historico.append(result)
                reset = input("Deseja continuar? S ou N: ").upper()

                if reset == "S":
                    continue
                else:
                    print("Histórico:", *self.historico)
                    break

    def menu(self):
        valid_op = ["i", "ii", "iii", "iv"]
        operador = input('''
        Defina a operação: 
        (i) soma 
        (ii) subtração 
        (iii) multiplicação 
        (iv) divisão: ''')
        return operador if operador in valid_op else "operador inválido"

    def get_data(self):
        num1 = float(input("Digite o número 1: "))
        num2 = float(input("Digite o número 2: "))
        return num1, num2

    def calc(self, operador, num1, num2):
        match operador:
            case "i":
                return f"{num1} + {num2} = {num1 + num2}\n"
            case "ii":
                return f"{num1} - {num2} = {num1 - num2}\n"
            case "iii":
                return f"{num1} x {num2} = {num1 * num2}\n"
            case "iv":
                if num2 != 0:
                    return f"{num1} / {num2} = {num1 / num2}\n"
                else:
                    return "Não é possível dividir por zero.\n"

user = Calculator(input("Digite o seu nome: "))
user.play()
