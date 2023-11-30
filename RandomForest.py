
############################# Análise de Base de Comportamento Web com Inteligência Artifical - Classificador RandomForest ############################
# ------------------------------------------------------
# Renan Alcoléa de Souza        (FACENS)   RA: 142591 
# Patrick Escórcia Taraborelli  (IPT)      RA: 43404
# Valdeclébio Farrapo Costa     (UFC)      RA: XXXXX 
# ------------------------------------------------------

# Importando as bibliotecas necessárias
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier

def accuracyRF(x_train, x_test, y_train, y_test):   
    classificador = RandomForestClassifier(n_estimators=100)  # variar de 50 em 50 de  (10 a 300)
    classificador.fit(x_train, y_train)
    accuracy = classificador.score(x_test, y_test)
    print('\nA porcentagem de acerto da Random Forest é de: ' + str((accuracy) * 100) + '%') 

def predictRF(sample, x_train, y_train):    
    classificador = RandomForestClassifier(n_estimators=100)  
    classificador.fit(x_train, y_train)  
    sample = sample.reshape(1, -1)
    predicao = classificador.predict(sample)
    print(predicao)
