#set ( $prog = $project.substring(0, 1).toUpperCase() + $project.substring(1) )
"""${project-description}

"""
__author__ = '${user-name}'

from dataclasses import dataclass, field
import logging
from pathlib import Path
from . import ${prog}Error

logger = logging.getLogger(__name__)


@dataclass
class FirstClassObj(object):
    path: Path = field()
    """The path to some resource."""


@dataclass
class ${appclass}(object):
    """${project-description}

    """
    an_inst: FirstClassObj = field()
    """An instance not given on the commnd line."""

    dry_run: bool = field(default=False)
    """If given, don't do anything, just act like it."""

    def doit(self, out_dir: Path = None):
        """Does something interesting.

        :param out_dir: the directory to output the data

        """
        if logger.isEnabledFor(logging.INFO):
            logger.info(f'path: out_dir: {out_dir}, dry_run: {self.dry_run}')
            logger.info(f'instance: {self.an_inst}')
        logger.debug('some debug message')
        self._out_dir = out_dir
        return 0

    def error(self):
        """Demonstrate error throwing.

        """
        raise ${prog}Error('Testing error usage')


@dataclass
class PrototypeApplication(object):
    CLI_META = {'is_usage_visible': False}

    app: Application = field()

    def proto(self):
        """Prototype test."""
        if logger.isEnabledFor(logging.INFO):
            logger.info('do something more')
