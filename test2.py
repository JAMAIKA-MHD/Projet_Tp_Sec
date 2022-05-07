# Just a simple function to execute shell commands and display the output

import subprocess
from subprocess import Popen, CalledProcessError

COLOR_END = '\033[0m'
COLOR_DARKGREY = '\033[1;30m'
 
out_t = lambda s: COLOR_DARKGREY + s + COLOR_END

def exec_cmd(cmd):
    print( '\n> {}'.format(cmd))

    p = Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    for line in iter(p.stdout.readline, b''):
        print (out_t('| ' + line.rstrip()))

    output = p.communicate()[0] 

    if p.returncode != 0:
        raise CalledProcessError(p.returncode, cmd)

    return output


print(exec_cmd("date"))