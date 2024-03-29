"""${project-description}

"""
__author__ = '${user-name}'

from dataclasses import dataclass, field
import logging
from pathlib import Path
from zensols.config import ConfigFactory

logger = logging.getLogger(__name__)


@dataclass
class ${appclass}(object):
    """${project-description}

    """
    config_factory: ConfigFactory = field()
    """Creates this instance and provides prototyping."""

    dry_run: bool = field(default=False)
    """If given, don't do anything, just act like it."""

    def proto(self, out_dir: Path = None):
        """Used for prototyping.

        :param out_dir: the directory to output the data

        """
        if logger.isEnabledFor(logging.INFO):
            logger.info(f'path: out_dir: {out_dir}, dry_run: {self.dry_run}')
        if logger.isEnabledFor(logging.DEBUG):
            logger.debug('some debug message')
        self._out_dir = out_dir
        return 0
