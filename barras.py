# Bibliotecas do Sistema
import matplotlib.pyplot as plt
import random  # Excluir essa biblioteca para a execução do projeto


#Geração de dados aleatórios para preencher os eixos x e y dos gráficos
def FiltrarEntrada(dados):
  y = []

  # Dados gerados aleatoriamente
  for i in range(5):
    y.append(int (random.random() * 10))
  
  x = ["A", "B", "C", "D", "E" ]
  
  # Retorno da função com os dados preenchidos com os eixos x e y
  return (x, y)

# Função de geração de gráfico usando a biblioteca matplotlib 
def GerarGrafico(x, y):
  plt.bar(x, y)
  plt.title('SEU TÍTULO')
  plt.xlabel('NOME DO EIXO X')
  plt.ylabel('NOME DO EIXO Y')
  plt.savefig('barras.png')
  plt.close()


# Função que será chamada no arquivo main
def ApresentarGraficoDeBarras(dados):
  tuplaDados = FiltrarEntrada(dados)
  GerarGrafico(tuplaDados[0], tuplaDados[1])