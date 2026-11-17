# Desafio M01 · Calculadora de terminal
# Enunciado: aulas/M01_fundamentos/desafio/apostila.md no material do cursoprint("=== Calculadora Simples ===")
while True:
  print("Calculadora Simples")
  print("1 - Adição (+)")
  print("2 - Subtração (-)")
  print("3 - Multiplicação (*)")
  print("4 - Divisão (/)")

  operacao = input("Escolha a operação (1/2/3/4): ")

  if operacao in ["1", "2", "3", "4"]:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == "1":
      resultado = num1 + num2
      print(f"Resultado: {num1} + {num2} = {resultado}")
      break  

    elif operacao == "2":
      resultado = num1 - num2
      print(f"Resultado: {num1} - {num2} = {resultado}")
      break

    elif operacao == "3":
      resultado = num1 * num2
      print(f"Resultado: {num1} * {num2} = {resultado}")
      break

    elif operacao == "4":
      if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")
        break
      else:
        print("Erro: Não é possível dividir por zero. Tente novamente!")
    
  else:
    print("Opção inválida! Tente novamente.")
