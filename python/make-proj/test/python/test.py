import logging
import unittest
from pathlib import Path
from ${namespace} import ${appclass}, FirstClassObj
from instfac import InstanceFactory

if 0:
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)


class Test${appclass}(unittest.TestCase):
    def setUp(self):
        self.app: ${appclass} = InstanceFactory(
            'doit --level=err'.split(), reload_factory=False).instance()

    def test_somedata(self):
        app = self.app
        should = Path('to/some/file.dat')
        res: int = app.doit(should)
        self.assertEqual(${appclass}, type(app))
        self.assertEqual(0, res)
        self.assertTrue(isinstance(app.an_inst, FirstClassObj))
        self.assertTrue(str(app.an_inst.path).startswith('target'))
        self.assertEqual(should, app._out_dir)
        self.assertEqual(False, app.dry_run)
