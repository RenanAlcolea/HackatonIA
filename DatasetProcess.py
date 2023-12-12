import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from imblearn.under_sampling import RandomUnderSampler

##############################################################################################################################

def DatasetProcess():
    df = OpenNewDataset()
    df = converter_coluna_para_bytes(df, 'Bytes')
    df = converter_coluna_flags_para_amazon_vpc(df, 'Flags')    
    x_train, x_test, y_train, y_test  = SplitAndShuffleDataset(df)
    
    return x_train, x_test, y_train, y_test
    
    
def OpenNewDataset():
    df1 = pd.read_csv('CIDDS-001/CIDDS-001-internal-week1.csv', dtype={8: str})   
    df2 = pd.read_csv('CIDDS-001/CIDDS-001-external-week3.csv', dtype={8: str})
    df = pd.concat([df1, df2], ignore_index=True)
    df = df[~df['class'].isin(['victim','suspicious','unknown'])]
    return df

##############################################################################################################################

def converter_coluna_para_bytes(df, coluna):
    df[coluna] = df[coluna].apply(converter_M_para_bytes)
    df[coluna] = pd.to_numeric(df[coluna], errors='coerce')
    return df


def converter_M_para_bytes(valor):
    if isinstance(valor, str) and valor.endswith('M'):        
        return float(valor[:-1]) * 1024 * 1024
    else:        
        return valor    
##############################################################################################################################
def converter_coluna_flags_para_amazon_vpc(df, coluna):
    df[coluna] = df[coluna].apply(converter_para_amazon_vpc)
    return df

def converter_para_amazon_vpc(flag_string):    
    flag_values = {'F': 1, 'S': 2, 'R': 4, 'A': 16}
    
    if flag_string.startswith("0x"):
        flag_binary = bin(int(flag_string, 16))[2:].zfill(8)
        
        binary_flag_map = ['R', 'S', 'F', 'A']
        flags = [binary_flag_map[i] for i, bit in enumerate(flag_binary[-4:]) if bit == '1']
    else:
        
        flag_string = flag_string.replace('.', '')
        flags = [flag_string[i:i+2] if flag_string[i:i+2] in flag_values else flag_string[i] for i in range(len(flag_string))]

    
    if 'A' in flags and 'S' not in flags:
        flags.remove('A')

    
    amazon_vpc_value = 0
    for flag in flags:
        amazon_vpc_value |= flag_values.get(flag, 0)

    return amazon_vpc_value

##############################################################################################################################

def SplitAndShuffleDataset(df):

    
    df['class'] = df['class'].map({'normal': 0, 'attacker': 1})
    y = np.array(df['class'])
    

    x = df.drop(['Date first seen', 'Src IP Addr', 'Dst IP Addr', 'Flows', 'Tos', 'class', 'attackType', 'attackID', 'attackDescription'], axis=1, inplace=False)
    x = pd.get_dummies(x)
        
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42, stratify=y)   

    rus = RandomUnderSampler(random_state=42)
    x_train, y_train = rus.fit_resample(x_train, y_train)
    x_train.columns = x_train.columns.str.strip()
    x_test.columns = x_train.columns.str.strip()

    return x_train, x_test, y_train, y_test 

##############################################################################################################################
   
def prepararDados(x_train, x_test):     

    sc_x = StandardScaler()
    x_train = sc_x.fit_transform(x_train)
    x_test = sc_x.transform(x_test)

    return x_train, x_test  

##############################################################################################################################


