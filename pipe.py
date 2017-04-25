
# Subprocess.PIPE
from subprocess import Popen, PIPE, STDOUT

cmd = 'ls /etc/fstab /etc/non-existent-file'
p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
output = p.stdout.read()
print output
assert(output == ls: cannot access /etc/non-existent-file: No such file or directory /etc/fstab)
# Calling communicate after popen will capture the output it stdout

#Capturing the Output
import subprocess

output = subprocess.check_output([‘ls’, ‘-l’])

# Merging error and output channels - error message is captured rather than printed to console
output = subprocess.check_output(
    'echo to stdout; echo to stderr 1>&2; exit 1',
    shell=True,
    stderr=subprocess.STDOUT,
    )			
