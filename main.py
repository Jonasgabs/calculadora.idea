class Calculator:
    def __init__(self, nome):
        self.nome = nome
        self.historico = []
        


    def calc(self, operador, num1, num2):
        match operador:
            case "i":
                operador = "+"
                return operador, num1 + num2
            case "ii":
                operador = "-"
                return operador, num1 - num2
            case "iii":
                operador = "*"
                return operador, num1 * num2
            case "iv":
                if num2 != 0:
                    operador = "/"
                    return operador, num1 / num2
                else:
                    operador = "/"
                    return operador, "Não é possível dividir por zero.\n"

