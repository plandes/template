#!/usr/bin/env python

import unittest, logging, sys
from ${namespace} import HelloWorld
from ${namespace} import Config

logger = logging.getLogger('${namespace}.test')

class TestHelloWorld(unittest.TestCase):
    def test_somedata(self):
        hw = HelloWorld()
        msg = hw.message
        self.assertEqual('hello world', msg)

    def test_config(self):
        conf = Config('test-resources/a_conf_file.conf')
        self.assertEqual({'param1':'3.14'}, conf.options)

def main(args=sys.argv[1:]):
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()

if __name__ == '__main__':
    main()
