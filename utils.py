import os

# ------------------ Workspace ------------------
    
def check_valid_folder(path):
    if os.path.isdir(path) and os.path.exists(path):
        return path
    else:
        print('The specified path is not a valid folder. Please choose a valid path: ')
        new_path = input()
        return check_valid_folder(new_path)
    
def get_file_names(path):
    pcap_file_name = []
    hera_file_name = []
    csv_file_name = []

    if os.path.isdir(path):
        file_list = os.listdir(path)
        for file in file_list:
            if os.path.splitext(os.path.basename(file))[1] == ".pcap" or os.path.splitext(os.path.basename(file))[1] == ".pcapng":
                pcap_file_name.append(file)
                hera_file_name.append(os.path.splitext(os.path.basename(file))[0] + ".hera")
                csv_file_name.append(os.path.splitext(os.path.basename(file))[0] + ".csv")
        return pcap_file_name, hera_file_name, csv_file_name
    else:
        pcap_file_name.append(path)
        hera_file_name.append(os.path.splitext(os.path.basename(path))[0] + ".hera")
        csv_file_name.append(os.path.splitext(os.path.basename(path))[0] + ".csv")
        return pcap_file_name, hera_file_name, csv_file_name

def check_last_digit(string):
    if string[-1] == '/':
        return string
    else:
        return string + '/'
    

# ------------------ Argus File ------------------

argus_fields = ['-A | Generate application byte metrics in each audit record.',
                '-O | Turn off Berkeley Packet Filter optimizer. If you think it generates bad code.',
                '-Z | Collect packet size information for all flows (to generate mean, max, min and standard deviation).',
                '-J | Generate packet performance (jitter) data in each audit record.',
                '−m | Provide MAC address information in argus records.',
                '−R | Generate argus records such that response times can be derived from transaction data.']

default_argus_values = ['-A | Generate application byte metrics in each audit record.',
                        '-Z | Collect packet size information for all flows (to generate mean, max, min and standard deviation).',
                        '-J | Generate packet performance (jitter) data in each audit record.',]

# ------------------ Features ------------------

# 'stime', 'ltime', 'saddr', 'daddr', 'proto', 'sport', 'dport'

features = ['srcid', 'trans', 'flgs', 'seq', 'dur', 'runtime', 'idle', 'mean', 'stddev', 'sum', 'min', 'max', 
            'smac', 'dmac', 'soui', 'doui', 'stos', 'dtos', 'sdsb', 'ddsb', 'sco', 'dco', 'sttl', 'dttl', 'shops', 
            'dhops', 'sipid', 'dipid', 'smpls', 'dmpls', 'autoid', 'sas', 'das', 'ias', 'cause', 'nstroke', 
            'snstroke', 'dnstroke', 'pkts', 'spkts', 'dpkts', 'bytes', 'sbytes', 'dbytes', 'appbytes', 'sappbytes', 
            'dappbytes', 'pcr', 'load', 'sload', 'dload', 'loss', 'sloss', 'dloss', 'ploss', 'psloss', 'pdloss', 
            'retrans', 'sretrans', 'dretrans', 'pretrans', 'psretrans', 'pdretrans', 'sgap', 'dgap', 'rate', 'srate', 
            'drate', 'dir', 'sintpkt', 'sintpktmin', 'sintpktmax', 'sintdist', 'sintpktact', 'sintdistact', 'sintpktidl', 
            'sintdistidl', 'dintpkt', 'dintpktmin', 'dintpktmax', 'dintdist', 'dintpktact', 'dintdistact', 'dintpktidl', 
            'dintdistidl', 'sjit', 'sjitact', 'sjitidle', 'djit', 'djitact', 'djitidle', 'state', 'label', 
            'suser', 'duser', 'swin', 'dwin', 'svlan', 'dvlan', 'svid', 'dvid', 'svpri', 'dvpri', 'srng', 
            'erng', 'stcpb', 'dtcpb', 'tcprtt', 'synack', 'ackdat', 'tcpopt', 'inode', 'offset', 'smeansz', 
            'dmeansz', 'spktsz', 'smaxsz', 'dpktsz', 'dmaxsz', 'sminsz', 'dminsz', 'Ssaddr', 'Sdaddr']

default_features = ['bytes', 'sbytes', 'dbytes', 'pkts', 'spkts', 'dpkts', 'dur', 'runtime', 'idle', 'flgs', 
                    'tcpopt', 'Ssaddr', 'Sdaddr']

cic_10_features = ['sintpkt', 'sintpktmax', 'sintpktmin', 'dintpkt', 'dintpktmax', 'dintpktmin', 'mean', 'stddev', 
                   'max', 'min']

unswnb15_features = ['state', 'dur', 'sbytes', 'dbytes', 'sttl', 'dttl', 'sloss', 'dloss', 'sload', 'dload', 'spkts', 
                     'dpkts', 'swin', 'dwin', 'stcpb', 'dtcpb', 'smeansz', 'dmeansz','sjit', 'djit', 'sintpkt', 
                     'dintpkt', 'tcprtt', 'synack', 'ackdat']

botiot_features = ['flgs', 'dir', 'pkts', 'bytes', 'state', 'srcid', 'seq', 'dur', 'mean', 'stddev', 'smac', 'dmac', 
                   'sum', 'min', 'max', 'soui', 'doui', 'sco', 'dco', 'spkts', 'dpkts', 'sbytes', 'dbytes', 'rate', 
                   'srate', 'drate']