"""${project-description}

"""
__author__ = '${user}'

from dataclasses import dataclass, field
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


@dataclass
class ${appclass}(object):
    """${project-description}

    """
    path: Path
    out_dir: Path = field(default=None)
    dry_run: bool = field(default=False)

    def tmp(self):
        if logger.isEnabledFor(logging.INFO):
            logger.info(f'path: {self.path}, out_dir: {self.out_dir}, ' +
                        f'dry_run: {self.dry_run}')
