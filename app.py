print("="*60)
print("🧮  Bem-vindo à CalcPro – Sua Calculadora Inteligente!")
print("="*60)

class Calculadora:
    def _init_(self):
        self.num1 = 0
        self.num2 = 0
        self.operacao = ""

    def ler_primeiro_valor(self):
        try:
            self.num1 = float(input("Digite o primeiro número: "))
        except ValueError:
            print("Erro: insira apenas números.")
            self.ler_primeiro_valor()

    def escolher_operacao(self):
        self.operacao = input("Escolha a operação (+, -, *, /): ")
        if self.operacao not in ["+", "-", "*", "/"]:
            print("Operação inválida.")
            self.escolher_operacao()

    def ler_segundo_valor(self):
        try:
            self.num2 = float(input("Digite o segundo número: "))
            if self.operacao == "/" and self.num2 == 0:
                print("Erro: divisão por zero! Digite outro número.")
                self.ler_segundo_valor()
        except ValueError:
            print("Erro: insira apenas números.")
            self.ler_segundo_valor()

    def calcular(self):
        if self.operacao == "+":
            return self.num1 + self.num2
        elif self.operacao == "-":
            return self.num1 - self.num2
        elif self.operacao == "*":
            return self.num1 * self.num2
        elif self.operacao == "/":
            return self.num1 / self.num2

# Executando o programa
calc = Calculadora()
calc.ler_primeiro_valor()
calc.escolher_operacao()
calc.ler_segundo_valor()

resultado = calc.calcular()
print(f"Resultado é: {resultado}")