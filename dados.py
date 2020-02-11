import requests

############################################################
# Função que busca todos os dados e os retorna no formato json
############################################################

def getDados():
    return requests.get('http://albertocn.sytes.net/2019-2/pi/projeto/geracao_energia.json').json()
    
############################################################
# funções para o grafico de linha
############################################################
def getIndexParaOrdenar(item):
    return item[0]

def ordenarDadosComoTuplas():

    dados = getDados()
    
    listaDadosAgrupados = []
    for dado in dados:
        listaDadosAgrupados.append((dado['dia'],dado['energiaDia']))
    
    listaDadosAgrupados.sort(key=getIndexParaOrdenar)
    return listaDadosAgrupados

############################################################
# funções para o grafico de barra
############################################################

def getTotalDeEnergiaDoMes(dados, mes):
    totalDeEnergia = 0
    inicioDoMes = ''
    fimDoMes = ''

    if mes < 10:
        inicioDoMes = '2019-0' + str(mes) + '-01'
        fimDoMes = '2019-0' + str(mes) + '-31'

    else:
        inicioDoMes = '2019-' + str(mes) + '-01' 
        fimDoMes = '2019-' + str(mes) + '-31' 

    for dado in dados:
        if dado['dia'] >= inicioDoMes and dado['dia'] <= fimDoMes :
            totalDeEnergia = totalDeEnergia + dado['energiaDia']
    
    return totalDeEnergia

def ordenarDadosPorMes():
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Sembro", "Outubro", "Novembro", "Dezembro"]
    dadosJson = getDados()

    listaDeDadosPorMes = []

    for i in range(12):
        listaDeDadosPorMes.append((meses[i] ,getTotalDeEnergiaDoMes(dadosJson, i+1)))
    
    return listaDeDadosPorMes
    
############################################################
# funções para o grafico boxplot
############################################################

def getDadosPorEstacao():

    dadosOrdenados = ordenarDadosComoTuplas()

    estacoes = [
        {
            'nomeEstacao': 'Outuno',
            'dataInicio': '2019-03-20',
            'dataFim' : '2019-07-20',
            'energiaGastaNaEstacao': []
        },
        {
            'nomeEstacao': 'Inverno',
            'dataInicio': '2019-07-21',
            'dataFim' : '2019-09-22',
            'energiaGastaNaEstacao': []
        },
        {
            'nomeEstacao': 'Primavera',
            'dataInicio': '2019-09-23',
            'dataFim' : '2019-12-21',
            'energiaGastaNaEstacao': []
        },
        {
            'nomeEstacao': 'Verão',
            'dataInicio': '2019-12-22',
            'dataFim' : '2019-03-19',
            'energiaGastaNaEstacao': []
        },
    ]

    for dado in dadosOrdenados:
        for estacao in estacoes:
            if estacao['dataInicio'] <= dado[0] and estacao['dataFim'] >= dado[0]:
                estacao['energiaGastaNaEstacao'].append(dado[1])
            elif estacao['dataFim'] >= dado[0]:
                estacao['energiaGastaNaEstacao'].append(dado[1])                

    return estacoes
