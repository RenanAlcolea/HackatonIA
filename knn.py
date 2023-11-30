
############################# Análise de Base de Comportamento Web com Inteligência Artifical - Classificador KNN ############################
# ------------------------------------------------------
# Renan Alcoléa de Souza        (FACENS)   RA: 142591 
# Patrick Escórcia Taraborelli  (IPT)      RA: 43404
# Valdeclébio Farrapo Costa     (UFC)      RA: XXXXX 
# ------------------------------------------------------


# Bibliotecas para Ler/manipular/ver nossos dados
from sklearn import preprocessing, model_selection, neighbors
from sklearn.metrics import confusion_matrix,f1_score
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import classification_report


def accuracyKNN(k, x_train, x_test, y_train, y_test):
    for i in range(1,k+1):             
        classificador = neighbors.KNeighborsClassifier(n_neighbors = i, metric='euclidean')        
        classificador.fit(x_train,y_train)
        accuracy = classificador.score(x_test,y_test)
        pred = classificador.predict(x_test)
        report = classification_report(y_test, pred)
        print(report)
        print('A Por centagem de acerto do KNN com K valendo' + ' ' + str(i) + ' ' + 'é de: + ' + str((accuracy)*100) + ' ' + '%') 

def plot_K_Accuracy(k_range, x_train, y_train, x_test, y_test):
    scores = []
    for k in k_range:
        clf = neighbors.KNeighborsClassifier(n_neighbors=k)
        clf.fit(x_train, y_train)
        score = clf.score(x_test, y_test)
        scores.append(score)
    plt.figure()
    plt.xlabel('k')
    plt.ylabel('Precisão')
    plt.scatter(k_range, scores)
    plt.xticks([i for i in k_range])
    plt.grid()
    plt.show()

def plot_KNN_F1_score(k_range, x_train, y_train, x_test, y_test):
    f1_scores = []
    for k in k_range:
        clf = neighbors.KNeighborsClassifier(n_neighbors=k)
        clf.fit(x_train, y_train)
        y_pred = clf.predict(x_test)
        f1 = f1_score(y_test, y_pred, average='weighted')  
        f1_scores.append(f1)

    plt.figure()
    plt.xlabel('k')
    plt.ylabel('F1 Score')
    plt.plot(k_range, f1_scores, marker='o')
    plt.xticks([i for i in k_range])
    plt.grid()
    plt.show()


def confusion_MatrixKNN(k, x_train, x_test, y_train, y_test):
    classificador = neighbors.KNeighborsClassifier(n_neighbors=k, metric='euclidean')
    classificador.fit(x_train, y_train)
    y_pred = classificador.predict(x_test)

    # Calculando a matriz de confusão
    conf_matrix = confusion_matrix(y_test, y_pred)

    # Visualizando a matriz de confusão
    plt.figure(figsize=(10, 7))
    sns.heatmap(conf_matrix, annot=True, fmt="d")
    plt.title(f"Matriz de Confusão para k = {k}")
    plt.ylabel("Verdadeiro")
    plt.xlabel("Predito")
    plt.show()

def predictKNN(k, sample, x_train, y_train):
    classificador = neighbors.KNeighborsClassifier(n_neighbors = k, metric='euclidean')        
    classificador.fit(x_train,y_train)  
    sample = sample.reshape(1,-1)
    predicao= classificador.predict(sample)
    print(predicao)
