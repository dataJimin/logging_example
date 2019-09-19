import module1
import module2

import logging
import os

if __name__ == "__main__":
    # logging for global
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='global.log',
                    filemode='a')
    
    # logging for specific module
    logger2 = logging.getLogger('module2')
    
    fh2 = logging.FileHandler('module2.log')
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh2.setFormatter(formatter)
    logger2.addHandler(fh2)
    
    logger2.setLevel(logging.DEBUG)

    module1.func1()
    module2.func1()


