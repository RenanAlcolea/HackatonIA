############################# Análise de Base de Comportamento Web com Inteligência Artifical - Classificador SVM ############################

from sklearn import model_selection
from sklearn.metrics import f1_score,recall_score,precision_score,confusion_matrix
from sklearn.svm import SVC
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

def accuracySVM(x_train, x_test, y_train, y_test):   
    classificador = SVC()   
    classificador.fit(x_train, y_train)
    accuracy = classificador.score(x_test, y_test)
    print('\nA porcentagem de acerto do SVM é de: ' + str((accuracy) * 100) + '%') 


def F1ScoreSVM(x_train, x_test, y_train, y_test):
    classificador = SVC()
    classificador.fit(x_train, y_train)
    y_pred = classificador.predict(x_test)
    f1 = f1_score(y_test, y_pred, average='binary') 
    print('\nO F1 Score do SVM é: ' + str(f1))

def recallSVM(x_train, x_test, y_train, y_test):
    classificador = SVC()
    classificador.fit(x_train, y_train)
    y_pred = classificador.predict(x_test)
    recall = recall_score(y_test, y_pred, average='binary') 
    print('\nO Recall do SVM é: ' + str(recall))

def precisionSVM(x_train, x_test, y_train, y_test):
    classificador = SVC()
    classificador.fit(x_train, y_train)
    y_pred = classificador.predict(x_test)
    precision = precision_score(y_test, y_pred, average='binary')
    print('\nA precisão do SVM é: ' + str(precision))

def confusionMatrixSVM(x_train, x_test, y_train, y_test):
    classificador = SVC()
    classificador.fit(x_train, y_train)
    y_pred = classificador.predict(x_test)
    conf_matrix = confusion_matrix(y_test, y_pred)
    
    plt.figure(figsize=(10, 7))
    sns.heatmap(conf_matrix, annot=True, fmt="d")
    plt.title("Matriz de Confusão para SVM")
    plt.ylabel("Verdadeiro")
    plt.xlabel("Predito")
    plt.show()


def predictSVM(samples, x_train, y_train):    
    classificador = SVC(C=1.0, kernel='rbf')
    classificador.fit(x_train, y_train)    
    predicoes = classificador.predict(samples)    
    contagem_classes = Counter(predicoes)    
    labels = contagem_classes.keys()
    sizes = contagem_classes.values()

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal') 
    plt.title('Distribuição das Classes Previstas (SVM)')
    plt.show()