import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

data = pd.read_csv("data/news.csv")

data['label'] = data['label'].map({
    'FAKE': 0,
    'REAL': 1
})

x = data['text']
y = data['label']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2,random_state=3)

vectorization = TfidfVectorizer(stop_words='english')
x_train = vectorization.fit_transform(x_train)
x_test = vectorization.transform(x_test)

model = LogisticRegression(class_weight='balanced', max_iter=1000)
model.fit(x_train, y_train)

pred = model.predict(x_test)

accuracy = accuracy_score(y_test,pred)
print("Accuracy:", accuracy)

joblib.dump((model, vectorization), 'model/model.pkl')

print("Model Saved Successfully")