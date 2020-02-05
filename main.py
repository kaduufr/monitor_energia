
############################################################
# Dados da Equipe
############################################################
# Nome do Aluno 1
# Nome do Aluno 2
# Turma
# Graficos sorteados: 
# 3 2 3
############################################################
# Arquivos com bibliotecas definidas pelo(a) programador(a)
############################################################
import linha
import barras
import boxplot
import dados

# dados para serem tratados

dadosComoJson = dados.getDados()


############################################################
# Chamada das funções para a geração dos gráficos
############################################################

# barras.ApresentarGraficoDeBarras(dados)
linha.ApresentarGraficoDeLinha(dados.ordenarDadosComoDicionario(dadosComoJson))
# boxplot.ApresentarGraficoBoxplot(dados)