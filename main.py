import logging
import logging.config

import sub


def main():


    logging.config.fileConfig('logging.conf')

    logger01 = logging.getLogger('logger_log01')
    logger02 = logging.getLogger('logger_log02')

    logger01.debug('debug message 01 äöü')
    logger01.info('info message 01')
    logger01.warning('warn message 01')
    logger01.error('error message 01')
    logger01.critical('critical message 01')

    logger02.debug('debug message 02 äöü')
    logger02.info('info message 02')
    logger02.warning('warn message 02')
    logger02.error('error message 02')
    logger02.critical('critical message 02')

    pass


if __name__ == '__main__':
    main()
    sub.sub()