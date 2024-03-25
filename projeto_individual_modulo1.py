# Função para verificar se um candidato atende aos critérios de nota mínima
def buscar_candidatos(lista, nota_minima):
    candidatos_atendidos = []
    for i, resultado in enumerate(lista, start=1): # Permite percorrer uma lista (ou qualquer iterável) ao mesmo tempo em que acompanha o índice de cada elemento
        notas = [int(x[1:]) for x in resultado.split('_')]  # Extrai as notas de cada etapa / # split = oferece uma maneira eficaz de dividir strings, facilitando a manipulação e extração de informações relevantes.
        if all(nota >= minima for nota, minima in zip(notas, nota_minima)): # All = vai analisar todos os itens da lista, ou seja, o resultado só é positivo (Foi) se todos os valores da lista forem positivos. / # zip = Ela permite combinar elementos de duas ou mais listas em uma única estrutura de dados.
            candidatos_atendidos.append(i)  # append = é usado para adicionar elementos ao final de uma lista existente.
    return candidatos_atendidos

# Exemplo de lista de resultados
resultados = [
    "e5_t9_p8_s8",
    "e9_t7_p7_s8",
    "e8_t5_p4_s9",
    "e2_t2_p2_s1",
    "e9_t9_p8_s9"
]

# Exemplo de critérios de busca (nota mínima de e, t, p, s)
critérios_busca = [4, 4, 8, 8]

# Buscar candidatos que atendam aos critérios
candidatos_atendidos = buscar_candidatos(resultados, critérios_busca)

# Mostrar resultados
if candidatos_atendidos:
    print("Candidatos que atendem aos critérios:")
    for candidato in candidatos_atendidos:
        print(f"Candidato {candidato}")
else:
    print("Nenhum candidato atende aos critérios especificados.")
