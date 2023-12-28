# from loguru import logger
import configparser
import sys
import json
import os
import logging


config_path = os.path.dirname(__file__)
print(config_path)
path = os.path.join(config_path, "project_modules.state")
print(path)
state_config = configparser.ConfigParser()
state_config.read(path)
print(state_config.sections(), "====================")
