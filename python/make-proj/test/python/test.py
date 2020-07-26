import logging
import unittest
from zensols.config import ImportConfigFactory
from ${namespace} import ${appclass}, AppConfig

# logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Test${appclass}(unittest.TestCase):
    def setUp(self):
        self.config = AppConfig('resources/${project}.conf')
        self.factory = ImportConfigFactory(self.config)

    def test_somedata(self):
        ${appshortname}: ${appclass} = self.factory('${appshortname}')
        path = ${appshortname}.path
        self.assertEqual('target/${appshortname}.dat', str(path))
