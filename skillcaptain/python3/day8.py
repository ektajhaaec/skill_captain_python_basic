import logging

logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename="day9.log",level =logging.DEBUG)
    logger.info('started')
    logger_name =input("Enter logger name i.e-DEBUG, INFO, WARNING, ERROR, CRITICAL)")
    logger_message = input ("Enter the message to be displayed")
    if logger_name == "DEBUG":
        logger.info(logger_message)
    elif logger_name == "INFO":
        logger.debug(logger_message)
    elif logger_name == "WARNING" :
        logger.warning(logger_message)   
    elif logger_name == "ERROR":
        logger.error(logger_message)
    elif logger_name ==  "CRITICAL" :
        logger.critical(logger_message)
    
    logger.info('finished')
if __name__ =='__main__':
    main()
