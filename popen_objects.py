

### Popen Objects ###

# Run shell with specified args
args = ['cd', '~']
try:
    p = subprocess.Popen(args, shell=True)
    assert p.args == args
    assert True
except Exception as e:
    assert False


# Run shell with specified args
# Recommended way to pass args when shell=True
args = 'cd ~'
try:
    p = subprocess.Popen(args, shell=True)
    assert p.args == args
    assert True
except Exception as e:
    assert False


# Run executable that does not exist
# Recommended way when passing args into executable
args = ['Hello.py']
try:
    p = subprocess.Popen(args)
    assert False
except Exception as e:
    assert isinstance(e, FileNotFoundError)
    assert True

# Run executable that does not exist
# Recommended way when passing no args into executable
args = 'Hello.py'
try:
    p = subprocess.Popen(args)
    assert False
except Exception as e:
    assert isinstance(e, FileNotFoundError)
    assert True


# Wait for child to terminate
args = 'gedit'
p = None
try:
    p = subprocess.Popen(args)
    p.wait(2)   # Time to wait for process in seconds
    assert False
except Exception as e:
    assert isinstance(e, subprocess.TimeoutExpired)
    assert True
    p.kill()



# Wait for child to terminate
args = 'gedit'
p = None
try:
    p = subprocess.Popen(args)
    p.wait(2)   # Time to wait for process in seconds
    assert False
except Exception as e:
    assert isinstance(e, subprocess.TimeoutExpired)
    assert True
    p.send_signal(9)    # SIGKILL number


# Wait for child to terminate
args = 'gedit'
p = None
try:
    p = subprocess.Popen(args)
    p.wait(2)   # Time to wait for process in seconds
    assert False
except Exception as e:
    assert isinstance(e, subprocess.TimeoutExpired)
    assert True
    p.terminate()


# Wait for child to terminate
args = 'gedit'
p = None
try:
    p = subprocess.Popen(args)
    p.wait(2)   # Time to wait for process in seconds
    assert False
except Exception as e:
    assert isinstance(e, subprocess.TimeoutExpired)
    assert True
    p.send_signal(15)   # SIGTERM number


# Reading output 
args = 'echo \"Hello, world!\"'
try:
    p = subprocess.Popen(args, stdout=subprocess.PIPE, shell=True)
    assert p.stdout.read().decode('utf-8') == 'Hello, world!\n'
    assert True
except Exception as e:
    assert False


# Reading output 
args = 'echo \"According to all known laws of aviation...\"'
try:
    p = subprocess.Popen(args, stdout=subprocess.PIPE, shell=True)
    assert p.stdout.read().decode('utf-8') == 'According to all known laws of aviation...\n'
    assert True
except Exception as e:
    assert False
