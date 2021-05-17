"""Prototyping REPL fodder.

"""
__author__ = '${user-name}'

import logging
from ${namespace} import ${appclass}
from instfac import InstanceFactory

logger = logging.getLogger(__name__)


def tmp():
    fac = InstanceFactory('doit --level debug'.split())
    ${appshortname}: ${appclass} = fac.instance()
    ${appshortname}.doit()


def main():
    print()
    run = 1
    {1: tmp,
     }[run]()


main()
