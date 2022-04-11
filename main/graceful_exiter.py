"""captures the exit signal."""
import signal
from .console import console

class GracefulExiter():
    """Helper class that intercepts the interrupt signal."""

    def __init__(self):
        """Object init."""
        signal.signal(signal.SIGINT, self.change_state)

    def change_state(self, signum, frame):
        """Print message, stop processing."""
        console.print("Received interrupt signal. Exitting now!", style='bad')
        signal.signal(signal.SIGINT, signal.SIG_DFL)
