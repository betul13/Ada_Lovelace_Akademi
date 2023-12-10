import numpy as np
import pandas as pd
df = pd.DataFrame({
    'Population': [35.467, 63.951, 80.94 , 60.665, 127.061, 64.511, 318.523],
    'GDP': [
        1785387,
        2833687,
        3874437,
        2167744,
        4602367,
        2950039,
        17348075
    ],
    'Surface Area': [
        9984670,
        640679,
        357114,
        301336,
        377930,
        242495,
        9525067
    ],
    'HDI': [
        0.913,
        0.888,
        0.916,
        0.873,
        0.891,
        0.907,
        0.915
    ],
    'Continent': [
        'America',
        'Europe',
        'Europe',
        'Europe',
        'Asia',
        'Europe',
        'America'
    ]
}, columns=['Population', 'GDP', 'Surface Area', 'HDI', 'Continent'])
df
df.index = [
    'Canada',
    'France',
    'Germany',
    'Italy',
    'Japan',
    'United Kingdom',
    'United States',
]
df


df.columns
df.index
df.info()
df.describe()
df.head()
df.size
df.shape

df.loc["Canada"]

df.iloc[0]

df["Continent"].to_frame()

df[["Continent", "GDP"]]

df[1:3]
df.loc['France': 'Italy']
a = df.loc['France': 'Italy', 'GDP']
type(a)
df.loc['France': 'Italy', ['GDP', 'Population']]

df.loc[df['Population'] > 70]

df.drop("Canada")
df.drop(['Canada', 'Japan'])

df.drop(columns=["Population", "HDI"])

df.drop(['Population', 'HDI'], axis=1)
df.drop(['Population', 'HDI'], axis="columns")

df[['Population', 'GDP']] / 100

langs = pd.Series(
    ['French', 'German', 'Italian'],
    index=['France', 'Germany', 'Italy'],
    name='Language'
)

df["language"] = langs
df["Language"] = langs
df = df.drop(["language"], axis="columns")


new_row = pd.Series({
    'Population': 83.000,
    'Continent': 'Europe',
    'Language': 'Türkçe'
}, name = "Türkiye"
)

new_row
new_row = new_row.to_frame()
pd.concat([df, new_row.T], ignore_index=False)

