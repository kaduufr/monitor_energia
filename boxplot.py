# Bibliotecas do Sistema
import matplotlib.pyplot as plt
import random  # Excluir essa biblioteca para a execução do projeto

#Geração de dados aleatórios para preencher os eixos x e y dos gráficos
def FiltrarEntrada(dados):

  estacoes = []
  dadosDeCadaEstacao= []

  for dado in dados:
    estacoes.append(dado['nomeEstacao'])
    dadosDeCadaEstacao.append(dado['energiaGastaNaEstacao'])
  
  # Retorno da função com os dados preenchidos com os eixos x e y
  return (estacoes, dadosDeCadaEstacao)

# Função de geração de gráfico usando a biblioteca matplotlib 
def GerarGrafico(x, y):
  plt.boxplot(y, labels=x)
  plt.title('SEU TÍTULO')
  plt.xlabel('NOME DO EIXO X')
  plt.ylabel('NOME DO EIXO Y')
  plt.savefig('boxplot.png')
  plt.close()


# Função que será chamada no arquivo main
def ApresentarGraficoBoxplot(dados):
  tuplaDados = FiltrarEntrada(dados)
  GerarGrafico(tuplaDados[0], tuplaDados[1])