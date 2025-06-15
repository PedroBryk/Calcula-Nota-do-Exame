def calcular_media_semestral(nota1b, nota2b):
    return (nota1b + nota2b) / 2

def calcular_nota_exame(media_semestral):
    return max(0, 10 - media_semestral)

def main():
    print("=== Cálculo da Nota do Exame ===")
    try:
        nota1b = float(input("Digite a nota do 1º bimestre: "))
        nota2b = float(input("Digite a nota do 2º bimestre: "))

        media = calcular_media_semestral(nota1b, nota2b)
        nota_exame = calcular_nota_exame(media)

        print(f"\nSua média semestral é: {media:.2f}")
        print(f"Você precisa tirar pelo menos {nota_exame:.2f} no exame para ser aprovado.")

    except ValueError:
        print("Por favor, insira apenas números válidos.")

if __name__ == "__main__":
    main()