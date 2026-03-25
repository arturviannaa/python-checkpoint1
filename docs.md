# Sistema de Triagem Hospitalar (Simples)

## Descrição

Esse código é um script simples em Python que simula uma triagem básica de pacientes.  
A ideia é pegar algumas informações e classificar o nível de urgência do atendimento.

## Objetivo

Classificar o paciente em:

- Emergência
- Urgência
- Pouco urgente

Com base em:

- Temperatura
- Nível de dor
- Dificuldade para respirar

## Como funciona

O programa pede os seguintes dados:

- Nome do paciente
- Temperatura corporal
- Nível de dor (0 a 10)
- Se tem dificuldade para respirar (S ou N)

Depois disso, ele aplica as regras:

- Se tiver dificuldade para respirar OU temperatura maior ou igual a 39 OU dor maior ou igual a 8 → Emergência
- Senão, se temperatura maior ou igual a 37.5 OU dor maior ou igual a 5 → Urgência
- Caso contrário → Pouco urgente

## Código

```python
nome = input("Nome do paciente: ")
temperatura = float(input("Temperatura corporal (°C): "))
nivel_dor = int(input("Nível de dor (0 a 10): "))
dificuldade_respirar = input("Apresenta dificuldade para respirar? (S/N): ").strip().upper()

classificacao = "Pouco Urgente (Verde)"

if dificuldade_respirar == "S" or temperatura >= 39.0 or nivel_dor >= 8:
    classificacao = "Emergência (Vermelho)"
elif temperatura >= 37.5 or nivel_dor >= 5:
    classificacao = "Urgência (Amarelo)"

print(f"\nResultado da Triagem")
print(f"Paciente: {nome}")
print(f"Classificação: {classificacao}")
```