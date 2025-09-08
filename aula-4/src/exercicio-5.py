alunos_e_notas = {
    "Marcos": [7, 6, 2, 5],
    "Aleff": [10, 8, 9, 5],
    "Lucas": [1, 8, 9, 5],
}

def calcula_media_alunos(notas: dict[str, list[int]]) -> dict[str, int]:
    result = {}
    for aluno in notas:
        soma_notas: int = 0
        for nota in notas[aluno]:
            soma_notas += nota
        media: int = soma_notas // 4
        result[aluno] = media
    return result

print(calcula_media_alunos(alunos_e_notas))

# alunos_e_medias = {
#     "Marcos": 5,
#     "Aleff": 8
# }
