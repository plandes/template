import logging

logger = logging.getLogger('${namespace}.hw')


class ${appclass}(object):
    """Invoke Hello World.

    """
    def __init__(self, message='hello world', out_dir=None):
        logger.debug('init: %s' % message)
        self._message = message
        self.out_dir = out_dir

    @property
    def message(self):
        return self._message

    def print_message(self):
        print('output: {} to {}'.format(self.message, self.out_dir))
