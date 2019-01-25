#install libs via pip3(unix) or pip(windows)
#pip3 install --user paramiko && pip3 install --user scp (Linux/macOS)
#pip-install --upgrade paramiko(windows)
#pip-install --upgrade scp(windows)
import paramiko #connection to host via ssh
from scp import SCPClient #copying file to remote host
import constants #contains hostname, username and others.

inpType = int(input('Choose any:\n1. Copy file to remote server\n2. Delete file from remote server\n')) #enter requered number(just 1 or 2)

client = paramiko.SSHClient() #init ssh
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
def connectTo(): #created function to connect after entering inpType (soft works faster)
    client.connect(hostname=constants.host, username=constants.user, password=constants.pwd, port=constants.port) #connect(obviously, lol)
    
if(inpType==1):
    client.load_system_host_keys()
    connectTo() #connect to host
    WhereFrom = input('File to remote computer: ') #enter file to copy
    with SCPClient(client.get_transport()) as scp:
        scp.put(WhereFrom) #choose file co copy
        scp.get(WhereFrom) #copy to remote host
    client.close() #close connection
    print('Successfully') #print if connection closed Successfully
    
elif(inpType==2):
    inp = input('Which file you want to delete? : ') #enter file to delete
    connectTo() #connect to host
    delCom = 'rm ' + str(inp) #bash command rm + name of file
    if 'rm -rf' in delCom:
        print('Restricted action!')
    else:
        stdin,stdout,stderr = client.exec_command(delCom) #use command
        print('Successfully') #print if connection closed Successfully
    client.close() #close connection
else:
    print('Ooops, sorry, you missed!') #if missclicked
    
