import logging

logger = logging.getLogger(__name__)

def func1():
    logger.debug('debug from module1')
    logger.info('info from module1')
    logger.warning('warning from module1')
    logger.error('error from module1')
    logger.critical('critical from module1')