

notasAlunos = {
    "Bianca": 8.5,
    "Bruno": 6.0,
    "José": 7.2,
    "Tadeu": 9.0,
    "Rogerio": 5.5
}

print("Notas dos alunos:")
print(notasAlunos)

print("\nAlunos com nota maior ou igual a 7:")
for nome, nota in notasAlunos.items():
    if nota >= 7:
        print(f"{nome}: {nota}")