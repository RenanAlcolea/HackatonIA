import pandas as pd
import matplotlib.pyplot as plt

###############################################################################################################################################

########### Análise Dataset CIDDS-001 ###########

def analysis_train():
    
    df1_train = pd.read_csv('CIDDS-001/CIDDS-001-internal-week1.csv', dtype={8: str})   
    df2_train = pd.read_csv('CIDDS-001/CIDDS-001-external-week3.csv', dtype={8: str})
    df_train = pd.concat([df1_train, df2_train], ignore_index=True)
    df_train = df_train[~df_train['class'].isin(['victim','suspicious','unknown'])]

    contagem_classes = df_train['class'].value_counts()
    print(contagem_classes)
    
    contagem_classes.plot(kind='bar') 

    
    plt.title('Contagem de Classes')
    plt.xlabel('Classe')
    plt.ylabel('Quantidade')
    plt.tight_layout()    
    plt.show()

###############################################################################################################################################

########### Análise Dataset NSL-KDD ###########

def analysis_test():
    df_test = pd.read_csv("NSL-KDD/KDDTest+.csv", names=[
        'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land',
        'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in', 'num_compromised',
        'root_shell', 'su_attempted', 'num_root', 'num_file_creations', 'num_shells',
        'num_access_files', 'num_outbound_cmds', 'is_host_login', 'is_guest_login', 'count',
        'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate',
        'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count',
        'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate',
        'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'dst_host_serror_rate',
        'dst_host_srv_serror_rate', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate',
        'label', 'difficulty_level'])
   
    contagem_classes = df_test['label'].value_counts()
    print(contagem_classes)    
    contagem_classes.plot(kind='bar')    
    plt.title('Contagem de Classes')
    plt.xlabel('Classe')
    plt.ylabel('Quantidade')
    plt.tight_layout()    
    plt.show()

###############################################################################################################################################



