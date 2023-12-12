############################# Análise de Base de Comportamento Web com Inteligência Artifical - Classificador Random Forest ############################

from sklearn import model_selection
from sklearn.metrics import f1_score,recall_score,precision_score,confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns


def accuracyRF(x_train, x_test, y_train, y_test):   
    classificador = RandomForestClassifier(n_estimators=100)  
    classificador.fit(x_train, y_train)
    accuracy = classificador.score(x_test, y_test)
    print('\nA acurácia do Random Forest é de: ' + str((accuracy) * 100) + '%') 

def F1ScoreRF(x_train, x_test, y_train, y_test):
    classificador = RandomForestClassifier(n_estimators=100)
    classificador.fit(x_train, y_train)
    y_pred = classificador.predict(x_test)
    f1 = f1_score(y_test, y_pred)

    print('\nO F1 Score do Random Forest é de: ' + str((f1) * 100) + '%')

def precisionRF(x_train, x_test, y_train, y_test):    
    classificador = RandomForestClassifier(n_estimators=100)  
    classificador.fit(x_train, y_train)    
    y_pred = classificador.predict(x_test)    
    precisao = precision_score(y_test, y_pred)
    
    print('\nA precisão do Random Forest é de: ' + str((precisao) * 100) + '%') 

def recallRF(x_train, x_test, y_train, y_test):   
    classificador = RandomForestClassifier(n_estimators=100)
    classificador.fit(x_train, y_train)
    y_pred = classificador.predict(x_test)
    recall = recall_score(y_test, y_pred)

    print('\nO recall do Random Forest é de: ' + str((recall) * 100) + '%')

def confusion_matrixRF(x_train, x_test, y_train, y_test):   
    classificador = RandomForestClassifier(n_estimators=100)
    classificador.fit(x_train, y_train)
    y_pred = classificador.predict(x_test)
    conf_matrix = confusion_matrix(y_test, y_pred)

    print('\nMatriz de confusão do Random Forest:')
    print(conf_matrix)
    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix, annot=True, fmt='g', cmap='Blues')
    plt.title('Matriz de Confusão - Random Forest')
    plt.ylabel('Verdadeiros')
    plt.xlabel('Previstos')
    plt.show()

def predictRF(samples, x_train, y_train):
    
    classificador = RandomForestClassifier(n_estimators=200)
    classificador.fit(x_train, y_train)
    
    predicoes = classificador.predict(samples)
    
    contagem_classes = Counter(predicoes)
    
    labels = contagem_classes.keys()
    sizes = contagem_classes.values()
    
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal') 
    plt.title('Distribuição das Classes Previstas (Random Forest)')    
    plt.show()

    from collections import Counter


def predictRF(samples, x_train, y_train):
    
    classificador = RandomForestClassifier(n_estimators=200)
    classificador.fit(x_train, y_train)
    
    predicoes = classificador.predict(samples)    
    
    contagem_classes = Counter(predicoes)    
    
    labels_map = {0: 'Normal', 1: 'Attacker'}    
    
    labels = [labels_map[label] if label in labels_map else label for label in contagem_classes.keys()]
    sizes = contagem_classes.values()    
    
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal') 
    plt.title('Distribuição das Classes Previstas (Random Forest)')    
    plt.show()
