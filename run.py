
#Example of run
import subprocess
import os
import signal



class Result(object):
	Def __init__(Self, command=None, retcode=None,output=None):
		self.command = command or ''
	        self.retcode = retcode
	        import tempfile
	        self.output = output
	        self.success = False
	        if retcode == 0:
	            self.success = True


def run(command):
	    process = subprocess.Popen(command, shell=True)
	    process.communicate()
	    return Result(command=command, retcode=process.returncode)

def run_capture(command):
	    outpipe = subprocess.PIPE
	    errpipe = subprocess.STDOUT
	    process = subprocess.Popen(command, shell=True, stdout=outpipe,
	                                                    stderr=errpipe)
	    output, _ = process.communicate()
	    return Result(command=command, retcode=process.returncode, output=output)




def run_killpid(pid):
	    os.kill(pid, signal.SIGTERM)
	

	if __name__ == '__main__':
	    print('---[ .success ]---')
	    print(run('ls').success)
	    print(run('dir').success)



            print('---[ capture ]---')
	    print(len(run_capture('ls').output))
	    print(len(run_capture('dir').output))
