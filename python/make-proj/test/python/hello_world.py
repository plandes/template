#!/usr/bin/env python

import logging
import unittest
import sys
from ${namespace} import HelloWorld

logging.basicConfig(level=logging.DEBUG)

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
