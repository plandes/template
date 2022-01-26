#set ( $d = "$")
#!/usr/bin/env python

"""${project-description}

"""
__author__ = '${user-name}'

from dataclasses import dataclass
import logging
from io import StringIO
from zensols.cli import CliHarness
from zensols.cli import ProgramNameConfigurator

logger = logging.getLogger(__name__)
CONFIG = """
[default]
root_dir = ${d}{appenv:root_dir}

[cli]
class_name = zensols.cli.ActionCliManager
apps = list: log_cli, app

[log_cli]
class_name = zensols.cli.LogConfigurator
format = ${d}{program:name}: %%(message)s
log_name = ${d}{program:name}
level = debug

[app]
class_name = ${d}{program:name}.Application
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


if (__name__ == '__main__'):
    CliHarness(
        app_config_resource=StringIO(CONFIG),
        app_config_context=ProgramNameConfigurator(
            None, default='${project}').create_section(),
        proto_args='',
    ).run()
