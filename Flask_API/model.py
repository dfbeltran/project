import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv('Salary_Data.csv')
X = df.iloc[:,:-1].values
y = df.iloc[:,1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

lr = LinearRegression(fit_intercept=True)
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)

pickle.dump(lr, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))

print(model.predict([[1.8]]))