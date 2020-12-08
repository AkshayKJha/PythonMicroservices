from logging.config import dictConfig
import logging
import os
import json

def configureLogging ( app, default_path='logging.json',
    default_level=logging.Info):
    if os.path.exists(default_path):
    with open(default_path, 'rt') as f:
       try:
          config=json.load(f)
          dictConfig(config)
       except Exception as exception:
          app.logger.error(exception)
          logging.basicConfig(level=default_level)
     else
        logging.basicConfig(level=default_level)
