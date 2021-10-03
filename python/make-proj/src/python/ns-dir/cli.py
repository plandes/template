#set ( $prog = $project.substring(0, 1).toUpperCase() + $project.substring(1) )
"""Command line entry point to the application.

"""
__author__ = '${user-name}'

from typing import List, Any, Dict
import sys
from zensols.cli import ApplicationFactory, ActionResult, CliHarness


class ${prog}ApplicationFactory(ApplicationFactory):
    def __init__(self, *args, **kwargs):
        kwargs['package_resource'] = '${namespace}'
        super().__init__(*args, **kwargs)


def main(args: List[str] = sys.argv, **kwargs: Dict[str, Any]) -> ActionResult:
    harness = CliHarness(
        relocate=False,
        app_factory_class=${prog}ApplicationFactory)
    harness.invoke(args, **kwargs)
