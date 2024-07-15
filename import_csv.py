import csv

# Nome dos arquivos CSV
arquivo_abril = 'abril_2024.csv'
arquivo_maio = 'maio_2024.csv'
arquivo_combinado = 'combinado_abril_maio_2024.csv'

# Lista para armazenar as linhas combinadas
dados_combinados = []

# Ler os dados do arquivo CSV de abril (com cabeçalho)
with open(arquivo_abril, newline='', encoding='utf-8') as csvfile:
    # Abre o arquivo 'arquivo_abril' no modo de leitura ('r')
    # 'newline=''' evita a adição automática de novas linhas pelo Python
    # 'encoding='utf-8'' define a codificação do arquivo para UTF-8
    leitor = csv.reader(csvfile)
    # Cria um leitor de CSV que itera sobre cada linha do arquivo CSV

    for linha in leitor:
        # Itera sobre cada linha no arquivo CSV
        dados_combinados.append(linha)
        # Adiciona cada linha (uma lista de valores) à lista 'dados_combinados'

# Ler os dados do arquivo CSV de maio (ignorando o cabeçalho)
with open(arquivo_maio, newline='', encoding='utf-8') as csvfile:
    # Abre o arquivo 'arquivo_maio' no modo de leitura ('r')
    # 'newline=''' evita a adição automática de novas linhas pelo Python
    # 'encoding='utf-8'' define a codificação do arquivo para UTF-8
    leitor = csv.reader(csvfile)
    # Cria um leitor de CSV que itera sobre cada linha do arquivo CSV

    next(leitor)
    # Pula a primeira linha do arquivo CSV (cabeçalho)
    
    for linha in leitor:
        # Itera sobre cada linha no arquivo CSV, começando da segunda linha
        dados_combinados.append(linha)
        # Adiciona cada linha (uma lista de valores) à lista 'dados_combinados'

# Escrever os dados combinados em um novo arquivo CSV
with open(arquivo_combinado, 'w', newline='', encoding='utf-8') as csvfile:
    # Abre o arquivo 'arquivo_combinado' no modo de escrita ('w')
    # 'newline=''' evita a adição automática de novas linhas pelo Python
    # 'encoding='utf-8'' define a codificação do arquivo para UTF-8
    escritor = csv.writer(csvfile)
    # Cria um escritor de CSV que permite escrever linhas no arquivo CSV

    for linha in dados_combinados:
        # Itera sobre cada linha na lista 'dados_combinados'
        escritor.writerow(linha)
        # Escreve cada linha da lista 'dados_combinados' no novo arquivo CSV

print("Arquivos CSV unidos e salvos com sucesso!")
# Exibe uma mensagem indicando que os arquivos CSV foram unidos e salvos com sucesso