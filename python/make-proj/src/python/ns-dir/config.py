#set ( $prog = $project.substring(0, 1).toUpperCase() + $project.substring(1) )
from __future__ import annotations
"""This program's application factory.

"""
__author__ = 'Paul Landes'

from dataclasses import dataclass
from pathlib import Path
from zensols.config import DictionaryConfig, EnvironmentConfig
from zensols.cli import ApplicationFactory


@dataclass
class ${prog}ApplicationFactory(ApplicationFactory):
    @classmethod
    def instance(cls, root_dir: Path = Path('.'),
                 reload_factory: bool = False,
                 *args, **kwargs) -> ${prog}ApplicationFactory:
        dconf = DictionaryConfig(
            {'appenv': {'root_dir': str(root_dir)}})
        econf = EnvironmentConfig(
            section_name='env',
            includes=set('HOME'.split()))
        return cls(package_resource='${namespace}',
                   children_configs=(dconf, econf),
                   reload_factory=reload_factory)
