import logging

logger = logging.getLogger(__name__)

def func1():
    logger.debug('debug from module2')
    logger.info('info from module2')
    logger.warning('warning from module2')
    logger.error('error from module2')
    logger.critical('critical from module2')