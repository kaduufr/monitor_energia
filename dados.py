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
    
