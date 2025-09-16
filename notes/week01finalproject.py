import pandas as pd 
import numpy as np

df=pd.read_csv('D:/365-Day-Data-AI-Roadmap/notes/sales.csv')
print(df.head())

df2=pd.read_csv('D:/365-Day-Data-AI-Roadmap/notes/products.csv')
print(df2.head())

mergeddata=pd.merge(df,df2,on='ProductID')
print(mergeddata)

mergeddata['Revenue']=mergeddata['Quantity']*mergeddata['Price']
print(mergeddata)

grouped_mergeddata=mergeddata.groupby("Category")['Revenue'].sum()
print(grouped_mergeddata)

print(grouped_mergeddata.idxmax())


###numby and pandas mix election data to be analyzeed

import pandas as pd
import numpy as np

data = {
    'Candidate': ['Candidate A', 'Candidate B', 'Candidate C', 'Candidate D'],
    'Region': ['North', 'South', 'North', 'South'],
    'Votes': np.array([180000, 250000, 120000, 310000]) # Using a NumPy array here!
}

df = pd.DataFrame(data)
print(df)
df['Vote_Share']=(df['Votes']/df['Votes'].sum())*100
df['Final Votes']=df["Votes"]+500
print(df)
high_performers_df=df[df['Votes']>200000]

print(high_performers_df)
