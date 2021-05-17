#set ( $prog = $project.substring(0, 1).toUpperCase() + $project.substring(1) )
"""Command line entry point to the application.

"""
__author__ = '${user-name}'

from typing import List, Any
from . import ${prog}ApplicationFactory


def main(args: List[str] = None) -> Any:
    cli = ${prog}ApplicationFactory.instance()
    cli.invoke(args)
