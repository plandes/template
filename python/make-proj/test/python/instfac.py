"""Contains a utility class to create instances.

"""
__author__ = 'Paul Landes'

import logging
from typing import Any, List
from dataclasses import dataclass, field
from pathlib import Path
from zensols.config import DictionaryConfig
from zensols.cli import Application, ApplicationFactory

logger = logging.getLogger(__name__)


@dataclass
class InstanceFactory(object):
    args: List[str] = field(default_factory=list)
    """The command line arguments."""

    config_file: Path = field(default=Path('test-resources/${project}.conf'))
    """The path to the test configuration file."""

    root_dir: Path = Path('.')
    """The root directory."""

    reload_factory: bool = field(default=True)
    """Whether or not to reload classes."""

    @property
    def cli(self) -> ApplicationFactory:
        dconf = DictionaryConfig({'appenv': {'root_dir': str(self.root_dir)}})
        return ApplicationFactory(
            '${namespace}',
            children_configs=(dconf,),
            reload_factory=self.reload_factory)

    def instance(self) -> Any:
        args = list(self.args)
        args.extend(['-c', str(self.config_file)])
        cli: ApplicationFactory = self.cli
        try:
            app: Application = cli.create(args)
            res, invokable = app.invoke_but_second_pass()
            return invokable.instance
        except SystemExit as e:
            raise ValueError(f'commnd line error: {e}')
