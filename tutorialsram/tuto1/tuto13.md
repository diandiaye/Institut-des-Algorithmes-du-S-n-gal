
# Institut des Algorithmes du Sénégal

# Modèle de prédiction en quelques lignes de codes



```ruby
#Ton premier modèle de Data Science en quelques lignes de code
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
df = pd.read_csv('data.csv')
X, y = df.drop(['Prix'], axis = 1), df['Prix']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
reg = LinearRegression()
reg.fit(X_train,y_train)
prediction = reg.predict(X_test)
print(prediction)
```

```ruby
import matplotlib.pyplot as plt
df.plot(x='surface', y='Prix', style='o')
plt.title('surface vs Price')
plt.xlabel('surface')
plt.ylabel('Prix')
plt.show()
```

