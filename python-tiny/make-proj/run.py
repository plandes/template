#set ( $d = "$")
#!/usr/bin/env python

from io import StringIO
from zensols.cli import CliHarness

CONFIG = """
[default]
root_dir = ${d}{appenv:root_dir}

[cli]
apps = list: log_cli, app

[log_cli]
class_name = zensols.cli.LogConfigurator
format = %%(asctime)-15s %%(message)s
log_name = ${appshortname}
level = debug

[app]
class_name = ${appshortname}.${appclass}
"""


if (__name__ == '__main__'):
    CliHarness(
        app_config_resource=StringIO(CONFIG),
        proto_args='',
        proto_factory_kwargs={'reload_pattern': '^${appshortname}'},
    ).run()
