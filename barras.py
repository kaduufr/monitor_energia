# Bibliotecas do Sistema
import matplotlib.pyplot as plt

################################################
# Mostra o total de energia gerada em cada mês (kwh) de um certo ano. Para isso
# será preciso fazer o somatório do total de energia gerada em cada dia do mês
# correspondente a cada barra do gráfico 

def FiltrarEntrada(dados):
  
  y = []
  x = []
  
  for dadoDoMes in dados:
    x.append(dadoDoMes[0])
    y.append(dadoDoMes[1])

  # Retorno da função com os dados preenchidos com os eixos x e y
  return (x, y)

# Função de geração de gráfico usando a biblioteca matplotlib 
def GerarGrafico(x, y):
  plt.bar(x, y)
  plt.title('SEU TÍTULO')
  plt.xlabel('Meses')
  plt.ylabel('Energia Total')
  plt.savefig('barras.png')
  plt.close()


# Função que será chamada no arquivo main
def ApresentarGraficoDeBarras(dados):
  tuplaDados = FiltrarEntrada(dados)
  GerarGrafico(tuplaDados[0], tuplaDados[1])