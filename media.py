nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Cálculo da média ponderada
media = (nota1 * 1 + nota2 * 1 + nota3 * 2) / 4

print(f"Sua média é: {media:.2f}")
if media >= 6:
   print("Você foi aprovado")
elif 3 < media < 6:
    print("Você está de recuperação")
else:
   print("Você foi reprovado")