import configparser, logging

logger = logging.getLogger('${namespace}.hw')

class HelloWorld(object):
    """
    Invoke Hello World.
    """
    def __init__(self, message='hello world'):
        logger.debug('init: %s' % message)
        self._message = message

    @property
    def message(self):
        return self._message
