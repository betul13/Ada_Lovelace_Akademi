import pandas as pd

#Pandas Series

g7_pop = pd.Series([34.24, 44.5, 56.7, 78.5, 678.6])

g7_pop.name = "G7 Population in millions"

g7_pop.values, g7_pop.dtypes

g7_pop.index = ["Canada", "France", "Germany", "Italy", "Japan"]

pd.Series(g7_pop, index = ["France", "Germany"])

g7_pop.iloc[-1]

g7_pop[["Canada", "France"]]

g7_pop[(g7_pop > g7_pop.mean()) | (g7_pop > ((g7_pop.std())/2 + g7_pop.mean()))]

g7_pop["Canada":"France"].mean()