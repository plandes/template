"""${project-description}

"""
__author__ = '${user}'

from dataclasses import dataclass, field
import logging
from pathlib import Path
from zensols.config import Configurable

logger = logging.getLogger(__name__)


@dataclass
class ${appclass}(object):
    """${project-description}

    """
    config: Configurable

    dry_run: bool = field(default=False)
    """If given, don't do anything, just act like it."""

    def doit(self, out_dir: Path = None):
        """Does something interesting.

        :param out_dir: the directory to output the data

        """
        if logger.isEnabledFor(logging.INFO):
            logger.info(f'path: out_dir: {out_dir}, dry_run: {self.dry_run}')
        self.config.remove_section('some_inst')
        logger.debug('some debug message')
        self._out_dir = out_dir
        return 0
