def ler_e_processar_dataset(ficheiro):
    with open(ficheiro, "r") as arquivo:
        linhas = arquivo.readlines()[1:]  # Ignorar cabeçalho

    modalidades = set()
    aptos = inaptos = 0
    distribuicao_idades = {}

    for linha in linhas:
        id, index, data, primeiro_nome, ultimo_nome, idade, gerero, morada, modalidade, clube, email, federado, resultado = linha.strip().split(',')
        idade = int(idade)

        # Atualizar lista de modalidades
        modalidades.add(modalidade)

        # Contar atletas aptos e inaptos
        if resultado == "true":
            aptos += 1
        else:
            inaptos += 1

        # Distribuição por escalão etário
        escalao = (idade // 5) * 5
        if escalao not in distribuicao_idades:
            distribuicao_idades[escalao] = 0
        distribuicao_idades[escalao] += 1

    # Processamento final
    modalidades_ordenadas = sorted(list(modalidades))
    total_atletas = aptos + inaptos
    percentagem_aptos = (aptos / total_atletas) * 100
    percentagem_inaptos = (inaptos / total_atletas) * 100
    distribuicao_ordenada = sorted(distribuicao_idades.items())

    return modalidades_ordenadas, percentagem_aptos, percentagem_inaptos, distribuicao_ordenada



modalidades, aptos, inaptos, distribuicao = ler_e_processar_dataset('emd.csv')

print("Modalidades ordenadas alfabeticamente:", modalidades)
print(f"Percentagem de atletas aptos: {aptos:.2f}%")
print(f"Percentagem de atletas inaptos: {inaptos:.2f}%")
print("Distribuição de atletas por escalão etário:", distribuicao)
