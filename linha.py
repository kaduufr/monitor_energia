# Bibliotecas do Sistema
import matplotlib.pyplot as plt

#Geração de dados aleatórios para preencher os eixos x e y dos gráficos
def FiltrarEntrada(dados):
  x = []
  y = []
  #tirar duvida com galileu porque como tem 365 de dados, as datas nao esta aparecendo
  for i in dados:
    x.append(i[0])
    y.append(i[1])
  # Dados gerado aleatoriamente

  # Retorno da função com os dados preenchidos com os eixos x e y
  return (x, y)

# Função de geração de gráfico usando a biblioteca matplotlib 
def GerarGrafico(x, y):
  plt.plot(x, y)
  plt.title('Grafico de energia/dia durante o ano')
  plt.xlabel('Dia')
  plt.ylabel('Energia')
  plt.savefig('linha.png')
  plt.close()

# Função que será chamada no arquivo main
def ApresentarGraficoDeLinha(dados):
  tuplaDados = FiltrarEntrada(dados)
  GerarGrafico(tuplaDados[0], tuplaDados[1])