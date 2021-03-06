import sys, os
sys.path.append(os.path.split(os.getcwd())[0])
sys.path.append(os.getcwd())

from unittest import TestCase

import logging_child

class TestChannel(TestCase):
    def test_formatter(selfs):

        from AVCommon import logger
        logger.init()
        from AVCommon.logger import logging
        globals()['logging']=logging

        formatter = logging.Formatter('%(asctime)s -%(levelname)s- %(filename)s:%(lineno)s   %(message)s')
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setFormatter(formatter)
        logger = logging.getLogger('')
        logger.addHandler(stdout_handler)
        logger.setLevel(logging.DEBUG)

        logging.debug('A debug message')
        logging.info('Some information')
        logging.warning('A shot across the bows')


        logging.debug('A debug message')
        logging.info('Some information')

        logging.warning('A shot across the bows')

        logging_child.ClassName("calling a child")
