import pandas as pd

def logsVPC():    
    df_vpc = importLogsVPC()
    df_vpc = calculate_time_delta(df_vpc)
    df_vpc = reordenar_colunas(df_vpc)
    df_vpc = new_Columns(df_vpc)
    df_vpc = atualizar_protocolos(df_vpc)
    return df_vpc

def importLogsVPC():
    df_vpc = pd.read_csv('Logs/Logs_eni-03ab7af9546ef7cce-all.csv', names=[
        'timestamp', 'account-id', 'action', 'az-id', 'bytes', 'dstaddr', 
        'dstport', 'end', 'flow-direction', 'instance-id', 'interface-id', 
        'log-status', 'packets', 'pkt-dst-aws-service', 'pkt-dstaddr', 
        'pkt-src-aws-service', 'pkt-srcaddr', 'protocol', 'region', 'srcaddr', 
        'srcport', 'start', 'sublocation-id', 'sublocation-type', 'subnet-id', 
        'tcp-flags', 'traffic-path', 'type', 'version', 'vpc-id'
    ])

    df_vpc.drop(['account-id', 'action', 'az-id', 'dstaddr', 'flow-direction', 'instance-id', 'interface-id', 'log-status', 'pkt-srcaddr', 'pkt-dstaddr',
        'pkt-dst-aws-service', 'pkt-src-aws-service', 'region', 'sublocation-id', 'srcaddr',
        'sublocation-type', 'subnet-id', 'timestamp', 'traffic-path', 'type', 'version', 'vpc-id'], axis=1, inplace=True)



def calculate_time_delta(df_vpc):   
    duration = df_vpc['end'] - df_vpc['start']    
    df_vpc.insert(0, 'duration', duration)
    df_vpc.drop(['end', 'start'], axis=1, inplace=True)

    return df_vpc

def reordenar_colunas(df_vpc):
    reordenado = ['duration', 'srcport', 'dstport', 'packets', 'bytes', 'tcp-flags', 'protocol']
    df_vpc = df_vpc[reordenado]
    df_vpc = df_vpc.rename(columns={'duration': 'Duration'})
    df_vpc = df_vpc.rename(columns={'srcport': 'Src Pt'})
    df_vpc = df_vpc.rename(columns={'dstport': 'Dst Pt'})
    df_vpc = df_vpc.rename(columns={'packets': 'Packets'})
    df_vpc = df_vpc.rename(columns={'bytes': 'Bytes'})
    df_vpc = df_vpc.rename(columns={'tcp-flags': 'Flags'})
    df_vpc.columns = df_vpc.columns.str.strip()
    
    return df_vpc

def new_Columns(df_vpc):
    df_vpc['Proto_ICMP'] = 0
    df_vpc['Proto_IGMP'] = 0
    df_vpc['Proto_TCP'] = 0
    df_vpc['Proto_UDP'] = 0
    
    return df_vpc    

def atualizar_protocolos(df_vpc):    
    df_vpc.loc[df_vpc['protocol'] == 1, 'Proto_ICMP'] = 1
    df_vpc.loc[df_vpc['protocol'] == 2, 'Proto_IGMP'] = 1
    df_vpc.loc[df_vpc['protocol'] == 6, 'Proto_TCP'] = 1
    df_vpc.loc[df_vpc['protocol'] == 17, 'Proto_UDP'] = 1
    df_vpc.drop(['protocol'], axis=1, inplace=True)
    
    return df_vpc




    
    











