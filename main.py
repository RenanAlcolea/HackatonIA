from DatasetProcess import DatasetProcess
from LogProcess import logsVPC
from KNN import accuracyKNN,F1ScoreKNN,recallKNN,precisionKNN,confusion_matrixKNN,predictKNN
from LogisticRegression import accuracyLR,F1ScoreLR,recallLR,precisionLR,confusion_matrixLR,predictLR
from SVM import accuracySVM,F1ScoreSVM,recallSVM,precisionSVM,confusionMatrixSVM,predictSVM
from RandomForest import accuracyRF, F1ScoreRF,recallRF,precisionRF,confusion_matrixRF,predictRF

def main():    
    
    print('[1] - KNN\n[2] - Logistic Regression\n[3] - SVM\n[4] - Random Forest')   
    opt = int(input('Digite o Classificador que deseja acessar: '))
    
    #KNN
    if(opt == 1):
        k = int(input('Digite o valor de k desejado: '))
        print('\n[1] - Acurácia\n[2] - F1-Score\n[3] - Recall\n[4] - Precisão\n[5] - Matrix de Confusão\n[6] - Predição') 
        alg = int(input('Digite o algoritmo que deseja processar: '))
        if(alg == 1):  
            x_train, x_test, y_train, y_test = DatasetProcess()
            accuracyKNN(k, x_train, x_test, y_train, y_test)            
        elif(alg == 2):
            x_train, x_test, y_train, y_test = DatasetProcess()
            F1ScoreKNN(range(1, k+1), x_train, y_train, x_test, y_test)
        elif(alg == 3):
            x_train, x_test, y_train, y_test = DatasetProcess()
            recallKNN(k, x_train, x_test, y_train, y_test)
        elif(alg == 4):
            x_train, x_test, y_train, y_test = DatasetProcess()
            precisionKNN(k, x_train, x_test, y_train, y_test)
        elif(alg == 5):
            x_train, x_test, y_train, y_test = lDatasetProcess()
            confusion_matrixKNN(k, x_train, x_test, y_train, y_test)
        elif(alg == 6):
            x_train, x_test, y_train, y_test = DatasetProcess()
            samples = logsVPC()
            predictKNN(k, samples, x_train, y_train)
        else:
            print('Opção Inválida, reinicie a aplicação.')        

    #LogisticRegression
    if(opt == 2):
        print('\n[1] - Acurácia\n[2] - F1-Score\n[3] - Recall\n[4] - Precisão\n[5] - Matrix de Confusão\n[6] - Predição') 
        alg = int(input('Digite o algoritmo que deseja processar: '))
        if(alg == 1):  
            x_train, x_test, y_train, y_test = DatasetProcess()        
            accuracyLR(x_train, x_test, y_train, y_test)
        elif(alg == 2):
            x_train, x_test, y_train, y_test = DatasetProcess()
            F1ScoreLR(x_train, x_test, y_train, y_test)            
        elif(alg == 3):
            x_train, x_test, y_train, y_test = DatasetProcess()           
            recallLR(x_train, x_test, y_train, y_test)
        elif(alg == 4):
            x_train, x_test, y_train, y_test = DatasetProcess()           
            precisionLR(x_train, x_test, y_train, y_test)
        elif(alg == 5):
            x_train, x_test, y_train, y_test = DatasetProcess()
            confusion_matrixLR(x_train, x_test, y_train, y_test)
        elif(alg == 6):
            x_train, x_test, y_train, y_test = DatasetProcess()
            samples = logsVPC()
            predictLR(samples, x_train,y_train)            
        else:
            print('Opção Inválida, reinicie a aplicação.')
            

    #SVM
    if(opt == 3):
        print('\n[1] - Acurácia\n[2] - F1-Score\n[3] - Recall\n[4] - Precisão\n[5] - Matrix de Confusão\n[6] - Predição') 
        alg = int(input('Digite o algoritmo que deseja processar: '))
        if(alg == 1):  
            x_train, x_test, y_train, y_test = DatasetProcess()      
            accuracySVM(x_train, x_test, y_train, y_test)
        elif(alg == 2):
            x_train, x_test, y_train, y_test = DatasetProcess()          
            F1ScoreSVM(x_train, x_test, y_train, y_test)
        elif(alg == 3):
            x_train, x_test, y_train, y_test = DatasetProcess()
            recallSVM(x_train, x_test, y_train, y_test)
        elif(alg == 4):
            x_train, x_test, y_train, y_test = DatasetProcess()
            precisionSVM(x_train, x_test, y_train, y_test)
        elif(alg == 5):
            x_train, x_test, y_train, y_test = DatasetProcess()           
            confusionMatrixSVM(x_train, x_test, y_train, y_test)
        elif(alg == 6):
            x_train, x_test, y_train, y_test = DatasetProcess()
            samples = logsVPC()
            predictSVM(samples, x_train, y_train)
        else:
            print('Opção Inválida, reinicie a aplicação.')

    #RandomForest
    if(opt == 4):
        print('\n[1] - Acurácia\n[2] - F1-Score\n[3] - Recall\n[4] - Precisão\n[5] - Matrix de Confusão\n[6] - Predição') 
        alg = int(input('Digite o algoritmo que deseja processar: '))
        if(alg == 1):  
            x_train, x_test, y_train, y_test = DatasetProcess()      
            accuracyRF(x_train, x_test, y_train, y_test)
        elif(alg == 2):
            x_train, x_test, y_train, y_test = DatasetProcess()
            F1ScoreRF(x_train, x_test, y_train, y_test)
        elif(alg == 3):
            x_train, x_test, y_train, y_test = DatasetProcess()           
            recallRF(x_train, x_test, y_train, y_test)
        elif(alg == 4):
            x_train, x_test, y_train, y_test = DatasetProcess()                      
            precisionRF(x_train, x_test, y_train, y_test)
        elif(alg == 5):
            x_train, x_test, y_train, y_test = DatasetProcess()           
            confusion_matrixRF(x_train, x_test, y_train, y_test)
        elif(alg == 6):
            x_train, x_test, y_train, y_test = DatasetProcess()
            samples = logsVPC()
            predictRF(samples, x_train, y_train)
            
            
        else:
            print('Opção Inválida, reinicie a aplicação.')            

if __name__ == "__main__":
    main()
