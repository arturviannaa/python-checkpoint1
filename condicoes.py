nome = input("Nome do paciente: ")
temperatura = float(input("Temperatura corporal (°C): "))
nivel_dor = int(input("Nível de dor (0 a 10): "))
dificuldade_respirar = input("Apresenta dificuldade para respirar? (S/N): ").strip().upper()

classificacao = "Pouco Urgente (Verde)"

if dificuldade_respirar == 'S' or temperatura >= 39.0 or nivel_dor >= 8:
    classificacao = "Emergência (Vermelho)"
elif temperatura >= 37.5 or nivel_dor >= 5:
    classificacao = "Urgência (Amarelo)"

print(f"\nResultado da Triagem")
print(f"Paciente: {nome}")
print(f"Classificação: {classificacao}")