import yaml 
import logging
import os
import sys

__project_name = 'resume-extractor'
__abs_path = os.path.dirname(__file__)
__root_path = __abs_path.split(__project_name)[0]
PROJECT_ROOT = os.path.join(__root_path, __project_name)


with open(os.path.join(PROJECT_ROOT, "settings.yml")) as stream:
    try:
        SETTINGS = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

def __create_logger():
    # Create a custom logger
    logger = logging.getLogger(f"{__name__}")
    logger.setLevel(logging.DEBUG)

    # Create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler('logfile.txt')
    c_handler.setLevel(logging.INFO)
    f_handler.setLevel(logging.DEBUG)

    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(levelname)s - %(message)s')
    f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger

logger = __create_logger()