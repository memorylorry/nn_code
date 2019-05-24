import paramiko
import pandas as pd

username = 'root'
password = 'centos'

df = pd.read_csv('/home/darling/PycharmProjects/py-demo/GatherInfo/machine.csv')

for i in df.index:
    try:
        ip = df.loc[i].values[0]
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username,password)

        print(ip)
        stdin, stdout, stderr = ssh.exec_command('free -g|awk \'{print $2"/"$3}\'')
        print(stdout.read().decode())
        ssh.close()
    except:
        pass
