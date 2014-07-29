from subprocess import PIPE
from subprocess import Popen


def run(command):
    assert (isinstance(command, list)), "Command must be a list"
    p = Popen(command, stdout=PIPE, stderr=PIPE)
    s, e = p.communicate()
    return s.decode('utf-8'), e.decode('utf-8'), p.returncode
