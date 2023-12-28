# from loguru import logger
import configparser
import sys
import json
import os
import logging

# handler = logging.getLogger('hai.state')
# print(logging.Formatter(fmt='%(asctime)s:%(levelname)s: %(message)s ',
#                                            datefmt="%Y-%m-%d %H:%M:%S"))
# handlers=[]
# handlers.append(logging.StreamHandler())
# print(handlers)
# logger.add(handler)

config_path = os.path.dirname(__file__)
print(config_path)
path = os.path.join(config_path, "project_modules.state")
print(path)
state_config = configparser.ConfigParser()
state_config.read(path)
print(state_config.sections(), "====================")
