"""${project-description}

"""
__author__ = '${user-name}'

from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)


@dataclass
class ${appclass}(object):
    """${project-description}

    """
    def proto(self):
        """Prototype method.

        """
        if logger.isEnabledFor(logging.DEBUG):
            logger.debug('starting prototype')
