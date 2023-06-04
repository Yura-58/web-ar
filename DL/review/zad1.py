import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
from flask import Flask, request, render_template
pip install flask scikit-learn pandas

app = Flask(__name__)

# Завантаження та попередня обробка даних
data = pd.read_csv(" <li> <a href=DL/review/Dataset 11000 Reviews.tsv>DL: Рецензія</a></li>, delimiter="\t")
texts = data['Text'].values
labels = data['Sentiment'].values

# Розбиття на тренувальний та тестовий набори даних
train_texts, test_texts, train_labels, test_labels = train_test_split(texts, labels, test_size=0.2, random_state=42)

# Векторизація тексту
vectorizer = CountVectorizer()
train_vectors = vectorizer.fit_transform(train_texts)
test_vectors = vectorizer.transform(test_texts)

# Побудова та навчання моделі
model = svm.SVC()
model.fit(train_vectors, train_labels)

# Функція класифікації тексту
def classify_text(text):
    vector = vectorizer.transform([text])
    prediction = model.predict(vector)[0]
    return prediction

# Маршрути веб-інтерфейсу
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    text = request.form['text']
    prediction = classify_text(text)
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)