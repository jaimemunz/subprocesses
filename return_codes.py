
# Return Codes

## Get return code of run process
try: 
    subprocess.run([‘cd’, ‘~’])
    assert e.returncode == 0 
except:
    assert False

## Check if returncode is non-zero
try: 
    completed_process = subprocess.run([‘cd’, ‘~/does_not_exist’])
    completed_process.check_returncode()
except subprocess.CalledProcessError:
     assert True #check_returncode() will throw when return code is non-zero

## Automatically check return code when run
try:
   completed_process = subprocess.run([‘cd’, ‘~/does_not_exist’], check=True)
except subprocess.CalledProcessError:
    assert True # check=True will automatically throw error if returncode is not 0
