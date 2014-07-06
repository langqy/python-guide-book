import subprocess


# Command with shell expansion
subprocess.call(["echo", "hello world"])
subprocess.call(["echo", "$HOME"])
subprocess.call('echo $HOME',shell=True)


