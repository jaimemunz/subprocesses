# Exceptions
import subprocess

# exception subprocess.TimeoutExpired
# Subclass of subprocessError raised when a timeout expires while waiting for a while process
try :
    subprocess.run ( [‘python3.5’, ‘./tick.py’], timeout = 2)
except subprocess.TimeoutExpired as e:
    assert isinstance (e, subprocess.SubprocessError)
    assert e.cmd == [‘python3.5’, ‘./tick.py’]
    assert e.timeout == 2



# exception subprocess.CalledProcessError
# Subclass of SubprocessError, raised when a process run by check_call() or check_output 
# returns a non-zero exit status 
try :
    subprocess.check_call( [‘false’] ) # False command always exits with a non-zero code
except subprocess.CalledProcessError as e :
    assert isinstance (e, subprocess.SubprocessError)
    assert e.returncode == 0    # Exit status of the child process
    assert e.cmd == [‘false’]    # Command that was used to spawn the child process
    
