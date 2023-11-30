
############################# Análise de Base de Comportamento Web com Inteligência Artifical - Classificador Regressão Logística ############################
# ------------------------------------------------------
# Renan Alcoléa de Souza        (FACENS)   RA: 142591 
# Patrick Escórcia Taraborelli  (IPT)      RA: 43404
# Valdeclébio Farrapo Costa     (UFC)      RA: XXXXX 
# ------------------------------------------------------

# Bibliotecas para Ler/manipular/ver nossos dados
import matplotlib.pyplot as plt
from sklearn import preprocessing, model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import recall_score, f1_score



def accuracyLR(x_train, x_test, y_train, y_test):     
    classificador = LogisticRegression(C=1.0, max_iter=100000)  #Testar C Prox de 0 até mais ou menos range 10) [0.001, 0.01, 0.1, 1, 10, 100, 1000]
    classificador.fit(x_train, y_train)
    accuracy = classificador.score(x_test, y_test)
    print('\nA porcentagem de acerto da Regressão Logística é de: ' + str((accuracy) * 100) + '%') 

def recallLR(x_train, x_test, y_train, y_test):
    classificador = LogisticRegression(C=1.0, max_iter=100000)
    classificador.fit(x_train, y_train)
    y_pred = classificador.predict(x_test)
    recall = recall_score(y_test, y_pred)
    print('\nO Recall da Regressão Logística é de: ' + str((recall) * 100) + '%')


def plot_LR_F1_score(x_train, x_test, y_train, y_test):    
    classificador = LogisticRegression(C=1.0, max_iter=100000)
    classificador.fit(x_train, y_train)    
    
    y_pred = classificador.predict(x_test)
    
    f1 = f1_score(y_test, y_pred, average='weighted')  #average 'macro'
    print('F1 Score da Regressão Logística:', f1)
    
    plt.bar(['F1 Score'], [f1], color='blue')
    plt.ylim(0, 1)  
    plt.ylabel('F1 Score')
    plt.title('F1 Score da Regressão Logística')
    plt.show()
    


def predictLR(sample, x_train, y_train):    
    classificador = LogisticRegression(max_iter=100000)  
    classificador.fit(x_train, y_train)  
    sample = sample.reshape(1, -1)
    predicao = classificador.predict(sample)
    print(predicao)


