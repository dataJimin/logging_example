import module1
import module2

import logging
import os

if __name__ == "__main__":
    logger1 = logging.getLogger('module1')
    logger2 = logging.getLogger('module2')
    
    fh1 = logging.FileHandler('module1.log')
    logger1.addHandler(fh1)
    logger1.setLevel(logging.DEBUG)
    
    module1.func1()
    
    fh2 = logging.FileHandler('module2.log')
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh2.setFormatter(formatter)
    logger2.addHandler(fh2)
    
    logger2.setLevel(logging.DEBUG)
    
    module2.func1()

