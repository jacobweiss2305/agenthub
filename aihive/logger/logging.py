from datetime import datetime
from typing import Optional


class Logging:
    """
    A logging utility class that provides formatted logging functionality.
    """

    def __init__(self, debug: bool = False):
        """
        Initialize the logging utility.

        Args:
            debug (bool): Whether to enable debug logging. Defaults to False.
        """
        self.debug = debug

    def log(self, message: str, level: str = "INFO", timestamp: Optional[datetime] = None) -> None:
        """
        Log a message with the specified level and optional timestamp.

        Args:
            message (str): The message to log
            level (str): The log level (INFO, WARNING, ERROR, DEBUG)
            timestamp (datetime, optional): Custom timestamp. Uses current time if None.
        """
        if level == "DEBUG" and not self.debug:
            return

        ts = timestamp or datetime.now()
        timestamp_str = ts.strftime("%Y-%m-%d %H:%M:%S")

        # ANSI color codes for different log levels
        colors = {
            "INFO": "\033[92m",     # Green
            "WARNING": "\033[93m",   # Yellow
            "ERROR": "\033[91m",     # Red
            "DEBUG": "\033[90m"      # Gray
        }
        
        color = colors.get(level, "\033[0m")
        reset = "\033[0m"
        bracket_color = "\033[97m"   # White

        print(f"{bracket_color}[{timestamp_str}]{reset} {color}{level:<8}{reset} {message}")

    def info(self, message: str) -> None:
        """Log an info message."""
        self.log(message, "INFO")

    def warning(self, message: str) -> None:
        """Log a warning message."""
        self.log(message, "WARNING")

    def error(self, message: str) -> None:
        """Log an error message."""
        self.log(message, "ERROR")

    def debug(self, message: str) -> None:
        """Log a debug message."""
        self.log(message, "DEBUG")
