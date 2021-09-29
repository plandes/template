#set ( $prog = $project.substring(0, 1).toUpperCase() + $project.substring(1) )
from __future__ import annotations
"""Command line entry point to the application.

"""
__author__ = '${user-name}'

from typing import List, Any, Dict
from dataclasses import dataclass
import sys
from pathlib import Path
from zensols.config import DictionaryConfig
from zensols.cli import ApplicationFactory


@dataclass
class ${prog}ApplicationFactory(ApplicationFactory):
    def __init__(self, *args, **kwargs):
        kwargs['package_resource'] = '${namespace}'
        super().__init__(*args, **kwargs)


def main(args: List[str] = sys.argv[1:], **kwargs: Dict[str, Any]):
    cli = ${prog}ApplicationFactory.instance(**kwargs)
    cli.invoke(args)
