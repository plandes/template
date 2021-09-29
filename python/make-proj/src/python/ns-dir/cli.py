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
from zensols.cli import ApplicationFactory, ActionResult, CliHarness
from . import ${prog}Error


class ${prog}ApplicationFactory(ApplicationFactory):
    def __init__(self, *args, **kwargs):
        kwargs['package_resource'] = '${namespace}'
        super().__init__(*args, **kwargs)

    def _handle_error(self, ex: Exception):
        try:
            super()._handle_error(ex)
        except ${prog}Error as e:
            self._dump_error(e)


def main(args: List[str] = sys.argv, **kwargs: Dict[str, Any]) -> ActionResult:
    harness = CliHarness(
        relocate=False,
        app_factory_class=${prog}ApplicationFactory)
    return harness.invoke(args, **kwargs)
