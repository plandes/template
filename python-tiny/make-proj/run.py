#!/usr/bin/env python

from io import StringIO
from zensols.cli import CliHarness

CONFIG = """
[default]
root_dir = ${d}{appenv:root_dir}

[cli]
class_name = zensols.cli.ActionCliManager
apps = list: log_cli, app

[log_cli]
class_name = zensols.cli.LogConfigurator
format = %%(asctime)-15s %%(message)s
log_name = ${project}
level = debug

[app]
class_name = ${project}.${appshortname}.${appclass}
"""


CliHarness(
    app_config_resource=StringIO(CONFIG),
    proto_args='',
    proto_factory_kwargs={'reload_pattern': '^${project}'},
).run()
