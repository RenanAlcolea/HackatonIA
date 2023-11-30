from Dataset_Load import carregar_dados,preparar_dados,get_sample
from KNN import accuracyKNN, plot_K_Accuracy, plot_KNN_F1_score, confusion_MatrixKNN, predictKNN
from LogisticRegression import accuracyLR,plot_LR_F1_score,predictLR
from SVM import accuracySVM,predictSVM
from RandomForest import accuracyRF,predictRF

def main():
    
    k = int(input('Digite o valor de k desejado: '))

    # Carregando os dados
    df_train, df_test = carregar_dados()

    # Preparando os dados
    x_train, x_test, y_train, y_test = preparar_dados(df_train, df_test)

    #KNN
    accuracyKNN(k, x_train, x_test, y_train, y_test)
    plot_K_Accuracy(range(1, k+1), x_train, y_train, x_test, y_test)
    #plot_KNN_F1_score(range(1, k+1), x_train, y_train, x_test, y_test)
    #confusion_MatrixKNN(k, x_train, x_test, y_train, y_test)
    #predict(k, get_sample(), x_train, x_test, y_train, y_test)

    #LogisticRegression
    #accuracyLR(x_train, x_test, y_train, y_test)
    #plot_LR_F1_score(x_train, x_test, y_train, y_test)
    #predictLR(get_sample(), x_train,y_train)

    #SVM
    #accuracySVM(x_train, x_test, y_train, y_test)
    #predictSVM(get_sample(), x_train, y_train)

    #RandomForest
    #accuracyRF(x_train, x_test, y_train, y_test)
    #predictRF(get_sample(), x_train, y_train)
    

if __name__ == "__main__":
    main()
