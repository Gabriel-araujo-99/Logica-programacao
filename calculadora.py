#!/usr/bin/env python3
from datetime import datetime

def registrar_operacao(operacao, resultado):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    linha = f"[{agora}] {operacao} = {resultado}\n"
    with open("historico_calculadora.txt", "a") as arq:
        arq.write(linha)

def adicao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 + num2
    print("Resultado:", resultado)
    registrar_operacao(f"{num1} + {num2}", resultado)

def subtracao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 - num2
    print("Resultado:", resultado)
    registrar_operacao(f"{num1} - {num2}", resultado)

def multiplicacao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 * num2
    print("Resultado:", resultado)
    registrar_operacao(f"{num1} * {num2}", resultado)

def divisao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if num2 == 0:
        print("Erro: divisão por zero!")
        return
    resultado = num1 / num2
    print("Resultado:", resultado)
    registrar_operacao(f"{num1} / {num2}", resultado)

def mostrar_menu():
    print("\n=== CALCULADORA COM HISTÓRICO ===")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

def main():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma operação (1-5): ")

        if escolha == '1':
            adicao()
        elif escolha == '2':
            subtracao()
        elif escolha == '3':
            multiplicacao()
        elif escolha == '4':
            divisao()
        elif escolha == '5':
            print("Encerrando calculadora. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
