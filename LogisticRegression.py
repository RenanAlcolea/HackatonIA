############################# Análise de Base de Comportamento Web com Inteligência Artifical - Classificador Regressão Logística ############################

import matplotlib.pyplot as plt
from sklearn import preprocessing, model_selection
from sklearn.linear_model import LogisticRegression
import seaborn as sns
from sklearn.metrics import recall_score, f1_score,precision_score,confusion_matrix
from collections import Counter


def accuracyLR(x_train, x_test, y_train, y_test):     
    classificador = LogisticRegression(C=1.0, max_iter=100000)  
    classificador.fit(x_train, y_train)
    accuracy = classificador.score(x_test, y_test)
    print('\nAcurácia da Regressão Logística é de: ' + str((accuracy) * 100) + '%') 

def F1ScoreLR(x_train, x_test, y_train, y_test):    
    classificador = LogisticRegression(C=1.0, max_iter=100000)
    classificador.fit(x_train, y_train)    
    y_pred = classificador.predict(x_test)
    
    f1 = f1_score(y_test, y_pred, average='macro')  
    print('F1 Score da Regressão Logística: ', str(f1 * 100) + '%')
    
    plt.scatter(['F1 Score'], [f1], color='blue')
    plt.ylim(0, 1)
    plt.ylabel('F1 Score')
    plt.title('F1 Score da Regressão Logística')
    plt.grid()
    plt.show()

def recallLR(x_train, x_test, y_train, y_test):
    classificador = LogisticRegression(C=1.0, max_iter=100000)
    classificador.fit(x_train, y_train)
    y_pred = classificador.predict(x_test)
    recall = recall_score(y_test, y_pred)
    print('\nO Recall da Regressão Logística é de: ' + str(recall * 100) + '%')

def precisionLR(x_train, x_test, y_train, y_test):
    classificador = LogisticRegression(C=1.0, max_iter=100000)
    classificador.fit(x_train, y_train)
    y_pred = classificador.predict(x_test)
    precision = precision_score(y_test, y_pred)
    print('\nA Precisão da Regressão Logística é de: ' + str(precision * 100) + '%')


def confusion_matrixLR(x_train, x_test, y_train, y_test):
    classificador = LogisticRegression()
    classificador.fit(x_train, y_train)
    y_pred = classificador.predict(x_test)    
    conf_matrix = confusion_matrix(y_test, y_pred)

    plt.figure(figsize=(10, 7))
    sns.heatmap(conf_matrix, annot=True, fmt="d")
    plt.title("Matriz de Confusão para Regressão Logística")
    plt.ylabel("Verdadeiro")
    plt.xlabel("Predito")
    plt.show()


def predictLR(samples, x_train, y_train):
    classificador = LogisticRegression(max_iter=100000)
    classificador.fit(x_train, y_train)    
    predicoes = classificador.predict(samples)    
    contagem_classes = Counter(predicoes)    
    labels = contagem_classes.keys()
    sizes = contagem_classes.values()
    
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  
    plt.title('Distribuição das Classes Previstas (Regressão Logística)')    
    plt.show()

