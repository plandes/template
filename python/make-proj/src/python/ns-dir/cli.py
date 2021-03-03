"""Command line entry point to the application.

"""
__author__ = 'plandes'

from typing import List, Any
from zensols.config import DictionaryConfig
from zensols.cli import ApplicationFactory


def main(args: List[str] = None) -> Any:
    conf = DictionaryConfig({'appenv': {'root_dir': '.'}})
    cli = ApplicationFactory('${namespace}', children_configs=(conf,))
    cli.invoke(args)
