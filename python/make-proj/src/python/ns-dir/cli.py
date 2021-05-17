#set ( $prog = $project.substring(0, 1).toUpperCase() + $project.substring(1) )
from __future__ import annotations
"""Command line entry point to the application.

"""
__author__ = '${user-name}'

from typing import List, Any
from dataclasses import dataclass
from pathlib import Path
from zensols.config import DictionaryConfig
from zensols.cli import ApplicationFactory


@dataclass
class ${prog}ApplicationFactory(ApplicationFactory):
    @classmethod
    def instance(cls: type, root_dir: Path = Path('.'),
                 *args, **kwargs) -> ${prog}ApplicationFactory:
        dconf = DictionaryConfig({'appenv': {'root_dir': str(root_dir)}})
        return cls(package_resource='${namespace}',
                   children_configs=(dconf,),
                   **kwargs)


def main(args: List[str], **kwargs: Dict[str, Any]) -> Any:
    cli = ${prog}ApplicationFactory.instance(**kwargs)
    cli.invoke(args)
