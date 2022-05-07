import subprocess
import os
#output = subprocess.run(["ls",'-a'])
#p = subprocess.Popen(['ls', '-a'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#print(subprocess.run(['ipconfig'], stdout=subprocess.PIPE).stdout.decode('utf-8'))
#print("this is output :  ",p.stdout.read().decode().replace("\\n","\n"))

#output = os.popen("ls")
#print(type(output.read().encode()))
batcmd="ls"
result = subprocess.Popen(batcmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,text='utf-8')
print(result.stdout.read())