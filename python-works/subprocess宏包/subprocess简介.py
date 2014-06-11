import subprocess




# Command with shell expansion
subprocess.call('echo $HOME',shell=True)
name=subprocess.getoutput('whoami')

print(name)
