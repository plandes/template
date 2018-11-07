import logging
import unittest
from ${namespace} import ${appclass}, AppConfig

# logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('${namespace}.test')


class Test${appclass}(unittest.TestCase):
    def setUp(self):
        self.config = AppConfig('resources/${appshortname}.conf')

    def test_somedata(self):
        app = ${appclass}(self.config)
        msg = app.message
        self.assertEqual('hello world', msg)
