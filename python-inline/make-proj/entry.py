#set ( $d = "$")
#!/usr/bin/env python

"""${project-description}

"""
__author__ = '${user-name}'

from dataclasses import dataclass
import logging
from pathlib import Path
from io import StringIO
from zensols.cli import CliHarness

logger = logging.getLogger(__name__)
CONFIG = """
[default]
root_dir = ${d}{appenv:root_dir}

[cli]
class_name = zensols.cli.ActionCliManager
apps = list: add_prog_cli, log_cli, app

[add_prog_cli]
class_name = zensols.cli.ProgramNameConfigurator
default = ${d}{appenv:prog}

[log_cli]
class_name = zensols.cli.LogConfigurator
format = ${d}{prog:name}: %%(message)s
log_name = ${d}{prog:name}
level = debug

[app]
class_name = ${d}{appenv:prog}.Application
"""


@dataclass
class ${appclass}(object):
    """${project-description}

    """
    def proto(self):
        """Prototype method.

        """
        if logger.isEnabledFor(logging.DEBUG):
            logger.debug('starting prototype')


if __name__ == '__main__':
    CliHarness(
        app_config_resource=StringIO(CONFIG),
        app_config_context={'appenv': {'prog': Path(__file__).stem}},
        proto_args='',
    ).run()
