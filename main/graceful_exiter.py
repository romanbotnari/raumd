import signal

class graceful_exiter():

    def __init__(self):
        signal.signal(signal.SIGINT, self.change_state)

    def change_state(self, signum, frame):
        console.print("..Exitting..", style='bad')
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        return