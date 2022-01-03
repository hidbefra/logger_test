import logging.config

def sub():
    logging.config.fileConfig('logging.conf')

    logger01 = logging.getLogger('logger_log01')
    
    logger01.debug('debug message 01 äöü')
    logger01.info('info message 01')
    logger01.warning('warn message 01')
    logger01.error('error message 01')
    logger01.critical('critical message 01')
    
    pass