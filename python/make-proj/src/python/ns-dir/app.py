import logging

logger = logging.getLogger(__name__)


class ${appclass}(object):
    """Invoke Hello World.

    """

    SECTION = '${appshortname}'

    def __init__(self, config, message='hello world', out_dir=None):
        logger.debug('init: %s' % message)
        self.config = config
        self._message = message
        self.out_dir = out_dir

    @property
    def message(self):
        return self._message

    def print_message(self):
        print('output: {} to {}'.format(self.message, self.out_dir))

    def tmp(self):
        path = self.config.get_option_path('file_path', self.SECTION)
        logger.info(f'invoking with {path}')
