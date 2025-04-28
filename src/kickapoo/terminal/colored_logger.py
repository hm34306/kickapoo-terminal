import logging
from kickapoo.terminal.colors import ColorName, FontFormat


class CustomFormatter(logging.Formatter):
    grey: str = ColorName.GREY
    yellow: str = ColorName.YELLOW
    red: str = ColorName.RED
    bold_red: str = FontFormat.BOLD + ColorName.RED
    reset: str = ColorName.RESET

    FORMATS = {
        logging.DEBUG: grey  + "%(levelname)s - %(message)s" + reset,
        logging.INFO: grey + "%(levelname)s - %(message)s" + reset,
        logging.WARNING: yellow + "%(levelname)s - %(message)s" + reset,
        logging.ERROR: red + "%(levelname)s - %(message)s" + reset,
        logging.CRITICAL: bold_red + "%(levelname)s - %(message)s" + reset
    }

    def format(self, record: logging.LogRecord):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
    

def get_logger(name: str, log_level: str=logging.INFO) -> logging.Logger :

    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    ch = logging.StreamHandler()
    ch.setLevel(log_level)

    ch.setFormatter(CustomFormatter())

    logger.addHandler(ch)

    return logger
