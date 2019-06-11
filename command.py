import subprocess

# function for getting command output as string (and waiting for the command to finish)
def command_wait(command):
    child = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    child.wait()
    output = child.communicate()[0]
    return output.decode()

    
class Command:
    """a class for handling system commands"""
    def __init__(self, command):
        self.command = command
        self.is_executed = False
        self.is_done = False

    # executes command
    def execute(self):
        self.child = subprocess.Popen(self.command, stdout=subprocess.PIPE, shell=True)
        self.is_executed = True

    # asks if done executing. returns boolean. raises ValueError if called before command execution
    def done(self):
        if self.is_executed:
            if self.child.poll() is not None:
                self.is_done = True
                return True
            else:
                return False
        else:
            raise ValueError('completion checked before execution')

    # returns result. raises ValueError if called before the command is done
    def result(self):
        if self.is_done:
            return self.child.communicate()[0].decode()
        else:
            raise ValueError('result called before the command was done')
