from main import Calculator

def get_data():
    num1 = float(input("Digite o número 1: "))
    num2 = float(input("Digite o número 2: "))
    return num1, num2


def menu():
    valid_op = ["i", "ii", "iii", "iv"]
    operador = input('''
    Defina a operação: 
    (i) soma 
    (ii) subtração 
    (iii) multiplicação 
    (iv) divisão: ''')
    return operador if operador in valid_op else "operador inválido"


def start(Calculator):
    print("Olá!", Calculator.nome, "Vamos calcular")  
    while True:
        operador = menu()
        if operador == "operador inválido":
            print("Operador inválido, por favor insira o código correto.")
            continue
        else:
            num1, num2 = get_data()
            op, result = Calculator.calc(operador, num1, num2)
            
            if op == "+":
                op = f"{num1} + {num2} = {result}\n"
            elif op == "-":
                op = f"{num1} - {num2} = {result}\n"
            elif op == "*":
                op = f"{num1} x {num2} = {result}\n"
            elif op == "/":
                op = f"{num1} / {num2} = {result}\n"
                        
            print(op)
            Calculator.historico.append(op)
            reset = input("Deseja continuar? S ou N: ").upper()

            if reset == "S":
                continue
            else:
                print("Histórico:", *Calculator.historico)
                break


user = Calculator(input("Digite o seu nome: "))

start(user)
