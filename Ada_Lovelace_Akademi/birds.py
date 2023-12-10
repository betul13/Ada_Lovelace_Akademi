import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches
import seaborn as sns
import numpy as numpy
import pandas as pd

birds = pd.read_csv(r"C:\Users\bett0\Downloads\birds.csv")

birds.dtypes
birds.info()



###### ilk üç kategori######
top_categories = birds['Category'].value_counts().head(3).index

sns.countplot(x='Category', data=birds, order=top_categories)
plt.show()




#####cinsine göe max kanat uzunlukları ########

genus_max_wingspan_df = birds.groupby('Genus')['MaxWingspan'].max().reset_index()
# Plotting
plt.figure(figsize=(12, 6))
sns.barplot(x='Genus', y='MaxWingspan', data=genus_max_wingspan_df)
plt.xticks(rotation=90)
plt.xlabel('Kuş Cinsi')
plt.ylabel('Maksimum Kanat Uzunluğu')
plt.title('Kuş Cinsine Göre Maksimum Kanat Uzunluğu')
plt.show()


sns.histplot(data=birds, x='MinBodyMass', kde=True)
plt.show()



plt.barh(y = birds["Family"].value_counts().sort_values(ascending=False).iloc[0:5].index,
         width =birds["Family"].value_counts().sort_values(ascending=False).iloc[0:5].values)

plt.show()

family_counts = birds["Family"].value_counts()

#Aile sayısı
# Seri -> Dataframe
family_counts_df = pd.DataFrame({'Family': family_counts.index, 'SpeciesCount': family_counts.values})

# Plotting
plt.figure(figsize=(10, 6))
sns.barplot(x='Family', y='SpeciesCount', data=family_counts_df)
plt.xticks(rotation=90)
plt.xlabel('Family')
plt.ylabel('Number of Species')
plt.title('Number of Species per Family')
plt.show()