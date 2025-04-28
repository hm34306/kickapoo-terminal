#!/bin/env python
import colorful as cf
import logging

from kickapoo.terminal.colored_logger import get_logger

log = get_logger(__name__, logging.DEBUG)

def demo() -> None:
    log.info("Info Color")
    log.debug("Debug Color")
    log.warning("Warning Color")
    log.error("Error Color")
    log.critical("Critical Color")

if __name__ == "__main__":
    demo()
