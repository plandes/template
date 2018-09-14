import logging
import unittest
from ${namespace} import ${appclass}

# logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('${namespace}.test')


class Test${appclass}(unittest.TestCase):
    def test_somedata(self):
        app = ${appclass}()
        msg = app.message
        self.assertEqual('hello world', msg)
