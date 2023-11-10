
############################# Análise de Base de Comportamento Web com Inteligência Artifical - Classificador KNN ############################
# ------------------------------------------------------
# Renan Alcoléa de Souza (FACENS)	       RA: 142591 
# Patrick 		         (IPT)             RA: 171892 
# Valdeclébio Farrapo    (UFC)             RA: 
# ------------------------------------------------------

# Bibliotecas para Ler/manipular/ver nossos dados
import pandas as pd
import numpy as np

# Biblioteca para criar nosso modelo de ML
from sklearn import preprocessing, model_selection, neighbors
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# Valor de K que é o número de vizinhos próximos que serão levados em consideração para a comparação
k = input('Digite o valor de k desejado: ')
k = int(k)

# Carregando na variável df (dataframe) o arquivo CSV KDDTrain
df = pd.read_csv("KDDTrain+.csv", names=[
    'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land',
    'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in', 'num_compromised',
    'root_shell', 'su_attempted', 'num_root', 'num_file_creations', 'num_shells',
    'num_access_files', 'num_outbound_cmds', 'is_host_login', 'is_guest_login', 'count',
    'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate',
    'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count',
    'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate',
    'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'dst_host_serror_rate',
    'dst_host_srv_serror_rate', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate',
    'label', 'difficulty_level'
])


# Cabecalho com a pré apresentação dos dados (apenas os 5 primeiros dados)
#print(df.head())

# Informações básicas sobre o dataframe como Número totais de coluna, bem como seus tipos e um resumo de quantidade por Tipos
#print(df.info())

# Breve descrição de algumas estatística dos atributos que possuem valor numérico
#print(df.describe())

# Breve descrição dos atributos do tipo object (string)
#print(df.describe(include=['object']))

#########################################################################

# Definindo a classe que será verificada
y = np.array(df['label'])

# Excluindo o atributo "Class" que contem o resultado do Dataframe original uma vez que já obtivemos a copia na variável Y
df.drop(['label'],axis=1,inplace=True)

# Transformando em informação númerica os atributos do tipo object (texto)
df_dummy = pd.get_dummies(df)

# Passando a variável X a parte referente ao teste
x = np.array(df_dummy)


#x = pd.DataFrame(x)
#print(x.head())


###############################################################################################################
def masstest(k,x,y):
    
    for i in range(1,k+1):         

        x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size= 0.2, random_state=888)       
       
        #Normalização dos atributos para que obtenham o mesmo peso.
        sc_x = StandardScaler()
        x_train = sc_x.fit_transform(x_train)
        x_test = sc_x.fit_transform(x_test)        
       
        classificador = neighbors.KNeighborsClassifier(n_neighbors = i, metric='euclidean')        
        classificador.fit(x_train,y_train)
        accuracy = classificador.score(x_test,y_test)
        print('A Por centagem de acerto do KNN com K valendo' + ' ' + str(i) + ' ' + 'é de: + ' + str(accuracy) + ' ' + '%')      
##############################################################################################################


##############################################################################################################
def predicao(k, sample):    
    x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size= 0.2, random_state=0)  
    sc_x = StandardScaler()
    x_train = sc_x.fit_transform(x_train)
    x_test = sc_x.fit_transform(x_test) 
    clf = neighbors.KNeighborsClassifier(n_neighbors = k, metric='euclidean')        
    clf.fit(x_train,y_train)  
    sample = sample.reshape(1,-1)
    predicao= clf.predict(sample)
    print(predicao)
##############################################################################################################

# Novo exemplo de entrada para comparação comm o algorítmo KNN para verificação se é um comportamento normal ou uma anomalia
sample = np.array([0.8261,0.6742,300.0935,0.7273,0.0791,0.8793,0.9563,
0.3193,0.9997,0.7164,0.0179,0.4493,0.5410,0.6669,0.3183,0.9055,0.1363,
0.4749,100.5502,0.9028,0.9632,0.2976,0.5401,0.7857,0.3345,0.6991,
0.0935,0.7307,0.0692,0.8698,0.3257,0.2074,0.9964,0.5653,0.2081,0.0934,
0.5149,0.9674,0.1848,0.0919,0.4197,0.7634,500.3038,0.2860,0.4441,
800.7194,0.0909,0.8340,0.5949,0.0674,0.4301,0.5339,0.4956,0.0999,
0.8964,0.9961,0.7069,0.7377,0.4731,0.8692,0.4475,200.0894,0.9901,
0.3843,0.7989,0.3109,300.2027,0.2356,0.4904,0.0472,0.5350,0.8940,
0.9026,0.0723,0.0145,0.6727,0.1811,0.9115,0.1159,40.9690,0.1697,
0.7131,0.1162,0.9507,0.2026,0.7140,0.8468,0.5608,200.1480,300.4620,
0.0898,0.5390,500.7984,.7569,0.7161,0.4652,0.3266,0.4945,0.5332,
0.8274,0.7018,0.6609,0.7173,0.0399,0.7191,0.5511,0.2917,0.9036,
0.5485,0.3103,0.9103,0.9382,0.1655,0.6062,0.0671,0.1713,0.3159,
0.8286,0.8367,0.8115,0.4329,0.0473,18])

masstest(k,x,y)
#predicao(k,sample)






