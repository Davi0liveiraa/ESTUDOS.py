print("\n[CALCULADORA DE HORAS EXTRAS]")
nome = input(str("\nQual seu nome?\n"))
nome_maiusc = nome.capitalize() 
print("\nBem vindo,", nome_maiusc, "!")
print("")
salario = float(input("Qual seu salário bruto? "))
print(f"R${salario:.2f}")
hora_mensal = int(input("Quantas horas mensais? [220], [200] ou [180]\n"))
match hora_mensal:
    case 220:
        valor_hora = salario / 220
    case 200:
        valor_hora = salario / 200
    case 180:
        valor_hora = salario / 180
    case _:
        while hora_mensal not in [220, 200, 180]: 
            hora_mensal = int(input("\nHoras semanais inválidas. Digite [220], [200] ou [180]. "))
            valor_hora = salario / hora_mensal
print(f"\nValor da sua hora é: R$ {valor_hora:.2f}\n")

quantidade_h_e = float(input("Quantas horas extras você fez? "))
porcentagem = int(input("Qual a porcentagem da hora extra? [60] ou [100].\n"))
match porcentagem:
    case 60:
        valor_hora_extra = (valor_hora * 1.6) * quantidade_h_e
        print(f"Você fez {quantidade_h_e:.0f} horas extras (60%).\n")
    case 100:
        valor_hora_extra = (valor_hora * 2.0) * quantidade_h_e
        print(f"Você fez {quantidade_h_e:.0f} horas extras (100%).\n")
    case _:
        while porcentagem not in [60, 100]:
            porcentagem = int(input("\nPorcentagem inválida. Digite [60] ou [100].\n"))
            match porcentagem:
                case 60:
                    valor_hora_extra = (valor_hora * 1.6) * quantidade_h_e
                    print(f"Você fez {quantidade_h_e:.0f} horas extras (60%).\n")
                case 100:
                    valor_hora_extra = (valor_hora * 2.0) * quantidade_h_e
                    print(f"Você fez {quantidade_h_e:.0f} horas extras (100%).")

largura = 31
altura = 12
mensagem = f"Total em reais R${valor_hora_extra:.2f}"
mensagem2 = "Obrigado por nos utilizar :)"
mensagens = [mensagem, mensagem2]

def desenhar_linha_horizontal(largura):
    return "+" + "-" * (largura - 2) + "+\n"

def desenhar_linhas_laterais(largura, altura, mensagens):
    resultado = ""
    for i in range(altura - 2):
        if i == (altura // 3) - 1:
            mensagem = mensagens[0]
            texto_inicio = (largura - 2 - len(mensagem)) // 2
            resultado += "|" + " " * texto_inicio + mensagem + " " * (largura - 2 - texto_inicio - len(mensagem)) + "|\n"
        elif i == 2 * (altura // 3) - 1:S
            mensagem = mensagens[1]
            texto_inicio = (largura - 2 - len(mensagem)) // 2
            resultado += "|" + " " * texto_inicio + mensagem + " " * (largura - 2 - texto_inicio - len(mensagem)) + "|\n"
        else:
            resultado += "|" + " " * (largura - 2) + "|\n"
    return resultado

output = desenhar_linha_horizontal(largura)
output += desenhar_linhas_laterais(largura, altura, mensagens)
output += desenhar_linha_horizontal(largura)

print(output)