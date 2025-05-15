import logging

logger =logging.getLogger(__name__)

def do_something():
    # logger.info("do something")
    logger_name =input("Enter logger name i.e-DEBUG, INFO, WARNING, ERROR, CRITICAL)")
    logger_message = input ("Enter the message to be displayed")

