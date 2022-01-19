import subprocess
    
class Command:
    """
    for handling system commands (asynchronously or synchronously)
    """
    def __init__(self, *args: str, execute=False) -> None:
        """
        args: command arguments
        execute: if the command is to executed immediatly
        """
        self._args = args
        self._child = None
        self._done = False

        if execute:
            self.execute()

    def execute(self) -> None:
        """
        executes command
        """
        self._child = subprocess.Popen(self._args, stdout=subprocess.PIPE, shell=True)
        self._executed = True

    def done(self) -> bool:
        """
        asks if done executing. returns boolean. raises error, if called before command execution
        """
        if self._child is not None:
            if self._child.poll() is not None:
                self._done = True
                return True
            else:
                return False
        else:
            raise RuntimeError('subprocess completion checked before execution')

    def wait(self) -> str:
        """
        waits for the command to finish and returns result
        """
        return self._child.communicate()[0].decode()

    def result(self) -> str:
        """
        returns result. raises error if called before the command is done
        """
        if self._done:
            return self._child.communicate()[0].decode()
        else:
            raise RuntimeError('result called before the subprocess was done')