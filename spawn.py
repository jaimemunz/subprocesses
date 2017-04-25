#Spawning new processes:

>from subprocess import run
#subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, shell=False, timeout=None, check=False, encoding=None, errors=None)
>>>run(‘uname -r’)
3.7.0-7-generic
>>>run(‘uname -r’).stdout
3.7.0-7-generic
>>>run(‘uname-a’).status
0
>>>run(‘rm not existing_directory’).stderr
Rm:cannot remove `not existing_directory’: No such file directory

>>>print run(‘ls-la’,’wc-l)
14
>>>print run(‘ls-la’,’wc-l,’wc-c’)
3
>>>run((‘ls-la’,’wc-l,’wc-c’)
ls -ls | wc -l | wc -c


