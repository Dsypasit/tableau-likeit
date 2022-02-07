import numpy as np
import pandas as pd
import altair as alt
cols = []
melb = pd.read_csv(
  'Tableua\Superstore.csv', encoding='windows-1252'#, usecols = cols
).sample(n=1000).reset_index(drop=True)
melb.head()

alt.Chart(melb).mark_bar().encode(
   x = 'Regionname', y = 'avg_price:Q'
).transform_aggregate(
   avg_price = 'mean(Price)', groupby = ['Regionname']
).properties(
   height = 300, width = 500
)