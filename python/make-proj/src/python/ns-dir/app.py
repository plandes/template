"""${project-description}

"""
__author__ = '${user}'

import logging

logger = logging.getLogger(__name__)


class ${appclass}(object):
    """Invoke Hello World.

    """
    SECTION = '${appshortname}'

    def __init__(self, config, message='hello world', out_dir=None,
                 dry_run=False):
        logger.debug(f'init: {message}')
        self.config = config
        self._message = message
        self.out_dir = out_dir
        self.dry_run = dry_run

    @property
    def message(self):
        return self._message

    def print_message(self):
        print(f'output: {self.message} to {self.out_dir}')

    def tmp(self):
        path = self.config.get_option_path('file_path', self.SECTION)
        logger.info(f'invoking with {path}')
