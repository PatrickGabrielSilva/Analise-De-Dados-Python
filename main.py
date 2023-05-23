# importar base de dados
import pandas as pd
import plotly.express as px

# carregar o DataFrame a partir do arquivo CSV
tabela = pd.read_csv("C:\\Users\\patrick.ssoares\\Desktop\\chatgpt\\Intensivão de python\\clientes.csv", encoding="latin", sep=";")


# Deletar colunas desnecessárias
    # axis = 0 se for uma linha, axis = 1 para deletar uma coluna
tabela = tabela.drop("Unnamed: 8", axis=1)

tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")
tabela = tabela.dropna()
    #print(tabela.info())


# Entender como estão as notas dos clientes
    #print(tabela.describe())

# Criar o Gráfico
grafico = px.histogram(tabela, x="Salário Anual (R$)" ,y="Nota (1-100)")

# Mostra o Gráfico
grafico.show()