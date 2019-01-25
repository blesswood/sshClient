import paramiko #connect via ssh to host
import constants #contains hostname, username and others.

client = paramiko.SSHClient() #init ssh
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=constants.host, username=constants.user, password=constants.pwd, port=constants.port)
startDocker = "Docker start ng_serv" #start container nginx called ng_serv 
stdin,stdout,stderr = client.exec_command(startDocker)
print("Server started!")
client.close()
