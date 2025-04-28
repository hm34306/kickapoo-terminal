import logging
from kickapoo.terminal import color
from kickapoo.terminal.colors import FontFormat


class CustomFormatter(logging.Formatter):
    grey: color.Colorful.ColorfulStyle = color.grey
    cyan: color.Colorful.ColorfulStyle = color.cyan
    yellow: color.Colorful.ColorfulStyle = color.yellow
    red: color.Colorful.ColorfulStyle = color.red
    bold_red: color.Colorful.ColorfulStyle = color.bold_red
    reset: color.Colorful.ColorfulStyle = color.reset

    def __init__(self, format: str) -> None:
        self.msg_format = format

    @property
    def FORMATS(self):
        return {
            logging.DEBUG: color.format(f"{self.grey} {self.msg_format} {self.reset}"),
            logging.INFO: color.format(f"{self.cyan} {self.msg_format} {self.reset}"),
            logging.WARNING: color.format(f"{self.yellow} {self.msg_format} {self.reset}"),
            logging.ERROR: color.format(f"{self.red} {self.msg_format} {self.reset}"),
            logging.CRITICAL: color.format(f"{self.bold_red} {self.msg_format} {self.reset}"),
        }

    def format(self, record: logging.LogRecord):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
    

def get_logger(name: str, log_level: str=logging.INFO, msg_format="%(levelname)s - %(message)s") -> logging.Logger :

    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    ch = logging.StreamHandler()
    ch.setLevel(log_level)

    ch.setFormatter(CustomFormatter(msg_format))

    logger.addHandler(ch)

    return logger
