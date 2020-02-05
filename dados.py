import requests

############################################################
# Função que busca todos os dados e os retorna 
############################################################

def getDados():
    dados = requests.get('http://albertocn.sytes.net/2019-2/pi/projeto/geracao_energia.json').json()
    return dados

def ordenarDadosComoDicionario(dados):
    dicDados = {}
    for dado in dados:
        dicDados[dado['dia']] = dado['energiaDia']

    return sorted(dicDados.items(), key=str )    
    