#!/usr/bin/env python

import logging
logging.basicConfig(level=logging.DEBUG)
import unittest, sys
from ${namespace} import HelloWorld

logger = logging.getLogger('${namespace}.test')

class TestHelloWorld(unittest.TestCase):
    def test_somedata(self):
        hw = HelloWorld()
        msg = hw.message
        self.assertEqual('hello world', msg)

def main(args=sys.argv[1:]):
    unittest.main()

if __name__ == '__main__':
    main()
