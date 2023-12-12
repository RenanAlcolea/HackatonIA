############################# Análise de Base de Comportamento Web com Inteligência Artifical - Classificador KNN ############################

from sklearn import preprocessing, model_selection, neighbors
from sklearn.metrics import confusion_matrix,f1_score,recall_score,precision_score
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from sklearn.metrics import classification_report

def accuracyKNN(k, x_train, x_test, y_train, y_test):
    accuracies = []
    for i in range(1, k + 1):
        classifier = neighbors.KNeighborsClassifier(n_neighbors=i, metric='euclidean')
        classifier.fit(x_train, y_train)
        accuracy = classifier.score(x_test, y_test)
        accuracies.append(accuracy)
        print('A acurácia do KNN com K valendo' + ' ' + str(i) + ' ' + 'é de: + ' + str(accuracy*100) + ' ' + '%')

    plt.figure()
    plt.xlabel('k')
    plt.ylabel('Precisão')
    plt.scatter(range(1, k + 1), accuracies)
    plt.xticks(range(1, k + 1))
    plt.grid()
    plt.show()

def F1ScoreKNN(k_range, x_train, y_train, x_test, y_test):
    f1_scores = []
    for k in k_range:
        clf = neighbors.KNeighborsClassifier(n_neighbors=k)
        clf.fit(x_train, y_train)
        y_pred = clf.predict(x_test)
        f1 = f1_score(y_test, y_pred, average='macro')  
        print('o F1-Score do KNN com K valendo' + ' ' + str(k) + ' ' + 'é de: + ' + str(f1*100) + ' ' + '%')
        f1_scores.append(f1)

    plt.figure()
    plt.xlabel('k')
    plt.ylabel('F1 Score')
    plt.plot(k_range, f1_scores, marker='o')
    plt.xticks([i for i in k_range])
    plt.grid()
    plt.show()


def recallKNN(k, x_train, x_test, y_train, y_test):
    for i in range(1, k + 1):
        classificador = neighbors.KNeighborsClassifier(n_neighbors=i, metric='euclidean')
        classificador.fit(x_train, y_train)
        y_pred = classificador.predict(x_test)
        recall = recall_score(y_test, y_pred) 
        
        print('O Recall do KNN com K valendo ' + str(i) + ' é de: ' + str(recall * 100) + ' %')


def precisionKNN(k, x_train, x_test, y_train, y_test):
    for i in range(1, k + 1):
        classificador = neighbors.KNeighborsClassifier(n_neighbors=i, metric='euclidean')
        classificador.fit(x_train, y_train)
        y_pred = classificador.predict(x_test)
        precision = precision_score(y_test, y_pred)
        
        print('A Precisão do KNN com K valendo ' + str(i) + ' é de: ' + str(precision * 100) + ' %')
        

def confusion_matrixKNN(k, x_train, x_test, y_train, y_test):
    classificador = neighbors.KNeighborsClassifier(n_neighbors=k, metric='euclidean')
    classificador.fit(x_train, y_train)
    y_pred = classificador.predict(x_test)    
    conf_matrix = confusion_matrix(y_test, y_pred)
    
    plt.figure(figsize=(10, 7))
    sns.heatmap(conf_matrix, annot=True, fmt="d")
    plt.title(f"Matriz de Confusão para k = {k}")
    plt.ylabel("Verdadeiro")
    plt.xlabel("Predito")
    plt.show()


def predictKNN(k, samples, x_train, y_train):    
    classificador = neighbors.KNeighborsClassifier(n_neighbors=k, metric='euclidean')        
    classificador.fit(x_train, y_train)    
    predicoes = classificador.predict(samples)    
    contagem_classes = Counter(predicoes)    
    labels = contagem_classes.keys()
    sizes = contagem_classes.values()
    
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  
    plt.title('Distribuição das Classes Previstas')  
    plt.show()

