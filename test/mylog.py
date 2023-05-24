import coloredlogs
import logging
import sys


def getLogger(name):
    logging.basicConfig()
    logger = logging.getLogger(name)
    coloredlogs.install(logger=logger)
    logger.propagate = False
    coloredFormatter = coloredlogs.ColoredFormatter(
        fmt="%(funcName)s  %(message)s",
        level_styles=dict(
            debug=dict(color="green"),
            info=dict(color="blue"),
            warning=dict(color="yellow", bright=True),
            error=dict(color="red", bold=True, bright=True),
            critical=dict(color="black", bold=True, background="red"),
        ),
    )

    file_handler = logging.FileHandler(f"{name}.log")
    file_handler.setFormatter(logging.Formatter("%(funcName)s  %(message)s"))
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(coloredFormatter)
    logger.handlers = [stream_handler, file_handler]
    logger.setLevel(logging.DEBUG)
    return logger
