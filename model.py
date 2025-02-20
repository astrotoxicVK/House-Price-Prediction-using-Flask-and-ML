import pandas as pd 
from sklearn.linear_model import LinearRegression
import pickle

df=pd.read_json('Data/House_Price.json')

x=df[['Area(in sq. ft)', 'Number of Bedrooms']].values
y=df['Price(in Rs.)'].values.reshape(-1,1)

lin=LinearRegression()
lin.fit(x,y)
pickle.dump(lin,open('model.pkl','wb'))
print("Model retrained and saved successfully!")