#set ( $environ = $project.toUpperCase() )
#set ( $d = "$")
#!/usr/bin/env python

import sys
from io import StringIO
from pathlib import Path
from zensols.config import DictionaryConfig
from zensols.cli import ApplicationFactory

CONFIG = """
[default]
root_dir = ${d}{appenv:root_dir}

[cli]
class_name = zensols.cli.ActionCliManager
apps = list: log_cli, app

[log_cli]
class_name = zensols.cli.LogConfigurator
format = %%(asctime)-15s %%(message)s
default_level = info

[app]
class_name = ${namespace}.${appshortname}.${appclass}
"""


def main(**factory_kwargs):
    entry_path = Path(sys.argv[0])
    src_path = entry_path.parent / 'src'
    sys.path.append(str(src_path))
    dconf = DictionaryConfig({'appenv': {'root_dir': str(entry_path.parent)}})
    cli = ApplicationFactory(
        package_resource='${namespace}.${appshortname}',
        app_config_resource=StringIO(CONFIG),
        children_configs=(dconf,), **factory_kwargs)
    cli.invoke(sys.argv[1:])


if (__name__ == '__main__'):
    main()
