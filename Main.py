import pandas as pd
from bs4 import BeautifulSoup
import requests 
import time
import json

def gerador_de_ativos():


# Lista para armazenar os dados de todas as páginas
    all_data = []

    for page_index in range(1, 24):  # Alterar para o número de páginas que você precisa
        # Gerar a URL para a página específica
        url_total = f'https://api.infomoney.com.br/ativos/top-alta-baixa-por-ativo/acao?sector=Todos&orderAtributte=Volume&pageIndex={page_index}&p'
        
        # Fazer a requisição
        response = requests.get(url_total)
        
        # Verificar o status da resposta
        if response.status_code == 200:
            # Processar a resposta
            data = response.json()  # Assumindo que a resposta é em JSON
            data = data['Data']  # Acessar os dados da chave 'Data'
            all_data.append(data)  # Adiciona os dados da página à lista
            print(f"Dados da página {page_index} adicionados à lista.")
        else:
            print(f"Erro ao acessar a página {page_index}: {response.status_code}")

    # Criar uma lista para armazenar as informações dos ativos
    ativos_list = []

    # Percorrer os dados de todas as páginas coletadas e armazenar as informações de cada ativo
    for page_data in all_data:
        for ativo in page_data:
            ativo_info = {
                'Date': ativo['Date'],
                'StockCode': ativo['StockCode'],
                'StockName': ativo['StockName'],
                'ValueFormatted': ativo['ValueFormatted'],
                'ChangeDayFormatted': ativo['ChangeDayFormatted'],
                'Change12MFormatted': ativo['Change12MFormatted'],
                'VolumeFormatted': ativo['VolumeFormatted']
            }
            ativos_list.append(ativo_info)

    # Criar o DataFrame usando a lista de dicionários
    df = pd.DataFrame(ativos_list)

    # Exibir o DataFrame com os dados de todos os ativos
    print(df.head())  # Exibe as primeiras linhas do DataFrame

    # Exibir o DataFrame
    print(df)
    df.to_csv('ativos.csv', index=False)

    # Informar ao usuário que o arquivo foi salvo
    print("Arquivo CSV 'ativos.csv' salvo com sucesso!")

gerador_de_ativos()