#set ( $environ = $project.toUpperCase() )
#!/usr/bin/env python

from typing import List, Dict, Any
from dataclasses import dataclass
import sys
import os
from pathlib import Path
from zensols.config import DictionaryConfig
from zensols.cli import ApplicationFactory


@dataclass
class ${appclass}Factory(ApplicationFactory):
    @classmethod
    def instance(cls: type, root_dir: Path, **kwargs):
        dconf = DictionaryConfig({'appenv': {'root_dir': str(root_dir)}})
        return cls(package_resource='${namespace}.${appshortname}',
                   app_config_resource=root_dir / 'resources' / 'app.conf',
                   children_configs=(dconf,), **kwargs)


def main(args: List[str], **factory_kwargs: Dict[str, Any]):
    entry_path = Path(args[0])
    src_path = entry_path.parent / 'src'
    conf_path = entry_path.parent / 'etc' / '${project}.conf'
    if not conf_path.exists():
        conf_path = Path(os.environ['${environ}RC'])
    args = args + ['-c', str(conf_path)]
    sys.path.append(str(src_path))
    cli = ${appclass}Factory.instance(entry_path.parent, **factory_kwargs)
    cli.invoke(args[1:])


def proto():
    print('-->proto')
    try:
        main('_ proto'.split(), reload_pattern=r'^${namespace}')
    except SystemExit as e:
        print(f'exit: {e}')


if (__name__ == '__main__'):
    # when running from a shell, run the CLI entry point
    import __main__ as mmod
    if hasattr(mmod, '__file__'):
        main(sys.argv)
    # otherwise, assume a Python REPL and run the prototyping method
    else:
        proto()
