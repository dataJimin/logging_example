import module1
import module2

import logging
import os

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='global.log',
                    filemode='w')
    module1.func1()
    module2.func1()