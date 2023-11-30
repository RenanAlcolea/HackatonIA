
############################# Análise de Base de Comportamento Web com Inteligência Artifical - Classificador SVM ############################
# ------------------------------------------------------
# Renan Alcoléa de Souza        (FACENS)   RA: 142591 
# Patrick Escórcia Taraborelli  (IPT)      RA: 43404
# Valdeclébio Farrapo Costa     (UFC)      RA: XXXXX 
# ------------------------------------------------------

# Bibliotecas para Ler/manipular/ver nossos dados
from sklearn import model_selection
from sklearn.svm import SVC

def accuracySVM(x_train, x_test, y_train, y_test):   
    classificador = SVC(C=1.0, kernel='rbf',gamma=1.0)  #Testar C Prox de 0 até mais ou menos range 10) [0.001, 0.01, 0.1, 1, 10, 100, 1000]  
    # se usar kernel='rbf' tbm utilizar'gamma': [0.0001, 0.001, 0.01, 0.1, 1, 10]
    # se usar kernel = 'linear' gamma não tem efeito
    classificador.fit(x_train, y_train)
    accuracy = classificador.score(x_test, y_test)
    print('\nA porcentagem de acerto do SVM é de: ' + str((accuracy) * 100) + '%') 


def predictSVM(sample, x_train,y_train):    
    classificador = SVC(C=1.0, kernel='rbf') 
    classificador.fit(x_train, y_train)  
    sample = sample.reshape(1, -1)
    predicao = classificador.predict(sample)
    print(predicao)

